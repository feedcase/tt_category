# Generated by Django 3.1.4 on 2021-01-27 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category_api', '0006_auto_20210127_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siblings',
            name='siblings',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='siblings', to='category_api.categories'),
        ),
    ]