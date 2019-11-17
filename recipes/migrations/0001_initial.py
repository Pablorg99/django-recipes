# Generated by Django 2.2.3 on 2019-07-09 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(verbose_name='g')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dinner_guests', models.PositiveIntegerField()),
                ('procedure', models.TextField(verbose_name='Instructions')),
                ('publication_date', models.DateTimeField(verbose_name='Date Published')),
                ('ingredients', models.ManyToManyField(to='recipes.Ingredient')),
            ],
        ),
    ]