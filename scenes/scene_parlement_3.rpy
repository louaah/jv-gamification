label scene_parlement_3:
    # play music "music_parlement.mp3"

    scene parlement

    if fascho ==1:
        show pote at Position (xalign=0.75, yalign =0.5)
        pote "Bonjour collègue, vous êtes vous bien renseigné ? Je compte sur vous pour prendre la bonne décision, les choix ont des conséquences vous savez?"
        hide pote
    elif fascho ==2:
        show pote at Position (xalign=0.75, yalign =0.5)
        pote "Bonjour collègue ! Vous êtes sur la bonne voie, vous vous êtes bien renseigné? Je peux vous faire confiance pour faire le bon choix !"
        hide pote
    else :
        show pote at Position (xalign=0.75, yalign =0.5)
        pote "Camarade ! C’est une belle journée pour de belles décisions. J’ai parlé de vous à la présidente, elle souhaites vous rencontrer ! Continuer sur cette voie et se sera pour bientôt."
    
    hide pote 
    show chef at Position (xalign=0.75, yalign =0.5)
    chef "Réunion d’urgence aujourd’hui, comme vous avez pû le voir ces derniers jours, les manifestants cassent et font peur à la population. Les médias les entraînent dans cette spirale de violence en propageant des fake news à notre sujet." 
    chef "Il faut mettre un terme à cette violence et engager une milice qui s’occupe de faire régner l’ordre et protéger nos honnêtes citoyens."
    hide chef
   

    menu:
        "{b}Supprimer les médias problématiques et créer une milice armée pour lutter contre les casseurs.{/b}"
        "Oui":
            $ fascho += 1
            $ loi = True
            $ lois.append("media")
            $ lois_status.append("oui")
            jump scene_apres_vote_3
        "Non":
            $ loi = False
            $ lois.append("media")
            $ lois_status.append("non")
            jump scene_apres_vote_3

return