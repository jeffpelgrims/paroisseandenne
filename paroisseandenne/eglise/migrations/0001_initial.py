# Generated by Django 2.2.1 on 2019-05-12 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='eglise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=125)),
                ('rue', models.CharField(max_length=125)),
                ('numero', models.IntegerField()),
                ('c_postal', models.IntegerField()),
                ('ville', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('photo_url', models.CharField(max_length=1025)),
            ],
        ),
    ]
