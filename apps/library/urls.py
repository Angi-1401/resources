from django.urls import path

from . import views

urlpatterns = [
    path("collections/", views.CollectionListView.as_view(), name="collections"),
    path("faculties/", views.ResourcesListView1.as_view(), name="faculties"),
    path("publish-date/", views.ResourcesListView2.as_view(), name="publish-date"),
    path("author/", views.ResourcesListView3.as_view(), name="author"),
    path("title/", views.ResourcesListView4.as_view(), name="title"),
    path("subject/", views.ResourcesListView5.as_view(), name="subject"),
    path("all/", views.ResourcesListView6.as_view(), name="all"),
    path(
        "resource/<uuid:pk>/",
        views.ResourceDetailView.as_view(),
        name="resource-detail",
    ),
]
