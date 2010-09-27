from django.test import TestCase
from django.test.client import Client
from models import Person, HttpRequestData
from model_form import PersonDetail
from zlib import crc32
from django.conf import settings
from django.contrib.auth.models import User

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

#Ticket4
class ContextProcessorTest(TestCase):
    def loopback(self):
        response = self.client.get('/settings/')
        self.failUnlessEqual(response.context['settings']['SECRET_KEY'], settings.SECRET_KEY)
        
#Ticket5
class EditTest(TestCase):    
    def change(self):
        #login 
        username = 'root'
        password = '111111'
        login_path = '/accounts/login/'
        user = User.objects.create_user(username, 'vasya@mail.ru', password)
        user.save()
        response = self.client.get(login_path)        
        token = response.context['csrf_token']
        response = self.client.post(login_path, {'username': username, 
                                                 'password': password,
                                                 'csrfmiddlewaretoken': token}) 
        self.failUnlessEqual(response.status_code, 302, 'person edit fail - login failed')
        #change data
        person = Person.objects.all()[0]    #get person for save
        target_path = '/bio/edit/'
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