from django.core.management.base import BaseCommand, CommandError
from django.contrib.admin.models import ContentType

class Command(BaseCommand):
    args = '<none ...>'
    help = 'prints all project models and the count of objects in every model'
    
    def handle(self, *args, **options):                    
            all_content_types = ContentType.objects.all()   #get all objects from admin models
            self.stdout.write("MODEL " + "-" * 77 + " COUNT\n")     #header
            for curr_content_type in all_content_types:             #iterate to get model class
                curr_model = curr_content_type.model_class()
                model_name_len = len(str(curr_model))   #forman output
                append_len = 80 - model_name_len
                append_str = " " * append_len
                self.stdout.write( "%s : %s %d \n" % (curr_model, append_str, curr_model.objects.count())) #content
                
            self.stdout.write("-" * 90 + "\n") #footer