# Generated by Django 4.2 on 2024-06-08 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TuModelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introducetunombre', models.CharField(max_length=100)),
                ('introducetudireccindecorreoelectrnico', models.EmailField(max_length=254)),
                ('asunto', models.CharField(max_length=30)),
                ('mensaje', models.CharField(max_length=500)),
                ('aceptolascondicionesdeusoylapolticadeprivacidad', models.BooleanField(default=False)),
            ],
        ),
    ]
