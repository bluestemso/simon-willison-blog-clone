# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 20:35


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_metadata_default'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='tweet_html',
            field=models.TextField(blank=True, help_text=b'Paste in the embed tweet HTML, minus the script tag,\n        to display a tweet in the sidebar next to this entry.', null=True),
        ),
    ]
