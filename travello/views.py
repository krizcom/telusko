from django.shortcuts import render,redirect
from .models import Food,Student
from .form import StudentForm

# Create your views here.

def index(request):

    food1 = Food()
    food1.name = 'Veggie'
    food1.food = 'Vegetable and fruits'
    food1.price = 200
    food1.img = '01.jpg'

    food2 = Food()
    food2.name = 'Pizza'
    food2.food = 'cheese and stuff'
    food2.price = 455
    food2.img = '02.jpg'

    food3 = Food()
    food3.name = 'watever'
    food3.food = 'Vegetable and fruits'
    food3.price = 208
    food3.img = '03.jpg'
 
    food4 = Food()
    food4.name = 'watever'
    food4.food = 'Vegetable and fruits'
    food4.price = 203
    food4.img = '04.jpg'

    foods = [food1,food2,food3,food4]
 
    return render(request,'index.html',{'foods': foods})

def show(request):
    students = Student.objects.all()
    return render(request,"show.html",{'student':students})

def edit(request, id):
    students = Student.objects.get(id=id)
    return render(request, 'edit.html',{'student':students})

def update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, '/edit.html', {'student': student})

def destroy(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("/show")

def create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = StudentForm()
    print("18" + str(form.__doc__))
    print("19" + str(form))
    return render(request, 'create.html', {'form': form})