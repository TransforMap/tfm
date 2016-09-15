from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from places.models import *


class Command(BaseCommand):
    help = 'Run ETL for specified or all clients'

    def add_arguments(self, parser):
        parser.add_argument('--maps', nargs='+', default=[])

    def handle(self, *args, **options):
		raise NotImplementedError()
