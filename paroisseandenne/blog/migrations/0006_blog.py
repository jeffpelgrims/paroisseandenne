# Generated by Django 2.2.1 on 2019-05-13 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_meditation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre_article', models.CharField(max_length=255)),
                ('date_article', models.DateField(auto_now=True)),
                ('contenu', models.TextField()),
            ],
        ),
    ]
