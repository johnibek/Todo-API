from rest_framework import permissions

class AuthorEditPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return view

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user
