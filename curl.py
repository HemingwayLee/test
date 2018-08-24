from django.http import HttpResponse
from .models import Question

def insert(request):
  q = Question(name='ywlee', age=33)
  q.save()
  return HttpResponse("Created!! the id is " + str(q.id))

def delete(request):
  q = Question.objects.filter(id=2)
  q.delete()
  return HttpResponse("Hello, check your console")

def update(request):
  q = Question.objects.filter(id=1)
  q.update(name='rose')
  return HttpResponse("Hello, check your console")

def search(request):
  output = ""
  for val in Question.objects.all().values():
    output += val['name'] + "<br>"

  return HttpResponse(output)
