# Generated by Django 3.2.4 on 2021-06-25 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('import_file', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=2)),
            ],
        ),
    ]
