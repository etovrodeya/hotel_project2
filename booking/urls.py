from django.conf.urls import include,url
from . import views

urlpatterns=(
    url(r'^$',views.bookingCreate,name='create'),
    url(r'^list/$',views.bookingList,name='list'),
    url(r'^detail/(?P<booking_id>[0-9]+)/$',views.bookingDetail,name='detail'),
    url(r'^edit/(?P<booking_id>[0-9]+)/$',views.BookingEdit.as_view()),
    )
