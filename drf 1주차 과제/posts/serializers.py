from dataclasses import field
from rest_framework import serializers
from posts.models import Post
from comments.serializers import CommentSerializer

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many = True, read_only=True)
    class Meta:
        model = Post
        fields = "__all__"
    
