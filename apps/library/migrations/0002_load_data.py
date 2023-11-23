import json
import os

from django.db import migrations


def load_data(apps, schema_editor):
    app_name = "library"
    app_models = apps.get_app_config(app_name).get_models()
    fixtures_dir = os.path.abspath(
        os.path.join(os.getcwd(), "apps", "library", "fixtures")
    )

    for model in app_models:
        fixture_file = os.path.join(fixtures_dir, model.__name__ + ".json")

        with open(fixture_file.lower(), "r", encoding="utf-8") as f:
            data = json.load(f)
            model.objects.bulk_create(model(**item) for item in data)


class Migration(migrations.Migration):
    dependencies = [("library", "0001_initial")]

    operations = [
        migrations.RunPython(load_data),
    ]
