from django.shortcuts import render


# Create your views here.
def index(request):
    """Home page of site."""
    return render(request, "index.html")
