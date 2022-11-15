from django.shortcuts import render, redirect
from .forms import CourseForm
from .models import Course
from django.contrib import messages

def course(request):
    course = Course.objects.all()
    form = CourseForm()
    context = {
        'course':course, 
        'form':form
    }
    return render(request, 'register/index.html', context)

def register(request):

    if request.method == 'POST':
        form = CourseForm(request.POST or None)
        if form.is_valid():
            id_course = form.cleaned_data.get('id_course')
            name = form.cleaned_data.get('name')
            credit = form.cleaned_data.get('credit')

            course = Course.objects.create(id_course=id_course, name=name, credit=credit)
            messages.success(request, f'{name}, successfully registered')

            return redirect('index')
    else:
        form = CourseForm()
        messages.error(request, f'{id_course}, had been already registered')
    return redirect('index')

def remove(request, id_course):
    Course.objects.filter(id_course=id_course).delete()
    return redirect('index')

def edit(request, id_course):
    course = Course.objects.get(id_course=id_course)
    return render(request, 'register/edit.html', {'course':course})

def new_data(request):
    form = CourseForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        id_course = form.cleaned_data.get('id_course')
        print(id_course)
        # name = form.cleaned_data.get('name')
        # credit = form.cleaned_data.get('credit')
        #     course = Course.objects.get(id_course=id_course)
        #     course.name = name
        #     course.credit = credit
        #     course.save()
    return redirect('index')
    

    