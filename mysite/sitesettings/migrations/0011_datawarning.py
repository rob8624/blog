# Generated by Django 4.2.8 on 2023-12-13 11:36

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0084_query_searchpromotion_querydailyhits'),
        ('sitesettings', '0010_rename_caontactinfo_contactinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataWarning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, max_length=300)),
                ('policy', wagtail.fields.RichTextField()),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]