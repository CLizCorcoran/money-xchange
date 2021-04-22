# Generated by Django 3.2 on 2021-04-22 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0007_alter_transactions_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this portfolio entry', primary_key=True, serialize=False)),
                ('symbol', models.CharField(max_length=3)),
                ('quantity', models.IntegerField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
