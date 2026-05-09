label scene_parlement_3:
    # play music "music_parlement.mp3"

    scene parlement

    if fascho ==1:
        show pote at right
        pote "Bonjour collègue, j’espère que vous vous êtes bien renseigné pour la votation d’aujourd’hui. Je compte sur vous pour prendre la bonne décision, les choix ont des conséquences vous savez?"
    elif fascho ==2:
        show pote at right
        pote "Bonjour collègue ! Vous êtes sur la bonne voie, vous vous êtes bien renseigné sur la votation du jour? Je sais que je peux vous faire confiance pour fairele bon choix !"
    else 
        show pote at right
        pote "Camarade ! Quel plaisir de vous voir, c’est une belle journée pour prendre de belles décisions. J’ai parlé de vous à la présidente, elle est intéressée à vous rencontrer ! Continuer sur cette voie et se sera pour bientôt."
    
    hide pote 
    show chef at right 
    chef "La votation du jour est a propos de bla bla bla "
    "À votre tour de donner vos avis maintenant en votant oui ou non..."

    hide chef

   

    menu:
        "Oui":
            $ fascho += 1
            $ loi = True
            jump scene_apres_vote_3
        "Non":
            $ loi = False
            jump scene_apres_vote_3

return