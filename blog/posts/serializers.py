from django.conf import settings
from rest_framework import serializers

from .models import Post

MAX_POST_LENGTH = settings.MAX_POST_LENGTH
POST_ACTION_OPTIONS = settings.POST_ACTION_OPTIONS

class PostCreateSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Post
        fields = ['id','content','likes']
    def get_likes(self,obj):
        return obj.likes.count()
    def validate_content(self, value):
        if len(value) > MAX_POST_LENGTH:
            raise serializers.ValidationError("Post Length is bigger than 261")
        return value

class PostSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only = True)
    # user = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Post
        fields = ['id','content','likes','title','image','user']

    def get_likes(self,obj):
        return obj.likes.count()


class PostActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()
    content = serializers.CharField(allow_blank = True, required = False)
    # Field-level validation
    def validate_action(self, value):
        value = value.strip().lower()
        if not value in POST_ACTION_OPTIONS:
            raise serializers.ValidationError('Invalid Action')
        return value