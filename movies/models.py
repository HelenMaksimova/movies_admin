import uuid

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class FilmWorkType(models.TextChoices):
    movie = "movie", _("movie")
    tv_show = "tv_show", _("tv show")


class PersonType(models.TextChoices):
    actor = "actor", _("actor")
    director = "director", _("director")
    writer = "writer", _("writer")


class Genre(TimeStampedMixin, UUIDMixin):
    name = models.CharField(_("name"), max_length=255, unique=True)
    description = models.TextField(_("description"), blank=True, null=True)

    class Meta:
        db_table = f'{settings.CONTENT_SCHEMA}"."genre'
        verbose_name = _("Genre")
        verbose_name_plural = _("Genres")

    def __str__(self) -> str:
        return self.name


class Person(TimeStampedMixin, UUIDMixin):
    full_name = models.CharField(_("full name"), max_length=255)

    class Meta:
        db_table = f'{settings.CONTENT_SCHEMA}"."person'
        verbose_name = _("Person")
        verbose_name_plural = _("Persons")
        indexes = [
            models.Index(fields=["full_name"], name="person_full_name_idx"),
        ]

    def __str__(self) -> str:
        return self.full_name


class FilmWork(TimeStampedMixin, UUIDMixin):
    title = models.TextField(_("title"))
    description = models.TextField(_("description"), blank=True, null=True)
    creation_date = models.DateField(_("creation date"), blank=True, null=True)
    rating = models.FloatField(
        _("rating"),
        blank=True,
        null=True,
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],
    )
    type = models.CharField(
        _("type"),
        max_length=255,
        choices=FilmWorkType.choices,
        default=FilmWorkType.movie,
    )
    genres = models.ManyToManyField(Genre, through="GenreFilmWork")
    persons = models.ManyToManyField(Person, through="PersonFilmWork")

    class Meta:
        db_table = f'{settings.CONTENT_SCHEMA}"."film_work'
        verbose_name = _("Film work")
        verbose_name_plural = _("Film works")
        indexes = [
            models.Index(fields=["rating"], name="film_work_rating_idx"),
            models.Index(
                fields=["title", "creation_date"],
                name="film_work_title_date_idx",
            ),
        ]

    def __str__(self) -> str:
        return self.title


class GenreFilmWork(UUIDMixin):
    film_work = models.ForeignKey("FilmWork", on_delete=models.CASCADE)
    genre = models.ForeignKey("Genre", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = f'{settings.CONTENT_SCHEMA}"."genre_film_work'
        verbose_name = _("Film work genre")
        verbose_name_plural = _("Film work genres")
        unique_together = [["film_work", "genre"]]


class PersonFilmWork(UUIDMixin):
    film_work = models.ForeignKey("FilmWork", on_delete=models.CASCADE)
    person = models.ForeignKey("Person", on_delete=models.CASCADE)
    role = models.CharField(
        _("role"),
        max_length=16,
        choices=PersonType.choices,
        default=PersonType.actor,
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = f'{settings.CONTENT_SCHEMA}"."person_film_work'
        verbose_name = _("Film work person")
        verbose_name_plural = _("Film work persons")
        unique_together = [["film_work", "person", "role"]]
