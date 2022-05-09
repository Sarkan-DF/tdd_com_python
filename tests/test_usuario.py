from src.leilao.dominio import Usuario, Leilao
import pytest

from src.leilao.exececoes import LanceInvalidos


@pytest.fixture
def cecilia():
    return Usuario("Cecilia", 100.00)


@pytest.fixture
def leilao_beneficente():
    return Leilao("Leilão beneficente de celular")


def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(cecilia, leilao_beneficente):
    cecilia.propoe_lance(leilao_beneficente, 50.0)
    assert cecilia.carteira == 50.0


def test_deve_permitir_propor_lances_quando_o_valor_eh_menor_que_o_valor_da_carteira(cecilia, leilao_beneficente):
    cecilia.propoe_lance(leilao_beneficente, 1.0)
    assert cecilia.carteira == 99.0


def test_deve_permitir_propor_lances_quando_o_valor_eh_igual_ao_valor_da_carteira(cecilia, leilao_beneficente):
    cecilia.propoe_lance(leilao_beneficente, 100.0)
    assert cecilia.carteira == 0.0


def test_nao_deve_permitir_propor_lances_com_valor_maior_que_o_valor_da_carteira(cecilia, leilao_beneficente):
    with pytest.raises(LanceInvalidos):
        cecilia.propoe_lance(leilao_beneficente, 200.0)