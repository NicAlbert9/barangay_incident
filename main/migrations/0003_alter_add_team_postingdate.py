# Generated by Django 5.2.1 on 2025-05-16 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_add_team_postingdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_team',
            name='postingDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
