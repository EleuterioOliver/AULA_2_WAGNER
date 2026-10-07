def verificar_situacao(nota1,nota2,frequencia):
    media = (nota1 + nota2)/2

    if frequencia < 75:
        return "REPROVADO POR FALTA"

    if media >= 7:
        return "APROVADO"

    if media >= 5:
        return "RECUPERAÇÂO"
    
    return "REPROVADO"