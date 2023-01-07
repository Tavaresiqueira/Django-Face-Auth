from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

class CognitoBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        if password:
            #to candle superuser admin screen login
            user = super().authenticate(request,username=username,password=password)
        else:
            try:
                user = User.objects.get(username=username)
                #print('*****************')
            except User.DoesNotExist:
                # Create a new user. There's no need to set a password
                user = User(username=username)
                user.is_staff = False
                user.is_active = True
                user.save()
        return user