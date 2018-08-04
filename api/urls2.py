from django.urls import path,include,re_path
from rest_framework.urlpatterns import format_suffix_patterns

from api import views
'''
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('music',views.MusicViewSet)
'''

urlpatterns = [
    #path('',include(router.urls))
    path('music/',views.music_list),
    path('music/<int:pk>/',views.music_detail),
    #re_path(r'^music/$', views.music_list),
    #re_path(r'^music/(?P<pk>[0-9]+)/$', views.music_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)