# Generated by Django 4.1 on 2023-03-29 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("calculadora", "0002_jugadores"),
    ]

    operations = [
        migrations.CreateModel(
            name="partidas",
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
                ("fecha", models.CharField(max_length=8)),
                ("id_usuario", models.CharField(max_length=5)),
                ("minutos_jugados", models.IntegerField()),
                ("puntaje", models.IntegerField()),
            ],
        ),
    ]