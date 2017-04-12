from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^other_details$', views.other_details, name='other_details'),
    url(r'^pincode$', views.pincode, name='pincode'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]