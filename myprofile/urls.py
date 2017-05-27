from django.conf.urls import include,url
from . import views

urlpatterns=(
    url(r'^$',views.main,name='main'),
    url(r'^login/$',views.login,name='login'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^registrate/$',views.registrate,name='registrate'),
    url(r'^profile/$',views.profile,name='profile'),
    )
