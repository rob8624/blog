# Generated by Django 4.1.8 on 2023-04-26 23:37

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_blogpage_blogpagegalleryimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='page_title',
            field=wagtail.fields.RichTextField(blank=True),
        ),
    ]
