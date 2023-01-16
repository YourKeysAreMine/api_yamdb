from django.contrib.auth import get_user_model
from django.db import models

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


class Review(models.Model):
    """Это - ревью к произведению"""
    title_id = models.ForeignKey(
        Title, #Добавить модель Title на которую здесь сошлёмся!
        on_delete=models.CASCADE,
        related_name='rewievs'
    )
    text = models.TextField()
    authtor = models.ForeignKey(
        #Здесь при удалении автора я хочу оставить его комментарии, как сделать?
        User, on_delete=models.SET_DEFAULT, related_name='rewievs')
    score = models.IntegerField()
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
    review_id = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField()
    authtor = models.ForeignKey(
        #Здесь при удалении автора я хочу оставить его комментарии, как сделать?
        User, on_delete=models.SET_DEFAULT, related_name='comments')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий к ревью'
        verbose_name_plural = 'Комментарии к ревью'

    def __str__(self) -> str:
        return self.title
