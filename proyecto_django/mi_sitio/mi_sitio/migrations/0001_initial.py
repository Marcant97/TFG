# Generated by Django 4.2 on 2024-05-20 11:40

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
                ('eligetutalladecamiseta', models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('XL', 'XL')], max_length=100)),
                ('aceptoelreglamentodelaprueba', models.BooleanField(default=False)),
            ],
        ),
    ]