# Generated by Django 5.1.2 on 2024-12-17 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0002_business_loginid_cart_loginid_complaint_loginid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='labour',
            name='hour',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='labour',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
