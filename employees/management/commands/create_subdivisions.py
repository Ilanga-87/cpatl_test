import os
import sys

current_path = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_path, '..'))

os.chdir(project_root)

sys.path.append(project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'company.settings')

import django
django.setup()

from django.core.management.base import BaseCommand
from employees.models import Subdivision
from services.subdivisions_data import data


class Command(BaseCommand):
    help = 'Create subdivisions in the database'

    def handle(self, *args, **kwargs):
        self.create_subdivisions(data)

    def create_subdivisions(self, data):
        self.stdout.write("Initiating company creation...")
        created_subdivisions = {}

        for entry in data:
            name = entry['name']
            parent_name = entry['parent']

            parent = created_subdivisions.get(parent_name)

            subdivision = Subdivision.objects.create(name=name, parent=parent)

            created_subdivisions[name] = subdivision

        self.stdout.write(self.style.SUCCESS("Company created successfully."))