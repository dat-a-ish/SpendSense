from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required


# @login_required
def hello_world(request):
    return HttpResponse("Hello, World!")
