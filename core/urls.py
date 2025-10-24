from django.urls import path
from core import views


app_name = 'core'


urlpatterns = [
    path('',views.index, name='index'),
    path('client_membership_application/', views.client_membership_application, name='cli_create'),
    path('create/step2', views.cligeoposadd, name='cligeoposadd'),

]
