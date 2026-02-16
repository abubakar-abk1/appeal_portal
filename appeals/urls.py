from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('submit_appeal/', views.submit_appeal, name='submit_appeal'),
    path('page/<str:pk>', views.page, name='page'),
]
