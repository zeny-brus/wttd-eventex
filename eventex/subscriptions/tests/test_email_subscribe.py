from django.test import TestCase

from django.core import mail



class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Fulano Ciclano', cpf='12345678901',
                    email='fulano@email.com', phone='00-999999999')
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'fulano@email.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = ['Fulano Ciclano',
                    '12345678901',
                    'fulano@email.com',
                    '00-999999999']
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
