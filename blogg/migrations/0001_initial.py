# Generated by Django 4.0 on 2022-01-04 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('intro', models.TextField()),
                ('body', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
