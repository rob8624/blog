# Generated by Django 4.1.8 on 2023-10-25 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_alter_blogdetailpage_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogauthor',
            name='facebook',
            field=models.CharField(blank=True, default='facebook', max_length=200),
        ),
        migrations.AlterField(
            model_name='blogauthor',
            name='instagram',
            field=models.CharField(blank=True, default='instagram', max_length=200),
        ),
        migrations.AlterField(
            model_name='blogauthor',
            name='twitter',
            field=models.CharField(blank=True, default='twitter', max_length=200),
        ),
    ]