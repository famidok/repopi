# Generated by Django 4.2.2 on 2023-07-04 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commandTool', '0006_alter_response_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='end_time',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
