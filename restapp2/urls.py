from django.conf.urls import url
from .import views
app_name='restapp2'

urlpatterns=[
    url(r'^$', views.input, name='input'),
    url(r'^insert$',views.insert,name='insert'),
    url(r'^display$',views.display,name='display'),
    url(r'^productapi$',views.productlist.as_view()),
]