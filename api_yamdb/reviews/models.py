# Не забыть отсортировать импорты!

from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

User = get_user_model()


class Category(models.Model):
    """Это - категории произведений: Фильм, Книга, Музыка и.т.п."""
    name = models.CharField(max_length=50,
                            verbose_name='Наименование категории')
    slug = models.SlugField(max_length=15,
                            unique=True,
                            verbose_name='Название в адресной строке'
                            )

    class Meta:
        verbose_name = 'Категория произведений'
        verbose_name_plural = 'Категории произведений'

    def __str__(self) -> str:
        return self.title


class Genre(models.Model):
    """Это - наименование жанра произведения"""
    name = models.CharField(max_length=50,
                            verbose_name='Жанр')
    slug = models.SlugField(max_length=25,
                            unique=True,
                            verbose_name='Название жанра в адресной строке'
                            )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self) -> str:
        return self.title


class Title(models.Model):
    """Это - фильмы с годом их выпуска и категорией произведения"""
    def get_deleted_user(self):
        return User.objects.get_or_create(username="deleted")[0]

    name = models.CharField(max_length=50,
                            verbose_name='Название фильма')
    # Подумать над тем, как сделать валидатор реального года!
    year = models.IntegerField()
    category = models.ForeignKey(
        Category,
        on_delete=models.SET(get_deleted_user),
        related_name='titles'
    )

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self) -> str:
        return self.title


class Genre_Title(models.Model):
    """Это - таблица многие ко многим, связывающая Genre и Title"""
    title_id = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='titles'
    )
    genre_id = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        related_name='genres'
    )

    class Meta:
        verbose_name = 'Жанр-Фильм'
        verbose_name_plural = 'Жанр-Фильм'

    def __str__(self) -> str:
        return self.title


class Review(models.Model):
    """Это - ревью к произведению"""
    def get_deleted_user(self):
        return User.objects.get_or_create(username="deleted")[0]

    title_id = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='rewievs'
    )
    text = models.TextField()
    authtor = models.ForeignKey(
        User, on_delete=models.SET(get_deleted_user), related_name='rewievs')
    score = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)])
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Ревью'
        verbose_name_plural = 'Ревью'
        constraints = [
            models.UniqueConstraint(fields=['title_id', 'author'],
                                    name='unique_follow')
        ]

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    """Это - комментарии к ревью фильма"""
    def get_deleted_user(self):
        return User.objects.get_or_create(username="deleted")[0]

    review_id = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField()
    authtor = models.ForeignKey(
        User, on_delete=models.SET(get_deleted_user), related_name='comments')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий к ревью'
        verbose_name_plural = 'Комментарии к ревью'

    def __str__(self) -> str:
        return self.title
