# Generated by Django 2.2.5 on 2019-11-25 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_info', '0004_auto_20191124_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='One_School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=256)),
                ('profession_name', models.CharField(max_length=256)),
                ('student_type', models.CharField(max_length=256)),
                ('year', models.CharField(max_length=256)),
                ('top_score', models.CharField(max_length=256)),
                ('avg_score', models.CharField(max_length=256)),
                ('lowest_score', models.CharField(max_length=256)),
                ('lowest_rank', models.CharField(max_length=256)),
                ('epoch', models.CharField(max_length=256)),
            ],
        ),
    ]
