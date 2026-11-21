from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name="Жанр")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Advertisement(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название рекламы")
    vast_url = models.URLField(blank=True, null=True, verbose_name="VAST XML ссылка на рекламу")
    video_file = models.FileField(upload_to='ads/', blank=True, null=True, verbose_name="Или рекламный видеофайл (mp4)")
    is_active = models.BooleanField(default=True, verbose_name="Активна ли реклама")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Реклама"
        verbose_name_plural = "Реклама перед видео"


class Movie(models.Model):
    TITLE_TYPES = (
        ('movie', 'Фильм'),
        ('series', 'Сериал'),
    )

    title = models.CharField(max_length=250, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    release_year = models.IntegerField(verbose_name="Год выпуска")
    genres = models.ManyToManyField(Genre, verbose_name="Жанры")
    poster = models.ImageField(upload_to='posters/', blank=True, null=True, verbose_name="Постер")
    poster_url = models.URLField(blank=True, null=True, verbose_name="Ссылка на постер (TMDB)")
    rating = models.FloatField(default=0.0, verbose_name="Рейтинг")
    content_type = models.CharField(max_length=10, choices=TITLE_TYPES, default='movie', verbose_name="Тип контента")

    video_file = models.FileField(upload_to='movies/', blank=True, null=True, verbose_name="Видео фильма (mp4)")
    trailer_url = models.URLField(blank=True, null=True, verbose_name="Ссылка на трейлер (YouTube)")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фильм / Сериал"
        verbose_name_plural = "Фильмы и Сериалы"


class Episode(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='episodes', verbose_name="Сериал")
    season_number = models.IntegerField(default=1, verbose_name="Номер сезона")
    episode_number = models.IntegerField(default=1, verbose_name="Номер серии")
    title = models.CharField(max_length=250, verbose_name="Название серии")
    video_file = models.FileField(upload_to='episodes/', verbose_name="Видео файла серии (mp4)")

    def __str__(self):
        return f"{self.movie.title} - Сезон {self.season_number} Серия {self.episode_number}: {self.title}"

    class Meta:
        verbose_name = "Серия сериала"
        verbose_name_plural = "Серии сериалов"