# Generated by Django 4.1.8 on 2023-10-11 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitesettings', '0007_footernotices_settings_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='footernotices',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
