# Generated by Django 5.1.2 on 2024-12-12 09:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='loginid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.usertable'),
        ),
        migrations.AddField(
            model_name='cart',
            name='loginid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.usertable'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='loginid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.usertable'),
        ),
        migrations.AddField(
            model_name='farmer',
            name='loginid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.usertable'),
        ),
        migrations.AddField(
            model_name='labour',
            name='loginid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.usertable'),
        ),
        migrations.AddField(
            model_name='policy',
            name='loginid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.usertable'),
        ),
        migrations.AddField(
            model_name='product',
            name='loginid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.usertable'),
        ),
        migrations.AddField(
            model_name='request',
            name='loginid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.usertable'),
        ),
    ]
