from datetime import datetime
from collections import Counter

print(" ")
print("Numerologia Kármica")
print("--------------------")
print(" ")

nome = input("Digite seu nome: ")
while True:
    data_nascimento = input("Digite sua data de nascimento (DDMMAAAA): ")

    if len(data_nascimento) != 8 or not data_nascimento.isdigit():
        print("Formato de data inválido. Digite novamente.")
        continue

    dia = int(data_nascimento[:2])
    mes = int(data_nascimento[2:4])
    ano = int(data_nascimento[4:])
    break

print("")
print("No Calculo do Ano Pessoal:")
futuro = input(
    f"Digite (S) para {datetime.now().year + 1} ou (N) para {datetime.now().year}: ")


def verifica_numero(num):
    if num > 22:
        # Transforma o número em uma string para poder separar os dígitos
        num_str = str(num)
        # Inicializa a variável soma como zero
        soma = 0
        # Percorre cada dígito da string e soma ao valor de soma
        for digito in num_str:
            soma += int(digito)

        # Verifica se a soma está no intervalo de 1 a 22
        if soma <= 22:
            return soma
        else:
            # Chama a função recursivamente para somar novamente os dígitos
            return verifica_numero(soma)
    else:
        # Retorna o número sem modificação se for menor ou igual a 22
        return num


def subtrair_digitos(num):
    # Converte o número em uma string para poder separar os dígitos
    num_str = str(num)
    resultado = 0

    # Itera sobre os dígitos do número, subtraindo cada par consecutivo
    for i in range(len(num_str)-1):
        resultado += int(num_str[i]) - int(num_str[i+1])

    return abs(resultado)


def somar_digitos(numero):
    # Inicializa a variável soma com o valor zero
    soma = 0
    # Enquanto o número for maior que zero
    while numero > 0:
        # Adiciona o último dígito do número à soma
        soma += numero % 10
        # Remove o último dígito do número
        numero = numero // 10
    # Retorna a soma dos dígitos
    return soma


def converter_mes(numero):
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
             'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

    if numero == 0:
        return "Ocorrerá o ano todo"
    elif numero > 12:
        numero = sum([int(d) for d in str(numero)])

    mes_index = numero - 1

    if mes_index < 0 or mes_index >= len(meses):
        raise ValueError("Número inválido")

    return meses[mes_index]


def calcular_arcanos(ciclo_inicio, mva, ano_atual):
    arcanos = []
    ciclo = ciclo_inicio

    while ciclo <= ano_atual + 50:
        soma = ciclo + mva
        arcano = verifica_numero(somar_digitos(soma))
        arcanos.append((ciclo, arcano))
        ciclo += mva

    return arcanos


def verificar_mes_positivo(n):
    while n > 12:
        n = sum(map(int, str(n)))
    return n


def verificar_mes_negativo(n):
    if n > 12:
        # Converta o número em string para acessar os dígitos individualmente
        str_n = str(n)

        # Subtraia o primeiro dígito pelo segundo dígito
        resultado = int(str_n[0]) - int(str_n[1])
    else:
        resultado = n

    return abs(resultado)


def encontrar_ciclo_atual(ano_atual, ciclos_arcanos):
    for i, (ciclo, arcano) in enumerate(ciclos_arcanos):
        # Verifique se i+1 não ultrapassa o limite da lista
        if i + 1 < len(ciclos_arcanos) and ano_atual < ciclos_arcanos[i + 1][0]:
            return ciclo, arcano
    return ciclos_arcanos[-1]


def calcular_ano_pessoal(ano_atual, mva, arcano_ciclo_atual):
    soma = ano_atual + mva
    arcano = verifica_numero(soma)
    resultado_ano = arcano + arcano_ciclo_atual
    return verifica_numero(resultado_ano)


def separar_numero(numero):
    numero_str = str(numero)
    if len(numero_str) != 4:
        raise ValueError("Número deve conter 4 dígitos")
    primeiro_numero = int(numero_str[:2])
    segundo_numero = int(numero_str[2:])
    return primeiro_numero, segundo_numero


