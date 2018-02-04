from django.http import HttpResponse
from lighthousedjango.models import Event,User
from lighthousedjango.serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt

def success(request):
	return HttpResponse("that good succcc")

def cool_shit(request):
	result_str = ""
	for event in Event.objects.all():
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

@csrf_exempt
def sign_in(request):
	if(request.method == "POST"):
		username =request.POST["username"]
		password = request.POST["password"]
		try:
			user = User.objects.get(username=username,hashed_password=password)
		except:
			return HttpResponse(str(-1), 200)
		return HttpResponse(str(user.pk), 200)
	elif(request.method == "GET"):
		username = request.GET["username"]
		password = request.GET["password"]
		try:
			user = User.objects.get(username=username, hashed_password=password)
		except:
			return HttpResponse(str(-1), 200)
		return HttpResponse(str(user.pk), 200)
	return HttpResponse("hello")


@csrf_exempt
def sign_up(request):
	if(request.method == "POST"):
		username = request.POST["username"]
		password = request.POST["password"]
		black_list = {
			"reddit":30,
			"facebook":25,
			"twitter":15,
			"tumblr":10,
			"youtube":15,
			"instagram":40
		}
		json_black_list = str(black_list)
		json_totals = "{}"
		data = {
			"username":username,
			"hashed_password":password,
			"blocked_websites":json_black_list,
			"totals":json_totals,
		}
		new_user = UserSerializer(data=data)
		new_user.run_validation(data=data)
		if (new_user.is_valid()):
			new_user.save()
			return HttpResponse("Model created sucessfully", 200)
		else:
			return HttpResponse("Could not create model",400)
	if (request.method == "GET"):
		username = request.GET["username"]
		password = request.GET["password"]
		black_list = {
			"reddit": 30,
			"facebook": 25,
			"twitter": 15,
			"tumblr": 10,
			"youtube": 15,
			"instagram": 40
		}
		json_black_list = str(black_list)
		json_totals = "{}"
		data = {
			"username": username,
			"hashed_password": password,
			"blocked_websites": json_black_list,
			"totals": json_totals,
		}
		new_user = UserSerializer(data=data)
		new_user.run_validation(data=data)
		if (new_user.is_valid()):
			new_user.save()
			return HttpResponse("Model created sucessfully", 200)
		else:
			return HttpResponse("Could not create model", 400)
