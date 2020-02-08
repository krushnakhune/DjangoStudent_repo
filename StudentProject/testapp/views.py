from django.shortcuts import render,redirect
from .models import StudentData

def home(request):
    students=StudentData.objects.all()
    return render(request,'testapp/home.html',{'students':students})

def add_student(request):
    return render(request,'testapp/add_student.html')

def create(request):
    roll=request.POST.get("roll")
    fname=request.POST.get("fname")
    lname=request.POST.get("lname")
    cls=request.POST.get("cls")
    section=request.POST.get("sec")
    telugu=request.POST.get("telugu")
    hindi=request.POST.get("hindi")
    english=request.POST.get("english")
    math=request.POST.get("math")
    science=request.POST.get("science")
    social=request.POST.get("social")

    data=StudentData(
        student_roll=roll,
        student_fname=fname,
        student_lname=lname,
        student_class=cls,
        student_section=section,
        telugu=telugu,
        hindi=hindi,
        english=english,
        maths=math,
        science=science,
        social=social
    )
    data.save()
    students=StudentData.objects.all()
    return render(request,'testapp/home.html',{'students':students})

def edit_student(request,id):
    students=StudentData.objects.get(pk=id)
    return render(request,'testapp/edit_student.html',{'students':students})

def update_student(request,id):
    students=StudentData.objects.get(pk=id)
    students.student_roll=request.POST.get('roll')
    students.student_fname=request.POST.get('fname')
    students.student_lname=request.POST.get('lname')
    students.student_class=request.POST.get('cls')
    students.student_section=request.POST.get('sec')
    students.telugu=request.POST.get('telugu')
    students.hindi=request.POST.get('hindi')
    students.english=request.POST.get('english')
    students.maths=request.POST.get('maths')
    students.science=request.POST.get('science')
    students.social=request.POST.get('social')
    students.save()
    return redirect('/')

def delete_student(request,id):
    students=StudentData.objects.get(pk=id)
    students.delete()
    return redirect('/')