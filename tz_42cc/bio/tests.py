from django.test import TestCase
from models import Person, HttpRequestData
from zlib import crc32
from django.conf import settings

#Ticket1
class BioTest(TestCase):
    fixtures = ['initial_data.json',]   #my fixtures
            
    def simpleTest(self):
        response = self.client.get('/')
        # Check that the response is 200 OK.
        self.failUnlessEqual(response.status_code, 200)
        # find data pattern
        self.failIfEqual(response.content.find('0974865577'), -1, 'data pattern not found in response')
        
#Ticket3
class HttpRequestLogTest(TestCase):
    def loopback(self):
        self.client.get('/?key=value')
        log_data_obj = HttpRequestData.objects.filter(path = '/')
        self.failIf(log_data_obj.count() == 0, 'http requests not stored in the DB')
        self.failUnlessEqual(log_data_obj[0].request, u"<QueryDict: {u'key': [u'value']}>", 'http requests data not stored in the DB correctly')

#Ticket4
class ContextProcessorTest(TestCase):
    def loopback(self):
        response = self.client.get('/settings/')
        self.failUnlessEqual(response.context['settings']['SECRET_KEY'], settings.SECRET_KEY)
        
#Ticket5
class EditTest(TestCase):    
    def change(self):
        person = Person.objects.all()[0]    #get person for save
        target_path = '/edit/'
        response = self.client.get(target_path)
        token = response.context['csrf_token']
        data = {'name': 'john', 
                'surname': 'smith',
                'contacts': 'hidden',
                'birthdate': '1983-06-24',
                'csrfmiddlewaretoken': token,
                }
        response = self.client.post(target_path, data)
        person.save()   #Re-write initial data
        response_name = ''
        try:
            response_name = response.context['form']['name'].data
        except:
            self.assertTrue(False, "person edit fail - incorrect response")        
        self.failUnlessEqual(response_name, data['name'], 'person edit fail - incorrect data')