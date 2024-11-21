from rest_framework.permissions import BasePermission

class IsAuthorOrReadOnly(BasePermission):
    """
    Custom permission to allow only authors of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read-only permissions for GET, HEAD, and OPTIONS requests
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True

        # Write permissions only for the author
        return obj.author == request.user

