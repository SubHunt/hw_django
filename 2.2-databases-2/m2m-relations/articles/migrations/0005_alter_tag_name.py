# Generated by Django 4.2.1 on 2023-05-12 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_tag_articles_alter_scope_article_alter_scope_is_main_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
