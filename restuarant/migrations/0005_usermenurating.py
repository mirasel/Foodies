# Generated by Django 2.1.5 on 2019-01-27 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restuarant', '0004_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='usermenurating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(max_length=10)),
                ('ratingcode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restuarant.menu')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
