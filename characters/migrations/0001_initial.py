# Generated by Django 4.1.3 on 2022-11-15 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('height', models.DecimalField(decimal_places=1, max_digits=5)),
                ('mass', models.DecimalField(decimal_places=1, max_digits=5)),
                ('hair_color', models.CharField(max_length=150)),
                ('skin_color', models.CharField(max_length=150)),
                ('eye_color', models.CharField(max_length=150)),
                ('gender', models.CharField(max_length=7)),
                ('movies', models.ManyToManyField(to='movies.movie')),
            ],
        ),
    ]
