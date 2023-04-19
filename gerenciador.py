from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    titulo = 'Sinopse'
    texto_principal = ''
    with open('./arquivos_texto/texto_principal.txt', 'r', encoding='utf-8')\
            as file:
        texto_principal += file.read()

    return render_template('index.html', titulo=titulo,
                           texto_pagina=texto_principal)


@app.route('/historia')
def historia():
    titulo = 'Historia'
    texto_principal = ''
    with open('./arquivos_texto/texto_historia.txt', 'r', encoding='utf-8')\
            as file:
        texto_principal += file.read()

    return render_template('historia.html', titulo=titulo,
                           texto_pagina=texto_principal)


@app.route('/personagem')
def personagens():
    raiz = './arquivos_texto/personagens/'
    titulo = 'Personagens'
    subtitulo = ['Monkey D. Luffy', 'Roronoa Zoro', 'Vinsmoke Sanji', 'Nami',
                 'Usoop', 'Tony Tony Chopper', 'Nico Robin', 'Franky',
                 'Brook', 'Jinbei']
    
    texto_luffy = ''
    with open(f'{raiz}luffy.txt', 'r', encoding='utf-8')\
            as file:
        texto_luffy += file.read()

    texto_zoro = ''
    with open(f'{raiz}zoro.txt', 'r', encoding='utf-8')\
            as file:
        texto_zoro += file.read()

    texto_sanji= ''
    with open(f'{raiz}sanji.txt', 'r', encoding='utf-8')\
            as file:
        texto_sanji += file.read()

    texto_nami= ''
    with open(f'{raiz}nami.txt', 'r', encoding='utf-8')\
            as file:
        texto_nami += file.read()

    texto_usoop= ''
    with open(f'{raiz}usoop.txt', 'r', encoding='utf-8')\
            as file:
        texto_usoop += file.read()

    texto_chooper= ''
    with open(f'{raiz}chopper.txt', 'r', encoding='utf-8')\
            as file:
        texto_chooper += file.read()

    texto_robin= ''
    with open(f'{raiz}robin.txt', 'r', encoding='utf-8')\
            as file:
        texto_robin += file.read()

    texto_franky= ''
    with open(f'{raiz}franky.txt', 'r', encoding='utf-8')\
            as file:
        texto_franky += file.read()

    texto_brook= ''
    with open(f'{raiz}brook.txt', 'r', encoding='utf-8')\
            as file:
        texto_brook += file.read()

    texto_jinbei= ''
    with open(f'{raiz}jinbei.txt', 'r', encoding='utf-8')\
            as file:
        texto_jinbei += file.read()

    return render_template('personagens.html', titulo=titulo,
                           subtitulo0=subtitulo[0],
                           subtitulo1=subtitulo[1],
                           subtitulo2=subtitulo[2],
                           subtitulo3=subtitulo[3],
                           subtitulo4=subtitulo[4],
                           subtitulo5=subtitulo[5],
                           subtitulo6=subtitulo[6],
                           subtitulo7=subtitulo[7],
                           subtitulo8=subtitulo[8],
                           subtitulo9=subtitulo[9],
                           texto0=texto_luffy,
                           texto1=texto_zoro,
                           texto2=texto_sanji,
                           texto3=texto_nami,
                           texto4=texto_usoop,
                           texto5=texto_chooper,
                           texto6=texto_robin,
                           texto7=texto_franky,
                           texto8=texto_brook,
                           texto9=texto_jinbei,
                           )

@app.route('/akuma_no_mi')
def akuma():
    raiz = './arquivos_texto/akuma_no_mi/'
    subtitulo = ['Gomu Gomu no Mi (Fruta da Borracha)', 'Hana Hana no Mi (Fruta da Flor)',
                 'Mera Mera no Mi (Fruta do Fogo)', 'Magu Magu no Mi (Fruta do Magma)',
                 'Yami Yami no Mi (Fruta da Escuridão)']
    
    fruta = ['Paramecia', 'Logia', 'Zoan']

    personagem = ['Monkey D. Luffy', 'Nico Robin','Portgas D. Ace/Sabo',
                  'Sakazuki', 'Marshall D. Teach']

    texto_gomu_gomu = ''
    with open(f'{raiz}gomu_gomu.txt', 'r', encoding='utf-8')\
            as file:
        texto_gomu_gomu += file.read()

    texto_hana_hana = ''
    with open(f'{raiz}hana_hana.txt', 'r', encoding='utf-8')\
            as file:
        texto_hana_hana += file.read()

    texto_mera_mera = ''
    with open(f'{raiz}mera_mera.txt', 'r', encoding='utf-8')\
            as file:
        texto_mera_mera += file.read()

    texto_magu_magu = ''
    with open(f'{raiz}magu_magu.txt', 'r', encoding='utf-8')\
            as file:
        texto_magu_magu += file.read()

    texto_yami_yami = ''
    with open(f'{raiz}yami_yami.txt', 'r', encoding='utf-8')\
            as file:
        texto_yami_yami += file.read()

    return render_template('akuma_no_mi.html', subtitulo0=subtitulo[0],
                           subtitulo1=subtitulo[1],
                           subtitulo2=subtitulo[2],
                           subtitulo3=subtitulo[3],
                           subtitulo4=subtitulo[4],
                           texto0=texto_gomu_gomu,
                           texto1=texto_hana_hana,
                           texto2=texto_mera_mera,
                           texto3=texto_magu_magu,
                           texto4=texto_yami_yami,
                           tipo_fruta0 = fruta[0],
                           tipo_fruta1 = fruta[1],
                           tipo_fruta2 = fruta[2],
                           nome0 = personagem[0], 
                           nome1 = personagem[1], 
                           nome2 = personagem[2], 
                           nome3 = personagem[3], 
                           nome4 = personagem[4],                           
                           )

@app.route('/curiosidades')
def curiosidade():
    raiz = './arquivos_texto/curiosidades/'
    titulo = 'Curiosidades'
    subtitulo = ['Pode parecer, mas One Piece não é o anime mais longo da história',
                 'Originalmente, One Piece seria uma série de cinco anos',
                 'One Piece e Eiichiro Oda estão no The Guinnes Book of World Records',
                 'Luffy é dublado por Mayumi Tanaka, uma mulher de 67 anos',
                 'A amizade entre Oda e Masashi Kishimoto que gerou easter eggs',]

    curiosidade1 = ''
    with open(f'{raiz}primeira.txt', 'r', encoding='utf-8')\
            as file:
        curiosidade1 += file.read()

    curiosidade2 = ''
    with open(f'{raiz}segunda.txt', 'r', encoding='utf-8')\
            as file:
        curiosidade2 += file.read()

    curiosidade3 = ''
    with open(f'{raiz}terceira.txt', 'r', encoding='utf-8')\
            as file:
        curiosidade3 += file.read()

    curiosidade4 = ''
    with open(f'{raiz}quarta.txt', 'r', encoding='utf-8')\
            as file:
        curiosidade4 += file.read()

    curiosidade5 = ''
    with open(f'{raiz}quinta.txt', 'r', encoding='utf-8')\
            as file:
        curiosidade5 += file.read()

    return render_template('curiosidades.html', titulo=titulo,
                           subtitulo0 = subtitulo[0],
                           subtitulo1 = subtitulo[1],
                           subtitulo2 = subtitulo[2],
                           subtitulo3 = subtitulo[3],
                           subtitulo4 = subtitulo[4],
                           texto1=curiosidade1,
                           texto2=curiosidade2,
                           texto3=curiosidade3,
                           texto4=curiosidade4,
                           texto5=curiosidade5,
                           )

app.run(debug=True)
