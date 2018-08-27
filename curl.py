from django.http import HttpResponse
from .models import Question

def insert(request, name, age):
  qs = Question(name=name, age=age)
  qs.save()
  return HttpResponse("Created!! the id is " + str(qs.id))

def delete(request, qid):
  qs = Question.objects.filter(id=qid)
  
  # we can delete directly, it is fine. No exception
  # qs.delete()
  
  if qs.count() == 0:
    return HttpResponse("Not found!!")
  else:
    qs.delete()
    return HttpResponse("Delete!!")
  
def update(request, qid, name):
  qs = Question.objects.filter(id=qid)
  
  # we can update directly, it is fine. No exception
  # qs.update(name=name)

  # both ok
  # if qs.count() == 0:
  if not qs.exists():
    return HttpResponse("Not found!!")
  else:
    qs.update(name=name)
    return HttpResponse("Updated!!")

def show_all(request):
  output = ""
  for val in Question.objects.all().values():
    output += str(val['id']) + " " + val['name'] + " " + str(val['age']) + "<br>"

  return HttpResponse(output)

def update2(request, name, age):
  question, created = Question.objects.update_or_create(
    name=name, age=age)
  
  if created:
      return HttpResponse("new Question object created!!")
  else:
      return HttpResponse("Question object exists!!")




