# Generated by Django 4.2.1 on 2023-08-22 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='uid',
            field=models.IntegerField(),
        ),
    ]
