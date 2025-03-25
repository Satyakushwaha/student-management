from django.urls import path
from management import views
urlpatterns = [
    path('home/',views.home,name='home'),
    path('add/',views.add,name='add'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('update/<int:pk>',views.update,name='update'),
    path('register/',views.register,name='register'),
    path('',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout')


]