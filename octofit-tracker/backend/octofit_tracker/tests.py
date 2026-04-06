from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Marvel', description='Marvel superheroes')
        self.assertEqual(team.name, 'Marvel')

    def test_create_user(self):
        team = Team.objects.create(name='DC', description='DC superheroes')
        user = User.objects.create(email='batman@dc.com', username='Batman', team=team, is_superhero=True)
        self.assertEqual(user.username, 'Batman')

    def test_create_activity(self):
        team = Team.objects.create(name='Marvel')
        user = User.objects.create(email='spiderman@marvel.com', username='Spiderman', team=team)
        activity = Activity.objects.create(user=user, activity_type='Running', duration=30, date='2024-01-01')
        self.assertEqual(activity.activity_type, 'Running')

    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Upper body workout')
        self.assertEqual(workout.name, 'Pushups')

    def test_create_leaderboard(self):
        team = Team.objects.create(name='Marvel')
        user = User.objects.create(email='ironman@marvel.com', username='Ironman', team=team)
        leaderboard = Leaderboard.objects.create(user=user, points=100)
        self.assertEqual(leaderboard.points, 100)
