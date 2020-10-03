# Generated by Django 2.2 on 2020-09-30 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RealUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=100, unique=True)),
                ('FirstName', models.CharField(blank=True, max_length=100)),
                ('LastName', models.CharField(blank=True, max_length=100)),
                ('Phone_No', models.IntegerField(blank=True, null=True)),
                ('EmailID', models.EmailField(max_length=100, unique=True)),
                ('Occupation', models.CharField(blank=True, max_length=100)),
                ('City', models.CharField(blank=True, max_length=100)),
                ('Country', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]