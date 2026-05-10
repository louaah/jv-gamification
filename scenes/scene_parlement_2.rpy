label scene_parlement_2:
    # play music "music_parlement.mp3"

    scene parlement

    if fascho >= 1:
        show pote at right
        pote "Hey salut compatriote, ou devrais-je dire camarade? La présidente a vraiment de bonnes idées, mais elles ne sont pas faciles à mettre en place."
        pote "Surtout avec les autres là, déjà qu’ils n’arrivent même pas à se mettre d’accord entre eux, maintenant ils viennent ralentir nos plans de sauvetage. Avec la votation d’aujourd’hui cela devrait aller mieux ! Je compte sur toi, camarade !"
    else:
        show pote at right
        pote "Bonjour cher collègue, nous avons de grands projets aujourd’hui !  La présidente a vraiment de bonnes idées, mais elles ne sont pas faciles à mettre en place."
        pote "Surtout avec les autres là, déjà qu’ils n’arrivent même pas à se mettre d’accord entre eux, maintenant ils viennent ralentir nos plans de sauvetage. Je compte sur toi pour faire le bon choix !"

    hide pote 
    show chef at right 
    chef "Dehors, les gens se disputent pour du papier toilette, les supermarchés sont bondés et les vivres risquent de manquer. Je ne vais rien vous apprendre en disant celà, mais c’est évidemment de la faute des wokistes."
    chef "S’ils pouvaient arrêter de l’ouvrir pour un tout et pour un rien, on pourrait se concentrer sur les vrais problèmes du peuple…"
    chef "La votation d’aujourd’hui vise à réduire les distractions afin que nous puissions nous concentrer sur l’amélioration des conditions de vie du peuple et lutter contre la famine imminente."
    chef "Nous avons donc envisagé de supprimer les partis non majoritaires et de remplacer le système actuel d’élections par des listes électorales, ce système permet un meilleur contrôle d’une situation de crise."
    chef "Imaginez simplement ce parlement sans discorde, le rêve non?"

    menu:
        "{b}Dissoudre les partis et instaurer un système de vote à liste électorale.{/b}"


        "Oui":
            $ fascho += 1
            $ loi = True
            $ lois.append("partis")
            $ lois_status.append("oui")
            jump scene_apres_vote_2
        "Non":
            $ loi = False
            $ lois.append("partis")
            $ lois_status.append("non")
            jump scene_apres_vote_2

return