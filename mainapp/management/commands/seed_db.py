from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory
from django.contrib.auth.models import User
from authapp.models import CustomUser



class Command(BaseCommand):
    def handle(self, *args, **options):

        # ProductCategory.objects.all().delete()
        # for x in range (5):
        #     new_cat = ProductCategory()
        #     new_cat.save()

        # super_user = User.objects.create_superuser(
        #     'sashnikov','test@test.com', 123123
        # )

        CustomUser.objects.create_superuser(
            'KapodastR', 'test1@test.com', '54533987', age=30
        )

