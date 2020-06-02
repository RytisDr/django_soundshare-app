#from django.conf import settings
from .models import IpAddresses
from django.shortcuts import get_object_or_404


class LogVisitorsMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        client_ip_address = request.META.get('REMOTE_ADDR')
        try:
            repeatedVisitor = IpAddresses.objects.get(
                ip_address=client_ip_address)
            repeatedVisitor.save()
            print("again")
        except:
            print("new")
            newVisitor = IpAddresses()
            newVisitor.ip_address = client_ip_address
            newVisitor.save()

        response = self.get_response(request)
        response["visitor log"] = "visitor log"
        return response
