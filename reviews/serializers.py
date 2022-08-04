from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Review

class Serializer(serializers.ModelSerializer):
    is_stared=serializers.SerializerMethodField(read_only=True)

    details=serializers.HyperlinkedIdentityField(
        view_name='review',
        lookup_field='pk',
        format=None
    )

    star=serializers.HyperlinkedIdentityField(
        view_name='star-review',
        lookup_field='pk',
        format=None
    )

    class Meta:
        model=Review
        fields=('id','score','comment','title','created','reviewer','tags','is_stared','star','details')
        read_only_fields=('reviewer',)
        extra_kwargs={
            'tags':{'write_only': True},
        }

    def create(self,validated_data):
        validated_data['reviewer']=self.context.get('request').user
        
        review=super().create(validated_data)
        
        return review

    

    def get_is_stared(self,obj):
            logged_user=self.context.get('request').user
            return logged_user in obj.stars.all()

class StarSerializer(serializers.ModelSerializer):
    is_stared=serializers.SerializerMethodField(read_only=True)

    class Meta:
        model=Review
        fields=('id','is_stared')

    def update(self,instance,validated_data):
        logged_user=self.context.get('request').user
        
        if logged_user in instance.stars.all():
            instance.stars.remove(logged_user)
        else:
            instance.stars.add(logged_user)
        
        return super().update(instance,validated_data)

    def get_is_stared(self,obj):
            logged_user=self.context.get('request').user
            return logged_user in obj.stars.all()
