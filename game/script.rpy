# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define nome_protag = "protag"

define eu = Character(_("Eu"), color="#FFCA80")
define tio = Character(_("Tio"))
define marilda = Character(_("Marilda"), color="#AD848E")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg ceu with fade

    play music "musica pacifico.mp3"

    "Finalmente..."

    "Finalmente minhas férias chegaram!!!"

    "Agora poderei ter um período de sossego e viajar para longe daquele trabalho!"

    "Agora estou bem distante dele."

    "Talvez distante até demais..."

    "Falando nessa viagem, a história de como eu decidi meu destino foi no mínimo engraçada."

    "Eu comentei com meu tio a minha vontade de viajar para algum lugar tranquilo e pacato, e ele me recomendou que eu fosse para uma cidadezinha chamada Arretolândia."

    "Isso é praticamente do outro lado do país. Afinal, o estado do Ceará é bem distante de São Paulo."

    "Contudo, após muita insistência por parte dele, concordei em ir para lá."

    "Mas percebi que, quando eu perguntava o motivo disso, ele desconversava."

    "Falava para eu conhecer pessoas novas e explorar novos horizontes."

    "...O que é basicamente o contrário do que eu quero fazer."

    "Tudo bem que essa é a cidade-natal dele e dos meus pais..."
    
    "Mas isso não significa que esse seja um bom destino turístico."

    "Esse tio meu tem muita sorte que eu amo ele, ou eu o ignoraria e nem sairia do estado de São Paulo."

    # tio "Sobrinho, a sua família todinha cresceu em Arretolândia."

    # tio "Eu, seus pais, avôs e até seus bisavós!"

    # tio "Você tem que viver, nem que seja um pouco, as suas raízes!"

    # tio "Nossa família é cearense de berço."

    jump Lobby

label Lobby:
    stop music

    show bg protag_sala_estar with fade

    play music "musica casual.mp3"

    menu:
        "Quem vou conhecer Agora?"

        "Marilda":
            jump Marilda
        
        "Lucas":
            jump Lucas

        "Joana":
            jump Joana

        "Zeca":
            jump Zeca

        "Ana Clara":
            jump Ana_Clara

        "Vou ficar em casa hoje":
            jump fim

