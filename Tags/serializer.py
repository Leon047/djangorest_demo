from rest_framework import serializers

from .models import Tags, Users


class TagsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tags
        fields = ['languages', 'tags']

class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['user_name', 'tags']
