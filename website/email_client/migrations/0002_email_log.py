# Generated by Django 5.1.4 on 2024-12-28 11:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email_log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('SENT', 'Sent'), ('FAILED', 'Failed')], max_length=10)),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='email_client.client_registration')),
            ],
        ),
    ]