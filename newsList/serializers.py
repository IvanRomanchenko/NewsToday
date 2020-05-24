from rest_framework import serializers
from .models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'link', 'created', 'upvotes', 'author')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('article', 'name', 'content', 'created')