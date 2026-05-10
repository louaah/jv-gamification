label scene_parlement_5:

    # play music "music_parlement.mp3"

    scene parlement

    if (not loi) or (loi and fascho <= 2):
        show pote at right
        pote "Bonjour “camarade”, vous avez du courage de venir aujourd’hui. C’est le moment ou jamais pour montrer de quel côté de l’histoire vous voulez être."
        pote "Jusqu’à présent, vous nous avez toujours laissé le doute. Après aujourd’hui, vous n’aurez de toute façon plus le choix. Haha !"
        hide pote 

    elif loi and fascho <= 4:
        show chef at right 
        chef "Bonjour mon “cher” camarade, comment ça va aujourd’hui ? C’est une belle journée qui se profile pour nous."
        chef "Je compte sur toi pour les votations aujourd’hui. On pourra à nouveau “travailler” tard ce soir…après le banquet pour fêter notre victoire bien sûr."
        hide chef 

    show chef at right 
    chef "La votation du jour est a propos de bla bla bla "
    "À votre tour de donner vos avis maintenant en votant oui ou non..."

    hide chef
        

    menu:
        "Oui":
            $ fascho += 1
            $ loi = True
            jump scene_apres_vote_4
        "Non":
            $ loi = False
            jump scene_apres_vote_4

return