# Generated by Django 4.2.2 on 2023-06-27 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_job_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(default='', upload_to='jobs/'),
            preserve_default=False,
        ),
    ]
