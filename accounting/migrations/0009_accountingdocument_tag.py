# Generated by Django 2.2.4 on 2019-08-10 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
        ('accounting', '0008_auto_20190810_0832'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountingdocument',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='documents', to='tag.Tag'),
        ),
    ]