def numero_primal(numero):
    if numero <= 9:
        return numero
    else:
        soma_digitos = sum(int(d) for d in str(numero))
        return numero_primal(soma_digitos)


def ordenar_lista(lista):
    # Remove elementos duplicados e zero da lista
    lista_sem_dup = list(set(filter(lambda x: x != 0, lista)))

    # Ordena a lista em ordem decrescente
    lista_sem_dup.sort(reverse=True)

    return lista_sem_dup


def arcano_maior(numero):
    arcanos = {
        0: "Nulo",
        1: "O Mago",
        2: "A Papisa",
        3: "A Imperatriz",
        4: "O Imperador",
        5: "O Hierofante",
        6: "Os Amantes",
        7: "O Carro",
        8: "A Justiça",
        9: "O Eremita",
        10: "A Roda da Fortuna",
        11: "A Força",
        12: "O Enforcado",
        13: "A Morte",
        14: "A Temperança",
        15: "O Diabo",
        16: "A Torre",
        17: "A Estrela",
        18: "A Lua",
        19: "O Sol",
        20: "O Julgamento",
        21: "O Mundo",
        22: "O Louco"
    }

    if numero < 0 or numero > 22:
        raise ValueError("Número inválido")

    return arcanos[numero]


def arcano_piramide(numero):
    arcanos = {
        0: "O Louco",
        1: "O Mago",
        2: "A Papisa",
        3: "A Imperatriz",
        4: "O Imperador",
        5: "O Hierofante",
        6: "Os Amantes",
        7: "O Carro",
        8: "A Justiça",
        9: "O Eremita",
        10: "A Roda da Fortuna",
        11: "A Força",
        12: "O Enforcado",
        13: "A Morte",
        14: "A Temperança",
        15: "O Diabo",
        16: "A Torre",
        17: "A Estrela",
        18: "A Lua",
        19: "O Sol",
        20: "O Julgamento",
        21: "O Mundo",
        22: "O Louco"
    }

    if numero < 0 or numero > 22:
        raise ValueError("Número inválido")

    return arcanos[numero]


def repeticao_numeros(lista):
    # Conta a frequência de cada número na lista
    contagem = Counter(lista)

    # Encontra o número que mais aparece e o seu valor de contagem
    numero_mais_frequente, contagem_mais_frequente = contagem.most_common(1)[0]

    # Procura pelo primeiro número na lista que tem a contagem mais frequente
    for numero in lista:
        if contagem[numero] == contagem_mais_frequente:
            return numero

    # Caso não haja empate, retorna o número mais frequente
    return numero_mais_frequente


def remove_zeros(lista):
    """
    Remove os zeros de uma lista de números.

    Args:
        lista (list): Lista de números.

    Returns:
        list: Lista de números sem zeros.
    """
    return [x for x in lista if x != 0]


def imprimir_secao(nome_mes, positivo, negativo):
    resultado_piramide_ano = ""
    if positivo or negativo:
        resultado_piramide_ano += f"------------------------------\n"
        resultado_piramide_ano += f"{nome_mes}:\n"
        resultado_piramide_ano += f"------------------------------"
        resultado_piramide_ano += f"\n"
        if positivo:
            resultado_piramide_ano += f"\n"
            resultado_piramide_ano += f"Arcano(s) Positivo(s) =\n\n {positivo}"
            resultado_piramide_ano += f"\n"
        if negativo:
            resultado_piramide_ano += f"\n"
            resultado_piramide_ano += f"Arcano(s) Negativo(s) =\n\n {negativo}"
            resultado_piramide_ano += f"\n"
            resultado_piramide_ano += f"\n"
    else:
        resultado_piramide_ano += f"------------------------------\n"
        resultado_piramide_ano += f"{nome_mes}: Sem Influências \n"
        resultado_piramide_ano += f"------------------------------"
        resultado_piramide_ano += f"\n"
        resultado_piramide_ano += f"\n"

    return resultado_piramide_ano


pi = verifica_numero(dia)
pe = verifica_numero(mes)
pg = verifica_numero(pi + pe)
rva = verifica_numero(somar_digitos(ano))
mva = verifica_numero(somar_digitos(dia + mes + ano))
po = somar_digitos(pg)
df = subtrair_digitos(pg)
if df == 0:
    df = pg
