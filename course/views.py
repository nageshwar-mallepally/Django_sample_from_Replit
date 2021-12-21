from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Course


# Create your views here.
def course_view(request):
    all_course = Course.objects.all()
    return render(request, 'index.html',
                  {'all_items': all_course})

def addCourse(request):
    new_item = Course(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/')

def deleteCourse(request, c_id):
    item_to_delete = Course.objects.get(id=c_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/')
