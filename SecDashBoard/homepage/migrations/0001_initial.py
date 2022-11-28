# Generated by Django 4.1.3 on 2022-11-28 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(blank=True, max_length=50, null=True)),
                ('ipAddress', models.GenericIPAddressField()),
            ],
        ),
    ]
