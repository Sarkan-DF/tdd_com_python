from src.leilao.dominio import Usuario, Lance, Leilao

igor = Usuario("Igor")
cecilia = Usuario("Cecilia")

lance_do_igor = Lance(igor, 100.00)
lance_da_cecilia = Lance(cecilia, 200.00)

leilao_beneficente = Leilao("Leilao do Celular")

leilao_beneficente.lances.append(lance_do_igor)
leilao_beneficente.lances.append(lance_da_cecilia)

# for lance in leilao_beneficente.lances:
#     print(f"O usuario {lance.usuario.nome} deu um lance de {lance.valor}")
#
# avaliador = Avaliador()
# avaliador.avalia(leilao_beneficente)
#
# print(f"O menor lance foi {avaliador.menor_lance} e o maior lance foi {avaliador.maior_lance}")