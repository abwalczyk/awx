# Generated by Django 2.2.8 on 2020-02-12 17:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0109_v370_job_template_organization_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='instance',
            name='ip_address',
            field=models.CharField(blank=True, default=None, max_length=50, null=True, unique=True),
        ),
    ]
