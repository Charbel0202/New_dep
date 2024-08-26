from django.shortcuts import render, redirect
from .models import Student

# Create your views here.

def index(request):
    data = Student.objects.all().order_by('id')
    context = {"data": data}
    print(data)
    return render(request, "index.html", context)
    

def insertData(request):
    if request.method=="POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        age= request.POST.get('age')
        gender= request.POST.get('gender')
        query = Student(name=name, email=email, age=age, gender=gender)
        query.save()

    return redirect('index')


def delete(request, Student_id):
    try:
        student = Student.objects.get(id=Student_id)
        student.delete()
    except Student.DoesNotExist:
        pass
    return redirect("index")



def update(request, Student_id):
    dataUpdate = Student.objects.get(id=Student_id)
    print(dataUpdate)
    context = {"dataUpdate":dataUpdate}

    if request.method=="POST":
        dataUpdate.name = request.POST.get('name')
        dataUpdate.email = request.POST.get('email')
        dataUpdate.age = request.POST.get('age')
        dataUpdate.gender = request.POST.get('gender')
        dataUpdate.save()
        return redirect("/")


    return render(request, "update.html", context)