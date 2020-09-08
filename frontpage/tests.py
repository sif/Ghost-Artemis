from django.test import TestCase

from django.urls import reverse

# Unit tests
# Regression tests
# Integration tests
# TDD, write tests before writing code
# AssertTrue, AssertFalse, AssertEqual

class FrontPageTest(TestCase):
    def test_contact(self):
        url = reverse("contact")
        resp = self.client.get(url, follow=True)

        self.assertEqual(resp.status_code, 200)
