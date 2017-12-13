# Generated by Django 2.0 on 2017-12-13 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SESSION',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sess', models.CharField(max_length=30, unique=True, verbose_name='sess')),
            ],
        ),
        migrations.CreateModel(
            name='USER',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=20, unique=True, verbose_name='email')),
                ('pw', models.CharField(max_length=10, verbose_name='pw')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
            ],
        ),
        migrations.AddField(
            model_name='session',
            name='id_USER',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.USER'),
        ),
        migrations.AlterUniqueTogether(
            name='session',
            unique_together={('id_USER', 'sess')},
        ),
    ]