fd = verifica_numero(rva + df)
fm = verifica_numero(mva + pg)
ablo = verifica_numero(fd + fm)
do = verifica_numero(dia - mes)
ilka = pi + pe + rva + mva


# Acrescente a chamada à função `calcular_arcanos` após a definição de `ilka`
ano_atual = int(datetime.now().year)
if futuro == "S":
    ano_atual += 1
ciclos_arcanos = calcular_arcanos(ano, mva, ano_atual)

# Exiba os resultados dos arcanos regentes dos ciclos
resultado_ciclos = ""
for i, (ciclo, arcano) in enumerate(ciclos_arcanos[:-1]):
    resultado_ciclos += f"{ciclo - ano} até {ciclos_arcanos[i + 1][0] - ano} anos: Arcano regente do ciclo é : {arcano_maior(arcano)}\n"

resultado_ciclos += f"{ciclos_arcanos[-1][0] - ano} anos em diante: Arcano regente do ciclo é : {arcano_maior(ciclos_arcanos[-1][1])}\n"

# Armazene o ciclo atual após a chamada à função `calcular_ano_pessoal`
ciclo_atual, arcano_ciclo_atual = encontrar_ciclo_atual(
    ano_atual, ciclos_arcanos)


# Acrescente a chamada à função `calcular_ano_pessoal` após a definição de `resultado_ciclos`
arcano_ano_pessoal = calcular_ano_pessoal(ano_atual, mva, arcano_ciclo_atual)


l1, l2 = separar_numero(ano_atual + mva)
l3 = verifica_numero(ano_atual + mva)
l4 = arcano_ciclo_atual
l5 = verifica_numero(arcano_ano_pessoal)

m1p = verificar_mes_positivo(l1)
m2p = verificar_mes_positivo(l2)
m3p = verificar_mes_positivo(l3)
m4p = verificar_mes_positivo(l4)
m5p = verificar_mes_positivo(l5)
m6p = verificar_mes_positivo(m1p + m2p)
m7p = verificar_mes_positivo(m2p + m3p)
m8p = verificar_mes_positivo(m3p + m4p)
m9p = verificar_mes_positivo(m4p + m5p)
m10p = verificar_mes_positivo(m6p + m7p)
m11p = verificar_mes_positivo(m7p + m8p)
m12p = verificar_mes_positivo(m8p + m9p)
m13p = verificar_mes_positivo(m10p + m11p)
m14p = verificar_mes_positivo(m11p + m12p)
m15p = verificar_mes_positivo(m13p + m14p)

m1n = verificar_mes_negativo(l1)
m2n = verificar_mes_negativo(l2)
m3n = verificar_mes_negativo(l3)
m4n = verificar_mes_negativo(l4)
m5n = verificar_mes_negativo(l5)
m6n = abs(m1n - m2n)
m7n = abs(m2n - m3n)
m8n = abs(m3n - m4n)
m9n = abs(m4n - m5n)
m10n = abs(m6n - m7n)
m11n = abs(m7n - m8n)
m12n = abs(m8n - m9n)
m13n = abs(m10n - m11n)
m14n = abs(m11n - m12n)
m15n = abs(m13n - m14n)

a1p = verifica_numero(l1 + l2)
a2p = verifica_numero(l2 + l3)
a3p = verifica_numero(l3 + l4)
a4p = verifica_numero(l4 + l5)
a5p = verifica_numero(a1p + a2p)
a6p = verifica_numero(a2p + a3p)
a7p = verifica_numero(a3p + a4p)
a8p = verifica_numero(a5p + a6p)
a9p = verifica_numero(a6p + a7p)
a10p = verifica_numero(a8p + a9p)

a1n = (verifica_numero(abs(l1 - l2)))
a2n = (verifica_numero(abs(l2 - l3)))
a3n = (verifica_numero(abs(l3 - l4)))
a4n = (verifica_numero(abs(l4 - l5)))
a5n = (verifica_numero(abs(a1n - a2n)))
a6n = (verifica_numero(abs(a2n - a3n)))
a7n = (verifica_numero(abs(a3n - a4n)))
a8n = (verifica_numero(abs(a5n - a6n)))
a9n = (verifica_numero(abs(a6n - a7n)))
a10n = (verifica_numero(abs(a8n - a9n)))


