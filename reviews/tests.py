from django.urls import reverse,resolve
from rest_framework.test import( 
    APITestCase,
    )
from django.contrib.auth.models import User
from reviews.models import Review
from tags.models import Tag


class TestAPI(APITestCase):#Testing API tests urls,models,views by default
    def setUp(self):#test uses a separate database and destroys it after test
        user=User.objects.create(username='exa')
        user.set_password('463008')
        user.save()
        self.user=user
        self.tag=Tag.objects.create(label='TestAPI')
        self.client.login(username='exa',password='463008')
        self.review=Review.objects.create(
            score=5,
            comment='this is a test for Review model from TestModels',
            title='reviews-TestModels',
            reviewer=user,
        )

    def test_feed(self):
        url=reverse('feed-reviews')
        response=self.client.get(url)
        
        self.assertEqual(response.status_code, 200)

    def test_create_review(self):
        url=reverse('review-creation')
        data={
            'score':5,
            'comment':'this is a test for Review model from TestAPI',
            'title':'reviews-TestAPI',
            'tags':[self.tag.id,]
        }
        response=self.client.post(url,data,format='json')
        
        self.assertEqual(response.status_code, 201)

    def test_star_review(self):
        url=reverse('star-review',kwargs={'pk':self.review.pk})
        response=self.client.put(url,format='json')

        self.assertEqual(response.status_code, 200)



