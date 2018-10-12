# Generated by Django 2.0.8 on 2018-10-11 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team1_score', models.IntegerField()),
                ('team2_score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RegisterTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Team_Name', models.CharField(max_length=32)),
                ('Player1_Name', models.CharField(max_length=32)),
                ('Player2_Name', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='registergame',
            name='team1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team1', to='leaderboard.RegisterTeam'),
        ),
        migrations.AddField(
            model_name='registergame',
            name='team2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team2', to='leaderboard.RegisterTeam'),
        ),
    ]