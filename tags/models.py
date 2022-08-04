from django.db import models
from django.conf import settings
from django.utils import timezone

import uuid
import math
from autoslug import AutoSlugField


class TagQuerySet(models.QuerySet):
    def search(self,query):
        lookup = models.Q(label__icontains=query) 
        qs=self.filter(lookup)

        return qs


class Tag(models.Model):
    temp_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label=models.CharField(max_length=30,unique=True)
    slug=AutoSlugField(unique_with='id',populate_from='label')
    followers=models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='tags')
    created_on=models.DateTimeField(auto_now_add=True)

    objects=TagQuerySet.as_manager()

    def __str__(self):
        return self.label

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


            




        
