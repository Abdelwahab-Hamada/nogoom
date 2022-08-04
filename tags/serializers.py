from rest_framework import serializers 
from .models import Tag

class Serializer(serializers.ModelSerializer):
    is_follower=serializers.SerializerMethodField()

    follow=serializers.HyperlinkedIdentityField(
        view_name='follow-tag',
        lookup_field='slug',
        format=None
    )
    details=serializers.HyperlinkedIdentityField(
        view_name='tag',
        lookup_field='slug',
        format=None
    )
    reviews=serializers.HyperlinkedIdentityField(
        view_name='tag-reviews',
        lookup_field='slug',
        format=None
    )

    class Meta:
        model=Tag
        fields=('id','slug','label','is_follower','created','follow','details','reviews')
        lookup_field = 'slug'
    
    def get_is_follower(self,obj):
        logged_user=self.context.get('request').user
        
        return logged_user in obj.followers.all()

class FollowSerializer(serializers.ModelSerializer):
    is_follower=serializers.SerializerMethodField()

    class Meta:
        model=Tag
        fields=('id','is_follower')

    def update(self,instance,validated_data):
        logged_user=self.context.get('request').user
        
        if logged_user in instance.followers.all():            
            instance.followers.remove(logged_user)
        else:
            instance.followers.add(logged_user)
        
        return super().update(instance,validated_data)

    def get_is_follower(self,obj):
        logged_user=self.context.get('request').user
        
        return logged_user in obj.followers.all()

