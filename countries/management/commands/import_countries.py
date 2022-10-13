from django.core.management.base import BaseCommand, CommandError
from countries.models import Country, State, District


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('/Users/juwaini/PycharmProjects/for_fun/countries/countries.csv') as f:
            for row in f:
                if 'COUNTRY' in row:
                    continue
                column = row.strip().split(',')
                c, created = Country.objects.get_or_create(name=column[0])
                s, created = State.objects.get_or_create(name=column[1], country=c)
                District.objects.create(name=column[2], state=s)
