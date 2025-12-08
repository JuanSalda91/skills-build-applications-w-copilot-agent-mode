from djongo import models

class User(models.Model):
    id = models.ObjectIdField(primary_key=True, default=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=50)
    is_superhero = models.BooleanField(default=True)
    class Meta:
        db_table = 'users'

class Team(models.Model):
    id = models.ObjectIdField(primary_key=True, default=True)
    name = models.CharField(max_length=50, unique=True)
    class Meta:
        db_table = 'teams'

class Activity(models.Model):
    id = models.ObjectIdField(primary_key=True, default=True)
    user = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateField()
    class Meta:
        db_table = 'activities'

class Leaderboard(models.Model):
    id = models.ObjectIdField(primary_key=True, default=True)
    team = models.CharField(max_length=50)
    points = models.IntegerField()
    class Meta:
        db_table = 'leaderboard'

class Workout(models.Model):
    id = models.ObjectIdField(primary_key=True, default=True)
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    class Meta:
        db_table = 'workouts'
