# Generated by Django 5.0.6 on 2024-07-09 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0002_det_result_alter_det_model_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='det_result',
            name='photo',
            field=models.FileField(upload_to='detect_photo/after'),
        ),
    ]
