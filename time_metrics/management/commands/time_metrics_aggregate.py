from django.core.management.base import BaseCommand

from ...api import metrics_aggregate

class Command(BaseCommand):
    help = 'Generate fake users cities'

    def handle(self, *args, **options):
        metrics_aggregate()
