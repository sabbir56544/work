# Generated by Django 2.2.7 on 2020-06-30 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('std_id', models.IntegerField()),
                ('gender', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('group', models.CharField(max_length=30)),
            ],
        ),
    ]
