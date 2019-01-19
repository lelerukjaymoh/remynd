# Generated by Django 2.0.10 on 2019-01-19 12:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_item', models.CharField(max_length=400)),
                ('date_saved', models.DateTimeField(default=django.utils.timezone.now)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]