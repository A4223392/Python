from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from api import views

# 创建路由器并注册我们的视图。
router = DefaultRouter()
router.register('music', views.MusicViewSet)
router.register('user', views.UserViewSet)


# API URL现在由路由器自动确定。
# 另外，我们还要包含可浏览的API的登录URL。
urlpatterns = [
    url('', include(router.urls)),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

