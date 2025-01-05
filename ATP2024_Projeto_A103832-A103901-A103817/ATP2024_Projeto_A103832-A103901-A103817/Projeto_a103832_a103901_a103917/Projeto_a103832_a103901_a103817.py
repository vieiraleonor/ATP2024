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
def atualiza_data(nome_arquivo, bd):
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        json.dump(bd, f, ensure_ascii=False, indent=4)
    print("Publicação atualizada com sucesso!")

def atualizapublicacoes(nome_arquivo):
    basedados = CarregarBD(nome_arquivo)
    if not basedados:
        return "Erro ao carregar base de dados", None
    altera1 = input("Insira o DOI da publicação que pretende alterar: ").strip().lower()
    for estudo in basedados:
        doi_atual = estudo.get("doi", "").strip().lower()
        if doi_atual == altera1:
            altera2 = input(
                "Insira o nº correspondente ao que pretende alterar:\n"
                " 1-Palavras-chave\n 2-Resumo\n 3-Data de publicação\n 4-Autores\n 5-Afiliações\n"
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
            print("guardadando alterações...")
            atualiza_data(nome_arquivo, basedados)
            return "Publicação atualizada com sucesso", estudo
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
#-----------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------- INTERFACE ---------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
from PIL import Image
import FreeSimpleGUI as sg
import numpy as np

# Dados
BDArtigos = None
tiposfile = [("JSON (*.json)", "*.json")]
sg.theme('LightBrown11')
sg.set_options(text_color='#3c0000')

menu_inicial = [
    [sg.Text("", size=(3, 1)), sg.Button("Carregar BD", size=(20, 2), font=("Times New Roman", 14),button_color=('#3c0000'))],
    [sg.Text("", size=(3, 1)), sg.Button("Inserir Artigo", size=(20, 2), font=("Times New Roman", 14),button_color=('#3c0000'))],
    [sg.Text("", size=(3, 1)), sg.Button("Consultar Artigo", size=(20, 2), font=("Times New Roman", 14),button_color=('#3c0000'))],
    [sg.Text("", size=(3, 1)), sg.Button("Eliminar Artigo", size=(20, 2), font=("Times New Roman", 14),button_color=('#3c0000'))],
    [sg.Text("", size=(3, 1)), sg.Button("Atualizar Artigo", size=(20, 2), font=("Times New Roman", 14),button_color=('#3c0000'))],
    [sg.Text("", size=(3, 1)), sg.Button("Listagem", size=(20, 2), font=("Times New Roman", 14),button_color=('#3c0000'))],
    [sg.Text("", size=(3, 1)), sg.Button("Distribuição", size=(20, 2), font=("Times New Roman", 14),button_color=('#3c0000'))],
    [sg.Text("", size=(3, 1)), sg.Button("Guardar Alterações", size=(20, 2), font=("Times New Roman", 14),button_color=('#3c0000'))],   
]


rodape = [
    [sg.Text("", size=(3, 1)), sg.Button("Artigos Favoritos", size=(15, 2), font=("Times New Roman", 14),button_color=('#3c0000')),sg.Button("Importar BD", size=(15, 2), font=("Times New Roman", 14),button_color=('#3c0000')),
     sg.Text("", expand_x=True), sg.Button("Sair", size=(15, 2), font=("Times New Roman", 14),button_color=('#3c0000')),
     sg.Button("ⓘ Help", size=(15, 2), font=("Times New Roman", 14), key="-HELP-",button_color=('#3c0000'))]
]

cabeçalho = [
    [sg.Text("BANCO DE ARTIGOS CIENTÍFICOS", size=(60, 1), expand_x=True, justification="center",
             font=("Times New Roman", 32, "bold"), text_color="#3c0000")],
    [sg.Text("Bem-vindo!", size=(60, 1), expand_x=True, justification="center",
             font=("Times New Roman", 20), text_color="#3c0000")],
    [sg.Text('_' * 140, justification="center", text_color="#3c0000", pad=(0, 15))]
]

image_path = "C:/Users/maria/OneDrive/Documentos/ATP2024_Projeto_A103832-A103901-A103817/Projeto_a103832_a103901_a103917/descarregar-removebg-preview.png"
output_path = "C:/Users/maria/OneDrive/Documentos/ATP2024_Projeto_A103832-A103901-A103817/Projeto_a103832_a103901_a103917/image_resized.png"

#IMAGEM
with Image.open(image_path) as img:
    width = 400
    aspect_ratio = img.height / img.width
    height = int(width * aspect_ratio)
    img_resized = img.resize((width, height), Image.Resampling.LANCZOS)
    img_resized.save(output_path)
coluna_direita = sg.Column(
    [[sg.Image(filename=output_path)]],
    element_justification="center",
    vertical_alignment="center",
    expand_x=True
)

layout = [
    cabeçalho,
    [sg.Column(menu_inicial, element_justification='left'), coluna_direita],
    [sg.Column([[sg.Text("", size=(1, 1), key="-VE-", justification="center", font=("Times New Roman", 12))]], 
               element_justification="center", expand_x=True)],
    [sg.Text('_' * 140, justification="center", text_color="#341100", pad=(0, 15))],
    rodape  
]

window = sg.Window("Artigos Científicos", layout, size=(1000, 800), resizable=True, finalize=True)


window.set_min_size((800, 600))  
window['-VE-'].expand(expand_x=True)  

stop = False
while not stop:
    event, values = window.read()
    if event in ("Sair", sg.WIN_CLOSED):
            if BDArtigos:
                confirm = sg.popup_yes_no("Existem dados não guardados. Deseja guardá-los antes de sair?", title="Confirmar Saída", text_color="#3c0000")
                if confirm == "Yes":
                    guardar_publicacoes(BDArtigos,ficheiro_global)
                    sg.popup("Dados guardados com sucesso antes de sair!", title="Sucesso", text_color="#3c0000")
            stop = True

    elif event == "Guardar Alterações":
        if BDArtigos is None:
            BDArtigos = []

        if not BDArtigos:
            window["-VE-"].update("Não existem dados para guardar!")
        else:
            guardar_publicacoes(BDArtigos,ficheiro_global )
            window["-VE-"].update("Dados guardados com sucesso ")

    elif event == "Carregar BD":
        if BDArtigos is None:
            BDArtigos = []
        window["-VE-"].update("A carregar a base de dados...")

        formLayout = [
            [
                sg.Text("Base de dados:", font=("Times New Roman", 12), pad=(0, 30), text_color="#3c0000"),
                sg.Input(key="-FICHEIRO-", readonly=True, enable_events=True, text_color ="#3c0000"),
                sg.FileBrowse(file_types=tiposfile, size=(8, 1), font=("Times New Roman", 12),button_color = "#3c0000"),
                sg.Button(key="-CARREGAR-",button_text="Carregar", size=(12, 1), disabled=True, font=("Times New Roman", 12),button_color = "#3c0000")
            ]
        ]

        wform = sg.Window("Carregamento da base de dados", formLayout, size=(650, 100))
        stopform = False
        while not stopform:
            inputEvent, inputValues = wform.read()

            if inputEvent == sg.WIN_CLOSED:
                window["-VE-"].update("")
                stopform = True

            elif inputEvent == "-FICHEIRO-":
                wform["-CARREGAR-"].update(disabled=False)

            elif inputEvent == "-CARREGAR-":
                if inputValues["Browse"]:
                    BDArtigos = CarregarBD(inputValues["-FICHEIRO-"])  # Função de carregar BD
                    ficheiro_global = inputValues["-FICHEIRO-"]
                    print("-FICHEIRO-",ficheiro_global)
                    stopform = True
                    window["-VE-"].update("Base de dados carregada com sucesso!")
                    wform.close()

#------ INSERIR ARTIGO ------ 

    elif event == "Inserir Artigo":
        meses = ["--"] + [x for x in range(1, 13)]
        dias = ["--"] + [x for x in range(1, 32)]
        anos = ["--"] + [x for x in range(1980, 2026)]

        if not BDArtigos:
            window["-VE-"].update("Por favor, carregue uma base de dados!")
        else:
            window["-VE-"].update("A inserir um artigo...")

            formLayout = [
                [sg.Text("Os campos com * são de preenchimento obrigatório", size=(60, 1), font=("Times New Roman", 8), text_color="#3c0000")],
                [sg.Text("Abstract:*", size=(10, 1), font=("Times New Roman", 12), justification="center", text_color="#3c0000"), sg.InputText(key="-ABS-", size=(65, 1), enable_events=True)],
                [sg.Text("Keywords:*", size=(10, 1), font=("Times New Roman", 12), justification="center", text_color="#3c0000"), sg.InputText(key="-KEY-", size=(65, 1), enable_events=True)],
                [sg.Text("Autores:", size=(10, 1), font=("Times New Roman", 12), justification="center", text_color="#3c0000")],
                [
                    sg.Text("Nome do Autor:*", size=(15, 1), font=("Times New Roman", 12), text_color="#3c0000"), 
                    sg.InputText(key="-AUTOR-", size=(30, 1)), 
                    sg.Text("Afiliação:", size=(15, 1), font=("Times New Roman", 12), text_color="#3c0000"), 
                    sg.InputText(key="-AFI-", size=(30, 1)), 
                ],
                [sg.Button("Adicionar Autor", size=(12, 1), key="-ADD_AUTOR-", font=("Times New Roman", 12), button_color="#3c0000")],
                [sg.Listbox(values=[], size=(65, 5), key="-AUTOR_LIST-")],
                [sg.Text("Title:", size=(10, 1), font=("Times New Roman", 12), justification="center", text_color="#3c0000"), sg.InputText(key="-TIT-", size=(65, 1), enable_events=True)],
                [sg.Text("Publish Date:", size=(10, 1), font=("Times New Roman", 12), text_color="#3c0000"), sg.Combo(anos, default_value=anos[0], key="-ANO-"), sg.Combo(meses, default_value=meses[0], key="-MES-"), sg.Combo(dias, default_value=dias[0], key="-DIA-")],
                [sg.Text("PDF:", size=(10, 1), font=("Times New Roman", 12), text_color="#3c0000"), sg.InputText(key="-PDF-", size=(65, 1), enable_events=True)],
                [sg.Text("DOI*:", size=(10, 1), font=("Times New Roman", 12), text_color="#3c0000"), sg.InputText(key="-DOI-", size=(65, 1), enable_events=True), sg.Button("Validar DOI", key="-VALIDAR_DOI-", font=("Times New Roman", 12))],
                [sg.Text("URL:", size=(10, 1), font=("Times New Roman", 12), text_color="#3c0000"), sg.InputText(key="-URL-", size=(65, 1), enable_events=True)],
                [sg.Button("Inserir", size=(12, 1), disabled=True, key="-INS-", font=("Times New Roman", 12), button_color="#3c0000")]
            ]

            wform = sg.Window("Inserção de um artigo", formLayout, size=(750, 600))
            stopform = False
            autores = []
            doi_valido = False  

            def verificar_campos():
                if (inputValues["-ABS-"].strip() and inputValues["-KEY-"].strip() and 
                    doi_valido and autores):
                    wform["-INS-"].update(disabled=False)
                else:
                    wform["-INS-"].update(disabled=True)

            while not stopform:
                inputEvent, inputValues = wform.read()

                if inputEvent == sg.WIN_CLOSED:
                    stopform = True
                    wform.close()
                    window["-VE-"].update("")

                elif inputEvent == "-ADD_AUTOR-":
                    autor = inputValues["-AUTOR-"].strip()
                    afiliacao = inputValues["-AFI-"].strip()
                    if autor:
                        if not afiliacao:
                            afiliacao = "Desconhecido"
                        autores.append({"name": autor, "affiliation": afiliacao})
                        wform["-AUTOR_LIST-"].update(values=[f"{a['name']} - {a['affiliation']}" for a in autores])
                        wform["-AUTOR-"].update("")
                        wform["-AFI-"].update("")
                        verificar_campos()
                    else:
                        sg.popup("Erro: Nome do autor é obrigatório!", text_color="#3c0000")

                elif inputEvent in ["-ABS-", "-KEY-", "-TIT-", "-PDF-", "-URL-"]:
                    verificar_campos()
                    
                elif inputEvent == "-VALIDAR_DOI-":
                    doi = inputValues["-DOI-"].strip()
                    if valida_doi(doi):
                        sg.popup("DOI válido!", title="Validação de DOI", text_color="#3c0000")
                        doi_valido = True  
                    else:
                        sg.popup("Erro: O DOI deve começar com 'https:'.", title="Validação de DOI", text_color="#3c0000")
                        doi_valido = False  
                    verificar_campos()  

                elif inputEvent == "-INS-":
                    ano = inputValues["-ANO-"]
                    mes = inputValues["-MES-"]
                    dia = inputValues["-DIA-"]

                    if ano == "--" or mes == "--" or dia == "--":
                        data_publicacao = "Desconhecido"
                    else:
                        data_publicacao = f"{ano}-{int(mes):02d}-{int(dia):02d}"
                    #caso algum deste nao for preenchido, toma o valor de desconhecido
                    pdf = inputValues["-PDF-"].strip() if inputValues["-PDF-"].strip() else "Desconhecido"
                    url = inputValues["-URL-"].strip() if inputValues["-URL-"].strip() else "Desconhecido"
                    title = inputValues["-TIT-"].strip() if inputValues["-TIT-"].strip() else "Desconhecido"
                    
                    BDArtigos = inserirPubli(
                        BDArtigos,
                        inputValues["-ABS-"].strip(),
                        inputValues["-KEY-"].strip(),
                        autores,
                        inputValues["-DOI-"].strip(),
                        pdf,
                        data_publicacao,
                        title,
                        url
                    )
                    sg.popup("Artigo inserido com sucesso!", text_color="#3c0000")
                    stopform = True
                    wform.close()

            window["-VE-"].update("Artigo inserido com sucesso!")

#------ ELIMINAR ARTIGO ------

    elif event == "Eliminar Artigo":
         if not BDArtigos:
            window["-VE-"].update("Por favor, carregue uma base de dados!")
         else:
            window["-VE-"].update("A eliminar uma publicação...")

            formLayout = [
                [sg.Text("O campo com * é de preenchimento obrigatório", size=(60, 1), font=("Times New Roman", 8))],
                [sg.Text("DOI:*", size=(10, 1), font=("Times New Roman", 12), justification="center"), sg.InputText(key="-DOI-", size=(65, 1), enable_events=True)],
                [sg.Button("Eliminar", size=(12, 1), key="-DEL-", font=("Times New Roman", 12), button_color=("#3c0000")),
                 sg.Button("Cancelar", size=(12, 1), key="-CANCELAR-", font=("Times New Roman", 12), button_color=("#3c0000"))]
            ]

            wform = sg.Window("Eliminação de um artigo", formLayout, size=(750, 300))
            stopform = False

            while not stopform:
                inputEvent, inputValues = wform.read()

                if inputEvent == sg.WIN_CLOSED or inputEvent == "-CANCELAR-":
                    stopform = True
                    wform.close()
                    window["-VE-"].update("")

                elif inputEvent == "-DEL-":
                    doi = inputValues["-DOI-"].strip()
                    if not doi:
                        sg.popup("Erro: O campo DOI é obrigatório!", title="Erro", text_color="#3c0000")
                        continue

                    for i, pub in enumerate(BDArtigos):
                        if pub.get("doi") == doi:
                            del BDArtigos[i]
                            sg.popup(f"Publicação com DOI '{doi}' eliminada com sucesso!", title="Sucesso", text_color="#3c0000")
                            stopform = True
                            break
                    else:
                        sg.popup(f"Publicação com DOI '{doi}' não encontrada!", title="Erro", text_color="#3c0000")

            wform.close()
            window["-VE-"].update("Operação concluída!")

#------ CONSULTAR ARTIGO ------

    elif event == "Consultar Artigo":
        anos = [x for x in range (2023, 2041)]

        if not BDArtigos:
            window["-VE-"].update("Por favor, carregue uma base de dados!")
        else:
            window["-VE-"].update("A consultar tarefa...")
            resultados = []
            formLayout = [
                        [sg.Text("Selecione o parâmetro pelo qual pretende consultar o Artigo:", pad=((0, 0), (5, 10)), font=("Times New Roman", 12))],
                        [sg.Radio("Autor", "OPCAO", font=("Times New Roman", 12), default=False, enable_events=True, key="-OPC1-"),
                        sg.Radio("Título", "OPCAO", font=("Times New Roman", 12), default=False, enable_events=True, key="-OPC2-"),
                        sg.Radio("Ano", "OPCAO", font=("Times New Roman", 12), default=False, enable_events=True, key="-OPC3-"),
                        sg.Radio("Keyword", "OPCAO", font=("Times New Roman", 12), default=False, enable_events=True, key="-OPC4-"),
                        sg.Radio("Afiliação do Autor", "OPCAO", font=("Times New Roman", 12), default=False, enable_events=True, key="-OPC5-"),
                        sg.Button("Consultar", size=(10, 1), font=("Times New Roman", 12), pad=((10, 0), (5, 10)), button_color="#3c0000")],
                        [sg.InputText(key="-AUT-", visible=False, expand_x=True),
                        sg.InputText(key="-TIT-", visible=False, expand_x=True),
                        sg.InputText(key="-ANO-", visible=False, expand_x=True),
                        sg.InputText(key="-KEY-", visible=False, expand_x=True),
                        sg.InputText(key="-AFI-", visible=False, expand_x=True)],
                        [sg.Multiline("", size=(100, 10), key="-REPORT-", disabled=True)],
                        [sg.Text("Caso pretenda exportar estes dados, escreva o nome que pretende dar ao arquivo:", pad=((0, 0), (5, 10)), font=("Times New Roman", 12))],
                        [sg.InputText(key="-FNAME-", visible=True, expand_x=True)],
                        [sg.Button("Exportar Artigos", size=(15, 1), disabled=True, key='-EXP-', font=("Times New Roman", 12), button_color=('#3c0000')),
                        sg.Button("Adicionar aos Favoritos", size=(17, 1), disabled=True, key='-FAV-', font=("Times New Roman", 12), pad=(10, 0), button_color=('#3c0000'))]
                    ]

            wform = sg.Window("Consulta do Artigo", formLayout, size=(800,400))
            stopForm = False
            while not stopForm:
                resultados=[]
                inputEvent, inputValues = wform.read()
                if inputEvent == sg.WIN_CLOSED:
                    stopForm=True
                else:
                    if inputEvent=='-OPC1-':
                        wform["-AUT-"].update(visible=True)
                        wform["-KEY-"].update(visible=False)
                        wform["-TIT-"].update(visible=False)
                        wform["-ANO-"].update(visible=False)
                        wform["-AFI-"].update(visible=False)                      

                    if inputEvent=='-OPC2-':
                        wform["-AUT-"].update(visible=False)
                        wform["-KEY-"].update(visible=False)
                        wform["-TIT-"].update(visible=True)
                        wform["-ANO-"].update(visible=False)
                        wform["-AFI-"].update(visible=False)  

                    if inputEvent=='-OPC3-':
                        wform["-AUT-"].update(visible=False)
                        wform["-KEY-"].update(visible=False)
                        wform["-TIT-"].update(visible=False)
                        wform["-ANO-"].update(visible=True)
                        wform["-AFI-"].update(visible=False)
                        

                    if inputEvent=='-OPC4-':
                        wform["-AUT-"].update(visible=False)
                        wform["-KEY-"].update(visible=True)
                        wform["-TIT-"].update(visible=False)
                        wform["-ANO-"].update(visible=False)
                        wform["-AFI-"].update(visible=False)  

                    if inputEvent=='-OPC5-':
                        wform["-AUT-"].update(visible=False)
                        wform["-KEY-"].update(visible=False)
                        wform["-TIT-"].update(visible=False)
                        wform["-ANO-"].update(visible=False)
                        wform["-AFI-"].update(visible=True)  

                    if inputEvent== "Consultar":
                        if inputValues['-OPC1-']:
                            res = consultar_autor(BDArtigos,inputValues["-AUT-"])
                            wform["-REPORT-"].update(res)
                            wform["-EXP-"].update(disabled=False)
                            wform["-FAV-"].update(disabled=False)


                        elif inputValues['-OPC2-']:
                            res = consultarPubTitle(BDArtigos, inputValues["-TIT-"])
                            wform["-REPORT-"].update(res)
                            wform["-EXP-"].update(disabled=False)
                            wform["-FAV-"].update(disabled=False)

                        elif inputValues['-OPC3-']:
                            res = consultar_ano(BDArtigos, inputValues["-ANO-"])
                            wform["-REPORT-"].update(res)
                            wform["-EXP-"].update(disabled=False)
                            wform["-FAV-"].update(disabled=False)

                        elif inputValues['-OPC4-']:
                            res = consultar_keyword(BDArtigos, inputValues["-KEY-"])
                            wform["-REPORT-"].update(res)
                            wform["-EXP-"].update(disabled=False)
                            wform["-FAV-"].update(disabled=False)

                        elif inputValues['-OPC5-']:
                            res = consultar_afiliacao(BDArtigos, inputValues["-AFI-"])
                            wform["-REPORT-"].update(res)
                            wform["-EXP-"].update(disabled=False)
                            wform["-FAV-"].update(disabled=False)
                        
#------ EXPORTAR ------
                    elif inputEvent == "-EXP-":  
                        file_name = inputValues["-FNAME-"]  
                        if file_name:
                            exportar_dados(res,file_name)
#------ FAVORITOS ------
                    elif inputEvent == "-FAV-":
                        bd_fav = carregar_fav('favoritos.json')
                        adicionar_fav(bd_fav, res)
                        print(res)
                        guardar_fav('favoritos.json', bd_fav)

                window["-VE-"].update("Consulta realizada com sucesso!")
            window["-VE-"].update("")

#------ ARTIGOS FAVORITOS ------
    elif event == "Artigos Favoritos":
        bd_fav = carregar_fav('favoritos.json')
        
        if not bd_fav:
            window["-VE-"].update("Sem artigos Favoritos")
        else:
            window["-VE-"].update("A abrir Favoritos...")
            bd_fav_str = [str(artigo) for artigo in bd_fav]

            layout_favoritos = [
                [sg.Text("Artigos Favoritos:", font=("Times New Roman", 14), text_color="#3c0000")],
                [sg.Multiline(default_text="\n".join(bd_fav_str), size=(80, 20), disabled=True, text_color="#3c0000")],
                [sg.Button("Fechar", button_color = "#3c0000"), sg.Button("Remover Favoritos",button_color = "#3c0000" )]
            ]
            window_favoritos = sg.Window("Gerenciador de Favoritos", layout_favoritos)

            while True:
                event_favoritos, values_favoritos = window_favoritos.read()
                if event_favoritos == sg.WIN_CLOSED or event_favoritos == "Fechar":
                    break
                elif event_favoritos == "Remover Favoritos":
                    eliminar_favoritos("favoritos.json")
                    sg.popup("Todos os favoritos foram removidos com sucesso!", title="Sucesso")
                    break  

            window_favoritos.close()
            
 #------ LISTAR ------

    elif event == "Listagem":
        if not BDArtigos:
            window["-VE-"].update("Por favor, carregue uma base de dados!")
        else:
            window["-VE-"].update("A listar tarefas...")
            resultados = []

            estado_opc7 = False
            estado_opc8 = False
            estado_opc9 = False
            estado_opc10 = False

            formLayout = [
                [sg.Text("Selecione o parâmetro pelo qual pretende listar os seus Artigos:", pad=((0, 0), (5, 10)), font=("Times New Roman", 12))],
                [sg.Radio("Autores", "OPCAO", font=("Times New Roman", 12), default=True, enable_events=True, key="-OPC1-"),
                sg.Radio("Keywords", "OPCAO", font=("Times New Roman", 12), default=False, enable_events=True, key="-OPC2-"),
                sg.Button("Listar", size=(10, 1), font=("Times New Roman", 12), pad=((10, 0), (5, 10)),button_color=('#3c0000'))],
                [sg.Text("Ordenação:")],
                [sg.Radio("A-Z", "GRUPO_ALFABETICA", font=("Times New Roman", 12), default=False, enable_events=True, key="-OPC7-"),
                sg.Radio("Z-A", "GRUPO_ALFABETICA", font=("Times New Roman", 12), default=False, enable_events=True, key="-OPC8-")],
                [sg.Radio("Crescente", "GRUPO_QUANTIDADE", font=("Times New Roman", 12), default=False, enable_events=True, key="-OPC9-"),
                sg.Radio("Decrescente", "GRUPO_QUANTIDADE", font=("Times New Roman", 12), default=False, enable_events=True, key="-OPC10-")],
                [sg.Listbox(values=resultados, size=(100, 10), pad=((0, 0), (15, 10)), horizontal_scroll=True, key="-RES-", enable_events=True)]
            ]

            wform = sg.Window("Listagem", formLayout, size=(800, 300))
            stopForm = False

            while not stopForm:
                inputEvent, inputValues = wform.read()

                if inputEvent == sg.WIN_CLOSED:
                    stopForm = True

                elif inputEvent == "-OPC7-":  # A-Z
                    estado_opc7 = not estado_opc7
                    wform["-OPC7-"].update(value=estado_opc7)
                    if estado_opc7:
                        estado_opc8 = False
                        wform["-OPC8-"].update(value=False)

                elif inputEvent == "-OPC8-":  # Z-A
                    estado_opc8 = not estado_opc8
                    wform["-OPC8-"].update(value=estado_opc8)
                    if estado_opc8:
                        estado_opc7 = False
                        wform["-OPC7-"].update(value=False)

                elif inputEvent == "-OPC9-":  # Crescente
                    estado_opc9 = not estado_opc9
                    wform["-OPC9-"].update(value=estado_opc9)
                    if estado_opc9:
                        estado_opc10 = False
                        wform["-OPC10-"].update(value=False)

                elif inputEvent == "-OPC10-":  # Decrescente
                    estado_opc10 = not estado_opc10
                    wform["-OPC10-"].update(value=estado_opc10)
                    if estado_opc10:
                        estado_opc9 = False
                        wform["-OPC9-"].update(value=False)

                elif inputEvent == "Listar":
                    if inputValues["-OPC1-"]:
                        res = []
                        if estado_opc7:  
                            res = listAutores_alfcrescente(BDArtigos)
                        elif estado_opc8:  
                            res = listAutores_alfdecrescente(BDArtigos)

                        if estado_opc9:  
                            res = listAutores_pubcrescente(BDArtigos)
                        elif estado_opc10:  
                            res = listAutores_pubdescrescente(BDArtigos)

                        resultados = res
                        wform["-RES-"].update(values=resultados)
                    
                    elif inputValues["-OPC2-"]:
                        res = []
                        if estado_opc7:  
                            res = keywords_alf(BDArtigos)
                        elif estado_opc8:  # Se Z-A estiver selecionado
                            res = keywords_alf_invert(BDArtigos)

                        if estado_opc9:  # Se Crescente estiver selecionado
                            res = keywords_ocorr_crescente(BDArtigos)
                        elif estado_opc10:  # Se Decrescente estiver selecionado
                            res = keywords_ocorr_descrescente(BDArtigos)

                        resultados = res
                        wform["-RES-"].update(values=resultados)

                elif inputEvent == "-RES-":
                    if inputValues["-RES-"]:
                        keyword_selecionada = inputValues["-RES-"][0]
                        publicacoes_associadas = listarpubs_keywords(BDArtigos, keyword_selecionada)
                        if publicacoes_associadas:
                            wform["-RES-"].update(values=publicacoes_associadas)
                        else:
                            wform["-RES-"].update(values=[])
            wform.close()

#------ ATUALIZAR ------

    elif event == "Atualizar Artigo":
        if not BDArtigos:
            window["-VE-"].update("Por favor, carregue uma base de dados!")
        else:
            window["-VE-"].update("A atualizar um artigo...")

            meses = ["--"] + [f"{x:02d}" for x in range(1, 13)]
            dias = ["--"] + [f"{x:02d}" for x in range(1, 32)]
            anos = ["--"] + [x for x in range(1980, 2026)]

            formLayout = [
                [sg.Text("Insira o DOI do artigo a atualizar:", font=("Times New Roman", 12), justification="center")],
                [sg.InputText(key="-DOI-", size=(65, 1), enable_events=True)],
                [sg.Button("Buscar Artigo", size=(15, 1), key="-BUSCAR-", font=("Times New Roman", 12),button_color=('#3c0000'))],
                [sg.Text("", key="-STATUS-", size=(60, 1), text_color="red", font=("Times New Roman", 12))]
            ]

            buscarWindow = sg.Window("Atualizar Artigo", formLayout, size=(750, 200))
            stopBuscar = False
            artigo = None

            while not stopBuscar:
                buscarEvent, buscarValues = buscarWindow.read()

                if buscarEvent == sg.WIN_CLOSED:
                    stopBuscar = True
                    buscarWindow.close()

                elif buscarEvent == "-BUSCAR-":
                    doi = buscarValues["-DOI-"].strip()
                    artigo = next((pub for pub in BDArtigos if pub.get("doi") == doi), None)
                    if not artigo:
                        buscarWindow["-STATUS-"].update(f"Artigo com DOI {doi} não encontrado!")
                    else:
                        buscarWindow.close()
                        stopBuscar = True

            if artigo:
                autores = [{"name": a["name"], "affiliation": a.get("affiliation", "Desconhecido")} for a in artigo["authors"]]
                autores_list = [f"{a['name']} - {a['affiliation']}" for a in autores]

                formLayout = [
                    [sg.Text("Atualizar campos do artigo", size=(30, 1), font=("Times New Roman", 16), justification="center")],
                    [sg.Text("Abstract:", size=(10, 1), font=("Times New Roman", 12), justification="center"), sg.InputText(artigo.get("abstract", ""), key="-RESUMO-", size=(65, 1), enable_events=True)],
                    [sg.Text("Palavras-chave:", size=(10, 1), font=("Times New Roman", 12), justification="center"), sg.InputText(artigo.get("keywords", ""), key="-KEYWORDS-", size=(65, 1), enable_events=True)],
                    [sg.Text("Autores:", size=(10, 1), font=("Times New Roman", 12), justification="center")],
                    [
                        sg.Text("Nome do Autor:", size=(15, 1), font=("Times New Roman", 12)), 
                        sg.InputText(key="-AUTOR-", size=(30, 1)), 
                        sg.Text("Afiliação:", size=(15, 1), font=("Times New Roman", 12)), 
                        sg.InputText(key="-AFI-", size=(30, 1)), 
                    ],
                    [sg.Button("Adicionar Autor", size=(12, 1), key="-ADD_AUTOR-", font=("Times New Roman", 12),button_color=('#3c0000'))],
                    [sg.Listbox(values=autores_list, size=(65, 5), key="-AUTOR_LIST-",enable_events=True)],
                    [sg.Button("Remover Autor", size=(12, 1), key="-REMOVER_AUTOR-", font=("Times New Roman", 12), button_color="#3c0000", disabled=True)],
                    [sg.Text("Data de Publicação:", size=(15, 1), font=("Times New Roman", 12)), sg.Combo(anos, default_value=anos[0], key="-ANO-"), sg.Combo(meses, default_value=meses[0], key="-MES-"), sg.Combo(dias, default_value=dias[0], key="-DIA-")],
                    [sg.Button("Atualizar", size=(12, 1), disabled=False, key="-ATUALIZAR-", font=("Times New Roman", 12),button_color=('#3c0000'))],
                ]

                wform = sg.Window("Atualização de um artigo", formLayout, size=(750, 600))
                stopForm = False

                def atualizar_artigo():
                    ano = wform["-ANO-"].get()
                    mes = wform["-MES-"].get()
                    dia = wform["-DIA-"].get()

                    if ano == "--" or mes == "--" or dia == "--":
                        artigo["publish_date"] = "Desconhecido"
                    else:
                        artigo["publish_date"] = f"{ano}-{mes}-{dia}"

                    artigo["abstract"] = wform["-RESUMO-"].get().strip()
                    artigo["keywords"] = wform["-KEYWORDS-"].get().strip()
                    artigo["authors"] = [{"name": a["name"], "affiliation": a["affiliation"]} for a in autores]

                while not stopForm:
                    formEvent, formValues = wform.read()

                    if formEvent == sg.WIN_CLOSED:
                        stopForm = True
                        wform.close()

                    elif formEvent == "-ADD_AUTOR-":
                        nome = formValues["-AUTOR-"].strip()
                        afiliacao = formValues["-AFI-"].strip() or "Desconhecido"
                        if nome:
                            autor_existente = next((a for a in autores if a["name"].lower() == nome.lower()), None)
                            if autor_existente:
                                autor_existente["affiliation"] = afiliacao
                                sg.popup(f"Afiliação do autor '{nome}' atualizada para '{afiliacao}'.")
                            else:
                                autores.append({"name": nome, "affiliation": afiliacao})
                                sg.popup(f"Autor '{nome}' adicionado com sucesso!")
                            
                            wform["-AUTOR_LIST-"].update(values=[f"{a['name']} - {a['affiliation']}" for a in autores])
                            wform["-AUTOR-"].update("")
                            wform["-AFI-"].update("")
                        else:
                            sg.popup_error("O nome do autor é obrigatório!")
                        
                    elif formEvent == "-AUTOR_LIST-":
                        if wform["-AUTOR_LIST-"].get():
                            wform["-REMOVER_AUTOR-"].update(disabled=False)
                        else:
                            wform["-REMOVER_AUTOR-"].update(disabled=True)

                    elif formEvent == "-REMOVER_AUTOR-":
                        autor_selecionado = wform["-AUTOR_LIST-"].get()
                        if autor_selecionado:
                            autores = [a for a in autores if f"{a['name']} - {a['affiliation']}" != autor_selecionado[0]]
                            wform["-AUTOR_LIST-"].update(values=[f"{a['name']} - {a['affiliation']}" for a in autores])
                            wform["-REMOVER_AUTOR-"].update(disabled=True)
                            sg.popup("Autor removido com sucesso!", text_color="#3c0000")
                        else:
                            sg.popup("Erro: Nenhum autor selecionado!", text_color="#3c0000")

                    elif formEvent == "-ATUALIZAR-":
                                            atualizar_artigo()
                                            sg.popup("Artigo atualizado com sucesso!")
                                            stopForm = True
                                            wform.close()
        window["-VE-"].update("Artigo atualizado com sucesso!")


#------ DISTRIBUIÇÃO ------

    elif event == "Distribuição":
        if not BDArtigos:
            window["-VE-"].update("Por favor, carregue uma base de dados!")
        else:
            window["-VE-"].update("A produzir dados estatísticos...")
            formLayout = [
                [sg.Button("Publicações por ano", size=(20, 2), font=("Baskerville", 12), button_color=('#3c0000'))],  
                [sg.Button("Publicações por mês de um determinado ano", size=(22, 2), font=("Baskerville", 12), button_color=('#3c0000'))], 
                [sg.Button("Top 20 autores", size=(20, 2), font=("Baskerville", 12), button_color=('#3c0000'))],
                [sg.Button("Pub do Autor por Anos", size=(20, 2), font=("Baskerville", 12), button_color=('#3c0000'))],  
                [sg.Button("Top 20 palavras-chave", size=(20, 2), font=("Baskerville", 12), button_color=('#3c0000'))], 
                [sg.Button("Palavras-chave mais frequente por ano", size=(50, 3), font=("Baskerville", 12), button_color=('#3c0000'))] 
            ]

            wform = sg.Window("Análise de publicações", formLayout, size=(400, 400), resizable=False)  # Definido como False
            stopForm = False
            while not stopForm:
                inputEvent, inputValues = wform.read()

                if inputEvent == sg.WIN_CLOSED:
                    stopForm = True
                    wform.close() 
                    window["-VE-"].update("")

                else:
                    if inputEvent == "Publicações por ano":
                        grafico_publicacoes_por_ano(BDArtigos)
                    elif inputEvent == "Publicações por mês de um determinado ano":
                        layout_popup = [
                            [sg.Text("Insira o ano desejado:")],
                            [sg.InputText(key="-ANO-")],
                            [sg.Button("OK",button_color=('#3c0000')), sg.Button("Cancelar",button_color=('#3c0000'))]
                        ]
                        popup = sg.Window("Escolher Ano", layout_popup, modal=True)

                        while True:
                            popup_event, popup_values = popup.read()
                            if popup_event in (sg.WIN_CLOSED, "Cancelar"):
                                break
                            if popup_event == "OK":
                                ano = popup_values["-ANO-"]
                                if ano.isdigit(): 
                                    grafico_publicacoes_por_mes_ano(BDArtigos, ano)
                                    break
                                else:
                                    sg.popup("Por favor, insira um ano válido.")
                        popup.close()
                    elif inputEvent == "Top 20 autores":
                        grafico_publicacoes_por_autor(BDArtigos)
                    elif inputEvent == "Pub do Autor por Anos":
                        layout_popup = [
                            [sg.Text("Insira o nome do autor:")],
                            [sg.InputText(key="-AUTOR-")],
                            [sg.Button("OK", button_color=('#3c0000')), sg.Button("Cancelar", button_color=('#3c0000'))]
                        ]
                        popup = sg.Window("Escolher Autor", layout_popup, modal=True)
                        
                        while True:
                            popup_event, popup_values = popup.read()
                            if popup_event in (sg.WIN_CLOSED, "Cancelar"):
                                break
                            if popup_event == "OK":
                                autor = popup_values["-AUTOR-"].strip()
                                if autor: 
                                    grafico_publicacoes_por_autor_ano(BDArtigos, autor)  
                                    break
                                else:
                                    sg.popup("Por favor, insira um nome de autor válido.")
                        popup.close()
                    elif inputEvent == "Top 20 palavras-chave":
                        grafico_palavras_chave_frequencia(BDArtigos)
                    elif inputEvent == "Palavras-chave mais frequente por ano":
                        grafico_palavras_por_ano(BDArtigos)

#------ IMPORTAR ------

    elif event == "Importar BD":
        if BDArtigos is None:
            BDArtigos = []
            window["-VE-"].update("Nenhuma base de dados carregada. Inicializando uma nova base.")
        
        caminho_ficheiro = sg.popup_get_file(
            "Selecione o ficheiro para importar registos",
            file_types=[("JSON Files", "*.json"), ("Todos os Ficheiros", "*.*")]
        )
        
        if caminho_ficheiro:
            BDArtigos, novos_adicionados = importar_novos_registos(BDArtigos, caminho_ficheiro)
            
            if novos_adicionados > 0:
                window["-VE-"].update(f"{novos_adicionados} novos registos adicionados com sucesso!")
            else:
                window["-VE-"].update("Nenhum novo registo foi adicionado (possíveis duplicados).")
        else:
            window["-VE-"].update("Nenhum ficheiro foi selecionado.")


#------ HELP------
    
    elif event == "-HELP-":

        window["-VE-"].update("ⓘ Help...")

        help_text = """- Carregar BD 🗂: Deve carregar uma base de dados através do botão “CarregarBD” e guardá-la na memória da sua aplicação.
    - Inserir artigo 📩: É necessário preencher os campos seguintes: título, nome do autor, DOI, para que o sistema crie um novo artigo com essa informação.
    - Atualizar artigo 🔄: Os utilizadores podem atualizar as informações dos artigos, nomeadamente a data de publicação, o resumo, keywords, autores e afiliações.
    - Consultar artigo 🔎: Dado um identificador de um artigo, o sistema imprime a informação desse, de forma organizada.
    - Eliminar artigo ❌: Dado o DOI de um artigo, podemos eliminar a publicação correspondente.
    - Listagem 📋: O sistema lista os artigos contidas no sistema. É possível consultar os artigos por filtração, isto é, consultá-los por autores or por keywords.
    - Distribuição 📊:Apresenta gráficos de estatísticas, tais: distribuição de publicações por ano, distribuição de publicações por mês de um determinado ano, número de publicações por autor,
    distribuição de publicações de um autor por anos, distribuição de palavras-chave pela sua frequência (top 20 palavras-chave), Distribuição de palavras-chave mais frequente por ano.
    - Importar📥: O utilizador poderá importar novos registos dum outro ficheiro que tenha a mesma estrutura do ficheiro de suporte.
    - Guardar Alterações ✅ : O sistema guarda todas as alterações feitas na aplicação no final da sua utilização.
    - Sair  : Encerramento da aplicação."""


        formLayout = [
            [sg.Text(help_text, font=("Times New Roman", 12))],
            [sg.Button("Fechar", key="-CLOSE-", size=(10,1), disabled=False, font=("Times New Roman", 12),button_color=('#3c0000'))]
        ]

        wform = sg.Window("ⓘ Help", formLayout, size=(1250, 300))

        stopform = False
        while not stopform:
            inputEvent, inputValues = wform.read()

            if inputEvent == "-CLOSE-" or inputEvent == sg.WIN_CLOSED:
                stopform = True

        wform.close()


    else:
        window["-VE-"].update("Erro: Atividade não reconhecida!!")


window.close()