from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import Http404
from wiki.models import Page

# def index(req):
#     return HttpResponse('<html><body>Hello World!</body></html>')


def home(request):
	return render_to_response("home.html",{
		"page" : Page.objects.all().order_by('name')
	})
 
def page_specific(request, page_id):
	try:
		p = Page.objects.get(pk=page_id)
	except:
		raise Http404
 
	return render_to_response("page_specific.html",{
		"page" : p
	})
