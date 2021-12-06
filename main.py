#                                                FP2020/2021 @ IST1100731
#                                              Projecto 2 - Jogo do Moinho
#                                                     Edson da Veiga
########################################################################################################################

# TAD posicao
# Rep{coluna,linha} = dict
#################################################
# cria_posicao: str x str -> posicao
# cria_copia_posicao: posicao -> posicao
# obter_pos_c: posicao -> str
# obter_pos_l: posicao -> str
# eh_posicao: universal -> booleano
# posicoes_iguais: posicao x posicao -> booleano
# posicao_para_str: posicao -> str

# Construtor
def cria_posicao(col, lin):
    """Cria uma TAD posicao.

    :param col: str
    :param lin: str
    :return:  dict

    Recebe duas cadeias de carateres correspondentes a coluna col e a linha lin de uma posicão
    e devolve a TAD posicão correspondente.
    """
    if type(col) is str and type(lin) is str and len(col + lin) == 2 and 97 <= ord(col) <= 99 and 49 <= ord(lin) <= 51:
        return {'coluna': col, 'linha': lin}
    raise ValueError("cria_posicao: argumentos invalidos")


def cria_copia_posicao(posicao):
    """Cria uma copia da TAD posicao.

    :param posicao: posicao
    :return: posicao

    Recebe uma posicao e devolve uma copia nova da posicao.
    """
    return cria_posicao(posicao['coluna'], posicao['linha'])


# Seletores
def obter_pos_c(posicao):
    """Devolve coluna.

    :param posicao: posicao
    :return:  str

    Recebe uma TAD posicao e devolve a componente coluna da TAD posicao.
    """
    return posicao['coluna']


def obter_pos_l(posicao):
    """Devolve linha.

    :param posicao: posicao
    :return:  str

    Recebe uma TAD posicao e devolve a componente linha da TAD posicao
    """
    return posicao['linha']


# Reconhecedor
def eh_posicao(arg):
    """Reconhece posicao.

    :param arg: universal
    :return: bool

    Recebe um argumento de qualquer tipo e devolve True se o seu argumento corresponde a uma TAD posicao
    e False caso contrario.
    """
    return True if isinstance(arg, dict) and len(arg) == 2 and 'coluna' in arg and 'linha' in arg and \
                   isinstance(arg['coluna'], str) and isinstance(arg['linha'], str) and \
                   arg['coluna'] in ('a', 'b', 'c') and arg['linha'] in ('1', '2', '3') else False


# Teste
def posicoes_iguais(posicao_1, posicao_2):
    """Compara duas posicoes se sao iguais.

    :param posicao_1: posicao
    :param posicao_2: posicao
    :return: bool

    Recebe duas posicoes e devolve True apenas se posicao_1 e posicao_2 sao posicoes e sao iguais.
    """
    return eh_posicao(posicao_1) and eh_posicao(posicao_2) and obter_pos_c(posicao_1) == obter_pos_c(posicao_2) and \
           obter_pos_l(posicao_1) == obter_pos_l(posicao_2)


# Transformador
def posicao_para_str(posicao):
    """Transforma uma posicao em string.

    :param posicao: posicao
    :return: str

    Recebe uma posicao e devolve a cadeia de caracteres ‘cl’ que representa o seu
    argumento, sendo os valores c e l as componentes coluna e linha da posicao.
    """
    return str(obter_pos_c(posicao) + obter_pos_l(posicao))


