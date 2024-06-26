# Generated by Django 5.0.6 on 2024-06-23 10:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_author_comment_author_post_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ulikes', to='posts.author')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plikes', to='posts.post')),
            ],
        ),
    ]
