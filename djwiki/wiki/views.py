from django.http import HttpResponse

def index(req):
    return HttpResponse('<html><body>Hello World!</body></html>')