label scene_parlement_1:
    # play music "music_parlement.mp3"

    scene parlement

    show pote at right
    pote "Bonjour ! J’ai vu que toi aussi c’est ton premier jour, ça va pas trop le stress?"
    pote "Moi, j’ai pas réussi à fermer l'œil, je suis content de ne pas être le seul à découvrir le parlement, c’est vraiment impressionnant."
    pote "On est à la fois si nombreux et si peu avec tout ce qu’on doit faire."
    pote "Avec les conflits dans le monde, notre pays est vraiment en train de payer les pots cassés, il faut vraiment que l’on arrive à faire la différence pour nos électeurs."
    pote "Il va falloir être réactif et prendre les choses en main ! On doit être rapide si on veut sauver le pouvoir d’achat de la population."

    hide pote 
    show chef at right 
    chef "Comme vous avez pu le constater: le pays risque d'entrer en crise. Nous sommes dans la nécessité d’agir vite, le système traditionnel est, comme vous le savez, lent et fastidieux."
    chef "La votation d’aujourd’hui porte donc sur les pouvoirs décisionnels des ministres.  Je vous rappelle encore une fois que nous devons agir vite!! Mieux vaut prévenir que guérir, comme on dit dans le jargon."

   

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