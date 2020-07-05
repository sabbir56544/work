# Generated by Django 2.2.7 on 2020-06-30 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(max_length=30)),
                ('area_size', models.IntegerField()),
                ('area_disc', models.TextField()),
            ],
        ),
    ]
