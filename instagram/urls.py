from django.conf import settings
from django.conf.urls import url
from . import views
from django.conf.urls.static import static

urlpatterns=[
    
    url('^$',views.index,name = 'index'),
    url(r'^search/', views.search_images, name='search_results'),
    url(r'^image/(\d+)', views.get_image, name='image_results'),
    url(r'^new/image$', views.new_image, name='new-image'),
    url(r'^accounts/profile/$', views.user_profiles, name='profile'),
    url(r'^like/(\d+)', views.like_image, name='like_image'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
