from django.http import HttpResponse
from lighthousedjango import models
import json

def success(request):
	return HttpResponse("that good succcc")

def cool_shit(request):
	result_str = ""
	for event in models.Event.objects.all():
		result_str += "started: " + str(event.start) + " ended: " + str(event.end) + " and it was called " + str(event.title) +"<br />"
	return HttpResponse(result_str)


def log_activity(request):
	if(request.method == "POST"):
		user = request.POST["user"]
		website = request.POST["website"]
		year =request.POST["start_year"]
		month =request.POST["start_month"]
		day = request.POST["start_day"]
		duration = request.POST["duration"]

def sign_in(request):
	if(request.method == "POST"):
		username =request.POST["username"]
		password = request.POST["password"]
