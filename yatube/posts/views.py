from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Добро пожаловать на главную страницу")


def group_posts(request, slug):
    return HttpResponse(f"Посты в группе {slug}")
