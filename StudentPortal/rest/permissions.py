from rest_framework import permissions


class IsCreationOrIsAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated():
            if view.action == 'create':
                return True
            else:
                return False
        else:
            return True


class IsOwnerOrCreateOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        if view.action == 'create':
            return True
        try:
            return obj.owner == request.user
        except:
            return obj == request.user


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            return obj.owner == request.user
        except:
            return obj == request.user

 
class IsAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        else:
            return True


class IsAdminUserOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.is_staff


class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_staff


class IsGetContentEditor(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated() and (request.user.is_staff or request.user.groups.filter(name__icontains='content editor'))
