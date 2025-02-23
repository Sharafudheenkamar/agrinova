# Generated by Django 5.1.3 on 2024-12-18 16:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0006_policy_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='policy',
            name='date',
        ),
        migrations.AlterField(
            model_name='labour',
            name='hour',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.CreateModel(
            name='Bcomplaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=20, null=True)),
                ('Category', models.CharField(blank=True, max_length=100, null=True)),
                ('Details', models.CharField(blank=True, max_length=1000, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('docfile', models.FileField(blank=True, null=True, upload_to='bcomplalint')),
                ('loginid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.usertable')),
            ],
        ),
    ]
