# Generated by Django 3.1.4 on 2020-12-03 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='parents',
            new_name='parents_id',
        ),
    ]
