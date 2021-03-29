from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home' ),
    path('add/',views.create,name='create'),
    path('put/<str:pk>/',views.update,name='update'),
    path('del/<str:pk>/',views.delete,name='delete')
]
