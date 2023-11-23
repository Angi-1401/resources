from typing import Any
from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic
from django.views.decorators.http import require_GET
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

from .models import *
from .filters import *
from .tables import *


# Create your views here.
class CollectionListView(generic.ListView):
    model = Collection
    template_name = "library/collection.html"
    context_object_name = "collections"


class ResourcesListView1(SingleTableMixin, FilterView):  # FacultySchoolCareerFilter
    table_class = ResourceTable
    model = Resource
    template_name = "library/resource.html"
    filterset_class = FacultySchoolCareerFilter


class ResourcesListView2(SingleTableMixin, FilterView):  # PublishDateFilter
    table_class = ResourceTable
    model = Resource
    template_name = "library/resource.html"
    filterset_class = PublishDateFilter


class ResourcesListView3(SingleTableMixin, FilterView):  # AuthorFilter
    table_class = ResourceTable
    model = Resource
    template_name = "library/resource.html"
    filterset_class = AuthorFilter


class ResourcesListView4(SingleTableMixin, FilterView):  # TitleFilter
    table_class = ResourceTable
    model = Resource
    template_name = "library/resource.html"
    filterset_class = TitleFilter


class ResourcesListView5(SingleTableMixin, FilterView):  # SubjectThemeFiler
    table_class = ResourceTable
    model = Resource
    template_name = "library/resource.html"
    filterset_class = SubjectThemeFiler


class ResourcesListView6(SingleTableMixin, FilterView):  # AllFilter
    table_class = ResourceTable
    model = Resource
    template_name = "library/resource.html"
    filterset_class = AllFilter


class ResourceDetailView(generic.DetailView):
    model = Resource
    template_name = "library/resource_detail.html"
    context_object_name = "resource"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        uuid = self.kwargs.get("pk")
        context["uuid"] = uuid

        resource = context["resource"]

        if resource.career.exists():
            career = resource.career.first()
            context["career"] = career.name

            if career.school:
                context["school"] = career.school.name

                if career.school.faculty:
                    context["faculty"] = career.school.faculty.name

        if resource.format.exists():
            context["formats"] = resource.format.all()
        
        if resource.keyword.exists():
            context["keywords"] = resource.keyword.all()

        return context
