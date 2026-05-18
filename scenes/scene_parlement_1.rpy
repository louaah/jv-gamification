label scene_parlement_1:
    # play music "music_parlement.mp3"

    scene parlement

    show pote at Position (xalign=0.75, yalign =0.5)
    pote "Bonjour ! Toi aussi c’est ton premier jour, pas trop de stress?"
    pote "Moi, j’ai pas réussi à fermer l'œil, c’est vraiment impressionnant."
    pote "On est à la fois si nombreux et si peu avec tout ce qu’on doit faire."
    pote "Iil faut vraiment que l’on arrive à faire la différence pour aider nos électeurs."
    pote "Il va falloir être réactif si on veut sauver le pouvoir d’achat de la population."

    hide pote 
    show chef at Position (xalign=0.75, yalign =0.5)
    chef "Comme vous avez pu le constater: le pays risque d'entrer en crise. Nous sommes dans la nécessité d’agir vite, le système traditionnel est, comme vous le savez, lent et fastidieux."
    chef "La votation d’aujourd’hui porte donc sur les pouvoirs décisionnels des ministres.  Je vous rappelle encore une fois que nous devons agir vite!! Mieux vaut prévenir que guérir, comme on dit dans le jargon."
    hide chef
   

    menu:
        "{b}Autoriser les ministres à adopter de nouvelles lois sans passer par le système habituel de vote.{\b}"

        "Oui":
            $ fascho += 1
            $ loi = True
            $ lois.append("vote")
            $ lois_status.append("oui")
            jump scene_apres_vote_1
        "Non":
            $ loi = False
            $ lois.append("vote")
            $ lois_status.append("non")
            jump scene_apres_vote_1

return