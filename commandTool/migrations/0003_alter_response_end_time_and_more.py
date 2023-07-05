# Generated by Django 4.2.2 on 2023-07-04 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commandTool', '0002_response_delete_commandexecution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='response',
            name='execution_time',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='response',
            name='output_file',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='response',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]