from django.test import TestCase
from models import Person


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
