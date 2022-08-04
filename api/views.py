from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics
from .serializers import UserSerializer



class Register(generics.CreateAPIView):
    serializer_class=UserSerializer
    permission_classes = []


@api_view(['GET'])
def api_root(request):
    return Response({
        'api-auth':reverse('api-auth',request=request),
        'tags-api':reverse('tags-api',request=request),
        'reviews-api':reverse('reviews-api',request=request),
        'signUP':reverse('register',request=request),
        
        })