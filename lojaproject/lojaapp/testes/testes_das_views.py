from django.test import TestCase

from django.core import mail

from lojaapp import forms

class TestarForms(TestCase):

    def testar_formulario_fale_conosco_corretamente_preenchido(self):

        formulario = forms.FaleConoscoForm({

            'nome':'Francisco Maciel',

            'email_origem': 'francisco@teste.com',

            'mensagem': 'Testando a funcionalidade do formulário Fale Conosco'

            }

        )

        self.assertTrue(formulario.is_valid())

        formulario.enviar_mensagem_por_email()

        self.assertEqual(len(mail.outbox), 1)

        self.assertEqual(mail.outbox[0].subject, 'FALE CONOSCO: Mensagem recebida.')

    def testar_formulario_fale_conosco_invalido(self):

        formulario = forms.FaleConoscoForm({
            
                'mensagem': 'Testando a funcionalidade do formulário Fale Conosco'
            }

        )

        self.assertFalse(formulario.is_valid())