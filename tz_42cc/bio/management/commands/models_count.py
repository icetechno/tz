from django.contrib.admin.models import ContentType
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    args = '<none ...>'
    help = 'prints all project models and the count of objects in every model'

    def handle(self, *args, **options):
            # get all objects from admin models
            all_content_types = ContentType.objects.all()
            self.stdout.write("MODEL " + "-" * 77 + " COUNT\n")     # header
            # iterate to get model class
            for curr_content_type in all_content_types:
                curr_model = curr_content_type.model_class()
                model_name_len = len(str(curr_model))   # forman output
                append_len = 80 - model_name_len
                append_str = " " * append_len
                # content
                self.stdout.write("%s : %s %d \n" % (
                                                curr_model,
                                                append_str,
                                                curr_model.objects.count())
                )
            self.stdout.write("-" * 90 + "\n")  # footer