m1 = converter_mes(l1)
m2 = converter_mes(l2)
m3 = converter_mes(l3)
m4 = converter_mes(l4)
m5 = converter_mes(l5)


# ...

meses_positivos = [converter_mes(m1p), converter_mes(m2p), converter_mes(m3p), converter_mes(m4p), converter_mes(m5p), converter_mes(m6p), converter_mes(m7p), converter_mes(
    m8p), converter_mes(m9p), converter_mes(m10p), converter_mes(m11p), converter_mes(m12p), converter_mes(m13p), converter_mes(m14p), converter_mes(m15p)]
arcanos_positivos = [(arcano_piramide(a1p)), (arcano_piramide(a1p), arcano_piramide(a2p), arcano_piramide(a5p)), (arcano_piramide(a2p), arcano_piramide(a6p), arcano_piramide(a3p)), (arcano_piramide(a3p), arcano_piramide(a7p), arcano_piramide(a4p)), (arcano_piramide(a4p)),
                     (arcano_piramide(a1p), arcano_piramide(a5p)), (arcano_piramide(a5p), arcano_piramide(a8p), arcano_piramide(a2p), arcano_piramide(
                         a6p)), (arcano_piramide(a6p), arcano_piramide(a7p), arcano_piramide(a9p), arcano_piramide(a3p)), (arcano_piramide(a4p), arcano_piramide(a7p)),
                     (arcano_piramide(a5p), arcano_piramide(a8p)), (arcano_piramide(a8p), arcano_piramide(a6p), arcano_piramide(a9p), arcano_piramide(a10p)), (arcano_piramide(a7p), arcano_piramide(a9p)), (arcano_piramide(a8p), arcano_piramide(a10p)), (arcano_piramide(a10p), arcano_piramide(a9p)), (arcano_piramide(a10p))]

meses_negativos = [converter_mes(m1n), converter_mes(m2n), converter_mes(m3n), converter_mes(m4n), converter_mes(m5n), converter_mes(m6n), converter_mes(m7n),
                   converter_mes(m8n), converter_mes(m9n), converter_mes(m10n), converter_mes(m11n), converter_mes(m12n), converter_mes(m13n), converter_mes(m14n), converter_mes(m15n)]
arcanos_negativos = [(arcano_piramide(a1n)), (arcano_piramide(a1n), arcano_piramide(a2n), arcano_piramide(a5n)), (arcano_piramide(a2n), arcano_piramide(a6n), arcano_piramide(a3n)), (arcano_piramide(a3n), arcano_piramide(a7n), arcano_piramide(a4n)), (arcano_piramide(a4n)),
                     (arcano_piramide(a1n), arcano_piramide(a5n)), (arcano_piramide(a5n), arcano_piramide(a8n), arcano_piramide(a2n), arcano_piramide(
                         a6n)), (arcano_piramide(a6n), arcano_piramide(a7n), arcano_piramide(a9n), arcano_piramide(a3n)), (arcano_piramide(a4n), arcano_piramide(a7n)),
                     (arcano_piramide(a5n), arcano_piramide(a8n)), (arcano_piramide(a8n), arcano_piramide(a6n), arcano_piramide(a9n), arcano_piramide(a10n)), (arcano_piramide(a7n), arcano_piramide(a9n)), (arcano_piramide(a8n), arcano_piramide(a10n)), (arcano_piramide(a10n), arcano_piramide(a9n)), (arcano_piramide(a10n))]


# ...


# Roda das Encarnações

pre_1 = verifica_numero(dia)
if pre_1 > 9:
    pre_2 = numero_primal(pre_1)
else:
    pre_2 = 0

lista_1 = [pre_1, pre_2]

sre_1 = verifica_numero(mes)
if sre_1 > 9:
    sre_2 = numero_primal(sre_1)
