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
        read_only_fields = (
            'id',
            'created_at',
            'updated_at',
            'members',
        )

    def to_representation(self, instance):
        self.fields['author'] = MemberSummarizeSerializer(read_only=True)
        self.fields['members'] = MemberSummarizeSerializer(read_only=True, many=True)
        return super().to_representation(self.instance)

class CommentSerializer(serializers.ModelSerializer):
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
        read_only_fields = (
            'id',
            'created_at',
            'updated_at',
        )

    def to_representation(self, instance):
        self.fields['author'] = MemberSummarizeSerializer(read_only=True)
        return super().to_representation(self.instance)

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = (
            'id',
            'post',
            'member',
            'member_type',
        )