from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, CommentViewSet


router = DefaultRouter()
router.register(r'news', ArticleViewSet)
router.register(r'news/(?P<article_id>[^/.]+)/comments', CommentViewSet)
urlpatterns = router.urls
