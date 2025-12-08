from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users (superheroes)
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='Marvel'),
            User(email='captain@marvel.com', name='Captain America', team='Marvel'),
            User(email='spiderman@marvel.com', name='Spider-Man', team='Marvel'),
            User(email='batman@dc.com', name='Batman', team='DC'),
            User(email='superman@dc.com', name='Superman', team='DC'),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='DC'),
        ]
        for user in users:
            user.save()

        # Activities
        activities = [
            Activity(user='Iron Man', type='Running', duration=30, date='2025-12-08'),
            Activity(user='Captain America', type='Cycling', duration=45, date='2025-12-08'),
            Activity(user='Spider-Man', type='Swimming', duration=25, date='2025-12-08'),
            Activity(user='Batman', type='Running', duration=40, date='2025-12-08'),
            Activity(user='Superman', type='Cycling', duration=60, date='2025-12-08'),
            Activity(user='Wonder Woman', type='Swimming', duration=35, date='2025-12-08'),
        ]
        for activity in activities:
            activity.save()

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=100)
        Leaderboard.objects.create(team='DC', points=120)

        # Workouts
        workouts = [
            Workout(name='Pushups', difficulty='Easy'),
            Workout(name='Squats', difficulty='Medium'),
            Workout(name='Deadlift', difficulty='Hard'),
        ]
        for workout in workouts:
            workout.save()

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
