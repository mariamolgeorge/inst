from django.urls import path
from . import views

urlpatterns = [
    path('',views.hrget_home.as_view(),name='hrhome'),
    path('studentregister', views.get_register, name='studentregister'),
    path('trainerregister', views.get_trainer, name='trainerregister'),
    path('studentdisplay', views.display_student, name='studentdisplay'),
    path('displaytrainer', views.TrainerList.as_view(), name='displaytrainer'),
    path('deletetrainer/<int:pk>',views.TrainerUpdate.as_view(), name='deletetrainer'),
    path('edittrainer/<int:pk>',views.TrainerDelete.as_view(), name='edittrainer'),
]
