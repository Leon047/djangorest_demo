# Generated by Django 3.1.2 on 2020-11-08 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tags', '0002_auto_20201108_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tags.tags', verbose_name='user name'),
        ),
    ]
