from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    """
    message = "You is not the owner of this pet!"
    my_safe_method = ['GET','PUT', 'DELETE']
    def has_permission(self, request, view):
        if request.method in self.my_safe_method:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request.
        # GET, HEAD or OPTIONS requests are allowed.
        if request.method in SAFE_METHODS:
            return True
        return obj.owner == request.user
