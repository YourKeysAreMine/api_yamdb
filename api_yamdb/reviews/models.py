# Не забыть отсортировать импорты!

from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

User = get_user_model()


class Category(models.Model):
    """Это - категории произведений: Фильм, Книга, Музыка и.т.п."""
    name = models.CharField(max_length=50,
                            verbose_name='Наименование категории',
                            unique=True)
    slug = models.SlugField(max_length=15,
                            unique=True,
                            verbose_name='Название в адресной строке')

    class Meta:
        verbose_name = 'Категория произведений'
        verbose_name_plural = 'Категории произведений'

    def __str__(self):
        return self.name


class Genre(models.Model):
    """Это - наименование жанра произведения"""
    name = models.CharField(max_length=50,
                            verbose_name='Жанр',
                            unique=True)
    slug = models.SlugField(max_length=25,
                            unique=True,
                            verbose_name='Название жанра в адресной строке')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Title(models.Model):
    """Это - произведения с годом их выпуска и категорией произведения"""
    def get_deleted_user(self):
        return User.objects.get_or_create(username="deleted")[0]

    name = models.CharField(max_length=50,
                            verbose_name='Название фильма')
    # Подумать над тем, как сделать валидатор реального года!
    year = models.IntegerField()
    category = models.ForeignKey(
        Category,
        # ПОМЕНЯТЬ НА ЭТАПЕ ПАЙТЕСТА, ЕСЛИ ЧТО!
        on_delete=models.SET(get_deleted_user),
        related_name='categories',
        unique=True,
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name


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
        verbose_name = 'Жанр-Произведение'
        verbose_name_plural = 'Жанр-Произведение'

    def __str__(self):
        return self.name


class Review(models.Model):
    """Это - ревью к произведению"""
    def get_deleted_user(self):
        return User.objects.get_or_create(username="deleted")[0]

    title_id = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.TextField()
    author = models.ForeignKey(
        # ПОМЕНЯТЬ НА ЭТАПЕ ПАЙТЕСТА, ЕСЛИ ЧТО!
        User, on_delete=models.SET(get_deleted_user), related_name='authors')
    score = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        related_name='Оценка')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Ревью'
        verbose_name_plural = 'Ревью'
        constraints = [
            models.UniqueConstraint(fields=['title_id', 'author'],
                                    name='unique_review'),
        ]

    def __str__(self):
        return self.text


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
    author = models.ForeignKey(
        User, on_delete=models.SET(get_deleted_user), related_name='authors')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий к ревью'
        verbose_name_plural = 'Комментарии к ревью'

    def __str__(self):
        return self.text
