from unittest import TestCase
from src.leilao.dominio import Usuario, Lance, Leilao
from src.leilao.exececoes import LanceInvalidos


class TestLeiao(TestCase):

    def setUp(self):
        self.cecilia = Usuario("Cecilia", 500.0)
        self.igor = Usuario("Igor", 500.0)
        self.cady = Usuario("Cady", 500.0)

        self.lance_da_cecilia = Lance(self.cecilia, 80.00)
        self.lance_do_igor = Lance(self.igor, 100.00)
        self.lance_da_cady = Lance(self.cady, 150.00)

        self.leilao_beneficente = Leilao("Leilao do Celular")

    def test_deve_retornar_o_maior_e_o_menor_valor_de_uma_lance_quando_adicionado_em_ordem_crecente(self):
        self.leilao_beneficente.propoem(self.lance_da_cecilia)
        self.leilao_beneficente.propoem(self.lance_do_igor)

        menor_valor_experado = 80.00
        maior_valor_experado = 100.00

        self.assertEqual(menor_valor_experado, self.leilao_beneficente.menor_lance)
        self.assertEqual(maior_valor_experado, self.leilao_beneficente.maior_lance)

    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrecente(self):
        with self.assertRaises(LanceInvalidos):
            self.leilao_beneficente.propoem(self.lance_do_igor)
            self.leilao_beneficente.propoem(self.lance_da_cecilia)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_o_menor_lance_quando_adicionado_apenas_um_lance(self):
        self.leilao_beneficente.propoem(self.lance_do_igor)

        menor_valor_experado = 100.00
        maior_valor_experado = 100.00

        self.assertEqual(menor_valor_experado, self.leilao_beneficente.menor_lance)
        self.assertEqual(maior_valor_experado, self.leilao_beneficente.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_uma_lance_quando_adicionado_tres_lances_no_leilao(self):
        self.leilao_beneficente.propoem(self.lance_da_cecilia)
        self.leilao_beneficente.propoem(self.lance_do_igor)
        self.leilao_beneficente.propoem(self.lance_da_cady)

        menor_valor_experado = 80.00
        maior_valor_experado = 150.00

        self.assertEqual(menor_valor_experado, self.leilao_beneficente.menor_lance)
        self.assertEqual(maior_valor_experado, self.leilao_beneficente.maior_lance)

    # se o leilao nao tiver lances, deve permitir propor um lance
    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao_beneficente.propoem(self.lance_do_igor)

        quantidade_de_lances_recebido = len(self.leilao_beneficente.lances)
        self.assertEqual(1, quantidade_de_lances_recebido)

    # se o usuario for diferente, deve permitir propor um lance
    def test_deve_permitir_propor_um_lance_caso_o_usuario_seja_diferente(self):
        self.leilao_beneficente.propoem(self.lance_da_cecilia)
        self.leilao_beneficente.propoem(self.lance_do_igor)

        quantidade_de_lances_recebido = len(self.leilao_beneficente.lances)

        self.assertEqual(2, quantidade_de_lances_recebido)

    # se o ultimo usuario for o mesmo, não deve permitir propor um lance
    def test_nao_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_o_mesmo(self):
        lance_do_igor200 = Lance(self.igor, 200.00)

        with self.assertRaises(LanceInvalidos):
            self.leilao_beneficente.propoem(self.lance_do_igor)
            self.leilao_beneficente.propoem(lance_do_igor200)
