from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    SearchResults,
    PopularList,
    RecentList,
    Creation,
    Followed,
    Follow,
    Instance,
    tags_api_root,
)

urlpatterns=format_suffix_patterns([
    path('search/',SearchResults.as_view(),name='search-tags'),
    path('create/',Creation.as_view(),name='tag-creation'),
    path('popular/',PopularList.as_view(),name='popular-tags'),
    path('recent/',RecentList.as_view(),name='recent-tags'),
    path('followed/',Followed.as_view(),name='followed-tags'),
    path('<slug>/follow/',Follow.as_view(),name='follow-tag'),
    path('<slug>/details/',Instance.as_view(),name='tag'),
    path('', tags_api_root,name='tags-api'),

])

