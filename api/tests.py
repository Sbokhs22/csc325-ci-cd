
from django.test import TestCase
from django.urls import reverse


class StatusAPITests(TestCase):

    def test_status_returns_correct_message(self):
        response = self.client.get(reverse('api-status'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json()['message'],
            'CSC 325 CI/CD API'
        )

    def test_status_returns_ok(self):
        response = self.client.get(reverse('api-status'))

        self.assertEqual(response.json()['status'], 'ok')
        self.assertEqual(
            response['Content-Type'],
            'application/json'
        )

    def test_status_returns_version(self):
        response = self.client.get(reverse('api-status'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json()['version'],
            '1.1'
        )
