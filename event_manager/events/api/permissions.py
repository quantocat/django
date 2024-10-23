from rest_framework import permissions


class IsAdminuserOrReadOnly(permissions.IsAdminUser):
    """Normale User haben nur Leserechte, Admin darf auch schreiben."""
    def has_permission(self, request, view) -> bool:
        is_admin = super().has_permission(request, view)
        # SAFE_METHODS: GET, OPTIONS, TRACE,...
        return request.method in permissions.SAFE_METHODS or is_admin
