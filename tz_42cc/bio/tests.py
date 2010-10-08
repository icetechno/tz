from django.test import TestCase
from models import Person, HttpRequestData, SignalLog
from zlib import crc32
from django.conf import settings
from django.contrib.auth.models import User
from django.template.loader import get_template
from django.template import Context
from model_form import PersonForm
from django.core import management
import cStringIO


#Ticket1
class BioTest(TestCase):
    fixtures = ['initial_data.json', ]   # my fixtures

    def test_simpleTest(self):
        response = self.client.get('/')
        # Check that the response is 200 OK.
        self.failUnlessEqual(response.status_code, 200)
        # find data pattern
        self.failIfEqual(response.content.find('0974865577'),
                          -1,
                         'data pattern not found in response')


#Ticket3
class HttpRequestLogTest(TestCase):
    def test_loopback(self):
        self.client.get('/?key=value')
        log_data_obj = HttpRequestData.objects.filter(path='/')
        self.failIf(log_data_obj.count() == 0,
                    'http requests not stored in the DB')
        self.failUnlessEqual(log_data_obj[0].request,
                    u"<QueryDict: {u'key': [u'value']}>",
                    'http requests data not stored in the DB correctly')


#Ticket4
class ContextProcessorTest(TestCase):
    def test_loopback(self):
        response = self.client.get('/settings/')
        self.failUnlessEqual(response.context['settings']['SECRET_KEY'],
                             settings.SECRET_KEY)


#Ticket5
class EditTest(TestCase):
    def test_change(self):
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
        self.failUnlessEqual(response.status_code,
                             302,
                            'person edit fail - login failed')
        #change data
        person = Person.objects.all()[0]    # get person for save
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
        person.save()   # Re-write initial data
        res = str(response)
        self.failIfEqual(res.find(data['name']),
                             -1,
                             'person edit fail - incorrect data')


#Ticket6
class DateWidgetTest(TestCase):
    def test_load(self):
        # loading template
        template = get_template('bio/edit.html')
        c = Context({})
        # checkign JavaScript block CRC
        rendered_data = template.nodelist[0].blocks['js'].render(c)
        encoded_data = unicode(rendered_data).encode('utf-8')
        #for debug
        #print hex(crc32(encoded_data))
        self.failUnlessEqual(crc32(encoded_data),
                    - 0x592c8ca2,
                    'JavaScript code required by widget loaded incorrect')


#Ticket7
class ReverseTest(TestCase):
    def test_ifreversed(self):
        first_person = Person.objects.all()[0]
        form = PersonForm(instance=first_person)
        rendered_data = form.as_table()
        birthdate_pos = rendered_data.find("id_birthdate")
        name_pos = rendered_data.find("id_name")
        self.failUnless(birthdate_pos < name_pos, 'Fields are not reversed')


#Ticket8
class CustomTagTest(TestCase):
    def test_render(self):
        #create user
        username = 'root'
        password = '111111'
        user = User.objects.create_user(username, 'vasya@mail.ru', password)
        user.save()
        # Log in
        login = self.client.login(username=username, password=password)
        response = self.client.get('/')
        self.failIfEqual(
            response.content.find('a href="/admin/auth/user/1/">Edit root</a'),
            -1,
            'custom tag render error'
        )


#Ticket9
class CommandTest(TestCase):
    def test_mycommand_failure(self):
        #minimum count models in database
        MODELS_MIN = 9
        #new buffer
        new_io = cStringIO.StringIO()
        #execute my command and put out into my buffer
        management.call_command('models_count', stdout=new_io)
        #get buffer value
        command_output = new_io.getvalue()
        #set up test condition
        self.failUnless(command_output.count("<class") > MODELS_MIN,
                'models list are too small')


#Ticket10
class SignalTest(TestCase):
    def test_all(self):
        target_class = "<class 'tz_42cc.bio.models.Person'>"
        actions = ('init', 'save', 'delete')
        first_person = Person.objects.all()[0]
        first_person.name = 'test'
        first_person.save()
        first_person.delete()
        for action in actions:
            self.failUnless(
                SignalLog.objects.filter(type=action, souce=target_class),
                '%s action not found in logs' % action
            )


#Ticket11
class JqueryTest(TestCase):
    def test_edit(self):
        person = Person.objects.all()[0]
        #create user
        username = 'root',
        password = '111111'
        user = User.objects.create_user(username, 'vasya@mail.ru', password)
        user.save()
        # Log in
        login = self.client.login(username=username, password=password)
        target_path = '/edit/'
        response = self.client.get(target_path)
        token = response.context['csrf_token']
        # post form
        response = self.client.post(target_path, {'name': 'john',
                            'surname': 'smith',
                            'contacts': 'hidden',
                            'birthdate': '1983-06-24',
                            'csrfmiddlewaretoken': token, })
        person.save()
        
        res = str(response)
        self.failIfEqual(res.find('john'),
                             -1,
                             'person edit fail - incorrect data'
        )


#Ticket12
class LogTest(TestCase):
    def test_logs(self):
        response = self.client.get('/loglist/?secret_pattern=secret_pattern')
        self.failIfEqual(response.content.find('secret_pattern'),
                         -1,
                         'query not logged'
        )


#Ticket13
class LogOrderTest(TestCase):
    def test_logs(self):
        #make query
        target_path = '/loglist/'
        response = self.client.get(target_path)
        token = response.context['csrf_token']
        first_record = HttpRequestData.objects.get(pk=1)
        #Test if record exist and has default value
        self.failUnlessEqual(first_record.priority,
                             0,
                             'Log entry has wrong default priority value')
        response = self.client.post(target_path,
                            {'pk': '1',
                            'priority': 'Priority 9',
                            }
        )
        first_record = HttpRequestData.objects.get(pk=1)
        self.failUnlessEqual(first_record.priority,
                             8,
                             'Change priority failed')
