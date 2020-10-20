# Generated by Django 3.1 on 2020-08-16 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('status_id', models.IntegerField(primary_key=True, serialize=False)),
                ('ok', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('tz', models.CharField(blank=True, choices=[(0, 'Canada/Atlantic'), (1, 'Canada/Central'), (2, 'Canada/Eastern'), (3, 'Canada/Mountain'), (4, 'Canada/Pacific')], max_length=100, null=True, unique=True)),
                ('real_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('status_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='activtyapp.status')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityPeriod',
            fields=[
                ('activity_id', models.IntegerField(primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField(verbose_name='date started')),
                ('end_time', models.DateTimeField(verbose_name='date ended')),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activityperiod', to='activtyapp.members')),
            ],
        ),
    ]