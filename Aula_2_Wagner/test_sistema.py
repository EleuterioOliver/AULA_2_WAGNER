import pytest

from sistema import verificar_situacao

# def test_aluno_aprovado():
#     resultado = verificar_situacao(8, 6, 90)
#     assert resultado == "APROVADO"

# def test_aluno_recuperacao():
#     resultado = verificar_situacao(5, 5, 90)
#     assert resultado == "RECUPERAÇÂO"

# def test_aluno_reprovado():
#     resultado = verificar_situacao(3, 4, 90)
#     assert resultado == "REPROVADO"

# def test_aluno_frequencia():
#     assert verificar_situacao(10, 6, 70) == "REPROVADO POR FALTA"

@pytest.mark.parametrize(
    "nota1, nota2, frequencia, esperado",
    [
        (8, 6, 90, "APROVADO"),
        (7, 7, 80, "APROVADO"),
        (5, 4, 80, "REPROVADO"),
        (6, 7, 10, "REPROVADO POR FALTA")
    ]

)
def test_verificar_situacao(nota1, nota2, frequencia, esperado):
    assert verificar_situacao(nota1, nota2, frequencia) == esperado


             