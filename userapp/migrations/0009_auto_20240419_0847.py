# Generated by Django 3.2.23 on 2024-04-19 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0008_classone_classtw0'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='educcation',
            field=models.ManyToManyField(to='userapp.Education'),
        ),
    ]
