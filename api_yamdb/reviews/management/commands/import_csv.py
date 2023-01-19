import csv
from django.core.management.base import BaseCommand
from reviews.models import Category, Comment, Genre, Review, Title, Genre_Title

class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('static/data/category.csv', 'r', encoding='utf-8-sig', newline='') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                if row[0] != 'id': # Этой строчкой пропустил header!
                    _, created = Category.objects.get_or_create(
                        id=row[0],
                        name=row[1],
                        slug=row[2],
                    )
