# Generated by Django 4.1 on 2023-03-28 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("calculadora", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Jugadores",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("grupo", models.CharField(max_length=2)),
                ("num_lista", models.IntegerField()),
            ],
        ),
    ]