# Generated by Django 2.2.4 on 2019-09-06 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_snsdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snsdata',
            name='link',
        ),
    ]