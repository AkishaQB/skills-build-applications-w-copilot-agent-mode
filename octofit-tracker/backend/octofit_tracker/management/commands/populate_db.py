from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete existing data in correct order to avoid FK issues
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.filter(pk__isnull=False).delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')


        # Create Users (superheroes)
        users = [
            User.objects.create(username='Iron Man', email='ironman@marvel.com', team=marvel, is_superhero=True),
            User.objects.create(username='Captain America', email='cap@marvel.com', team=marvel, is_superhero=True),
            User.objects.create(username='Spider-Man', email='spiderman@marvel.com', team=marvel, is_superhero=True),
            User.objects.create(username='Batman', email='batman@dc.com', team=dc, is_superhero=True),
            User.objects.create(username='Superman', email='superman@dc.com', team=dc, is_superhero=True),
            User.objects.create(username='Wonder Woman', email='wonderwoman@dc.com', team=dc, is_superhero=True),
        ]

        # Create Activities
        from datetime import date
        for user in users:
            Activity.objects.create(user=user, activity_type='Running', duration=30, date=date.today())
            Activity.objects.create(user=user, activity_type='Cycling', duration=45, date=date.today())

        # Create Workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity interval training for heroes')
        Workout.objects.create(name='Power Yoga', description='Yoga for strength and flexibility')

        # Create Leaderboard (user-based)
        for user in users:
            Leaderboard.objects.create(user=user, points=1000 if user.team == marvel else 950)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
