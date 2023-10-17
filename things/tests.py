from django.test import TestCase
from things.models import Thing
from things.forms import ThingForm

# Create your tests here.
class ThingFormTestCase(TestCase):
    def setUp(self):
        self.form_input = {
            'name': "ash",
            'quantity': "5",
            'description': "hi",
        }

    # form acceps valid input data
    def test_valid_form(self):    
        form = ThingForm(data=self.form_input)
        self.assertTrue(form.is_valid())
        
    # form users model validation
    def test_form_uses_model_validation(self):
        self.form_input['quantity'] = 'a' # remember usernames have @ in our app
        form = ThingForm(data=self.form_input)
        self.assertFalse(form.is_valid())
