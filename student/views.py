from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Student


# Create your views here.
def students_view(request):
  all_students = Student.objects.all()
  return render(request, 'index.html', 
  {'all_items': all_students})

def addStudent(request):
  new_item = Student(content = request.POST['content'])
  new_item.save()
  return HttpResponseRedirect('/')

def deleteStudent(request, s_id):
  item_to_delete = Student.objects.get(id=s_id)
  item_to_delete.delete()
  return HttpResponseRedirect('/')
