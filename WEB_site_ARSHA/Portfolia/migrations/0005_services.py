# Generated by Django 4.2.6 on 2024-01-31 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolia', '0004_portfolia_mavjudmi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='services/')),
                ('name', models.CharField(max_length=200)),
                ('descrition', models.TextField()),
            ],
        ),
    ]
