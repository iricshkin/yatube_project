from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest

# Импортируем модель, чтобы обратиться к ней
from .models import Post, Group

POST_PER_PAGE = 10


def index(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all()[:POST_PER_PAGE]
    template = "posts/index.html"
    # В словаре context отправляем информацию в шаблон
    context = {
        "posts": posts,
    }
    return render(request, template, context)


# View-функция для страницы сообщества:
def group_posts(request: HttpRequest, slug: str) -> HttpResponse:
    template = "posts/group_list.html"
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:POST_PER_PAGE]
    context = {
        "group": group,
        "posts": posts,
    }
    return render(request, template, context)
