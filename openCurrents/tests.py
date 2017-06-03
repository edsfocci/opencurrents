from django.contrib.auth.models import User
from django.test import TestCase

######################################################################################
#Run this file in the manage.py directory as 'python manage.py test openCurrents.tests'
######################################################################################

class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
    
    def test_login(self):
        # send login data
        form_data = { 'user_email':'testuser','user_password':'secret' }
        response = self.client.post('/process_login/', form_data, follow=True)
        self.assertContains(response, "Invalid login/password", 1, 200)
        
    def test_log_success(self):
        form_data = { 'user_email':'testuser','user_password':'secret' }
        response = self.client.post('/process_login/', form_data, follow=True)
        print(response)
        self.assertContains(response, "Welcome", 1, 200)