# Funcoes de alto nıvel
def obter_posicoes_adjacentes(posicao):
    """Reconhece posicao.

    :param posicao: posicao
    :return: str

    Recebe uma posicao e devolve a cadeia de caracteres ‘cl’ que representa o seu
    argumento, sendo os valores c e l as componentes coluna e linha da posicao.
    """
    coluna = obter_pos_c(posicao)
    linha = obter_pos_l(posicao)
    if coluna == 'b' and linha == '2':
        return (cria_posicao('a', '1'), cria_posicao('b', '1'), cria_posicao('c', '1'),
                cria_posicao('a', '2'), cria_posicao('c', '2'), cria_posicao('a', '3'),
                cria_posicao('b', '3'), cria_posicao('c', '3'))
    elif coluna == 'b' and linha == '1':
        return cria_posicao('a', '1'), cria_posicao('c', '1'), cria_posicao('b', '2')
    elif coluna == 'b' and linha == '3':
        return cria_posicao('b', '2'), cria_posicao('a', '3'), cria_posicao('c', '3')
    elif coluna == 'a' and linha == '1':
        return cria_posicao('b', '1'), cria_posicao('a', '2'), cria_posicao('b', '2')
    elif coluna == 'a' and linha == '2':
        return cria_posicao('a', '1'), cria_posicao('b', '2'), cria_posicao('a', '3')
    elif coluna == 'a' and linha == '3':
        return cria_posicao('a', '2'), cria_posicao('b', '2'), cria_posicao('b', '3')
    elif coluna == 'c' and linha == '1':
        return cria_posicao('b', '1'), cria_posicao('b', '2'), cria_posicao('c', '2')
    elif coluna == 'c' and linha == '2':
        return cria_posicao('c', '1'), cria_posicao('b', '2'), cria_posicao('c', '3')
    elif coluna == 'c' and linha == '3':
        return cria_posicao('b', '2'), cria_posicao('c', '2'), cria_posicao('b', '3')


# Fucao aux
def list_pos():
    """Cria uma lista com string de todas as posicoes.

    :param ()
    :return: list

    Nao recebe nenhum argumento e devolve uma lista com string de todas as posicoes.
    """
    return (posicao_para_str(cria_posicao('a', '1')), posicao_para_str(cria_posicao('b', '1')),
            posicao_para_str(cria_posicao('c', '1')), posicao_para_str(cria_posicao('a', '2')),
            posicao_para_str(cria_posicao('b', '2')), posicao_para_str(cria_posicao('c', '2')),
            posicao_para_str(cria_posicao('a', '3')), posicao_para_str(cria_posicao('b', '3')),
            posicao_para_str(cria_posicao('c', '3')))


# TAD peca
# Rep{peca} = tuple
###########################################
# cria_peca: str -> peca
# cria_copia_peca: peca -> peca
# eh_peca: universal -> booleano
# posicoes_iguais: peca x peca -> booleano
# posicao_para_str: peca -> str

# Construtor
def cria_peca(peca):
    """Cria uma TAD peca.

    :param peca: str
    :return:  peca

    Recebe uma cadeia de carateres correspondente ao identificador de um dos dois jogadores (’X’ ou ’O’)
    ou a uma peca livre (’ ’) e devolve a peca correspondente. Se algum dos argumentos dados forem invalidos,
    a funcao gera um erro.
    """
    if peca in ('X', 'O', ' '):
        return peca,
    raise ValueError("cria_peca: argumento invalido")


def cria_copia_peca(peca):
    """Cria uma copia da TAD peca.

    :param peca: peca
    :return: peca

    Recebe uma peca e devolve uma copia nova da peca.
    """
    return cria_peca(peca[0])


# Reconhecedor
def eh_peca(arg):
    """Reconhece peca.

    :param arg: universal
    :return: bool

    Recebe um argumento de qualquer tipo e devolve True se o seu argumento corresponde a uma TAD peca
    e False caso contrario.
    """
    return True if isinstance(arg, tuple) and len(arg) == 1 and isinstance(arg[0], str) and arg[0] in ('X', 'O', ' ') \
        else False

# Teste
def pecas_iguais(peca_1, peca_2):
    """Compara duas posicoes se sao iguais.

    :param peca_1: peca
    :param peca_2: peca
    :return: bool

    Recebe duas pecas e devolve True apenas se peca_1 e peca_2 sao pecas e sao iguais.
    """
    return True if eh_peca(peca_1) and eh_peca(peca_2) and peca_1[0] == peca_2[0] else False


# Transformador
def peca_para_str(peca):
    """Transforma uma posicao em string.

    :param peca: peca
    :return: str

    Recebe uma peca e devolve a cadeia de caracteres que representa o
    jogador dono da peca, isto e, '[X]', '[O]' ou '[ ]'.
    """
    return str('[' + peca[0] + ']')


