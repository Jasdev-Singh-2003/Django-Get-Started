from django.urls import path
from MyWebApp.views import *

urlpatterns = [
  path('', HomeView, name='home'),
  path('contact/', contact, name='contact'),
  path('blog/', blog, name='blog'),
  path('error/', error, name='error'),
  path('userform/', userForm, name='userform'),
  path('djangoform/', djangoForm, name='djangoform'),
  path('about/', About.as_view(), name='about'),
  path('category/', category, name='category'),
  path('contacts/', contacts, name='contacts'),
  path('user/', user, name='user'),
  path('alldata/', alldata, name='alldata'),
  path('register/', register, name='register'),
  path('update/<int:id>', update, name='update'),
  path('delete/<int:id>', delete, name='delete'),
  path('products/', products, name='product'),
  path('products/<page>', products, name='products'),
]