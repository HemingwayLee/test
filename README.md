```python
from django.contrib.auth.models import User
from django.contrib.auth.middleware import get_user
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.conf import settings
from .models import LoginFailedIpTable

class blockerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f"call {request.path} {request.method}")
        if "login" in request.path and request.method == "POST":
            ip = self.get_client_ip(request)
            print(f"ip is {ip}")
            if self.is_ip_blocked(ip):
                print("blocked!")
                return JsonResponse({"message": "ip is blocked"}, status=400)

            print("not blocked")
            res = self.get_response(request)
            if not self.is_login_success(res):
                print("logging not success")
                history = LoginFailedIpTable.objects.filter(ip=ip).first()
                if history is None:
                    print("first time!!")
                    rec = LoginFailedIpTable(ip=ip, retry=1)
                    rec.save()
                else:
                    print(f"{history.retry} times!!")
                    history.retry += 1
                    history.save()

            return res
        else:
            return self.get_response(request)
        

    def is_login_success(self, response):
        if response.status_code == 200:
            return True
        else:
            return False

    def is_ip_blocked(self, ip):
        history = LoginFailedIpTable.objects.filter(ip=ip).first()

        # print(timezone.now())
        # print(history.updated)
        # print(timezone.timedelta(minutes=1))
        if history is not None and history.retry >= settings.LOGIN_RETRY_TIMES and timezone.now() < history.updated + timezone.timedelta(minutes=settings.LOGIN_WAIT_MINUTES):
            history.retry = 1
            history.save()
            return True

        return False

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

```



https://user-images.githubusercontent.com/8428372/84728084-6b33cc00-afcb-11ea-8954-b52a10213136.png


