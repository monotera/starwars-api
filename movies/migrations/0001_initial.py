# Generated by Django 4.1.3 on 2022-11-15 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('planets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('opening_text', models.CharField(max_length=350)),
                ('producer', models.CharField(max_length=150)),
                ('director', models.CharField(max_length=250)),
                ('planets', models.ManyToManyField(to='planets.planet')),
            ],
        ),
    ]
