# Generated by Django 4.2.6 on 2024-01-29 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category_portfolia',
            name='slug',
            field=models.SlugField(default=1, max_length=20, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category_portfolia',
            name='image',
            field=models.ImageField(blank=True, upload_to='photo/category'),
        ),
        migrations.AlterField(
            model_name='category_portfolia',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
