label scene_maison_5_2:
    # play music "music_maison.mp3"

    scene maison
    show partenaire at right

    partenaire "La loi est passée, je me demande quelles seront les conséquences pour mon travail. Nous avons une réunion d’urgence prévue demain à la première heure. Après c’est vrai qu’avec toutes ces manifestations et les dégâts… il faut faire quelque chose mais bon, toi comment s’est passé ta journée?"
    "QUOI ??? Tu as vu la présidente ???? Woaaaw, elle est comment ? Elle est aussi charismatique en vrai qu’à la télé? Damn, faut que tu racontes cela à tes parents."
    





    menu:
        "Décrire la présidente en détails et parler des intéractions avec potofascho.":
            $ fascho += 1
            jump scene_maison_5_3
            
        "Décrire la présidente vaguement  ":
            jump scene_maison_5_3
            

    

return