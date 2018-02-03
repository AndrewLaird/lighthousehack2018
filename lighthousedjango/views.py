from django.http import HttpResponse
from lighthousedjango import models


def success(request):
	return HttpResponse("that good succcc")

def cool_shit(request):
	result_str = ""
	for event in models.Event.objects.all():
		result_str += "started: " + event.start + " ended: " + event.end + " and it was called " + event.title +"\n"
	return HttpResponse(result_str)