from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SnippetViewSet


router = DefaultRouter()
router.register(r'snippets', SnippetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = [
#     path('snippets/', views.snippet_list, name='snippet_list'),
#     path('snippets/<int:pk>/', views.snippet_detail, name='snippet_detail'),
# ]