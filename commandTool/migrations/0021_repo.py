# Generated by Django 4.2.4 on 2023-08-11 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commandTool', '0020_result_name_alter_result_command'),
    ]

    operations = [
        migrations.CreateModel(
            name='Repo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mirrorName', models.CharField(default=None, max_length=200)),
                ('archiveUrl', models.URLField(default='https://depo.pardus.org.tr/pardus/')),
                ('dist', models.CharField(default=None, max_length=200)),
                ('components', models.CharField(default=None, max_length=200)),
            ],
        ),
    ]