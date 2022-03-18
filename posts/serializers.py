from rest_framework import serializers
from accounts.models import User
from .models import Post, Comment, Member

class MemberSummarizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'nickname',
            'image',
        )

class PostSummarizeSerializer(serializers.ModelSerializer):
    author = MemberSummarizeSerializer()
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'image',
            'created_at',
            'updated_at',
            'author',
            'comment_count',
            'member_count',
        )

class PostSerializer(serializers.ModelSerializer):
    members = MemberSummarizeSerializer(read_only=True, many=True)
    author = MemberSummarizeSerializer(read_only=True)
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

    def create(self, validated_data):
        validated_data["author"] = self.context.get("request").user
        return super().create(validated_data)

class CommentSerializer(serializers.ModelSerializer):
    author = MemberSummarizeSerializer(read_only=True)
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

    def create(self, validated_data):
        validated_data["author"] = self.context.get("request").user
        return super().create(validated_data)

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = (
            'id',
            'post',
            'member',
            'member_type',
        )