from django.urls import path
from . import views

urlpatterns = [
    path('',views.studentget_home.as_view(),name='studenthome'),
    path('studentfeedback', views.StudentFeedback.as_view(), name='studentfeedback'),


]
