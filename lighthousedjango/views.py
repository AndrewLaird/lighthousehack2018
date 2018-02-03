from django.http import HttpResponse
from lighthousedjango import models


def success(request):
	return HttpResponse("that good succcc")

def cool_shit(request):
	result_str = ""
	for event in models.Event.objects.all():
		result_str += "started: " + str(event.start) + " ended: " + str(event.end) + " and it was called " + str(event.title) +"<br />"
		#result_str = result_str.replace('\n', '<br />') this is a conflict
	return HttpResponse(result_str)
