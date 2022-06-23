from django.urls import path
from . import views

urlpatterns = [
      path('',views.ApiOverview,name='home'),
      path('signup/',views.signup,name='signup'),
      path('login/',views.login,name='login'),
      path('show/',views.show,name='show'),
      path('info/',views.info,name='info'),
      path('enroll/',views.enroll,name='enroll'),
]