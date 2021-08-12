# Generated by Django 3.2.6 on 2021-08-12 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CollegeApp', '0003_delete_prof'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('salary', models.FloatField()),
                ('dept', models.ManyToManyField(to='CollegeApp.Dept')),
            ],
        ),
    ]
