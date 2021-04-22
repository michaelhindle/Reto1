# Generated by Django 3.1.7 on 2021-03-25 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Red',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=200)),
                ('fecha_creacion', models.DateTimeField(verbose_name='Fecha de creacion')),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(default='', max_length=30)),
                ('votes', models.IntegerField(default=0)),
                ('red', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.red')),
            ],
        ),
    ]
