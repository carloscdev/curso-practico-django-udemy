# Generated by Django 5.0 on 2024-01-30 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0002_thread'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='thread',
            options={},
        ),
        migrations.AddField(
            model_name='thread',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
