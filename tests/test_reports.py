from django.urls import reverse
import pytest
from rest_framework.test import APIClient
from reports.models import Report

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


def test_report_create(api_client, admin_user):
    url = reverse("report-list")
    data = {
        "owner": admin_user.pk,
    }
    api_client.force_authenticate(user=admin_user)
    response = api_client.post(url, data)
    assert response.status_code == 201
    assert Report.objects.count() == 1
    assert Report.objects.get().owner_id == data["owner"]


def test_report_list(api_client, admin_user):
    url = reverse("report-list")
    api_client.force_authenticate(user=admin_user)
    response = api_client.get(url)
    assert response.status_code == 200
