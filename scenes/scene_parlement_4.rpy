label scene_parlement_4:
    # play music "music_parlement.mp3"

    scene parlement

    if fascho ==1:
        show pote at right
        pote "Bonjour, j’espère que vous vous êtes bien renseigné cette fois. Ce projet de loi est  magnifique et très important pour l’avenir de notre patrie. Si j’étais à votre place, je réfléchirais à quelle place vous voulez vous trouver dans quelques années…."

    elif fascho == 2:
        show pote at right
        pote "Bonjour ! Cela fait plaisir de vous voir aujourd’hui, le projet que nous allons voter est magnifique ! Notre patrie n’en sera qu'embellir après cette votation. Je ne vois aucune raison de voter contre, réfléchissez bien à l’avenir."
    elif fascho >=3 :
        show pote at right
        pote "Bonjour Camarade ! Quel plaisir de vous voir, la votation d’aujourd’hui représente l’un des plus beaux projets de notre patrie ! Avec cela, nous promettons un avenir radieux à nos compatriotes. Je sais que je peux compter sur vous. Nous irons loin ensemble !"

    
    hide pote 

    if fascho ==1:
        show chef at right 
        chef "Il est temps que vous vous repreniez en main, c’est le dernier avertissement que vous aurez de notre part. Notre patience a atteint sa limite.  Soyez prêt pour les prochaines votations…On aimerait pas qu'il vous arrive quelque chose. "

    if fascho == 2:
        show chef at right 
        chef "Nous avons encore de l'espoir pour vous camarade, au prochaine votation, cela sera votre dernière occasion de ne pas nous décevoir."

    if fascho >= 3 :
        show chef at right 
        chef "Camarade? Qu’est ce qu’il vous arrive? Ce n’est pas le moment de vous dégonfler. Nous comptons sur vous. C’est votre seul avertissement, au prochaine votation, vos actions auront des conséquences."
    hide chef 

    show chef at right 
    chef "Bon, vous le savez, je suis une femme du peuple. Mon ambition est de rétablir le bien-être collectif et, en ces temps de crise, de nombreuses mesures sont nécessaires."
    chef "Notre pays manque cruellement d'enfants. Notre population vieillit, et j'ai bien peur que, sans notre intervention, la nation ne coule tout droit vers sa fin."
    chef "Avec l'aide de nombreux experts, nous sommes arrivés à la conclusion que nous devons ABSOLUMENT repeupler nos terres."
    chef "Je vous propose donc de subventionner les naissances, d'offrir davantage d'aides aux familles, d'ouvrir de nouvelles crèches ainsi que de nombreux centres d'accueil pour les enfants."
    chef "Ces établissements seront bien évidemment supervisés par notre fabuleux État. Hors de question que nous élevions des perturbateurs. Hehe... j'ai... euh... nous avons déjà créé un excellent programme pour eux."
    hide chef


    menu:
        "{b}Offrir des aides financières aux familles pour chaque nouvel enfant et créer des institutions supervisées par l'État.{/b}"
        "Oui":
            $ fascho += 1
            $ loi = True
            $ lois.append("naissances")
            $ lois_status.append("oui")
            jump scene_apres_vote_4
        "Non":
            $ loi = False
            $ lois.append("naissances")
            $ lois_status.append("non")
            jump scene_apres_vote_4

return