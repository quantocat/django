# Generated by Django 5.1.1 on 2024-10-08 09:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_event'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Kategorie', 'verbose_name_plural': 'Kategorien'},
        ),
        migrations.AddField(
            model_name='event',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='events', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='sub_title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Untertitel'),
        ),
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='events.category'),
        ),
    ]
