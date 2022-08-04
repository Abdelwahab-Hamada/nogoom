from django.test import SimpleTestCase,TestCase,Client
from django.urls import reverse,resolve
from django.contrib.auth.models import User


class TestUrls(SimpleTestCase):
    def testAuth(self):
        url=reverse('api-auth')
        self.assertEquals(resolve(url).func.view_class.__name__,'APIAuthentication')

    def testRootAPI(self):
        url=reverse('root-api')
        self.assertEquals(resolve(url).func.view_class.__name__,'api_root')

class TestViews(TestCase):
    def setUp(self):
        user=User.objects.create(username='exa')
        user.set_password('463008')
        user.save()

    def testRootAPI(self):
        url=reverse('root-api')
        response=self.client.get(url)

        self.assertEquals(response.status_code,200)

    def testAuth(self):
        url=reverse('api-auth')
        credentials={
            'username':'exa',
            'password':'463008'
        }
        response=self.client.post(url,credentials,format='json')
        
        self.assertEquals(response.status_code,200)
        self.assertTrue(response.data['access'])




