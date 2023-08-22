# Generated by Django 4.2.1 on 2023-08-22 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(max_length=6)),
                ('uname', models.CharField(max_length=255)),
                ('uemail', models.EmailField(max_length=254)),
                ('urole', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]