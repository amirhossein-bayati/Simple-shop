from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('customer/<str:user_id>/', views.customer, name="customer"),
    path('user/', views.userPage, name='user'),

    path('create_order/', views.createOrder, name="create_order"),
    path('update_order/<str:order_id>', views.updateOrder, name="update_order"),
    path('delete_order/<str:order_id>', views.deleteOrder, name="delete_order"),

    path('register/', views.register, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),

    path('setting/', views.accountSetting, name="account_setting"),


]

