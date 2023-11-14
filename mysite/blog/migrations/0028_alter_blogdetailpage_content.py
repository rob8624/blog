# Generated by Django 4.1.8 on 2023-10-25 08:14

from django.db import migrations
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_alter_blogcategories_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdetailpage',
            name='content',
            field=wagtail.fields.StreamField([('title_and_text', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Add your title', required=True)), ('text', wagtail.blocks.TextBlock(help_text='Add additional text', required=False))])), ('image', wagtail.blocks.StructBlock([('small_image', wagtail.images.blocks.ImageChooserBlock(blank=True, required=False)), ('medium_image', wagtail.images.blocks.ImageChooserBlock(blank=True, required=False)), ('large_image', wagtail.images.blocks.ImageChooserBlock(blank=True, required=False)), ('text', wagtail.blocks.TextBlock(max_length=200, required=True))])), ('text_body', wagtail.blocks.StructBlock([('rich_text', wagtail.blocks.RichTextBlock(max_length=2000, required=False))])), ('gallery', wagtail.blocks.StructBlock([('gallery_images', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock)), ('gallery_heading', wagtail.blocks.TextBlock(max_length=200))])), ('code', wagtail.blocks.StructBlock([('language', wagtail.blocks.ChoiceBlock(choices=[('python', 'python'), ('javascript', 'javascript'), ('css', 'css'), ('html', 'html'), ('django', 'django')])), ('text', wagtail.blocks.TextBlock())])), ('quote', wagtail.blocks.StructBlock([('quote_text', wagtail.blocks.TextBlock(max_length=2000, required=False))])), ('embed', wagtail.blocks.StructBlock([('embed', wagtail.embeds.blocks.EmbedBlock())]))], use_json_field=True),
        ),
    ]
