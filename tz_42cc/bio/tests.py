from django.test import TestCase
from models import Person, HttpRequestData
from zlib import crc32
from django.conf import settings
from django.contrib.auth.models import User
from django.template.loader import get_template
from django.template import Context
from model_form import PersonForm

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

#Ticket6        
class DateWidgetTest(TestCase):
    def load(self):        
        #loading template
        template = get_template('bio/edit.html')
        c = Context({})        
        #checkign JavaScript block CRC
        rendered_data = template.nodelist[0].blocks['js'].render(c)
        encoded_data = unicode(rendered_data).encode('utf-8')
        self.failUnlessEqual(crc32(encoded_data), -0x1d02e87b , 'JavaScript code required by widget loaded incorrect')       

#Ticket7
class ReverseTest(TestCase):
    def check_ifreversed(self):
        first_person = Person.objects.all()[0]
        form = PersonForm(instance = first_person)
        rendered_data = form.as_table()
        birthdate_pos = rendered_data.find("id_birthdate")
        name_pos = rendered_data.find("id_name")
        self.failUnless(birthdate_pos < name_pos, 'Fields are not reversed')

#Ticket8
class CustomTagTest(TestCase):
    def check_render(self):
        #create user
        username = 'root'
        password = '111111'
        user = User.objects.create_user(username, 'vasya@mail.ru', password)
        user.save()
        # Log in
        login = self.client.login(username = username, password = password)
        response = self.client.get('/')
        self.failIfEqual(response.content.find('<a href="/admin/auth/user/1/">Edit root</a>'), -1, 'custom tag render error')