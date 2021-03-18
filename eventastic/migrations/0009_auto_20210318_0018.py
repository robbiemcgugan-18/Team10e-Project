# Generated by Django 2.2.17 on 2021-03-18 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventastic', '0008_auto_20210315_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='picture',
            field=models.ImageField(upload_to='category_images'),
        ),
        migrations.AlterField(
            model_name='event',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='event_images'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profilePicture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images'),
        ),
    ]
