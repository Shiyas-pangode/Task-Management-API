from rest_framework import permissions

class IsAdminOrManager(permissions.BasePermission):
    def has_permission(self, request, view):
        print("DEBUG: Checking permissions in IsAdminOrManager")
        print("DEBUG: User:", request.user)
        print("DEBUG: Authenticated:", request.user.is_authenticated)
        print("DEBUG: Role:", getattr(request.user, 'role', 'No Role Found'))
        
        if request.method in permissions.SAFE_METHODS:
            print("DEBUG: Read-only access granted")
            return True  

        
        if request.user.is_authenticated and request.user.role.lower() in ['admin', 'manager']:
            print("DEBUG: Access granted to Admin/Manager")
            return True

        print("DEBUG: Access Denied (403)")
        return False



class IsAdminManagerOrAssignedEmployee(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        print("DEBUG: Checking Task Permissions")
        print(f"DEBUG: User: {request.user}, Role: {request.user.role}, Task Assigned To: {obj.assigned_to}")

        if request.user.is_authenticated:
            if request.user.role.lower() in ['admin', 'manager']:
                print("DEBUG: Admin/Manager - Access Granted ")
                return True
            
            if request.user.role.lower() == "employee" and obj.assigned_to == request.user:
                print("DEBUG: Employee - Access Granted ")
                return True

        print("DEBUG: Access Denied ❌")
        return False

class IsAssignedEmployee(permissions.BasePermission):
    

    def has_object_permission(self, request, view, obj):
        print(f"DEBUG: User: {request.user}, Role: {request.user.role}, Task Assigned To: {obj.assigned_to}")

 
        if request.user.role.lower() in ["admin", "manager"]:
            return True

        
        return request.user.role.lower() == "employee" and obj.assigned_to == request.user

class IsAdminUser(permissions.BasePermission):
    """
    Custom permission to allow only admin users to delete tasks.
    """

    def has_permission(self, request, view):
        
        if request.method == "DELETE":
            return request.user.is_authenticated and request.user.role == "admin"
        return True
