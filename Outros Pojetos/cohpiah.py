import re

def le_assinatura():
    '''A funcao le os valores dos trac,os linguisticos do modelo
    e devolve uma assinatura a ser comparada com os textos.
    '''
    print("Bem-vindo ao detector automatico de COH-PIAH.")
    print("Informe a assinatura tipica de um aluno infectado.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relacao Type-Token:"))
    hlr = float(input("Entre a Razao Hapax Legomana:"))
    sal = float(input("Entre a complexidade media da sentenca:"))
    sac = float(input("Entre o tamanho medio de sentenca:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve
    uma lista contendo cada texto como um elemento.
    '''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas
    dentro do texto.
    '''
    # Garantir que a regex não crie strings vazias no final se o texto terminar com delimitador
    sentencas = re.split(r'[.!?]+', texto)
    return [s.strip() for s in sentencas if s.strip()] # Remove espaços em branco e elementos vazios

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases
    dentro da sentenca.
    '''
    # Similarmente, remove strings vazias e espaços em branco
    frases = re.split(r'[,:;]+', sentenca)
    return [f.strip() for f in frases if f.strip()]

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras
    dentro da frase.
    '''
    # Divide por espaços, quebras de linha e tabulações
    palavras = re.split(r'[ \n\t]+', frase)
    return [p.strip() for p in palavras if p.strip()] # Remove espaços e elementos vazios

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve
    o numero de palavras que aparecem uma unica vez.
    '''
    freq = dict()
    unicas = 0
    for p in lista_palavras:
        p = p.lower() # Considera palavras em minúsculas para contagem de unicas/diferentes
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    for p in freq:
        if freq[p] == 1:
            unicas += 1
    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve
    o numero de palavras diferentes utilizadas.
    '''
    freq = dict()
    for p in lista_palavras:
        p = p.lower() # Considera palavras em minúsculas
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
    return len(freq)

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas e devolve o grau de similaridade entre elas.'''
    s_ab = 0
    for i in range(6):
        s_ab += abs(as_a[i] - as_b[i])
    return s_ab / 6.0

def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e devolve a assinatura do texto.'''
    
    # 1. Obter todas as sentenças, frases e palavras do texto
    todas_as_sentencas = separa_sentencas(texto)
    
    todas_as_frases = []
    for s in todas_as_sentencas:
        todas_as_frases.extend(separa_frases(s))
    
    todas_as_palavras = []
    for f in todas_as_frases:
        todas_as_palavras.extend(separa_palavras(f))
    
    # --- Cálculos dos Traços Linguísticos ---

    # Para evitar ZeroDivisionError, verificar se as listas não estão vazias
    num_total_palavras = len(todas_as_palavras)
    num_total_sentencas = len(todas_as_sentencas)
    num_total_frases = len(todas_as_frases)

    # 1. Tamanho médio de palavra (wal)
    total_caracteres_palavras = sum(len(p) for p in todas_as_palavras)
    wal = total_caracteres_palavras / num_total_palavras if num_total_palavras > 0 else 0.0

    # 2. Relação Type-Token (ttr)
    num_palavras_diferentes = n_palavras_diferentes(todas_as_palavras)
    ttr = num_palavras_diferentes / num_total_palavras if num_total_palavras > 0 else 0.0

    # 3. Razão Hapax Legomana (hlr)
    num_palavras_unicas = n_palavras_unicas(todas_as_palavras)
    hlr = num_palavras_unicas / num_total_palavras if num_total_palavras > 0 else 0.0

    # 4. Tamanho médio de sentença (sal)
    # Considera-se o texto da sentença sem os delimitadores finais
    total_caracteres_sentencas = sum(len(s) for s in todas_as_sentencas)
    sal = total_caracteres_sentencas / num_total_sentencas if num_total_sentencas > 0 else 0.0

    # 5. Complexidade de sentença (sac)
    sac = num_total_frases / num_total_sentencas if num_total_sentencas > 0 else 0.0

    # 6. Tamanho médio de frase (pal)
    # Considera-se o texto da frase sem os delimitadores internos
    total_caracteres_frases = sum(len(f) for f in todas_as_frases)
    pal = total_caracteres_frases / num_total_frases if num_total_frases > 0 else 0.0

    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma assinatura
    (ass_cp) e deve devolver o texto mais similar a ass_cp.'''
    
    similaridades = []
    for texto in textos:
        assinatura_texto = calcula_assinatura(texto)
        similaridade = compara_assinatura(assinatura_texto, ass_cp)
        similaridades.append(similaridade)
    
    # Encontra o índice do texto com a menor similaridade (mais similar)
    idx_texto_infectado = similaridades.index(min(similaridades))
    
    # O exercício pede para retornar o índice, mas como o texto de saída é "O autor do texto X...",
    # O índice + 1 é o número do texto.
    return idx_texto_infectado + 1 # Retorna o número do texto (1-based index)

if __name__ == '__main__':
    assinatura_cohpiah = le_assinatura()
    textos_para_analise = le_textos()

    texto_infectado_numero = avalia_textos(textos_para_analise, assinatura_cohpiah)

    print(f"\nO autor do texto {texto_infectado_numero} está infectado com COH-PIAH")