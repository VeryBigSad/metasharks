import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from courses.models import Course
from users.models import User


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def curator_user(db):
    user = User.objects.create_user(
        email="curator@example.com",
        password="password",
        user_type="C",
        username="curator",
    )
    return user


@pytest.fixture
def course(db, curator_user):
    return Course.objects.create(
        name="Test Course",
        description="This is a test course",
        curator_id=curator_user.pk,
    )


@pytest.fixture
def admin_user(db):
    user = User.objects.create_user(
        email="admin@example.com", password="password", user_type="A", username="admin"
    )
    return user


def test_course_create(api_client, curator_user, admin_user):
    url = reverse("course-list")
    data = {
        "name": "New Course",
        "description": "This is a new course",
        "curator": curator_user.pk,
        "subjects": [],
    }
    api_client.force_authenticate(user=admin_user)
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert Course.objects.count() == 1
    assert Course.objects.get().name == data["name"]


def test_course_list(api_client, course):
    url = reverse("course-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["name"] == course.name


def test_course_detail(api_client, course):
    url = reverse("course-detail", args=[course.id])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["name"] == course.name


def test_course_update(api_client, admin_user, curator_user, course):
    url = reverse("course-detail", args=[course.id])
    data = {
        "name": "Updated Course",
        "description": "This is an updated course",
        "curator": curator_user.pk,
        "subjects": [],
    }
    api_client.force_authenticate(user=admin_user)

    response = api_client.put(url, data)
    assert response.status_code == status.HTTP_200_OK
    assert Course.objects.get().name == data["name"]


def test_course_delete(api_client, admin_user, course):
    url = reverse("course-detail", args=[course.id])
    api_client.force_authenticate(user=admin_user)
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Course.objects.count() == 0
