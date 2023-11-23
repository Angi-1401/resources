import django_tables2 as tbl

from .models import *


class ResourceTable(tbl.Table):
    title = tbl.LinkColumn(args=[tbl.A("pk")], orderable=False, verbose_name="Title")

    class Meta:
        model = Resource
        template_name = "django_tables2/bootstrap5-responsive.html"
        fields = (
            "publish_date",
            "title",
            "author",
        )
