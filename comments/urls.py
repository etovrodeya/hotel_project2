from django.conf.urls import include,url
from . import views

urlpatterns=(
    url(r'^$',views.commentList,name='list'),
    url(r'^review/$',views.commentReview,name='review'),
    url(r'^detail/(?P<comment_id>[0-9]+)/$',views.commentDetail,name='detail'),
    
    )
