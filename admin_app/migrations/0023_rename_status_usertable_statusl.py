# Generated by Django 3.2.14 on 2024-12-31 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0022_alter_usertable_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usertable',
            old_name='status',
            new_name='statusl',
        ),
    ]
