# Generated by Django 5.1.6 on 2025-02-18 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.CharField(max_length=50, unique=True)),
                ('company_name', models.CharField(max_length=100)),
                ('company_address', models.TextField()),
            ],
        ),
    ]
