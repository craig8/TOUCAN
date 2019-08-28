# Generated by Django 2.2.3 on 2019-08-27 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('canary_files', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CanaryLogItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('msg', models.CharField(max_length=4096)),
                ('stacktrace', models.TextField(null=True)),
                ('canary', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='canary_files.CanaryItem')),
            ],
        ),
    ]