# funcoes de alto nıvel
def peca_para_inteiro(peca):
    """Transforma uma peca em inteiro.

    :param peca: peca
    :return: int

    Recebe uma peca e devolve um inteiro valor 1, -1 ou 0, dependendo se a peca e do
    jogador 'X', 'O' ou livre, respetivamente.
    """
    codificador = {peca_para_str(cria_peca('X')): 1, peca_para_str(cria_peca('O')): -1,
                   peca_para_str(cria_peca(' ')): 0}
    return codificador[peca_para_str(peca)]


def quantidade_p_peca(tab):
    """Conta a quantidade de cada peca em um tabuleiro.

    :param tab: tabuleiro
    :return: int x int

    Recebe um tabuleiro e devolve a quantidade de cada peca no tabuleiro.
    """
    indice_1 = 0
    indice_2 = 0
    for pos in tab:
        if peca_para_str(tab[pos]) == peca_para_str(cria_peca('X')):
            indice_1 += 1
        elif peca_para_str(tab[pos]) == peca_para_str(cria_peca('O')):
            indice_2 += 1
    return indice_1, indice_2


# TAD tabuleiro
# Rep = dict
########################################################
# cria_tabuleiro: {} -> tabuleiro
# cria_copia_tabuleiro: tabuleiro -> tabuleiro
# obter_peca: obter_peca x posicao -> peca
# obter_vetor: tabuleiro x str -> tuplo de posocoes
# coloca_peca: tabuleiro x peca x posicao -> tabuleiro
# remove_peca: tabuleiro x posicao -> tabuleiro
# move_peca: tabuleiro x posicao x posicao -> tabuleiro
# eh_tabuleiro: universal -> booleano
# eh_posicao_livre: tabuleiro x posicao -> booleano
# tabuleiros_iguais: tabuleiro x tabuleiro -> booleano
# tabuleiro_para_str: tabuleiro -> str
# tuplo_para_tabuleiro: tuplo -> tabuleiro

# Construtor
def cria_tabuleiro():
    """Cria uma TAD tabuleiro.

    :param ()
    :return:  dict

    Nao recebe nenhum argumento e devolve um tabuleiro do jogo do moinho 3x3 sem posicoes
    ocupadas por pecas de jogador.
    """
    return dict(zip(list(p for p in list_pos()), list(cria_peca(' ') for p in range(0, 9))))


def cria_copia_tabuleiro(tab):
    """Cria uma copia da TAD tabuleiro.

    :param tab: tabuleiro
    :return: tabuleiro

    Recebe um tabuleiro e devolve uma copia nova do tabuleiro.
    """
    return dict(zip(list(p for p in list_pos()),
                    list(cria_copia_peca(tab[pos]) for pos in list_pos())))


# Seletores
def obter_peca(tab, posicao):
    """Seleciona a peca correspondente a posicao no tabuleiro.

    :param tab: tabuleiro
    :param posicao: posicao
    :return: peca

    Recebe um tabuleiro e uma posicao e devolve peca na posicao do tabuleiro. Se a posicao
    nao estiver ocupada, devolve uma peca livre.
    """
    return tab[posicao_para_str(posicao)]


def obter_vetor(tab, arg):
    """Seleciona as pecas de uma coluna ou linha.

    :param tab: tabuleiro
    :param arg: posicao
    :return: tuple

    Recebe um tabuleiro e um argumento ('a', 'b', 'c', '1', '2' e '3' e devolve todas as pecas
    da linha ou coluna especificada pelo seu argumento.
    """
    return (tuple(p for p in (obter_peca(tab, cria_posicao(arg, '1')),
                              obter_peca(tab, cria_posicao(arg, '2')),
                              obter_peca(tab, cria_posicao(arg, '3'))))) \
        if ord(arg) in (97, 98, 99) else (tuple(p for p in (obter_peca(tab, cria_posicao('a', arg)),
                                                            obter_peca(tab, cria_posicao('b', arg)),
                                                            obter_peca(tab, cria_posicao('c', arg)))))


