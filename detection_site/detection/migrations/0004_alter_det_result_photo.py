# Generated by Django 5.0.6 on 2024-07-09 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0003_alter_det_result_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='det_result',
            name='photo',
            field=models.ImageField(upload_to='detect_photo/after'),
        ),
    ]
