# Generated by Django 2.2.1 on 2019-05-12 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_jumbotron_jumbo_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meditation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('texte', models.TextField()),
            ],
        ),
    ]
