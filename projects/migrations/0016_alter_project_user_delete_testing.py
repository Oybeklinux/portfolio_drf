# Generated by Django 4.0.3 on 2022-08-10 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_alter_profile_social_github'),
        ('projects', '0015_alter_testing_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects', to='users.profile'),
        ),
        migrations.DeleteModel(
            name='Testing',
        ),
    ]
