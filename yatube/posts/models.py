from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField("Наименование", max_length=200)
    slug = models.SlugField("Адрес", unique=True, null=True)
    description = models.TextField("Описание")

    class Meta:
        verbose_name = "группa"
        verbose_name_plural = "группы"

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    text = models.TextField("Текст")
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="Автор",
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="posts",
        verbose_name="группа",
    )

    class Meta:
        ordering = ("-pub_date",)
        verbose_name = "пост"
        verbose_name_plural = "посты"
