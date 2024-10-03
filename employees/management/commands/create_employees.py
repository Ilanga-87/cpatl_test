import os
import sys

current_path = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_path, '..'))

os.chdir(project_root)

sys.path.append(project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'company.settings')

import django
django.setup()

import random

from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand
from django.utils import timezone
from mimesis import Person, Generic
from mimesis.locales import Locale
from mimesis.builtins import RussiaSpecProvider
from employees.models import Employee, Subdivision


class Command(BaseCommand):
    help = 'Populate the database with dummy data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--num_employees',
            type=int,
            default=60000,  # Default
            help='Number of employees to create'
        )

    def handle(self, *args, **kwargs):
        num_employees = kwargs['num_employees']

        person = Person(locale=Locale.RU)
        generic = Generic(locale=Locale.RU)
        generic.add_provider(RussiaSpecProvider)

        subdivisions = list(Subdivision.objects.all())

        if not subdivisions:
            raise ValidationError("Error: add subdivisions first")

        for _ in range(num_employees):
            fio = person.last_name() + ' ' + person.first_name() + ' ' + generic.russia_provider.patronymic()
            position = person.occupation()
            hire_date = timezone.now() - timezone.timedelta(days=random.randint(1, 1200))
            salary = random.randint(30, 500) * 1000

            subdivision = random.choice(subdivisions)


            Employee.objects.create(
                full_name=fio,
                position=position,
                hire_date=hire_date,
                salary=salary,
                subdivision=subdivision
            )

            self.stdout.write(self.style.SUCCESS(f'Successfully created data for employee: {fio}'))
        self.stdout.write(self.style.SUCCESS(f'-------- Successfully created data for employees'))