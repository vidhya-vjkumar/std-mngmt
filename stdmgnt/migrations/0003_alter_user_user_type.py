# Generated by Django 4.1.7 on 2023-03-07 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stdmgnt', '0002_alter_user_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.IntegerField(choices=[(1, 'HOD'), (2, 'Staff'), (3, 'Student')], default=1),
        ),
    ]
