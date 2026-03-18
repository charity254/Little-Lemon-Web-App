from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    # Add the remaining URL path configurations here
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('dashboard/login/', views.dashboard_login, name="dashboard_login"),
    path('dashboard/logout/', views.dashboard_logout, name="dashboard_logout"),
    path('dashboard/delete_booking/<int:pk>/', views.delete_booking, name="delete_booking"),
    path('dashboard/delete_menu_item/<int:pk>/', views.delete_menu_item, name="delete_menu_item"),
    path('dashboard/add_menu_item/', views.add_menu_item, name="add_menu_item"),
    path('dashboard/edit_menu_item/<int:pk>/', views.edit_menu_item, name="edit_menu_item"),
    path('dashboard/add_booking/', views.add_booking, name="add_booking"),
]