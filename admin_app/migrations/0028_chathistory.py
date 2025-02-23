# Generated by Django 5.1.3 on 2025-01-22 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0027_alter_labour_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_query', models.TextField()),
                ('chatbot_response', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