else:
    sre_2 = 0

lista_2 = [sre_1, sre_2]

tre_1 = verifica_numero(ano)
if tre_1 > 9:
    tre_2 = numero_primal(tre_1)
else:
    tre_2 = 0

lista_3 = [tre_1, tre_2]

vr1, vr2 = separar_numero(ano)
qre_1 = verifica_numero(vr2)
if qre_1 > 9:
    qre_2 = numero_primal(qre_1)
else:
    qre_2 = 0

lista_4 = [qre_1, qre_2]

if lista_1[0] != 0 and lista_2[0] != 0 and lista_3[0] != 0:
    x1 = verifica_numero(lista_1[0] + lista_2[0] + lista_3[0])
else:
    x1 = 0

if lista_1[0] != 0 and lista_2[0] != 0 and lista_3[1] != 0:
    x2 = verifica_numero(lista_1[0] + lista_2[0] + lista_3[1])
else:
    x2 = 0

if lista_1[0] != 0 and lista_2[1] != 0 and lista_3[0] != 0:
    x3 = verifica_numero(lista_1[0] + lista_2[1] + lista_3[0])
else:
    x3 = 0

if lista_1[0] != 0 and lista_2[1] != 0 and lista_3[1] != 0:
    x4 = verifica_numero(lista_1[0] + lista_2[1] + lista_3[1])
else:
    x4 = 0

if lista_1[1] != 0 and lista_2[0] != 0 and lista_3[0] != 0:
    x5 = verifica_numero(lista_1[1] + lista_2[0] + lista_3[0])
else:
    x5 = 0

if lista_1[1] != 0 and lista_2[0] != 0 and lista_3[1] != 0:
    x6 = verifica_numero(lista_1[1] + lista_2[0] + lista_3[1])
else:
    x6 = 0

if lista_1[1] != 0 and lista_2[1] != 0 and lista_3[0] != 0:
    x7 = verifica_numero(lista_1[1] + lista_2[1] + lista_3[0])
else:
    x7 = 0

if lista_1[1] != 0 and lista_2[1] != 0 and lista_3[1] != 0:
    x8 = verifica_numero(lista_1[1] + lista_2[1] + lista_3[1])
else:
    x8 = 0

if lista_1[0] != 0 and lista_2[0] != 0 and lista_4[0] != 0:
    x9 = verifica_numero(lista_1[0] + lista_2[0] + lista_4[0])
else:
    x9 = 0

if lista_1[0] != 0 and lista_2[0] != 0 and lista_4[1] != 0:
    x10 = verifica_numero(lista_1[0] + lista_2[0] + lista_4[1])
else:
    x10 = 0

if lista_1[0] != 0 and lista_2[1] != 0 and lista_4[0] != 0:
    x11 = verifica_numero(lista_1[0] + lista_2[1] + lista_4[0])
else:
    x11 = 0

if lista_1[0] != 0 and lista_2[1] != 0 and lista_4[1] != 0:
    x12 = verifica_numero(lista_1[0] + lista_2[1] + lista_4[1])
else:
    x12 = 0

if lista_1[1] != 0 and lista_2[0] != 0 and lista_4[0] != 0:
    x13 = verifica_numero(lista_1[1] + lista_2[0] + lista_4[0])
else:
    x13 = 0

if lista_1[1] != 0 and lista_2[0] != 0 and lista_4[1] != 0:
    x14 = verifica_numero(lista_1[1] + lista_2[0] + lista_4[1])
else:
    x14 = 0

if lista_1[1] != 0 and lista_2[1] != 0 and lista_4[0] != 0:
    x15 = verifica_numero(lista_1[1] + lista_2[1] + lista_4[0])
else:
    x15 = 0

if lista_1[1] != 0 and lista_2[1] != 0 and lista_4[1] != 0:
    x16 = verifica_numero(lista_1[1] + lista_2[1] + lista_4[1])
else:
    x16 = 0

lista_5 = [x1, x2, x3, x4, x5, x6, x7, x8,
           x9, x10, x11, x12, x13, x14, x15, x16]
lista_6 = ordenar_lista(lista_5)

