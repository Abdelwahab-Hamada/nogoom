from rest_framework import (
    generics,
    permissions
    )

from .serializers import Serializer,StarSerializer
from .models import Review

from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

class Instance(generics.RetrieveDestroyAPIView):
    queryset=Review.objects
    serializer_class=Serializer

class Star(generics.UpdateAPIView):
    queryset=Review.objects
    serializer_class=StarSerializer
    permission_classes=[permissions.IsAuthenticated]

class StaredReviews(generics.ListAPIView):
    queryset=Review.objects.prefetch_related('stars')
    serializer_class=Serializer

    def get_queryset(self, *args, **kwargs):
        logged_user=self.request.user
        qs = logged_user.stared_reviews.all()
        
        return qs

class OwnedReviews(generics.ListAPIView):
    queryset=Review.objects.prefetch_related('stars')
    serializer_class=Serializer

    def get_queryset(self, *args, **kwargs):
        logged_user=self.request.user
        qs = logged_user.reviews.all()
        
        return qs

class FeedReviews(generics.ListAPIView):
    queryset=Review.objects.prefetch_related('stars')
    serializer_class=Serializer

    def get_queryset(self, *args, **kwargs):
        logged_user=self.request.user
        qs = super().get_queryset(*args, **kwargs).filter(tags__followers=logged_user).distinct()
        
        return qs

class TagReviews(generics.ListAPIView):
    queryset=Review.objects.prefetch_related('stars')
    serializer_class=Serializer

    def get_queryset(self, *args, **kwargs):
        tag_slug=self.kwargs.get('slug')
        qs = super().get_queryset(*args, **kwargs).filter(tags__slug=tag_slug)
        
        return qs

class Creation(generics.CreateAPIView):
    serializer_class=Serializer
    permission_classes=[permissions.IsAuthenticated]


@api_view(['GET'])
def reviews_api_root(request):
    return Response({
        'feed':reverse('feed-reviews',request=request),
        'review-creation':reverse('review-creation',request=request),
        'user-reviews':reverse('user-reviews',request=request),
        'stared-reviews':reverse('stared-reviews',request=request),
        })