# Modificadores
def coloca_peca(tab, peca, posicao):
    """Coloca a peca numa posicao.

    :param tab: tabuleiro
    :param peca: peca
    :param posicao: posicao
    :return: tabuleiro

    Recebe um tabuleiro, uma peca e uma posicao e modifica destrutivamente o tabuleiro tab colocando a peca na posicao
    e devolve o proprio tabuleiro.
    """
    tab[posicao_para_str(posicao)] = peca
    return tab


def remove_peca(tab, posicao):
    """Remove a peca de uma posicao.

    :param tab: tabuleiro
    :param posicao: posicao
    :return: tabuleiro

    Recebe um tabuleiro, uma peca e uma posicao e modifica destrutivamente o tabuleiro tab removendo a peca na posicao
    e devolve o proprio tabuleiro.
    """
    tab[posicao_para_str(posicao)] = cria_peca(' ')
    return tab


def move_peca(tab, posicao_1, posicao_2):
    """Remove a peca de uma posicao.

    :param tab: tabuleiro
    :param posicao_1: posicao
    :param posicao_2: posicao
    :return: tabuleiro

    Recebe um tabuleiro e duas posicoes e modifica destrutivamente o tabuleiro tab movendo a peca que se encontra na
    posicao_1 para posicao posicao_2, e devolve o proprio tabuleiro.
    """
    if posicao_para_str(posicao_1) == posicao_para_str(posicao_2):
        return tab
    else:
        tab[posicao_para_str(posicao_2)] = tab[posicao_para_str(posicao_1)]
        tab[posicao_para_str(posicao_1)] = cria_peca(' ')
    return tab


# Reconhecedor
def eh_tabuleiro(arg):
    """Reconhece tabuleiro.

    :param arg: universal
    :return: bool

    Recebe um argumento de qualquer tipo e devolve True se o seu argumento
    corresponde a um TAD tabuleiro e False caso contrario.
    """
    if isinstance(arg, dict) and len(arg) == 9 and 'a1' in arg and 'b2' in arg:
        indice_1 = 0
        x = quantidade_p_peca(arg)[0]
        o = quantidade_p_peca(arg)[1]
        if x < 4 and o < 4 and abs(o - x) < 2:
            for jog in (cria_peca('X'), cria_peca('O')):
                if any(all(val == jog for val in obter_vetor(arg, n)) for n in ('a', 'b', 'c')) or \
                        any(all(val == jog for val in obter_vetor(arg, n)) for n in ('1', '2', '3')):
                    indice_1 += 1
            return indice_1 < 2
    return False


def eh_posicao_livre(tab, posicao):
    """Reconhece se e uma posicao livre no tabuleiro.

    :param tab: tabuleiro
    :param posicao: posicao
    :return: bool

    Recebe um tabuleiro e uma posicao e devolve True apenas no caso da posicao no tabuleiro
    corresponder a uma posicao livre.
    """
    return pecas_iguais(obter_peca(tab, posicao), cria_peca(' '))


# Teste
def tabuleiros_iguais(tab_1, tab_2):
    """Compara dois tabuleiros se sao iguais.

    :param tab_1: tabuleiro
    :param tab_2: tabuleiro
    :return: bool

    Recebe dois tabuleiros e devolve True apenas se tab_1 e tab_2 sao pecas e sao iguais.
    """
    lista_pos = (cria_posicao('a', '1'), cria_posicao('b', '1'), cria_posicao('c', '1'), cria_posicao('a', '2'),
                 cria_posicao('b', '2'), cria_posicao('c', '2'), cria_posicao('a', '3'), cria_posicao('b', '3'),
                 cria_posicao('c', '3'))
    if eh_tabuleiro(tab_1) and eh_tabuleiro(tab_2):
        return all(pecas_iguais(obter_peca(tab_1, indice_1), obter_peca(tab_2, indice_1)) for indice_1 in lista_pos)
    return False


