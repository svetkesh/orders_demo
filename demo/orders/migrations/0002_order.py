# Generated by Django 2.2 on 2020-06-04 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_order', models.DateField()),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tables', to='orders.Table')),
            ],
            options={
                'unique_together': {('date_order', 'reservation')},
            },
        ),
    ]
