# Generated by Django 3.2.12 on 2023-06-27 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('menu', models.JSONField()),
            ],
        ),
        migrations.DeleteModel(
            name='Dish',
        ),
    ]
