# Generated by Django 2.2.7 on 2019-12-02 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winupdate', '0004_winupdate_severity'),
    ]

    operations = [
        migrations.AddField(
            model_name='winupdate',
            name='action',
            field=models.CharField(choices=[('inherit', 'Inherit'), ('approve', 'Approve'), ('ignore', 'Ignore'), ('nothing', 'Do Nothing')], default='inherit', max_length=100),
        ),
    ]