from rest_framework.permissions import BasePermission
from metasharks.constants import SAFE_METHODS


class IsCuratorOrAdminOrReadOnly(BasePermission):
    """
    The request is authenticated as a curator, or gives read-only permission.
    """

    def has_permission(self, request, view) -> bool:
        return bool(
            request.method in SAFE_METHODS
            or (
                request.user
                and request.user.is_authenticated
                and (request.user.is_curator or request.user.is_admin)
            )
        )


class IsAdminOrReadOnly(BasePermission):
    """
    The request is authenticated as an admin, or gives read-only permission.
    """

    def has_permission(self, request, view) -> bool:
        return bool(
            request.method in SAFE_METHODS
            or (
                request.user and request.user.is_authenticated and request.user.is_admin
            )
        )
