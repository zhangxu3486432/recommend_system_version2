# Generated by Django 2.2.5 on 2019-11-18 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='mbti',
            new_name='personality_type',
        ),
    ]