encarnacao_atual = lista_6[0]
karma = 0
karma_causal = 0
karma_geral = 0
tendencia = 0
subtendencia = 0
frequencia = 0
subfrequencia = 0

if len(lista_6) == 2:
    if lista_6[1] >= encarnacao_atual - 3:
        karma = lista_6[1]
    if lista_6[1] < encarnacao_atual - 3:
        tendencia = lista_6[1]

if len(lista_6) == 3:
    if lista_6[1] >= encarnacao_atual - 3:
        karma = lista_6[1]
    if lista_6[1] < encarnacao_atual - 3:
        tendencia = lista_6[1]
    if karma != 0:
        tendencia = lista_6[2]
    if karma == 0:
        if lista_6[2] >= tendencia - 3:
            subtendencia = lista_6[2]
        else:
            frequencia = lista_6[2]

if len(lista_6) == 4:
    if lista_6[1] >= encarnacao_atual - 3:
        karma = lista_6[1]
    if lista_6[1] < encarnacao_atual - 3:
        tendencia = lista_6[1]
    if karma != 0:
        tendencia = lista_6[2]
    if karma == 0:
        if lista_6[2] >= tendencia - 3:
            subtendencia = lista_6[2]
        else:
            frequencia = lista_6[2]
    if karma != 0 and lista_6[3] >= tendencia - 3:
        subtendencia = lista_6[3]
    if subtendencia == lista_6[2]:
        frequencia = lista_6[3]

if len(lista_6) == 5:
    if lista_6[1] >= encarnacao_atual - 3:
        karma = lista_6[1]
    if lista_6[1] < encarnacao_atual - 3:
        tendencia = lista_6[1]
    if karma != 0:
        tendencia = lista_6[2]
    if karma == 0:
        if lista_6[2] >= tendencia - 3:
            subtendencia = lista_6[2]
        else:
            frequencia = lista_6[2]
    if karma != 0 and lista_6[3] >= tendencia - 3:
        subtendencia = lista_6[3]
    if subtendencia == lista_6[2]:
        frequencia = lista_6[3]
    if karma != 0:
        frequencia = lista_6[4]
    if karma == 0:
        subtendencia = lista_6[4]

if len(lista_6) > 5:
    if lista_6[1] >= encarnacao_atual - 3:
        karma = lista_6[1]
    if lista_6[1] < encarnacao_atual - 3:
        tendencia = lista_6[1]
    if karma != 0:
        tendencia = lista_6[2]
    if karma == 0:
        if lista_6[2] >= tendencia - 3:
            subtendencia = lista_6[2]
        else:
            frequencia = lista_6[2]
    if karma != 0 and lista_6[3] >= tendencia - 3:
        subtendencia = lista_6[3]
    if subtendencia == lista_6[2]:
        frequencia = lista_6[3]
    if karma != 0:
        frequencia = lista_6[4]
    if karma == 0:
        subtendencia = lista_6[4]
    if karma != 0:
        subfrequencia = lista_6[5]


if karma != 0:
    karma_causal = verifica_numero(karma + mva)
    karma_geral = verifica_numero(karma + rva)


lista_7 = [pi, pe, pg, po, df, rva, mva, fd, fm, ablo, do, encarnacao_atual, karma,
           tendencia, subtendencia, frequencia, subfrequencia, karma_causal, karma_geral]


arcano_repetido = arcano_maior(repeticao_numeros(remove_zeros(lista_7)))


ano_todo_positivo = ""
ano_todo_negativo = ""
janeiro_positivo = ""
janeiro_negativo = ""
fevereiro_positivo = ""
fevereiro_negativo = ""
marco_positivo = ""
marco_negativo = ""
abril_positivo = ""
abril_negativo = ""
maio_positivo = ""
maio_negativo = ""
junho_positivo = ""
junho_negativo = ""
julho_positivo = ""
julho_negativo = ""
agosto_positivo = ""
agosto_negativo = ""
setembro_positivo = ""
setembro_negativo = ""
outubro_positivo = ""
outubro_negativo = ""
novembro_positivo = ""
novembro_negativo = ""
dezembro_positivo = ""
dezembro_negativo = ""


