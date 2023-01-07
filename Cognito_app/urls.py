from django.urls import path
from django.views.generic.base import TemplateView
from . import views


urlpatterns = [
    path('', views.user_login,name='login'),
    path('registration/', views.user_registration,name='registration'),
    #path('dashboard/',views.show_quicksight_dashboard,name='dashboard'),
    path('forbidden/', TemplateView.as_view(template_name= 'pages_error403.html')),
    path('forbidden/login/', TemplateView.as_view(template_name= 'index.html')),
]