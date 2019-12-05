from django.shortcuts import render
from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import render,redirect,get_object_or_404

from adminapp.models import User,Course,Batch,Role,TimeTable,Placement,ClassRoom,Hr,Trainer
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from hrapp.forms import Student_form,Trainer_form,displaystudent_form,displaytrainer_form
# Create your views here.


class hrget_home(TemplateView):

    template_name = 'adminapp/hrbase.html'



def get_register(request):
    if request.method=='GET':
        obj=Student_form()
        return render(request, 'adminapp/studentregister.html', {'form':obj})
    if request.method=='POST':
        form=Student_form(request.POST)

        if form.is_valid():
            name = form.cleaned_data['user_name']
            address=form.cleaned_data['user_address']
            mobile=form.cleaned_data['user_mobile']
            doj=form.cleaned_data['user_doj']
            email=form.cleaned_data['user_email']
            username=form.cleaned_data['user_username']
            user_password=form.cleaned_data['user_password']
            confirmpassword=form.cleaned_data['confirm_password']
            coursename=form.cleaned_data['course_name']
            batchname=form.cleaned_data['batch_name']
            userpayment=form.cleaned_data['user_payment']
            rolename=form.cleaned_data['role_name']
            img=form.cleaned_data['image']

        try:
            # obj = User(username=name,email=email1, address=address1, password=passw1,coursename=course1,batch=batch1)
            form.save()
        except Exception as e:
            print(e.args)
        obj = Student_form()
        return render(request,  'adminapp/studentregister.html', {'form': obj})
        msg = "Data Inserted Sucessfully!!!!!!!!1"


def get_trainer(request):
    if request.method == 'GET':
        obj = Trainer_form()
        return render(request, 'adminapp/trainerregister.html', {'form': obj})
    if request.method == 'POST':
        form = Trainer_form(request.POST)

        if form.is_valid():
            coursename = form.cleaned_data['course_name']
            trainername=form.cleaned_data['trainer_name']
            trainermobile = form.cleaned_data['trainer_mobile']
            trainerdoj = form.cleaned_data['trainer_doj']
            traineremail = form.cleaned_data['trainer_email']
            trainerusername = form.cleaned_data['trainer_username']
            trainerpassword = form.cleaned_data['trainer_password']
            rolename = form.cleaned_data['role_name']

        try:
            # obj = User(username=name,email=email1, address=address1, password=passw1,coursename=course1,batch=batch1)
            form.save()
        except Exception as e:
            print(e.args)
        obj = Trainer_form()
        return render(request, 'adminapp/trainerregister.html', {'form': obj})
        msg = "Data Inserted Sucessfully!!!!!!!!1"




def display_student(request):
    if request.method=='GET':
        obj=Student_form()
        return render(request, 'adminapp/studentregister.html', {'form':obj})
    if request.method=='POST':
        form=Student_form(request.POST)

        if form.is_valid():
            name = form.cleaned_data['user_name']
            address=form.cleaned_data['user_address']
            mobile=form.cleaned_data['user_mobile']
            doj=form.cleaned_data['user_doj']
            email=form.cleaned_data['user_email']
            username=form.cleaned_data['user_username']
            user_password=form.cleaned_data['user_password']
            confirmpassword=form.cleaned_data['confirm_password']
            coursename=form.cleaned_data['course_name']
            batchname=form.cleaned_data['batch_name']
            userpayment=form.cleaned_data['user_payment']
            rolename=form.cleaned_data['role_name']
            img=form.cleaned_data['image']

        try:
            # obj = User(username=name,email=email1, address=address1, password=passw1,coursename=course1,batch=batch1)
            form.save()
        except Exception as e:
            print(e.args)
        obj = Student_form()
        return render(request,  'adminapp/studentregister.html', {'form': obj})
        msg = "Data Inserted Sucessfully!!!!!!!!1"

class TrainerList(ListView):
    model = Trainer
    template_name = 'adminapp/displaytrainer.html'
    context_object_name = 'object1'

class TrainerUpdate(UpdateView):
    model = Trainer
    exclude=['trainer_usernamr','trainer_password','trainer_doj']
    template_name = 'adminapp/traineredit.html'
    success_url = reverse_lazy('displaytrainer')
class TrainerDelete(DeleteView):
    model = Trainer
    fields='__all__'
    #template_name = 'classapp/dele1.html'
    success_url = reverse_lazy('view_list')