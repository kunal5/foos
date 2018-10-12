from django.db import models
# Create your models here.

class RegisterTeam(models.Model):
    Team_Name=models.CharField(max_length=32)
    Player1_Name = models.CharField(max_length=32)
    Player2_Name = models.CharField(max_length=32)
    def __str__(self):
        return self.Team_Name

class RegisterGame(models.Model):
    team1= models.ForeignKey(RegisterTeam, related_name='team1', on_delete=models.CASCADE)
    team1_score = models.IntegerField()
    team2= models.ForeignKey(RegisterTeam, related_name='team2', on_delete=models.CASCADE)
    team2_score = models.IntegerField()
