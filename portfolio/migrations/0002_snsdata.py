# Generated by Django 2.2.4 on 2019-08-30 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SnsData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.TextField()),
                ('text', models.TextField()),
                ('hashtag', models.TextField()),
                ('link', models.URLField()),
            ],
        ),
    ]