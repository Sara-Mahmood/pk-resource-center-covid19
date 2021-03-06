# Generated by Django 2.2.7 on 2020-04-25 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_auto_20200425_2203'),
    ]

    operations = [
        migrations.CreateModel(
            name='most_infected_city',
            fields=[
                ('entry_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('province', models.CharField(choices=[('Sindh', 'Sindh'), ('Punjab', 'Punjab'), ('KP', 'KP'), ('KPTD', 'KPTD'), ('GB', 'GB'), ('AJK', 'AJK'), ('ICT', 'ICT'), ('Taftan_mobile_lab', 'Taftan_mobile_lab'), ('Balochistan', 'Balochistan')], max_length=20)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
    ]
