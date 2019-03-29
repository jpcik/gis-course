# Generated by Django 2.1.7 on 2019-03-26 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swissgeo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Canton',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'cantons',
            },
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name_plural': 'cities'},
        ),
    ]
