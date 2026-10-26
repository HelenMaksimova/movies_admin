from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandParser


class Command(BaseCommand):
    help = "Creates a superuser only if it does not exist"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--username", default="admin", help="Superuser username"
        )
        parser.add_argument(
            "--email", default="admin@example.com", help="Superuser email"
        )
        parser.add_argument(
            "--password", default="admin", help="Superuser password"
        )

    def handle(self, *args, **options) -> None:
        User = get_user_model()
        username = options["username"]
        email = options["email"]
        password = options["password"]

        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING(f'Superuser "{username}" already exists!')
            )
        else:
            User.objects.create_superuser(
                username=username, email=email, password=password
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f'Superuser "{username}" created successfully!'
                )
            )
