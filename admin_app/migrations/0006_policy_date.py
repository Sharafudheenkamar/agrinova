# Generated by Django 5.1.3 on 2024-12-18 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0005_auto_20241217_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='policy',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