# Transformador
def tabuleiro_para_str(tab):
    """Representacao externa do tabuleiro.

    :param tab: tabuleiro
    :return: str

    Recebe um tabuleiro e devolve a cadeia de caracteres que representa o tabuleiro.
    """
    return '   a   b   c\n1 {}-{}-{}\n   | \ | / |\n2 {}-{}-{}\n   | / | \ |\n3 {}-{}-{}'.format(
        peca_para_str(obter_peca(tab, cria_posicao('a', '1'))), peca_para_str(obter_peca(tab, cria_posicao('b', '1'))),
        peca_para_str(obter_peca(tab, cria_posicao('c', '1'))), peca_para_str(obter_peca(tab, cria_posicao('a', '2'))),
        peca_para_str(obter_peca(tab, cria_posicao('b', '2'))), peca_para_str(obter_peca(tab, cria_posicao('c', '2'))),
        peca_para_str(obter_peca(tab, cria_posicao('a', '3'))), peca_para_str(obter_peca(tab, cria_posicao('b', '3'))),
        peca_para_str(obter_peca(tab, cria_posicao('c', '3'))))


def tuplo_para_tabuleiro(tuplo):
    """Transforma um tuplo em tabuleiro.

    :param tuplo: tuple
    :return: tabuleiro

    Recebe um tuplo e devolve o tabuleiro que e representado pelo tuplo com 3 tuplos.
    """
    tab = {posicao_para_str(cria_posicao('a', '1')): tuplo[0][0], posicao_para_str(cria_posicao('b', '1')): tuplo[0][1],
           posicao_para_str(cria_posicao('c', '1')): tuplo[0][2], posicao_para_str(cria_posicao('a', '2')): tuplo[1][0],
           posicao_para_str(cria_posicao('b', '2')): tuplo[1][1], posicao_para_str(cria_posicao('c', '2')): tuplo[1][2],
           posicao_para_str(cria_posicao('a', '3')): tuplo[2][0], posicao_para_str(cria_posicao('b', '3')): tuplo[2][1],
           posicao_para_str(cria_posicao('c', '3')): tuplo[2][2]}
    descodificador = {1: cria_peca('X'), -1: cria_peca('O'), 0: cria_peca(' ')}
    for indice_1 in (list_pos()):
        tab[indice_1] = descodificador[tab[indice_1]]
    return tab


# funcoes de alto nıvel
def obter_ganhador(tab):
    """Devolve o jogador ganhador.

    :param tab: tabuleiro
    :return: peca

    Recebe um tabuleiro e devolve a peca do jogador que venceu a partida, se nao houver vencedor devolve ' '.
    """
    for jog in (cria_peca('X'), cria_peca('O')):
        if any(all(val == jog for val in obter_vetor(tab, n)) for n in ('a', 'b', 'c')) or \
                any(all(val == jog for val in obter_vetor(tab, n)) for n in ('1', '2', '3')):
            return jog
    return cria_peca(' ')


def obter_posicoes_livres(tab):
    """Devolve posicoes livres.

    :param tab: tabuleiro
    :return: tuple

    Recebe um tabuleiro, e devolve o vector ordenado com todas as posicoes  livres do tabuleiro.
    """
    posicoes_livres = []
    for linha in ('1', '2', '3'):
        for coluna in ('a', 'b', 'c'):
            if eh_posicao_livre(tab, cria_posicao(coluna, linha)):
                posicoes_livres.append(cria_posicao(coluna, linha))
    return tuple(posicoes_livres)


def obter_posicoes_jogador(tab, peca):
    """Devolve posicoes ocupadas pela peca.

    :param tab: tabuleiro
    :param peca: peca
    :return: tuple

    Recebe um tabuleiro, e devolve o vector ordenado com todas as posicoes  ocupadas pela peca no tabuleiro.
    """
    return tuple(p for p in (cria_posicao('a', '1'), cria_posicao('b', '1'), cria_posicao('c', '1'),
                             cria_posicao('a', '2'), cria_posicao('b', '2'), cria_posicao('c', '2'),
                             cria_posicao('a', '3'), cria_posicao('b', '3'), cria_posicao('c', '3'))
                 if pecas_iguais(tab[posicao_para_str(p)], peca))


# Fucoes adicionais

