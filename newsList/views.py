from rest_framework import viewsets
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()