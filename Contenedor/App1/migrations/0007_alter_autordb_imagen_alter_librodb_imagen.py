# Generated by Django 5.0.2 on 2024-03-27 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App1", "0006_alter_librodb_options_autordb_imagen_librodb_imagen"),
    ]

    operations = [
        migrations.AlterField(
            model_name="autordb",
            name="imagen",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="imagenes/",
                verbose_name="Imagen Autor",
            ),
        ),
        migrations.AlterField(
            model_name="librodb",
            name="imagen",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="imagenes/",
                verbose_name="Imagen Autor",
            ),
        ),
    ]
