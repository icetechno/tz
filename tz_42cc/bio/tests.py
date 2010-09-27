from django.test import TestCase
from django.test.client import Client
from models import Person, HttpRequestData
from model_form import PersonDetail
from zlib import crc32

#Ticket1
class BioTest(TestCase):
    fixtures = ['initial_data.json',]   #my fixtures
    
    def testView(self):
        crc_value = -0x52959224
        client = Client()
        person = Person.objects.all()[0]  #first person in DB       
        form = PersonDetail(instance = person) 
        response = client.get('/bio/')        
        # Check that the response is 200 OK.
        self.failUnlessEqual(response.status_code, 200)
        # Check that the rendered context not moddifed and renders fine
        external_view = unicode(response.context['form']).encode('utf-8')
        internal_view = unicode(form).encode('utf-8')
        # Check that the rendered context not moddifed
        self.failUnlessEqual(crc32(internal_view), crc_value, 'content modifed, CRC32 not much')
        # Check that renders fine
        self.failUnlessEqual(external_view, internal_view, 'internal and external wiew are not equal')
        
#Ticket3
class HttpRequestLogTest(TestCase):
    def loopback(self):
        self.client.get('/?key=value')
        log_data_obj = HttpRequestData.objects.filter(path = '/')
        self.failIf(log_data_obj.count() == 0, 'http requests not stored in the DB')
        self.failUnlessEqual(log_data_obj[0].request, u"<QueryDict: {u'key': [u'value']}>", 'http requests data not stored in the DB correctly')
        