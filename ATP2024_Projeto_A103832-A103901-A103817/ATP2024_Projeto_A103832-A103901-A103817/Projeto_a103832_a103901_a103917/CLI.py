import json
#--------------- CARREGAR BD ------------------ 
import json

def CarregarBD(fnome):
    file = open(fnome, encoding='utf-8')
    bd = json.load(file)
    for pub in bd:              
        if 'publish_date' not in pub:
            pub['publish_date'] = 'Desconhecido'
        if 'keywords' not in pub:
            pub['keywords'] = 'Desconhecido'
        if 'title' not in pub:
            pub['title'] = 'Desconhecido'
        for autores in pub['authors']:
            if 'affiliation' not in autores:
                autores['affiliation']= 'Desconhecido'
    file.close()
    return bd

#-------------- EXPORTAR BD ------------------ 
def exportar_dados(dados, nome_arquivo):
    nome =nome_arquivo+'.json'
    with open(nome, 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)

#----------------- ADICIONAR FAVORITOS ------------------ 

def carregar_fav(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def adicionar_fav(bd_fav, artigo):
    if  artigo not in bd_fav:
        bd_fav.append(artigo)
    else: 
        return "Artigo já existe nos favoritos"
def guardar_fav(filepath, bd_fav):
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(bd_fav, file, ensure_ascii=False, indent=4)
    return "Favoritos guardados com sucesso!"
def mostrar_favoritos():
        favoritos = carregar_fav('favoritos.json')
        if not favoritos:
            return("Nenhum favorito encontrado.")
        else:
            favoritos_texto = "\n".join(favoritos)
            return("Favoritos Guardados", favoritos_texto)
def eliminar_favoritos(ficheiro):
    with open('favoritos.json', 'w', encoding='utf-8') as file:
        json.dump([], file)  

#----------------- NOVA PUBLICAÇÃO -----------------
def valida_doi(doi):
    for i in range(6):
        if doi[i] != "https:"[i]:
            return False
    return True

def inserirPubli(bd, abs, keyw, aut, doi, pdf, date, tit, url):
    if not valida_doi(doi):
        return ('O DOI deve começar com https:')
    
    nova_pub = {
        "abstract": str(abs),
        "keywords": str(keyw),
        "authors": aut,
        "doi": str(doi),
        "pdf": str(pdf),
        "publish_date": str(date),
        "title": str(tit),
        "url": str(url)
    }
    bd.append(nova_pub)
    return bd

#----------------- ATUALIZAR -----------------
def atualizapublicacoes(basedados):
    altera1 = input("Insira o DOI da publicação que pretende alterar: ").strip().lower()
    for estudo in basedados:
        doi_atual = estudo.get("doi", "").strip().lower()
        if doi_atual == altera1:
            altera2 = input(
                "Insira o nº correspondente ao que pretende alterar:\n"
                " 1-Palavras-chave\n 2-Resumo\n 3-Data de publicação\n 4-Autores\n 5-Afiliações\n 6-Titulo"
            ).strip()
#todas as opções de seleção
            if altera2 == "1":
                keywords = input("Insira as palavras-chave que pretende que representem este artigo:")
                estudo["keywords"] = keywords 

            elif altera2 == "2":
                resumo = input("Insira o que pretende ter como resumo deste artigo:")
                estudo["abstract"] = resumo  

            elif altera2 == "3":
                data = input("Insira a nova data da sua publicação:")
                estudo["publish_date"] = data  
            elif altera2 == "4":
                a3 = input("Qual é o autor que quer alterar?")
                found = False
                for autor in estudo.get("authors", []):  
                    if autor.get("name") == a3:  
                        novoautor = input("Insira o novo autor:")
                        autor["name"] = novoautor  
                        found = True
                if not found:
                    return "Esse autor não está presente neste artigo.", None

            elif altera2 == "5":
                a4 = input("Pretende alterar as afiliações de que autor?")
                found = False
                for autor in estudo.get("authors", []):  
                    if autor.get("name") == a4: 
                        novaafiliacao = input("Insira a nova afiliação do autor escolhido:")
                        autor["affiliation"] = novaafiliacao  
                        found = True
                if not found:
                    return "Esse autor não está presente neste artigo.", None

            else:
                return "Essa opção não existe.", None
            print("Guardando alterações...")
            return "Publicação atualizada com sucesso", basedados
    return "Não existe nenhuma publicação com esse DOI na nossa base de dados.", None

#---------------------------------------------------------- CONSULTAS ------------------------------------------------------------------------
#RETURN DA PUBLICAÇÃO INTEIRA
#-----------------PELO TITULO -----------------
def consultarPubTitle(bd, tit):
    titlower = tit.lower()
    encontrados=[]
    for pub in bd:
        titpublower = pub['title'].lower()
        if titlower in titpublower:  
            encontrados.append(pub)
       
    return encontrados if encontrados else "Nenhuma publicação encontrada."

#----------------- POR AUTOR -----------------
def consultar_autor(bd, nome_autor):
    nomelower = nome_autor.lower()
    encontrados = []  
    for pub in bd:
        for autor in pub['authors']: 
            if autor['name'].lower() == nomelower:
                encontrados.append(pub) 
    if not encontrados:
        return 'Autor nao existe'
    return sorted(encontrados, key=lambda x: x['title']) 

#----------------- POR ANO -----------------
def consultar_ano(bd, ano_input):
    pubs_do_ano = []
    for estudo in bd:
        if estudo['publish_date'] != "Desconhecido":
            ano = estudo['publish_date'].split('-')[0]
            if ano == ano_input:
                pubs_do_ano.append(estudo)
    if not pubs_do_ano:
        return "Nenhum artigo encontrado"
    return pubs_do_ano

#----------------- POR AFILIAÇÃO -----------------
def consultar_afiliacao(bd,afiliacao_input):
    encontrados = []
    minusc = afiliacao_input.lower()

    for estudo in bd:
        if 'authors'in estudo:
            for autor in estudo['authors']:
                if 'affiliation' in autor:
                    if autor['affiliation'].lower() == minusc:
                        encontrados.append(estudo)
    if encontrados:
        return encontrados
    else:
        return "Nenhum artigo encontrado"

#----------------- POR KEYWORD -----------------
def consultar_keyword(bd, keyword):
    titulos = []  
    keywordlower = keyword.lower()
    for pub in bd:
        if 'keywords' in pub:
            if keywordlower in pub['keywords'].lower():
                titulos.append(pub) 
    return titulos if titulos else "Nenhuma publicação encontrada com a palavra-chave fornecida."

#----------------- ELIMINAR -----------------
def eliminarPubli(bd, doi):
    for i, pub in enumerate(bd):
        if pub.get("doi") == doi:
            del bd[i]
            return f"Publicação com DOI '{doi}' eliminada com sucesso."
    return f"Publicação com DOI '{doi}' não encontrada."

#--------------------------------------------------------------------LISTAGEM---------------------------------------------------------------
# RETURN DE TITULOS 
#----------------- AUTORES -----------------
def listAutores(bd): 
    autores_dict = {}
    for pub in bd:
        if 'authors' in pub:
            for autor in pub['authors']:
                if 'name' in autor:
                    nome_autor = autor['name']
                    
                    if 'title' in pub:
                        nome_publicacao = pub['title']
                    else:
                        nome_publicacao = 'Título Desconhecido'
                    
                    if nome_autor not in autores_dict:
                        autores_dict[nome_autor] = []
                    autores_dict[nome_autor].append(nome_publicacao)
    lista_autores = []
    for autor, titl_publicacoes in autores_dict.items():
        lista_autores.append({
            'autor': autor,
            'publicacoes': titl_publicacoes
        })
    return lista_autores

#ORDENAÇÕES----------
# A-Z
def listAutores_alfcrescente(bd):
    lista = listAutores(bd)
    lista_ordenada = sorted(lista, key=lambda x: x['autor'].lower())  
    return lista_ordenada
# Z-A
def listAutores_alfdecrescente(bd):
    lista = listAutores(bd)
    lista_ordenada = sorted(lista, key=lambda x: x['autor'].lower(), reverse=True)  
    return lista_ordenada
# CRESCENTE
def listAutores_pubcrescente(bd):
    lista = listAutores(bd)
    lista_ordenada = sorted(lista, key=lambda x: len(x['publicacoes']))  
    return lista_ordenada
# DECRESCENTE
def listAutores_pubdescrescente(bd):
    lista = listAutores(bd)
    lista_ordenada = sorted(lista, key=lambda x: len(x['publicacoes']), reverse=True)
    return lista_ordenada

#----------------- POR KEYWORD -----------------
def listar_keywords(bd):
    keywords_list = []  
    for pub in bd:
        if 'keywords' in pub:  
            palavras = pub['keywords'].split(',')  
            for palavra in palavras:
                palavra = palavra.strip() 
                if palavra not in keywords_list: 
                    keywords_list.append(palavra)  
    return keywords_list  

#ORDENAÇÕES----------
#CRESCENTE
def keywords_ocorr_crescente(bd):
    lista_keywords = listar_keywords(bd) 
    lista_ordenada = sorted(lista_keywords, key=lambda x: lista_keywords.count(x))
    return lista_ordenada
#DECRESCENTE
def keywords_ocorr_descrescente(bd):
    lista_keywords = listar_keywords(bd)
    lista_ordenada = sorted(lista_keywords, key=lambda x: lista_keywords.count(x), reverse=True)
    return lista_ordenada
#A-Z
def keywords_alf(bd):
    lista_keywords = listar_keywords(bd) 
    lista_ordenada = sorted(lista_keywords, key=lambda x: x.lower()) 
    return lista_ordenada
#Z-A
def keywords_alf_invert(bd):
    lista_keywords = listar_keywords(bd)
    lista_ordenada = sorted(lista_keywords, key=lambda x: x.lower(), reverse=True) 
    return lista_ordenada

#----------------- PUBLICAÇÃO CONSOANTE A KEYWORD -----------------
def listarpubs_keywords(bd, keyword=None):
    keywordslista = [] 
    if keyword:
        keyword = keyword.strip().lower()  
    for pub in bd:
        if 'keywords' in pub:  
            palavras = pub['keywords'].split(',')  
            for palavra in palavras:
                palavra = palavra.strip().lower()  
                if palavra == keyword:  
                    keywordslista.append(pub['title'])  
    return keywordslista

# --------------------------------------------------------- RELATORIO -------------------------------------------------------------------------

#----------------- POR ANO -----------------
def pub_por_ano(bd):
    pub_ano = {}
    for pub in bd:
        if 'publish_date' in pub:
            if pub['publish_date'] != 'Desconhecido':
                ano = pub['publish_date'].split('-')  
                if ano[0] in pub_ano:
                    pub_ano[ano[0]] += 1
                else:
                    pub_ano[ano[0]] = 1
    return pub_ano

#----------------- MES DE UM ANO -----------------

def pub_mes_ano(bd, ano):
    pub_mes = {}
    ano_str = str(ano)
    meses = {
        "01": "Janeiro",
        "02": "Fevereiro",
        "03": "Março",
        "04": "Abril",
        "05": "Maio",
        "06": "Junho",
        "07": "Julho",
        "08": "Agosto",
        "09": "Setembro",
        "10": "Outubro",
        "11": "Novembro",
        "12": "Dezembro"
    }

    for pub in bd:
        if pub['publish_date'] == 'Desconhecido':
            continue  
        data = pub['publish_date'].split('-')
        if data[0] == ano_str:
            mes_num = data[1]  
            mes_nome = meses.get(mes_num)  
            if mes_nome in pub_mes:
                pub_mes[mes_nome] += 1
            else:
                pub_mes[mes_nome] = 1
    ordem_meses = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    pub_mes_ordenado = {mes: pub_mes[mes] for mes in ordem_meses if mes in pub_mes}
    return pub_mes_ordenado

#----------------- TOP20 AUTORES -----------------

def pub_por_autor(bd):
    pub_autor = {}
    for pub in bd:
        for autor in pub['authors']:
            nome = autor['name']
            if nome in pub_autor:
                pub_autor[nome] += 1
            else:
                pub_autor[nome] = 1
    top_autores = sorted(pub_autor.items(), key=lambda x: x[1], reverse=True)[:20]
    return dict(top_autores)

#----------------- AUTOR POR ANO -----------------
def pub_autor_por_ano(bd, autor):
    pub_autor_ano = {}
    for pub in bd:
        ano = pub['publish_date'].split('-')[0]  
        for a in pub['authors']:
            if a['name'].strip().lower() == autor.strip().lower(): 
                if ano in pub_autor_ano:
                    pub_autor_ano[ano] += 1
                else:
                    pub_autor_ano[ano] = 1
    return pub_autor_ano

#-----------------TOP20 PALAVRAS -----------------

def palavras_chave_frequencia(bd):
    palavras_count = {}
    for pub in bd:
        palavras = pub['keywords'].split(',')
        for palavra in palavras:
            if palavra != 'Desconhecido':
                palavra = palavra.strip()
                if palavra in palavras_count:
                    palavras_count[palavra] += 1
                else:
                    palavras_count[palavra] = 1
    top_palavras = sorted(palavras_count.items(), key=lambda x: x[1], reverse=True)[:20]
    return dict(top_palavras)

#----------------- PALAVRA POR ANO -----------------

def palavras_chave_por_ano(bd):
    ano_palavras = {}
    for pub in bd:
        ano = pub['publish_date'].split('-')[0] if pub['publish_date'] != 'Desconhecido' else None
        if ano is None:
            continue  
        palavras = pub['keywords'].split(',')
        for palavra in palavras:
            palavra = palavra.strip() 
            if palavra == 'Desconhecido':
                continue
            if ano not in ano_palavras:
                ano_palavras[ano] = {}
            if palavra in ano_palavras[ano]:
                ano_palavras[ano][palavra] += 1
            else:
                ano_palavras[ano][palavra] = 1
    palavra_mais_frequente = {}
    for ano, palavras in ano_palavras.items():
        max_frequencia = 0
        palavra_frequente = None
        
        for palavra, frequencia in palavras.items():
            if frequencia > max_frequencia:
                max_frequencia = frequencia
                palavra_frequente = palavra
        
        palavra_mais_frequente[ano] = palavra_frequente

    return palavra_mais_frequente

# ---------------------------------------------------------------- GRAFICOS -----------------------------------------------------------------

import matplotlib.pyplot as plt

def grafico_publicacoes_por_ano(bd):
    ano_count = pub_por_ano(bd)
    anos = list(ano_count.keys())
    contagem = list(ano_count.values())

    plt.figure(figsize=(10, 5))
    plt.bar(anos, contagem, color='#af1a21')
    plt.xlabel('Ano')
    plt.ylabel('Número de Publicações')
    plt.title('Distribuição de Publicações por Ano')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def grafico_publicacoes_por_mes_ano(bd, ano):
    mes_count = pub_mes_ano(bd, ano)
    meses = list(mes_count.keys())
    contagem = list(mes_count.values())

    plt.figure(figsize=(10, 5))
    plt.bar(meses, contagem, color='#3f5666')
    plt.xlabel('Mês')
    plt.ylabel('Número de Publicações')
    plt.title(f'Distribuição de Publicações por Mês em {ano}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    print(f"Gerando gráfico para o ano: {ano}")

def grafico_publicacoes_por_autor(bd):
    autor_count = pub_por_autor(bd)
    autores = list(autor_count.keys())
    contagem = list(autor_count.values())

    plt.figure(figsize=(10, 5))
    plt.barh(autores, contagem, color='#00543d')
    plt.xlabel('Número de Publicações')
    plt.title('Top 20 Autores por Número de Publicações')
    plt.tight_layout()
    plt.show()

def grafico_publicacoes_por_autor_ano(bd, autor):
    publicacoes_por_ano = pub_autor_por_ano(bd, autor)
    
    if not publicacoes_por_ano:
        print(f"Nenhuma publicação encontrada para o autor '{autor}'.")
        return

    anos = sorted(publicacoes_por_ano.keys())
    contagem = [publicacoes_por_ano[ano] for ano in anos]

    plt.figure(figsize=(10, 5))
    plt.bar(anos, contagem, color='#46220f')
    plt.xlabel('Ano')
    plt.ylabel('Número de Publicações')
    plt.title(f'Publicações de {autor} por Anos')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def grafico_palavras_chave_frequencia(bd):
    palavras_count = palavras_chave_frequencia(bd)
    palavras = list(palavras_count.keys())
    contagem = list(palavras_count.values())

    plt.figure(figsize=(10, 5))
    plt.barh(palavras, contagem, color='#8c5b65')
    plt.xlabel('Frequência')
    plt.title('Top 20 Palavras-Chave por Frequência')
    plt.tight_layout()
    plt.show()

import numpy as np

def grafico_palavras_por_ano(bd):
    palavra_mais_frequente = palavras_chave_por_ano(bd)
    anos = list(palavra_mais_frequente.keys())
    palavras_frequentes = list(palavra_mais_frequente.values())
    contagens = []
    for ano in anos:
        contagem = sum(1 for pub in bd if pub['publish_date'].startswith(ano) and palavra_mais_frequente[ano] in pub['keywords'])
        contagens.append(contagem)
    plt.figure(figsize=(10, 5))
    bar_width = 0.35
    x = np.arange(len(palavras_frequentes))  # Posições das barras
    bars = plt.bar(x, contagens, width=bar_width, color='#b2443a')
    for bar, palavra, ano in zip(bars, palavras_frequentes, anos):
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, f'{ano})', ha='center', va='bottom')

    plt.ylabel('Quantidade')
    plt.xlabel('Palavras-Chave Mais Frequentes')
    plt.title('Palavras-Chave Mais Frequentes por Ano')
    plt.xticks(x, palavras_frequentes, rotation=45)  # Rótulos do eixo x
    plt.tight_layout()
    plt.show()

#----------------- IMPORTAR BD -----------------
def importar_novos_registos(bd_atual, novo_ficheiro):

    with open(novo_ficheiro, 'r', encoding='utf-8') as f:
        novos_registos = json.load(f)
    dois_existentes = {pub.get('doi') for pub in bd_atual if 'doi' in pub}
    novos_adicionados = 0
    for novo_registo in novos_registos:
        if novo_registo.get('doi') not in dois_existentes:
            bd_atual.append(novo_registo)
            novos_adicionados += 1

    return bd_atual, novos_adicionados

#----------------- GUARDAR BD -----------------
def guardar_publicacoes(bd, fnome):
        f = open(fnome, 'w', encoding='utf-8')
        json.dump(bd, f, ensure_ascii=False, indent=4)
        print(f"Base de dados guardada com sucesso no arquivo '{fnome}'.")
        f.close()

#---------------------------------------------- MENU -----------------------------------------------------------
def main():
    return"""Menu:
        1. Carregar BD;
        2. Consultar Artigo;
        3. Inserir Nova Publicação;
        4. Atualizar Artigo;
        5. Importar Artigo;
        6. Guardar Alterações;
        7. Eliminar Artigo;
        8. Distribuição;
        9. Mostrar Favoritos;
        10. Help;
        0. Sair."""

print(main())
opc = int(input("Qual a opção que deseja realizar?"))

while opc != 0:
        #Carregar Dados
        if opc == 1:
            nome_arquivo = input("Digite o nome do arquivo que pretende carregar (.json): ")
            bd = CarregarBD(nome_arquivo)
            print("Base de dados carregada com sucesso!")
            print(main())
            opc = int(input("Qual a opção que deseja realizar?"))
        #Consultar
        elif opc == 2:
            file = ('favoritos.json')
            criterio = int(input('''Quer Consultar por que critério:
                                 \n 1.Autor \n 2.Ano\n 3.Título\n 4. Afiliação \n 5. Keyword'''))
            if criterio == 1:
                autor = input("Qual Autor quer consultar?")
                res_pub = (consultar_autor(bd, autor))
                print(res_pub)
                favorito = input("Quer adicionar aos Favoritos?\n (Digite Sim ou Não)")
                if favorito.lower() == 'sim':
                    bd_favs = carregar_fav(file)
                    adicionar_fav(bd_favs,res_pub)
                    guardar_fav(file,bd_favs)
                exportar = input("Quer exportar os dados consultados?\n (Digite Sim Não)")
                if exportar.lower == 'sim':
                    dados_exportado = input("Insira o nome do ficheiro onde pretende que os seus dados exportados sejam armazenados:")
                    exportar_dados(res_pub,dados_exportado)
                    if exportar_dados:
                        print("Dados exportados com sucesso!")
                print(main())
                opc = int(input("Qual a opção que deseja realizar?"))   

            elif criterio == 2:
                ano = input("Qual o ano que quer consultar?")
                res_ano = consultar_ano(bd, ano)
                print(res_ano)
                favorito = input("Quer adicionar aos Favoritos?\n (Digite Sim ou Não)")
                if favorito.lower() == 'sim':
                    bd_favs = carregar_fav(file)
                    adicionar_fav(bd_favs,res_ano)
                    guardar_fav(file,bd_favs)
                exportar = input("Quer exportar os dados consultados?\n (Digite Sim Não)")
                if exportar.lower == 'sim':
                    dados_exportados = input("Insira o nome do ficheiro onde pretende que os seus dados exportados sejam armazenados:")
                    exportar_dados(res_ano,dados_exportados)
                    if exportar_dados:
                        print("Dados exportados com sucesso!")
                print(main())
                opc = int(input("Qual a opção que deseja realizar?"))   

            elif criterio == 3:
                titulo = input("Qual o Titulo que quer consultar?")
                res_titulo=consultarPubTitle(bd, titulo)
                print(res_titulo)
                favorito = input("Quer adicionar aos Favoritos?\n (Digite Sim ou Não)")
                if favorito.lower() == 'sim':
                    bd_favs = carregar_fav(file)
                    adicionar_fav(bd_favs,res_titulo)
                    guardar_fav(file,bd_favs)
                exportar = input("Quer exportar os dados consultados?\n (Digite Sim Não)")
                
                if exportar.lower() == 'sim':
                    
                    dados_exportados = input("Insira o nome do ficheiro onde pretende que os seus dados exportados sejam armazenados:")
                    exportar_dados(res_titulo,dados_exportados)
                    if exportar_dados:

                        print("Dados exportados com sucesso!")
                print(main())
                opc = int(input("Qual a opção que deseja realizar?"))    

            elif criterio == 4:
                afiliacao = input("Qual a afiliação a consultar?")
                favorito = input("Quer adicionar aos Favoritos?\n (Digite Sim ou Não)")
                res_afiliacao = consultar_afiliacao(bd, afiliacao)
                print(res_afiliacao)
                if favorito.lower() == 'sim':
                    bd_favs = carregar_fav(file)
                    adicionar_fav(bd_favs,res_afiliacao)
                    guardar_fav(file,bd_favs)
                exportar = input("Quer exportar os dados consultados?\n (Digite Sim Não)")
                if exportar.lower == 'sim':
                    dados_exportados = input("Insira o nome do ficheiro onde pretende que os seus dados exportados sejam armazenados:")
                    exportar_dados(res_afiliacao,dados_exportados)
                    if exportar_dados:
                        print("Dados exportados com sucesso!")
                print(main())
                opc = int(input("Qual a opção que deseja realizar?"))

            elif criterio == 5:
                key = input("Qual a Keyword a consultar?")
                res_keyword = consultar_keyword(bd, key)
                print(res_keyword)
                favorito = input("Quer adicionar aos Favoritos?\n (Digite Sim ou Não)")
                if favorito.lower() == 'sim':
                    bd_favs = carregar_fav(file)
                    adicionar_fav(bd_favs,res_keyword)
                    guardar_fav(file,bd_favs)
                exportar = input("Quer exportar os dados consultados?\n (Digite Sim Não)")
                if exportar.lower == 'sim':
                    dados_exportados = input("Insira o nome do ficheiro onde pretende que os seus dados exportados sejam armazenados:")
                    exportar_dados(res_keyword,dados_exportados)
                    if exportar_dados:
                        print("Dados exportados com sucesso!")
                print(main())
                opc = int(input("Qual a opção que deseja realizar?"))
        #Inserir
        elif opc == 3:
            title = str(input("Digite o título da publicação: "))
            if not title: 
                title = "Desconhecido"
            while True:
                doi = str(input("Digite o DOI da publicação (https:...): "))
                if doi:
                    break
                print(" O DOI é obrigatório.")
            while True:
                date = str(input("Digite a data de publicação (ANO-MES-DIA): "))
                if date:
                    break
                print("A data de publicação é obrigatória. ")
            while True:
                keywords = str(input("Digite as palavras-chave da publicação: "))
                if keywords:
                    break
                print("As Keywords são obrigatórias. ")
            while True:
                abstract = str(input("Digite o resumo da publicação: "))
                if abstract: 
                    break 
                print("O resumo é obrigatório.")
            authors = []  
            while True:
                num_autores = int(input("Quantos autores deseja adicionar? "))
                if num_autores > 0:
                    for i in range(num_autores):
                        name = str(input(f"Digite o nome do autor {i + 1}: "))
                        affiliation = str(input(f"Digite a afiliação do autor {i + 1}: "))
                        authors.append({"name": name, "affiliation": affiliation})
                    break
                print("Deve haver pelo menos um autor.")
            pdf = str(input("Digite o link do pdf da publicação: "))
            if not pdf: 
                pdf = "Desconhecido"
            url = str(input("Digite o link URL da publicação: "))
            if not url: 
                url = "Desconhecido"
            
            inserirPubli(bd, abstract, keywords, authors, doi, pdf, date, title, url)
            print("Publicação inserida com sucesso!")
            print(bd)
            print(main())
            opc = int(input("Qual a opção que deseja realizar?"))            

        #Atualizar
        elif opc == 4: 
            atualizapublicacoes(bd)
            print(bd)
            print(main())      
            opc = int(input("Qual a opção que deseja realizar?"))

        #Importar
        elif opc == 5: 
            novo = input("Insira o nome do novo ficheiro que pretende importar (.json): ")
            importar_novos_registos(bd, novo)
            if importar_novos_registos:
                print('Ficheiro importado com sucesso!')  
            print(main())
            opc = int(input("Qual a opção que deseja realizar?"))      
        
        #Guardar
        elif opc == 6:
            guardar_publicacoes(bd, nome_arquivo)
            if guardar_publicacoes:
                print(f"Base de dados guardada com sucesso no arquivo '{nome_arquivo}'.")
            print(main())
            opc = int(input("Qual a opção que deseja realizar?"))

        #Eliminar
        elif opc == 7:
            doi = input("Digite o DOI da publicação que deseja eliminar: ")
            eliminarPubli(bd,doi)
            print(f"Publicação eliminada com sucesso!")
            print(main())
            opc = int(input("Qual a opção que deseja realizar?"))    

        #Distribuições
        elif opc == 8:
            criterio = int(input('''Quer visualizar qual distribuição:
                                 \n 1.Publicações por ano.\n 2.Publicações por ano de um determinado mês\n 3.Top 20 autores\n 4. Publicações de um autor/anos \n 5.Top 20 Palavras-Chave \n 6.Palavras-chave mais frequente por ano'''))
            if criterio == 1:
                grafico_publicacoes_por_ano(bd)
                print(main())
                opc = int(input("Qual a opção que deseja realizar?"))   

            elif criterio == 2:
                grafico_publicacoes_por_mes_ano(bd, ano)
                print(main())
                opc = int(input("Qual a opção que deseja realizar?"))   
            elif criterio == 3:
                grafico_publicacoes_por_autor(bd)
                print(main())
                opc = int(input("Qual a opção que deseja realizar?"))   
            elif criterio == 4:
                grafico_publicacoes_por_autor_ano
                print(main())
                opc = int(input("Qual a opção que deseja realizar?"))   
            elif criterio == 5:
                grafico_palavras_chave_frequencia(bd)
                print(main())
                opc = int(input("Qual a opção que deseja realizar?"))   
            elif criterio == 6:
                grafico_palavras_por_ano(bd)
                print(main())
                opc = int(input("Qual a opção que deseja realizar?"))   
        #Artigos Favoritos
        elif opc == 9:
            carregar_fav('favoritos.json')
            res_fav = mostrar_favoritos()
            print(res_fav)
            eliminar= input("Quer eliminar os artigos guardados? \n Sim \n Não")
            if eliminar.lower() == "sim":
                eliminar_favoritos(file)
            print("Artigos removidos com Sucesso!")
            print(main())
            opc = int(input("Qual a opção que deseja realizar?"))
            

        elif opc == 10:
            print( """- Carregar BD 🗂: Deve carregar uma base de dados através do botão “CarregarBD” e guardá-la na memória da sua aplicação.
    - Inserir artigo 📩: É necessário preencher os campos seguintes: título, nome do autor, DOI, para que o sistema crie um novo artigo com essa informação.
    - Atualizar artigo 🔄: Os utilizadores podem atualizar as informações dos artigos, nomeadamente a data de publicação, o resumo, keywords, autores e afiliações.
    - Consultar artigo 🔎: Dado um identificador de um artigo, o sistema imprime a informação desse, de forma organizada.
    - Eliminar artigo ❌: Dado o DOI de um artigo, podemos eliminar a publicação correspondente.
    - Listagem 📋: O sistema lista os artigos contidas no sistema. É possível consultar os artigos por filtração, isto é, consultá-los por autores or por keywords.
    - Distribuição 📊:Apresenta gráficos de estatísticas, tais: distribuição de publicações por ano, distribuição de publicações por mês de um determinado ano, número de publicações por autor,
    distribuição de publicações de um autor por anos, distribuição de palavras-chave pela sua frequência (top 20 palavras-chave), Distribuição de palavras-chave mais frequente por ano.
    - Importar📥: O utilizador poderá importar novos registos dum outro ficheiro que tenha a mesma estrutura do ficheiro de suporte.
    - Guardar BD ✅ : O sistema guarda todas as alterações feitas na aplicação no final da sua utilização.
    - Sair  : Encerramento da aplicação.""")
            print(main())
            opc = int(input("Qual a opção que deseja realizar?"))   

        else:
            print("Opção inválida. Tente novamente.")
            print(main())
            opc = int(input("Qual a opção que deseja realizar?")) 

if opc == 0:
    resposta = input ("Pretende guardar as alterações todas feitas?")
    if resposta.lower()=="sim":
        guardar_publicacoes(bd,nome_arquivo)
    print("Thats all folks ! Até à próxima!")

if __name__ == "__main__":
    main()