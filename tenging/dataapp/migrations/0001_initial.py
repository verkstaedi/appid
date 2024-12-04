# Generated by Django 5.1.2 on 2024-12-03 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notendur',
            fields=[
                ('nafn', models.CharField(db_column='Nafn', max_length=255, primary_key=True, serialize=False)),
                ('bilnumer', models.CharField(blank=True, db_column='Bilnumer', max_length=20, null=True)),
                ('vandamal', models.TextField(blank=True, db_column='Vandamal', null=True)),
                ('stadsetning', models.CharField(blank=True, db_column='Stadsetning', max_length=100, null=True)),
                ('buid_til', models.DateTimeField(blank=True, null=True)),
                ('kennitala', models.CharField(blank=True, max_length=100, null=True)),
                ('simanumer', models.CharField(blank=True, db_column='Simanumer', max_length=100, null=True)),
            ],
            options={
                'db_table': 'notendur',
                'managed': False,
            },
        ),
    ]
