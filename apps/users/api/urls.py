from django.urls import path 
from . import views
users_urlpatters=([
    path('list-user/',views.ListUser,name='list-user'),
    path('detail-user/<pk>',views.DetailUser,name='detail-user'),
    path('create-user/',views.CreateUser,name='create-user'),
    path('update-user/<pk>',views.UpdateUser,name='update'),
    path('delete-user/<pk>',views.DeleteUser,name='delete-user')
],'users')