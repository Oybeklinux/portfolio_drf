# Generated by Django 4.0.3 on 2022-07-06 06:39

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_profile_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='audios'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='file',
            field=models.FileField(blank=True, default='files/default.xlsx', null=True, upload_to='files', validators=[users.models.validate_file_extension]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos'),
        ),
    ]