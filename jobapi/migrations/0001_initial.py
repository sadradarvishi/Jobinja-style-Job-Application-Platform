# Generated by Django 5.1.7 on 2025-03-12 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=225)),
                ('title', models.CharField(max_length=225)),
                ('agreement', models.CharField(choices=[('full_time', 'full_time'), ('part_time', 'part_time'), ('remote', 'remote')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('salary', models.IntegerField(null=True)),
                ('description', models.TextField(max_length=400, null=True)),
                ('requirements', models.TextField(max_length=500)),
                ('is_available', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Job',
            },
        ),
    ]
