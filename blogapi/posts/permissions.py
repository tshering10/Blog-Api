from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Only allow owners of an object to edit/delete it.
    Others can only read.
    """

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS = GET, HEAD, OPTIONS (read-only)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write/delete permission only for the owner
        return obj.author == request.user
