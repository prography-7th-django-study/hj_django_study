from rest_framework import serializers
from members.models import Member
from profiles.models import Profile
from .models import Post,Comment

class PostMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'id',
            'nickname',
            'image',
        )

class PostListSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    member_count = serializers.SerializerMethodField()
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
    def get_author(self, obj):
        id = obj.author.id
        profile = Profile.objects.get(id=id)
        serializer = PostMemberSerializer(profile)
        return serializer.data

    def get_comment_count(self, obj):
        queryset = Comment.objects.filter(post=obj)
        count = queryset.count()
        return count

    def get_member_count(self, obj):
        queryset = Member.objects.filter(post=obj, is_member = 'Co')
        count = queryset.count()
        return count

class PostSerializer(serializers.ModelSerializer):
    members = PostMemberSerializer(read_only=True, many=True)
    author = PostMemberSerializer()
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

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'author',
            'description',
            'parent',
            'post',
            'created_at',
            'updated_at',
        )