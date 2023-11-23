from django.shortcuts import render
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

from .models import *


# Create your views here.
def collection_list(request):
    """Home page of site."""

    collections = Collection.objects.all()

    context = {
        "collections": collections,
    }

    return render(request, "library/collection.html", context)
