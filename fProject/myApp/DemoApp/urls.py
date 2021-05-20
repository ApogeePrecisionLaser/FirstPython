from django.urls import path

from . import views

urlpatterns = [
    path('',views.demo, name="home-page"),
    path('profile',views.profile),
    path('configuration',views.configuration),
    path('status',views.status),
    path('satellite_info',views.satellite_info),
    path('data_recode',views.data_recode),
    path('internet',views.internet),
    path('io_config',views.io_config),
    path('forward_upgrade',views.forward_upgrade),
    path('user_management',views.user_management),
    # path('',views.profile),
]