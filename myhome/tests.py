from django.test import TestCase, SimpleTestCase

# Create your tests here.
class SimpleTest(SimpleTestCase):
    def test_home_page_status(seft):
        response = seft.client.get('/about')
        seft.assertEquals(response.status_code, 200)
