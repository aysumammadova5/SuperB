from django.test import TestCase
from core.models import ContactUs

class ContactUsModelTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = {
            'name': 'Sevda',
            'email': 'muxtarli.sevda@gmail.com',
            'company': 'something',
            'phone': '0774040404',
            'address': 'text',
            'comment': 'text',
        }
        cls.contact = ContactUs.objects.create(**cls.data)


    def test_create_method(self):
        contact = ContactUs.objects.first()
        self.assertEqual(self.contact, contact)

    @classmethod
    def tearDownClass(cls):
        pass