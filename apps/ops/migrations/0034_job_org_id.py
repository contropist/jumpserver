# Generated by Django 3.2.14 on 2022-11-23 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ops', '0033_auto_20221118_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='org_id',
            field=models.CharField(blank=True, db_index=True, default='', max_length=36, verbose_name='Organization'),
        ),
    ]
