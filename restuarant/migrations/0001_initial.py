# Generated by Django 2.1.4 on 2018-12-27 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PlaceName', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='restuarants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restName', models.CharField(max_length=50)),
                ('rating', models.FloatField(max_length=10)),
                ('PlaceCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restuarant.place')),
            ],
        ),
    ]
