# Generated by Django 3.2.23 on 2024-04-19 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0005_category2'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category_2',
            field=models.ManyToManyField(to='userapp.Category2'),
        ),
    ]
