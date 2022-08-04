from django.urls import reverse,resolve
from rest_framework.test import( 
    APITestCase,
    )
from django.contrib.auth.models import User
from .models import Tag


class TestAPI(APITestCase):
    def setUp(self):
        user=User.objects.create(username='exa')
        user.set_password('463008')
        user.save()
        self.tag=Tag.objects.create(label='TestAPI')
        self.client.login(username='exa',password='463008')
        

    def test_followed_tags(self):#followed test makes onther listing views tests not necessary
        url=reverse('followed-tags')
        response=self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_create_tag(self):
        url=reverse('tag-creation')
        response=self.client.post(url,{'label':'exa'},format='json')

        self.assertEqual(response.status_code, 201)

    def test_follow_tag(self):
        url=reverse('follow-tag',kwargs={'slug':self.tag.slug})
        response=self.client.put(url)

        self.assertEqual(response.status_code, 200)

    def test_tag_reviews(self):
        url=reverse('tag-reviews',kwargs={'slug':self.tag.slug})
        response=self.client.get(url)

        self.assertEqual(response.status_code, 200)










        
