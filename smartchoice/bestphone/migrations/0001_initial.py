# Generated by Django 2.0.3 on 2018-04-01 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='table_11',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_no', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('users_review', models.FloatField()),
                ('expert_review', models.FloatField()),
                ('features', models.FloatField()),
                ('price1', models.FloatField()),
                ('newer', models.FloatField()),
                ('result', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='table_12',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_no', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('users_review', models.FloatField()),
                ('expert_review', models.FloatField()),
                ('features', models.FloatField()),
                ('price1', models.FloatField()),
                ('newer', models.FloatField()),
                ('result', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='table_13',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_no', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('users_review', models.FloatField()),
                ('expert_review', models.FloatField()),
                ('features', models.FloatField()),
                ('price1', models.FloatField()),
                ('newer', models.FloatField()),
                ('result', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='table_14',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_no', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('users_review', models.FloatField()),
                ('expert_review', models.FloatField()),
                ('features', models.FloatField()),
                ('price1', models.FloatField()),
                ('newer', models.FloatField()),
                ('result', models.FloatField()),
            ],
        ),
    ]
