from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns

from api import views


# API endpoints
urlpatterns = format_suffix_patterns([  
    path('',views.api_root),
    path('music/',views.MusicList.as_view(),name='music-list'),
    path('music/<int:pk>/',views.MusicDetail.as_view(),name='music-detail'),
    path('music/<int:pk>/highlight/',views.MusicHighlight.as_view(),name='music-highlight'),
    path('user',views.UserList.as_view(),name='user-list'),
    path('user/<int:pk>/',views.UserDetail.as_view(),name='user-detail')   
])

# 可瀏覽API的登錄和註銷視圖
urlpatterns +=[
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
]

