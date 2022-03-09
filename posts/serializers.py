from rest_framework import serializers
from accounts.models import User
from .models import Post,Comment

class PostMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'nickname',
            'image',
        )

class PostListSerializer(serializers.ModelSerializer):
    author = PostMemberSerializer(read_only=True)
    class Meta:
        model = Post
        fields = (
            'title',
            'image',
            'created_at',
            'updated_at',
            'author',
            'comment_count',
            'member_count',
        )

class PostSerializer(serializers.ModelSerializer):
    members = PostMemberSerializer(read_only=True, many=True)
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'description',
            'image',
            'created_at',
            'updated_at',
            'author',
            'members',
        )

class CommentWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'author',
            'description',
            'parent',
            'post',
            'created_at',
            'updated_at',
        )

class CommentReadSerializer(serializers.ModelSerializer):
    author = PostMemberSerializer()
    class Meta:
        model = Comment
        fields = (
            'id',
            'author',
            'description',
            'parent',
            'post',
            'created_at',
            'updated_at',
        )