# Generated by Django 4.1.2 on 2022-11-26 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('discord_id', models.CharField(max_length=200)),
                ('fromWhereKnows', models.CharField(choices=[('MON', 'Мониторинг'), ('METRO', 'Метро'), ('RAD', 'Сарафанное радио'), ('STICKS', 'Стикеры')], max_length=200)),
            ],
        ),
    ]