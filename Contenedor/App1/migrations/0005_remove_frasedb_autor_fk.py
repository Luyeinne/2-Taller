# Generated by Django 5.0.2 on 2024-03-22 00:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("App1", "0004_librodb_frasedb_libro_fk"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="frasedb",
            name="autor_fk",
        ),
    ]