label Marilda:

    label centro:

        scene centro with fade

        play musica "musica calma.mp3"

        "O frescor da manhã traz uma leve brisa que acaricia meu rosto enquanto ando pelas ruas tranquilas da cidade." 
        
        "Comparado ao caos incessante da cidade grande, o silêncio aqui quase parece um abraço acolhedor." 
        
        "Os comerciantes começam a abrir suas lojas com gestos lentos e despreocupados"
        
        "e poucos moradores vagam pela calçada, provavelmente comprando ingredientes frescos para o café da manhã."
        
        "Eu ainda não sei o que fazer com o tempo que tenho." 
        
        "Meu tio sugeriu que eu explorasse o lugar, conhecesse as pessoas, mas para quê?" 
        
        "Não vou ficar por tanto tempo assim."
        
        "Talvez fosse melhor apenas relaxar e tentar esquecer meus problemas..."

        jump choro_crianca

    label choro_crianca:

        stop music

        play sound "efeito choro.mp3" noloop

        play music "musica tensa.mp3"

        "Meus devaneios são interrompidos por um som abafado."

        "Parece... um choro."

        play sound "efeito choro.mp3" noloop

        "Olho ao redor e logo percebo uma criança cabisbaixa sentada em um banco, com os joelhos ralados e sujos."
        
        "Ela parece estar hiperventilando de dor, e seus olhos vermelhos devido ao choro intenso."

        # show matilda base at Transform(xpos=.35, ypos=.15) with dissolve

        show matilda base at Transform(xpos=.35, ypos=.35) with dissolve

        "Ao lado dela, uma senhora tenta acalmá-la com um carinho nos cabelos." 
        
        "Ela tem o rosto sereno e as mãos cuidadosas."
        
        "Seus olhos irradiam paciência e seu sorriso, acolhimento."

        "Tudo para fazer a criança se sentir melhor."

        marilda "Vai passar, meu bem, vai passar..."

        marilda "A vovó só precisa de algo para limpar esses joelhos machucados."

        marilda "Logo logo você estará correndo por aí de novo rumo a sua próxima aventura."
        
        "Em contraste, seus olhares discretos, porém frenéticos, buscam alguém para ajudar nessa crise."

        "E, de fato, há alguém ali que pode ajudá-los: {b}EU{/b}."

        "Perante essa situação, lembro-me do kit de primeiros socorros que sempre levo comigo na minha mochila."

        "E, com isso, sinto uma vontade ardente inexplicável de ajudar aqueles dois."

        menu:

            "Sendo assim, tiro o kit médico da mochila, me aproximo da dupla e..."

            "Ofereço à senhora o kit médico":

                eu "Com licença, talvez isso ajude?"

                "No meu tom de voz noto um pouco de timidez e nervosismo que eu não queria passar."

                "Ela levanta os olhos para mim, surpresa, mas logo sorri calorosamente como se eu fosse um velho amigo."
            
            "Aplico o kit médico à criança eu mesmo":

                eu "Ei, tudo bem se eu sarar o joelho?"

                "A criança, ainda sobrecarregada com a dor do joelho ralado, só acena com a cabeça em confirmação."

                "A senhora levanta os olhos para mim em surpresa," 
                
                "mas logo sorri calorosamente como se eu fosse um velho amigo."

                marilda "Deixa comigo, filho. Já fiz isso mil vezes."

        play music "musica alegre.mp3"
        
        play sound "efeito kit medico"

        "Permaneço em silêncio enquanto observo a senhora limpar os machucados com a precisão que só a experiência traria." 
        
        "Suas mãos se movem com uma leveza tranquila, como se cada gesto fosse calculado para acalmar e curar ao mesmo tempo." 
        
        "Em questão de minutos, o joelho é limpo e enfaixado."
        
        "A criança, que antes soluçava, agora já mais calma, olha para a senhora e a mim com gratidão."

        play sound "efeitos passos"

        "Resolvida a crise, a criança se levanta do banco e lenta e cuidadosamente caminha de volta para casa."

        "A senhora também se levanta enxugando as mãos com um lenço que tirou do bolso e se vira para mim com um sorriso caloroso."

        play sound "efeito marilda rindo"
        
        marilda "Ora, veja só! Um rapaz prevenido."

        marilda "Isso sim é o que eu chamo de estar preparado."
        
        marilda "Não esperava ver um moço da cidade carregando algo assim por aqui."

        eu "É sempre bom estar pronto para qualquer coisa."

        "Respondo rápida e espontaneamente."

        eu "Vários parceiros de viagens meus já me disseram que eu exagero na quantidade hora de {b}escolher os itens{/b} que eu vou levar."

        eu "Mas você tem que concordar comigo que isso tem suas vantagens."

        marilda "Definitivamente!"

        marilda "De qualquer forma, muito obrigada, meu jovem."

        marilda "Falo isso por mim e pela criança que você me ajudou a socorrer."

        eu "Eu me chamo [nome_protag]. Acabei de chegar na cidade."

        "Ela acena com a cabeça exibindo um sorriso de canto de boca como se já soubesse disso de algum jeito."

        marilda "Sabia que você não era daqui!"

        marilda "Meu nome é Marilda, mas todos me chamam de Dona Marilda. Eu cuido de algumas coisinhas por aqui..."

        "Ela faz um gesto vago, como se o \"cuidar\" envolvesse muito mais do que alguém poderia explicar por palavras."

        marilda "E o que te traz para essa cidadezinha pacata?"

        "Eu hesito por um momento." 
        
        "Não esperava alguém fazer essa pergunta."

        "Contudo, pensando melhor, eu deveria ter previsto isso."

        "E parece que eu vou ter que responder essa pergunta cada vez que conhecer uma pessoa nova daqui."

        "Mas eu não posso simplesmente falar que eu não sei."

        "E responder que foi porque meu tio disse para vir aqui seria um pouco estranho."

        "Então vou optar por uma meia-verdade."

        eu "Ah, estou... visitando a terra natal da minha família."

        "Tento soar casual, mas ela parece ler além das palavras."

        marilda "Hmmm... Sei."

        "Ela não força mais o assunto."

        marilda "De qualquer forma, você foi de grande ajuda hoje, e não gosto de deixar uma boa ação passar batida."

        marilda "Ela faz uma pausa, avaliando-me por um instante."
        
        marilda "Que tal você vir até minha casa mais tarde?" 
        
        marilda "Tenho algo especial que faço questão de te oferecer como agradecimento." 
        
        marilda "Nada de muito formal, só um chá caseiro e um pouco de pão fresco." 
        
        marilda "Quem sabe eu até te mostro meu jardim de ervas. Tenho certeza que vai gostar."

        "Ela sorri novamente, aquele sorriso gentil que faz parecer que ela já te conhece há anos."

    jump Lobby

label Lucas:
    "Ainda em desenvolvimento"
    jump Lobby

label Joana:
    "Ainda em desenvolvimento"
    jump Lobby

label Zeca:
    "Ainda em desenvolvimento"
    jump Lobby

label Ana_Clara:
    "Ainda em desenvolvimento"
    jump Lobby

# o jogo termina aqui
label fim: 
    "Mensagem dos devs: {b}Obrigado por jogar!{/b}"
    return