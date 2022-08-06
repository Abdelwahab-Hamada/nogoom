from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from django.conf import settings
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.middleware import csrf
from rest_framework import status

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class APIAuthentication(APIView):
    permission_classes = []

    def get(self,request,format=None):
        token=request.COOKIES.get(
            settings.SIMPLE_JWT['AUTH_COOKIE']
            ) 

        refreshToken=RefreshToken(token)
        refreshToken.blacklist()

        refreshToken.set_jti()#jwt id
        refreshToken.set_exp()#expiration
        refreshToken.set_iat()#issued at

        accessToken=refreshToken.access_token

        response = Response()

        response.set_cookie(
                    key = settings.SIMPLE_JWT['AUTH_COOKIE'], 
                    value = refreshToken,
                    expires = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                    secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                    httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                    samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
                )

        response.data={'access':str(accessToken)}
        return response

    def post(self, request, format=None):
        data = request.data
        response = Response()        
        username = data.get('username', None)
        password = data.get('password', None)
        
        logged_user = authenticate(username=username, password=password)
        
        if logged_user is not None:
            if logged_user.is_active:
                data = get_tokens_for_user(logged_user)
                response.set_cookie(
                    key = settings.SIMPLE_JWT['AUTH_COOKIE'], 
                    value = data["refresh"],
                    expires = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                    secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                    httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                    samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
                )
                csrf.get_token(request)   
                response["Access-Control-Allow-Credentials"]=True

                response.data = {'access':data['access']}
                return response
            else:
                return Response({"No active" : "This account is not active!!"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"Invalid" : "Invalid username or password!!"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,format=None):
        token=request.COOKIES.get(settings.SIMPLE_JWT['AUTH_COOKIE']) 
        refreshToken=RefreshToken(token)
        refreshToken.blacklist()        

        response = Response()
        response.delete_cookie(
                    settings.SIMPLE_JWT['AUTH_COOKIE'], 
                )
        response.delete_cookie(
                    'csrftoken', 
                )
        
        response.data={'logged out'}
        return response
