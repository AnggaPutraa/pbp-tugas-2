from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):

    def setUp(self):
        self.client = Client();
        self.urlToViewHtml = reverse(
            'mywatchlist:show_my_watch_list'
        )
        self.urlToViewJson = reverse(
            'mywatchlist:show_my_watchlist_json'
        )
        self.urlToViewXML = reverse(
            'mywatchlist:show_my_watchlist_xml'
        )

    def test_show_my_wish_list(self):
        response = self.client.get(
            self.urlToViewHtml
        )
        self.assertEqual(
            response.status_code,
            200
        )
        self.assertTemplateUsed(
            response,
            'mywatchlist.html'
        )

    def test_show_my_wish_list_as_json(self):
        response = self.client.get(
            self.urlToViewJson
        )
        self.assertEqual(
            response.status_code,
            200
        )

    def test_show_my_wish_list_as_xml(self):
        response = self.client.get(
            self.urlToViewXML
        )
        self.assertEqual(
            response.status_code,
            200
        )
