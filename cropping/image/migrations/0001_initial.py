# Generated by Django 4.0.3 on 2022-04-13 00:19

from django.db import migrations, models
import django.db.models.deletion
import image_cropping.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_field', image_cropping.fields.ImageCropField(upload_to='image/')),
                ('cropping', image_cropping.fields.ImageRatioField('image_field', '120x100', adapt_rotation=False, allow_fullsize=True, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping')),
                ('cropping_free', image_cropping.fields.ImageRatioField('image_field', '300x230', adapt_rotation=False, allow_fullsize=False, free_crop=True, help_text=None, hide_image_field=False, size_warning=True, verbose_name='cropping free')),
            ],
        ),
        migrations.CreateModel(
            name='ImageFK',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cropping', image_cropping.fields.ImageRatioField('image__image_field', '120x100', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='image.image')),
            ],
        ),
    ]