for i in range(15):
    if meses_positivos[i] == converter_mes(0):
        ano_todo_positivo += f"{arcanos_positivos[i]}\n"
    if meses_negativos[i] == converter_mes(0):
        ano_todo_negativo += f"{arcanos_negativos[i]}\n"
    if meses_positivos[i] == converter_mes(1):
        janeiro_positivo += f"{arcanos_positivos[i]}\n"
    if meses_negativos[i] == converter_mes(1):
        janeiro_negativo += f"{arcanos_negativos[i]}\n"
    if meses_positivos[i] == converter_mes(2):
        fevereiro_positivo += f"{arcanos_positivos[i]}\n"
    if meses_negativos[i] == converter_mes(2):
        fevereiro_negativo += f"{arcanos_negativos[i]}\n"
    if meses_positivos[i] == converter_mes(3):
        marco_positivo += f"{arcanos_positivos[i]}\n"
    if meses_negativos[i] == converter_mes(3):
        marco_negativo += f"{arcanos_negativos[i]}\n"
    if meses_positivos[i] == converter_mes(4):
        abril_positivo += f"{arcanos_positivos[i]}\n"
    if meses_negativos[i] == converter_mes(4):
        abril_negativo += f"{arcanos_negativos[i]}\n"
    if meses_positivos[i] == converter_mes(5):
        maio_positivo += f"{arcanos_positivos[i]}\n"
    if meses_negativos[i] == converter_mes(5):
        maio_negativo += f"{arcanos_negativos[i]}\n"
    if meses_positivos[i] == converter_mes(6):
        junho_positivo += f"{arcanos_positivos[i]}\n"
    if meses_negativos[i] == converter_mes(6):
        junho_negativo += f"{arcanos_negativos[i]}\n"
    if meses_positivos[i] == converter_mes(7):
        julho_positivo += f"{arcanos_positivos[i]}\n"
    if meses_negativos[i] == converter_mes(7):
        julho_negativo += f"{arcanos_negativos[i]}\n"
    if meses_positivos[i] == converter_mes(8):
        agosto_positivo += f"{arcanos_positivos[i]}\n"
    if meses_negativos[i] == converter_mes(8):
        agosto_negativo += f"{arcanos_negativos[i]}\n"
    if meses_positivos[i] == converter_mes(9):
        setembro_positivo += f"{arcanos_positivos[i]}\n"
    if meses_negativos[i] == converter_mes(9):
        setembro_negativo += f"{arcanos_negativos[i]}\n"
    if meses_positivos[i] == converter_mes(10):
        outubro_positivo += f"{arcanos_positivos[i]}\n"
    if meses_negativos[i] == converter_mes(10):
        outubro_negativo += f"{arcanos_negativos[i]}\n"
    if meses_positivos[i] == converter_mes(11):
        novembro_positivo += f"{arcanos_positivos[i]}\n"
    if meses_negativos[i] == converter_mes(11):
        novembro_negativo += f"{arcanos_negativos[i]}\n"
    if meses_positivos[i] == converter_mes(12):
        dezembro_positivo += f"{arcanos_positivos[i]}\n"
    if meses_negativos[i] == converter_mes(12):
        dezembro_negativo += f"{arcanos_negativos[i]}\n"


