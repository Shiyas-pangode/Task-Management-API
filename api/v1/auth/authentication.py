from django.contrib.auth.backends import ModelBackend
from users.models import CustomUser

class EmailUsernameModel(ModelBackend):
    def authentication(self , request , username=None,email=None,password=None ,**kwarg):
        
        try:
            user = CustomUser.objects.get(email=username)
        except CustomUser.DoesNotExist:
            try:
                user = CustomUser.objects.get(username=username)
            except CustomUser.DoesNotExist:
                return None

        if user.check_password(password):
            return user
        return None



