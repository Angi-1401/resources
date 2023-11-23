import django_filters
import string

from django_filters import widgets

from .models import *
from .forms import *


class FacultySchoolCareerFilter(django_filters.FilterSet):
    faculty = django_filters.ModelMultipleChoiceFilter(
        field_name="faculty",
        label="Facultad",
        queryset=Faculty.objects.all().order_by("name"),
    )

    school = django_filters.ModelMultipleChoiceFilter(
        field_name="school",
        label="Escuela",
        queryset=School.objects.all().order_by("name"),
    )

    career = django_filters.ModelMultipleChoiceFilter(
        field_name="career",
        label="Carrera",
        queryset=Career.objects.all().order_by("name"),
    )

    class Meta:
        model = Resource
        fields = ["faculty", "school", "career"]


class PublishDateFilter(django_filters.FilterSet):
    date = django_filters.NumberFilter(
        field_name="publish_date__year", label="Año de publicación", lookup_expr="exact"
    )

    class Meta:
        model = Resource
        fields = ["date"]


class AuthorFilter(django_filters.FilterSet):
    name = django_filters.ChoiceFilter(
        field_name="author",
        label="Apellido",
        choices=[(letter, letter) for letter in string.ascii_uppercase],
        method="filter_by_letter",
    )

    class Meta:
        model = Resource
        form = FilterByLetterForm
        fields = ["name"]

    def filter_by_letter(self, queryset, name, value):
        if value:
            queryset = queryset.filter(author__last_name__istartswith=value)
        return queryset


class TitleFilter(django_filters.FilterSet):
    title = django_filters.ChoiceFilter(
        field_name="title",
        label="Título",
        choices=[(letter, letter) for letter in string.ascii_uppercase],
        method="filter_by_letter",
    )

    class Meta:
        model = Resource
        form = FilterByLetterForm
        fields = ["title"]

    def filter_by_letter(self, queryset, name, value):
        if value:
            queryset = queryset.filter(title__istartswith=value)
        return queryset


class SubjectThemeFiler(django_filters.FilterSet):
    subject = django_filters.ModelMultipleChoiceFilter(
        field_name="subject",
        label="Materia",
        queryset=Subject.objects.all().order_by("name"),
    )

    theme = django_filters.ModelMultipleChoiceFilter(
        field_name="theme",
        label="Tema",
        queryset=Theme.objects.all().order_by("name"),
    )

    class Meta:
        model = Resource
        fields = ["subject", "theme"]


class AllFilter(django_filters.FilterSet):
    collection = django_filters.ModelMultipleChoiceFilter(
        field_name="collection",
        label="Colección",
        queryset=Collection.objects.all().order_by("name"),
    )

    faculty = django_filters.ModelMultipleChoiceFilter(
        field_name="faculty",
        label="Facultad",
        queryset=Faculty.objects.all().order_by("name"),
    )

    school = django_filters.ModelMultipleChoiceFilter(
        field_name="school",
        label="Escuela",
        queryset=School.objects.all().order_by("name"),
    )

    career = django_filters.ModelMultipleChoiceFilter(
        field_name="career",
        label="Carrera",
        queryset=Career.objects.all().order_by("name"),
    )

    author = django_filters.ChoiceFilter(
        field_name="author",
        label="Apellido del autor",
        choices=[(letter, letter) for letter in string.ascii_uppercase],
        method="filter_by_letter",
    )

    date = django_filters.NumberFilter(
        field_name="publish_date__year", label="Año de publicación", lookup_expr="exact"
    )

    subject = django_filters.ModelMultipleChoiceFilter(
        field_name="subject",
        label="Materia",
        queryset=Subject.objects.all().order_by("name"),
    )

    theme = django_filters.ModelMultipleChoiceFilter(
        field_name="theme",
        label="Tema",
        queryset=Theme.objects.all().order_by("name"),
    )

    class Meta:
        model = Resource
        fields = [
            "collection",
            "faculty",
            "school",
            "career",
            "date",
            "author",
            "subject",
            "theme",
        ]

    def filter_by_letter(self, queryset, name, value):
        if value:
            queryset = queryset.filter(author__last_name__istartswith=value)
        return queryset
