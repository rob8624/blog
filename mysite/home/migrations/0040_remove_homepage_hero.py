# Generated by Django 4.1.8 on 2023-10-27 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0039_terms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='hero',
        ),
    ]
