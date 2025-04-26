def notas (*n, sit=False):
    """
    -> função para analisar notas e situações de varios alunos.
    :param n:uma ou mais notas dos alunos (aceita varias)
    :param sit:valor opcional, indicando se deve ou não adicionar a situação
    :return:dicionario com varias informaçoes sobre a situalçao da turma
    """
    r =dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'boa'
        elif r['media'] >= 5:
            r['situação'] = 'razoavel'
        else:
            r['situação'] = 'ruim'
    return r



resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)
