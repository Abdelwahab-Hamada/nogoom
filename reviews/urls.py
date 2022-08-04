from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    TagReviews,
    Creation,
    FeedReviews,
    Star,
    StaredReviews,
    OwnedReviews,
    reviews_api_root,
    Instance,
)

urlpatterns =format_suffix_patterns([
    path('feed/',FeedReviews.as_view(),name='feed-reviews'),
    path('create/',Creation.as_view(),name='review-creation'),
    path('user/',OwnedReviews.as_view(),name='user-reviews'),
    path('stared/',StaredReviews.as_view(),name='stared-reviews'),
    path('<pk>/star/',Star.as_view(),name='star-review'),
    path('<pk>/details/',Instance.as_view(),name='review'),
    path('<slug>/',TagReviews.as_view(),name='tag-reviews'),
    path('',reviews_api_root,name='reviews-api')

])