def obter_movimento_manual(tab, peca):
    """Leitura da posicao escolhida pelo jogador.

    :param tab: tabuleiro
    :param peca: peca
    :return: tuple

    Esta funcao realiza a leitura de uma posicao introduzida manualmente por um jogador e devolve
    esta posicao escolhida.  Se o argumento dado for invalido, a funcao gera um erro.
    """
    if quantidade_p_peca(tab)[0] + quantidade_p_peca(tab)[1] != 6:
        posicao = (input("Turno do jogador. Escolha uma posicao: "))
        if len(posicao) == 2 and posicao[0] in ('a', 'b', 'c') and posicao[1] in ('1', '2', '3') and \
                eh_posicao_livre(tab, cria_posicao(posicao[0], posicao[1])):
            return cria_posicao(posicao[0], posicao[1]),
        raise ValueError("obter_movimento_manual: escolha invalida")
    else:
        posicao = (input("Turno do jogador. Escolha um movimento: "))
        pos_adj = []
        for pos in obter_posicoes_jogador(tab, peca):
            pos_adj += obter_posicoes_adjacentes(pos)
        pos_adj_livres = tuple(pos for pos in obter_posicoes_livres(tab) if pos in pos_adj)
        if (len(posicao) == 4 and posicao[0] in ('a', 'b', 'c') and posicao[1] in ('1', '2', '3') and
                posicao[2] in ('a', 'b', 'c') and posicao[3] in ('1', '2', '3') and
                pecas_iguais(tab[posicao_para_str(cria_posicao(posicao[0], posicao[1]))], peca) and
                cria_posicao(posicao[2], posicao[3]) in pos_adj_livres) or (len(pos_adj_livres) == 0 and
                (cria_posicao(posicao[0], posicao[1]) == cria_posicao(posicao[2], posicao[3])) and
                pecas_iguais(tab[posicao_para_str(cria_posicao(posicao[0], posicao[1]))], peca)):
            return cria_posicao(posicao[0], posicao[1]), cria_posicao(posicao[2], posicao[3]),
        raise ValueError("obter_movimento_manual: escolha invalida")


def minimax(tab, jogador, profundidade, seq_movimentos=()):
    """Funcao principal do jogo do moinho.

    :param tab: tabuleiro
    :param jogador: peca
    :param profundidade: int
    :param seq_movimentos ()
    :return: int x tuple

    O minimax e um algoritmo recursivo muito utilizado em teoria de jogos que pode
    sumarizar-se como a escolha do melhor movimento para um proprio assumindo que
    o adversario ira a escolher o pior possıvel.
    """
    movimentos = []
    posicoes_jogador = obter_posicoes_jogador(tab, jogador)
    melhor_seq_mov = None
    for pos in posicoes_jogador:
        for pos_adj in obter_posicoes_adjacentes(pos):
            if pos_adj in obter_posicoes_livres(tab):
                movimentos += pos, pos_adj,
    if obter_ganhador(tab) != cria_peca(' ') or profundidade == 0:
        return peca_para_inteiro(obter_ganhador(tab)), seq_movimentos
    if len(movimentos) == 0:
        return 0, (posicoes_jogador[0], posicoes_jogador[0],)
    else:
        descodificador = {1: cria_peca('X'), -1: cria_peca('O'), 0: cria_peca(' ')}
        melhor_res = -peca_para_inteiro(jogador)
        for pos in posicoes_jogador:
            for pos_adj in obter_posicoes_adjacentes(pos):
                if pos_adj in obter_posicoes_livres(tab):
                    novo_res, nova_seq_mov = minimax(move_peca(cria_copia_tabuleiro(tab), pos, pos_adj),
                    descodificador[-peca_para_inteiro(jogador)], profundidade-1,  seq_movimentos + (pos, pos_adj))
                    if melhor_seq_mov is None or (jogador == cria_peca('X') and novo_res > melhor_res) \
                            or (jogador == cria_peca('O') and novo_res < melhor_res):
                        melhor_res = novo_res
                        melhor_seq_mov = nova_seq_mov
        return melhor_res, melhor_seq_mov


