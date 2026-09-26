from django.conf import settings
from django.db import migrations


EDITOR_GROUP_NAME = "Editor"


def create_editor_group(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Group.objects.get_or_create(name=EDITOR_GROUP_NAME)


def delete_editor_group(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Group.objects.filter(name=EDITOR_GROUP_NAME).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_project_starred_by"),
        # Pastikan app auth (tempat model Group didefinisikan) sudah
        # dimigrasikan lebih dulu, tanpa menempel ke nomor migrasi auth
        # tertentu yang bisa berbeda antar versi Django.
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RunPython(create_editor_group, delete_editor_group),
    ]
