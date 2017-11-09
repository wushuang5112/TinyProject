# Create your views here.
from django.http import HttpResponse
from tasks import add


def index(request):
	sync = add.delay(100, 1000)
	print dir(sync)
	print sync.task_id
	# print sync.get()
	return HttpResponse('Hello World')

