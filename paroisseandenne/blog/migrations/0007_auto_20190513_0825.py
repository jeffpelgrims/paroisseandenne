# Generated by Django 2.2.1 on 2019-05-13 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_article',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
