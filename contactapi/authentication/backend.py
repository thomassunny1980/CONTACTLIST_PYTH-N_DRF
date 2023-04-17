import jwt

from django.conf import settings
from django.contrib.auth.models import User

from rest_framework import authentication,exceptions



class JWTAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)
        if not auth_data:
            return None
        prefix, token = auth_data.decode('utf-8').split(' ')

        try:
            key = 'JWT_SECRET_KEY'
            payload = jwt.decode(token,key,algorithms="HS256")
            user = User.objects.get(username=payload['username'])
            return (user,token)
        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed('Your token is invalid for login')
        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed('Your token is expired for login')
        
        return super().authenticate(request)