mapa = (f"""


Mapa Numerológico 
------------------

Nome: {nome}
Nascido(a) em: {dia}/{mes}/{ano}
Idade: {ano_atual - ano} anos
-------------------------------------------------------------------------------------

Leitura Principal
------------------

    Personalidade Interna: {arcano_maior(pi)} 
    Personalidade Externa: {arcano_maior(pe)} 
    Personalidade Geral: {arcano_maior(pg)} 
    Personalidade Oculta: {arcano_maior(po)} 
    Desafio: {arcano_maior(df)} 
    Regência de Vida Anterior: {arcano_maior(rva)} 
    Missão de Vida: {arcano_maior(mva)} 
    Força do Desafio: {arcano_maior(fd)} 
    Força da Missão: {arcano_maior(fm)}  
    Abalo: {arcano_maior(ablo)} 
    Desafio Oculto: {arcano_piramide(abs(do))}  
    Liberação do Karma = Entre os {ilka - 2} e {ilka + 2 } anos. 
    
-----------------------------------------------------------------------------------

Ciclos de Vida
---------------

Os ciclos de {nome} mudam a cada {mva} anos.

Segue os ciclos do Consulente:

{resultado_ciclos}


Ciclo Atual: {arcano_maior(arcano_ciclo_atual)}
Idade atual do Consulente: {ano_atual - ano} anos.


-----------------------------------------------------------------------------------

Ano Pessoal
------------

O Ano pessoal de {ano_atual} do(a) {nome} corresponde ao arcano do(a):  {arcano_piramide(l5)}


-----------------------------------------------------------------------------------

Pirâmide do Ano de {ano_atual}:
-------------------------------


----------------------{m15n}
----------------{m13n}----[{a10n}]---{m14n}
-----------{m10n}---[{a8n}]----{m11n}---[{a9n}]---{m12n}
------{m6n}---[{a5n}]---{m7n}----[{a6n}]---{m8n}---[{a7n}]---{m9n}
{m1n}---[{a1n}]---{m2n}---[{a2n}]---{m3n}---[{a3n}]---{m4n}---[{a4n}]---{m5n}    
{l1}---------{l2}--------{l3}---------{l4}----------{l5}
{m1p}---[{a1p}]---{m2p}---[{a2p}]---{m3p}---[{a3p}]--{m4p}---[{a4p}]----{m5p}
-----{m6p}---[{a5p}]--{m7p}----[{a6p}]---{m8p}---[{a7p}]---{m9p}
-----------{m10p}--[{a8p}]---{m11p}---[{a9p}]--{m12p}
----------------{m13p}---[{a10p}]---{m14p}
----------------------{m15p}


Legenda:
"" = meses
[] = arcanos


Arcanos que influenciarão cada mês de {ano_atual}:
--------------------------------------------------


{imprimir_secao("Ocorrerá o Ano Todo", ano_todo_positivo, ano_todo_negativo)}
{imprimir_secao("Janeiro", janeiro_positivo, janeiro_negativo)}
{imprimir_secao("Fevereiro", fevereiro_positivo, fevereiro_negativo)}
{imprimir_secao("Março", marco_positivo, marco_negativo)}
{imprimir_secao("Abril", abril_positivo, abril_negativo)}
{imprimir_secao("Maio", maio_positivo, maio_negativo)}
{imprimir_secao("Junho", junho_positivo, junho_negativo)}
{imprimir_secao("Julho", julho_positivo, julho_negativo)}
{imprimir_secao("Agosto", agosto_positivo, agosto_negativo)}
{imprimir_secao("Setembro", setembro_positivo, setembro_negativo)}
{imprimir_secao("Outubro", outubro_positivo, outubro_negativo)}
{imprimir_secao("Novembro", novembro_positivo, novembro_negativo)}
{imprimir_secao("Dezembro", dezembro_positivo, dezembro_negativo)}

{m3} é o coração do ano, o mês de maior importância no ano.

-----------------------------------------------------------------------------------

Roda das Encarnações:
---------------------
{lista_6}


    Encarnação Atual: {arcano_maior(encarnacao_atual)} 
    Karma: {arcano_maior(karma)} 
    Tendência: {arcano_maior(tendencia)} 
    Subtêndencia: {arcano_maior(subtendencia)} 
    Frequência: {arcano_maior(frequencia)} 
    Subfrequência: {arcano_maior(subfrequencia)} 
    Karma causal: {arcano_maior(karma_causal)} 
    Karma geral: {arcano_maior(karma_geral)} 

------------------------------------------------------------------------------------

Arcano que mais aparece no Mapa:
-------------------------------

{arcano_repetido}


------------------------------------------------------------------------------------

Resumo da Vida:
---------------

Antes dos {ilka} anos: {arcano_maior(verifica_numero(sum(lista_7)))}
Depois dos {ilka} anos: {arcano_maior(verifica_numero((sum(lista_7)) + ilka))}




""")

print(mapa)
