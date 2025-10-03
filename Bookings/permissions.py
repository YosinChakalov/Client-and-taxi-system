from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == "Admin"
    
class IsUserOrAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        if request.method == "POST":
            return request.user.role in ['User', 'Admin']
        if request.method == "PUT":
            return request.user.role in ['User', 'Admin']
        if request.method == "DELETE":
            return request.user.role in ['User', 'Admin']
        return False
    

class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        
        if request.user.role == 'Admin':
            return True
        
        if request.user.role == 'User':
            return obj.user == request.user
        
        if request.user.rol == 'Taxi':
            return obj.trip.driver_id == request.user
        
        return False