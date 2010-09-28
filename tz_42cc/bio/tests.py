from django.test import TestCase
from models import Person, HttpRequestData

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
        
