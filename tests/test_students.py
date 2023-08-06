import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from courses.models import Course
from students.models import StudentGroup
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
def student_group(db, course, curator_user):
    return StudentGroup.objects.create(
        name="A-1",
        curator_id=curator_user.pk,
        course_id=course.pk,
        start_date="2020-01-01",
        end_date="2020-12-31",
    )


@pytest.fixture
def student_user(db):
    return User.objects.create_user(
        email="lol@lol.lol",
        password="password",
        user_type="S",
        username="student",
    )


@pytest.fixture
def admin_user(db):
    user = User.objects.create_user(
        email="admin@example.com", password="password", user_type="A", username="admin"
    )
    return user


def test_studentgroup_create(api_client, course, student_user, curator_user):
    url = reverse("student-group-list")
    data = {
        "name": "B-1",
        "curator": curator_user.pk,
        "course": course.pk,
        "students": [student_user.pk],
        "start_date": "2020-01-01",
        "end_date": "2020-12-31",
    }
    api_client.force_authenticate(user=curator_user)
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert StudentGroup.objects.count() == 1
    assert StudentGroup.objects.get().name == data["name"]


def test_studentgroup_list(api_client, student_group):
    url = reverse("student-group-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["name"] == student_group.name


def test_studentgroup_detail(api_client, student_group):
    url = reverse("student-group-detail", args=[student_group.id])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["name"] == student_group.name


def test_studentgroup_update(
    api_client, student_user, course, curator_user, student_group
):
    url = reverse("student-group-detail", args=[student_group.id])
    data = {
        "name": "A-23",
        "curator": curator_user.pk,
        "course": course.pk,
        "students": [student_user.pk],
        "start_date": "2020-01-01",
        "end_date": "2020-12-31",
    }

    api_client.force_authenticate(user=curator_user)
    response = api_client.put(url, data)
    assert response.status_code == status.HTTP_200_OK
    assert StudentGroup.objects.get().name == data["name"]


def test_studentgroup_delete(api_client, curator_user, student_group):
    url = reverse("student-group-detail", args=[student_group.id])
    api_client.force_authenticate(user=curator_user)
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert StudentGroup.objects.count() == 0
