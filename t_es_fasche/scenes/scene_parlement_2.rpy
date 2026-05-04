label scene_parlement_2:
    # play music "music_parlement.mp3"

    scene parlement

    if fascho>=1:
        show pote at right
        pote "Hey salut compatriote, ou devrais-je dire camarade? La présidente a vraiment de bonnes idées, mais elles ne sont pas faciles à mettre en place. Surtout avec les autres là, déjà qu’ils n’arrivent même pas à se mettre d’accord entre eux, maintenant ils viennent ralentir nos plans de sauvetage. Avec la votation d’aujourd’hui cela devrait aller mieux ! Je compte sur toi, camarade !"
    else:
        show pote at right
        pote "Bonjour cher collègue, nous avons de grands projets aujourd’hui !  La présidente a vraiment de bonnes idées, mais elles ne sont pas faciles à mettre en place. Surtout avec les autres là, déjà qu’ils n’arrivent même pas à se mettre d’accord entre eux, maintenant ils viennent ralentir nos plans de sauvetage. Je compte sur toi pour faire le bon choix !"

    hide pote 
    show chef at right 
    chef "La votation du jour est a propos de bla bla bla "
    "À votre tour de donner vos avis maintenant en votant oui ou non..."

   

    menu:
        "Oui":
            $ fascho += 1
            $ loi = True
            jump scene_oui_2
        "Non":
            $ loi = False
            jump scene_non_2

return