from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == "admin"
    
class IsUserOrAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        if request.method == "POST":
            return request.user.role in ['user', 'admin']
        if request.method == "PUT":
            return request.user.role in ['user', 'admin']
        if request.method == "DELETE":
            return request.user.role in ['user', 'admin']
        return False
    

class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        
        if request.user.role == 'admin':
            return True
        
        if request.user.role == 'user':
            return obj.user == request.user
        
        if request.user.role == 'taxi':
            return obj.trip.driver_id == request.user
        
        return False
    
    