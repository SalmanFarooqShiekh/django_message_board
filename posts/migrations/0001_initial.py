# Generated by Django 4.0.5 on 2022-06-12 10:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('publication_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
