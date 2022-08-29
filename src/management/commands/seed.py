from django.core.management.base import BaseCommand, CommandError
import importlib
import glob, os

os.chdir("./src/seeds")


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("-m", "--model")

    def handle(self, *args, **options):
        model = options["model"]
        if not (model):
            for file in glob.glob("*.py"):
                self.stdout.write(file)
                module = importlib.import_module("src.seeds." + file.replace(".py", ""))
                module.seed()
        else:
            module = importlib.import_module("src.seeds." + model)
            module.seed()
        self.stdout.write(
            self.style.SUCCESS("Seed successfully: " + (str(model) if model else "all"))
        )
