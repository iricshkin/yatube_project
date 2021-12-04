from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Импортируем модель, чтобы обратиться к ней
from .models import Post, Group


# Create your views here.
def index(request):
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by("-pub_date")[:10]
    template = "posts/index.html"
    # В словаре context отправляем информацию в шаблон
    context = {
        "posts": posts,
    }
    return render(request, template, context)


# View-функция для страницы сообщества:
def group_posts(request, slug):
    template = "posts/group_list.html"
    group = get_object_or_404(Group, slug=slug)
    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by("-pub_date")[:10]
    context = {
        "group": group,
        "posts": posts,
    }
    return render(request, template, context)
