# Generated by Django 4.0.2 on 2022-04-16 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_blog_id_remove_blog_slug_blog_blogid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.TextField(),
        ),
    ]
