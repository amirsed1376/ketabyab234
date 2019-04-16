from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'login', views.login, name='login'),
    url(r'signup', views.sign_up, name='signup'),
    # url(r'home' ,views.home , name='home')
    ]