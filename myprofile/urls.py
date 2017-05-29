from django.conf.urls import include,url
from . import views

urlpatterns=(
    url(r'^$',views.main,name='main'),
    url(r'^login/$',views.login,name='login'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^registrate/$',views.registrate,name='registrate'),
    url(r'^profile/$',views.profile,name='profile'), 
    url(r'^imageLoad/$', views.imageLoad, name='imageLoad'),
    url(r'^budget-room/$', views.BudgetView.as_view(), name='budget'),
    url(r'^lux-room/$', views.LuxView.as_view(), name='lux'),
    url(r'^business-room/$', views.BusinessView.as_view(), name='business'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    
    )
