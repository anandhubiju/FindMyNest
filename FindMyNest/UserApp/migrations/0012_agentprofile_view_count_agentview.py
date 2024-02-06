# Generated by Django 4.2.7 on 2024-01-18 10:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0011_alter_userprofile_profile_editable'),
    ]

    operations = [
        migrations.AddField(
            model_name='agentprofile',
            name='view_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='AgentView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('agentProfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.agentprofile')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
