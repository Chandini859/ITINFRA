# Generated by Django 4.1.5 on 2023-02-06 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itapp', '0004_complaints_imageproof'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaints',
            name='imageproof',
        ),
        migrations.AddField(
            model_name='complaints',
            name='videoproof',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
    ]
