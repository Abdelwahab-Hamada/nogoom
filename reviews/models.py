from django.db import models
from django.conf import settings
from django.utils import timezone

import uuid
import math

from tags.models import Tag

class Review(models.Model):
    temp_id = models.UUIDField(default=uuid.uuid4)
    reviewer=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='reviews',on_delete=models.CASCADE)
    tags=models.ManyToManyField(Tag,related_name='reviews')
    score=models.IntegerField()
    comment=models.TextField()
    title=models.CharField(max_length=33)
    created_on=models.DateTimeField(auto_now_add=True)
    stars=models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='stared_reviews')
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def created(self):
        now = timezone.now()
        diff=now-self.created_on
        days=diff.days
        seconds=diff.seconds

        if days == 0:
            if 0 <= seconds < 60:
                return 'just now'

            if  60 <= seconds < 3600:
                minutes=math.floor(seconds/60)
                if minutes == 1:
                    return str(minutes) + " min ago"
                return str(minutes) + " mins ago"

            if 3600 <= seconds < 86400:
                hours= math.floor(seconds/3600)
                if hours == 1:
                    return str(hours) + " hr ago"
                return str(hours) + " hrs ago"

        if 1 <= days < 30:
            if days == 1:
                return str(days) + " dy ago"
            return str(days) + " dys ago"

        if 30 <= days < 365:
            months= math.floor(days/30)
            if months == 1:
                return str(months) + " mon ago"
            return str(months) + " mons ago"

        if days >= 365:
            years= math.floor(days/365)
            if years == 1:
                return str(years) + " yr ago"
            return str(years) + " yrs ago"
