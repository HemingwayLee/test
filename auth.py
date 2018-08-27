from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import auth 

# before use GET request, now we should use POST
#  or we can signout at frontend (remove token from header)
#  if we have nothing to destory in the backend database...
@require_http_methods(["GET"])
def signout(request):
  auth.logout(request)
  return render(request, 'form_template.html')

def signin(request):
  return render(request, 'form_template.html')

# HTTP/1.1" 405 will return if we other methods
@require_http_methods(["POST"])
def doSignin(request):

  # We can do it like this as well...
  # if request.method != 'POST':
  #   return HttpResponse("we support post request only")

  # We might not need this, because we need to check user's account and passowrd again
  # if request.user.is_authenticated: 
  #   return HttpResponseRedirect('/hello/')

  username = request.POST.get('username', '')
  password = request.POST.get('password', '')
  
  user = auth.authenticate(username=username, password=password)

  if user is not None and user.is_active:
    print("Successful, redirect to hello...")
    auth.login(request, user)
    return HttpResponseRedirect('/hello/')
  else:
    print("user not exist... redirect to signin page...")
    return render(request, 'form_template.html')

# This will return HTTP/1.1" 302
# @login_required
def hello(request):
  if request.user.is_authenticated: 
    return render(request, 'hello.html')
  else:
    return render(request, 'form_template.html')
