from django.urls import reverse
import pytest
from rest_framework.test import APIClient
from subjects.models import Subject

from users.models import User


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def admin_user(db):
    user = User.objects.create_user(
        email="admin@example.com",
        password="password",
        user_type="A",
        username="admin",
        is_staff=True,
        is_superuser=True,
    )
    return user


@pytest.fixture
def subject(db):
    return Subject.objects.create(
        name="Math",
        description="Math subject description",
    )


def test_subject_create(api_client, admin_user):
    url = reverse("subject-list")
    data = {
        "name": "Math",
        "description": "Math subject description",
    }
    api_client.force_authenticate(user=admin_user)
    response = api_client.post(url, data)
    assert response.status_code == 201
    assert Subject.objects.count() == 1
    assert Subject.objects.get().name == data["name"]


def test_subject_list(api_client, admin_user):
    url = reverse("subject-list")
    api_client.force_authenticate(user=admin_user)
    response = api_client.get(url)
    assert response.status_code == 200


def test_subject_detail(api_client, admin_user, subject):
    url = reverse("subject-detail", kwargs={"pk": subject.pk})
    api_client.force_authenticate(user=admin_user)
    response = api_client.get(url)
    assert response.status_code == 200


def test_subject_update(api_client, admin_user, subject):
    url = reverse("subject-detail", kwargs={"pk": subject.pk})
    data = {
        "name": "Math",
        "description": "Math subject description",
    }
    api_client.force_authenticate(user=admin_user)
    response = api_client.put(url, data)
    assert response.status_code == 200


def test_subject_delete(api_client, admin_user, subject):
    url = reverse("subject-detail", kwargs={"pk": subject.pk})
    api_client.force_authenticate(user=admin_user)
    response = api_client.delete(url)
    assert response.status_code == 204
    assert Subject.objects.count() == 0
