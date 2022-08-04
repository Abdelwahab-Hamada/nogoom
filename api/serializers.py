from rest_framework import serializers 
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username','password','id')
        extra_kwargs={
            'password':{'write_only': True},
        }
        
    def create(self,validated_data):
        req=self.context.get('request')
        username=req.data['username']
        password=req.data['password']

        user=User.objects.create_user(
            username=username,
            password=password)
        

        return user
    

   
        
        
