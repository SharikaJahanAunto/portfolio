# Generated by Django 5.1.1 on 2024-09-15 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Service/'),
        ),
    ]
