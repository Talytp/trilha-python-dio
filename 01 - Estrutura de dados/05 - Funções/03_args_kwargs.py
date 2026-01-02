def exibir_poema(data_extenso, titulo, *lista, **dicionario):
    texto = "\n".join(lista) 
    meta_dados = "\n".join([f"{dados.title()}: {valor}" for dados, valor in dicionario.items()])
    mensagem = f"{data_extenso}\n\n{titulo}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)


exibir_poema(
    "Sexta-feira, 02 de janeiro de 2026",
    "Zen of Python",
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",
    autor="Tim Peters",
    ano=1999,
)
#args age como tupla
#kargs é esttutura chave valor, então sabemos que kargs começou quando atribuimos valor as variáveis autor e ano