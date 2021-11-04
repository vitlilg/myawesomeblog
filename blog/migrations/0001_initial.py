# Generated by Django 3.2.8 on 2021-11-04 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=30)),
                ('blog_date', models.DateField()),
                ('blog_text', models.CharField(max_length=300)),
                ('blog_image', models.ImageField(upload_to='blog_images/')),
            ],
        ),
    ]
