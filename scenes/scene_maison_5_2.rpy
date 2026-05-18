label scene_maison_5_2:
    # play music "music_maison.mp3"

    scene maison
    show partenaire at Position (xalign=0.75, yalign =0.5)


    partenaire "La loi est passée, je me demande quelles seront les conséquences à mon travail. Nous avons une réunion d’urgence prévue demain matin."
    partenaire "C’est vrai qu’avec toutes ces manifestations et les dégâts... il faut faire quelque chose...toi comment s’est passé ta journée?"
    partenaire "QUOI ??? Tu as vu la présidente ???? Woaaaw, elle est comment ? Elle est aussi charismatique en vrai qu’à la télé? Damn, faut que tu racontes cela à tes parents."
    
    hide partenaire





    menu:
        "Décrire la présidente et parler des intéractions avec potofascho.":
            $ fascho += 1
            jump scene_maison_5_3
            
        "Décrire la présidente vaguement..":
            jump scene_maison_5_3
            

    

return