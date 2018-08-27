from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
  HTTP_400_BAD_REQUEST,
  HTTP_404_NOT_FOUND,
  HTTP_200_OK
)
from rest_framework.response import Response

# Most views requires CSRF protection, but a few do not.
#  We don't need csrf token for this function
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
  username = request.data.get("username")
  password = request.data.get("password")
  
  if username is None or password is None:
    return Response({'error': 'Please provide both username and password'}, status=HTTP_400_BAD_REQUEST)
  
  user = authenticate(username=username, password=password)
  
  if not user:
    return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)
  
  token, _ = Token.objects.get_or_create(user=user)
  return Response({'token': token.key}, status=HTTP_200_OK)

# We need to send the following key/value in header 
#  Authorization: Token <token>
@csrf_exempt
@api_view(["GET"])
def sample_api(request):
  print(request.user)
  print(request.user.id)
  print(request.auth)

  data = {'sample_data': 123}
  return Response(data, status=HTTP_200_OK)


# Ref: https://medium.com/quick-code/token-based-authentication-for-django-rest-framework-44586a9a56fb





