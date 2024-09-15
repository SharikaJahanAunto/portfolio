# Generated by Django 5.1.1 on 2024-09-13 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fb_link', models.URLField(max_length=1000)),
                ('l_link', models.URLField(max_length=1000)),
                ('t_link', models.URLField(max_length=1000)),
                ('y_link', models.URLField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='about',
            name='age',
            field=models.IntegerField(),
        ),
    ]