def obter_movimento_auto(tab, peca, nivel):
    """Seleciona uma posicao de forma automatica.

    :param tab: tabuleiro
    :param peca: peca
    :param nivel: str
    :return: tuple

    Devolve a posicao escolhida automaticamente de acordo com a estrategia seleccionada. Se algum dos argumentos
    dados forem invalidos, a funcao  gera um erro.
    """
    if quantidade_p_peca(tab)[0] + quantidade_p_peca(tab)[1] != 6:

        def vitoria(tabu, pec):
            for pos in obter_posicoes_livres(tabu):
                if pecas_iguais(obter_ganhador(coloca_peca(tabu, pec, pos)), pec):
                    remove_peca(tabu, pos)
                    return pos
                remove_peca(tabu, pos)
            return ()

        def bloqueio(tabu, pec):  # block rule
            descodificador = {1: cria_peca('X'), -1: cria_peca('O'), 0: cria_peca(' ')}
            return vitoria(tabu, descodificador[-peca_para_inteiro(pec)])

        def centro(tabu, pec):  # center rule
            return cria_posicao('b', '2') if eh_posicao_livre(tabu, cria_posicao('b', '2')) else ()

        def canto_vazio(tabu, pec):  # opposite corner rule
            cantos = (cria_posicao('a', '1'), cria_posicao('c', '1'), cria_posicao('a', '3'), cria_posicao('c', '3'))
            for c in cantos:
                if eh_posicao_livre(tabu, c):
                    return c
            return ()

        def lateral_vazio(tabu, pec):  # side rule
            return cria_posicao('b', '1') if eh_posicao_livre(tabu, cria_posicao('b', '1')) else ()

        for estrategia in (vitoria, bloqueio, centro, canto_vazio, lateral_vazio):
            if len(estrategia(tab, peca)) == 2:
                return estrategia(tab, peca),
    else:

        def facil(tabu, pec):
            pos_ocu = obter_posicoes_jogador(tabu, pec)
            for pos in pos_ocu:
                for pos_adj in obter_posicoes_adjacentes(pos):
                    if pos_adj in obter_posicoes_livres(tabu):
                        return pos, pos_adj,
            return pos_ocu[0], pos_ocu[0],

        def normal(tabu, pec):
            mov = minimax(tabu, pec, 1)[1]
            return mov[0], mov[1],

        def dificil(tabu, pec):
            mov = minimax(tabu, pec, 5)[1]
            return mov[0], mov[1],

        if nivel == "normal":
            return normal(tab, peca)

        if nivel == "facil":
            return facil(tab, peca)

        if nivel == "dificil":
            return dificil(tab, peca)


def eh_fim_jogo(tab):
    """
    Verifica se e fim de jogo.

    :param tab: tabuleiro
    :return: bool


    Recebe um tabuleiro, e verifica se o jogo terminou.
    """
    return obter_ganhador(tab) in (cria_peca('X'), cria_peca('O'))



def moinho(peca, nivel):
    """Funcao principal do jogo do moinho.

    :param peca: str
    :param nivel: str
    :return: vecedor or computador

    Verifica se ha um vecedor, caso houver devolve o vencedor, caso contrario chamada a jogada do adversario.
    """
    if peca in ('[X]', '[O]') and nivel in ('facil', 'normal', 'dificil'):
        tab = cria_tabuleiro()
        peca = cria_peca('X') if peca == '[X]' else cria_peca('O')
        jog_atual = cria_peca('X')

        print('Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade {}.\n'.format(nivel) + tabuleiro_para_str(tab))
        while not eh_fim_jogo(tab):
            if pecas_iguais(peca, jog_atual):
                p = obter_movimento_manual(tab, jog_atual)
            else:
                print("Turno do computador (" + nivel + "):")
                p = obter_movimento_auto(tab, jog_atual, nivel)
            if len(p) == 1:
                tab = coloca_peca(tab, jog_atual, p[0])
            else:
                tab = move_peca(tab, p[0], p[1])
            print(tabuleiro_para_str(tab))
            descodificador = {1: cria_peca('X'), -1: cria_peca('O'), 0: cria_peca(' ')}
            jog_atual = descodificador[-peca_para_inteiro(jog_atual)]
        if obter_ganhador(tab) != cria_peca(' '):
            if obter_ganhador(tab) == cria_peca('X'):
                return '[X]'
            else:
                return '[O]'
    raise ValueError("moinho: argumentos invalidos")

