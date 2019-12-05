from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render
from django.urls import reverse_lazy

from adminapp.models import User,Course,Batch,Role,TimeTable,Placement,ClassRoom,Hr,Trainer,Feedback
from django.views.generic import TemplateView, ListView, CreateView
from django.views import generic
from adminapp.models import Course
# Create your views here.

class studentget_home(TemplateView):

    template_name = 'adminapp/studentbase.html'

class StudentFeedback(CreateView):
    model=Feedback

    fields=['user_name','batch_name','feedback_data','trainer_name','feedback_date']
    template_name = 'adminapp/studentfeedback.html'
    success_url=reverse_lazy('studentfeedback')







# Create your views here.

# Create your views here.
