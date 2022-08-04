from rest_framework import (
    generics,
    permissions
    )

from .serializers import Serializer,FollowSerializer

from .models import Tag

from django.db.models import Count,Max

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


class SearchResults(generics.ListAPIView):
    queryset=Tag.objects.prefetch_related('followers')
    serializer_class=Serializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        results=Tag.objects.none()
        if q is not None:
            results=qs.search(q)
        return results

class PopularList(generics.ListAPIView):
    queryset=Tag.objects.prefetch_related('followers')
    serializer_class=Serializer

    def get_queryset(self, *args, **kwargs):
        qs=super().get_queryset(*args, **kwargs).annotate(
                count_followers=Count('followers')).order_by(
                    '-count_followers','-created_on'
                )

        return qs

class RecentList(generics.ListAPIView):
    queryset=Tag.objects.prefetch_related('followers')
    serializer_class=Serializer

    def get_queryset(self, *args, **kwargs):
        qs=super().get_queryset(*args, **kwargs).annotate(
                count_followers=Count('followers')).order_by(
                    '-created_on','-count_followers',
                )

        return qs

class Followed(generics.ListAPIView):
    queryset=Tag.objects
    serializer_class=Serializer
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        logged_user=self.request.user
        qs = logged_user.tags.prefetch_related('followers')
        # .annotate(
        #     recently_used=Max('reviews__created_on')).order_by('-recently_used')


        return qs

class Creation(generics.CreateAPIView):
    serializer_class=Serializer
    permission_classes=[permissions.IsAuthenticated]


class Follow(generics.UpdateAPIView):
    queryset=Tag.objects
    serializer_class=FollowSerializer
    lookup_field='slug'
    permission_classes=[permissions.IsAuthenticated]


class Instance(generics.RetrieveDestroyAPIView):
    queryset=Tag.objects
    serializer_class=Serializer
    lookup_field='slug'

@api_view(['GET'])
def tags_api_root(request):
    return Response({
        'search':reverse('search-tags',request=request),
        'create-tag':reverse('tag-creation',request=request),
        'popular':reverse('popular-tags',request=request),
        'recent':reverse('recent-tags',request=request),
        'followed':reverse('followed-tags',request=request),
        
        
        })
    
    



