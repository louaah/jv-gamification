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
        chef "Je compte sur toi aujourd’hui. On pourra à nouveau “travailler” tard ce soir…après le banquet pour fêter notre victoire bien sûr."
        hide chef 

    show chef at right 
    chef"Vous avez vu ce qu'il se passe en dehors de nos frontières ? Les gauchiasses se liguent une nouvelle fois contre nous. Les pays frontaliers considèrent notre gouvernement comme fasciste... {b}tousse tousse{/b}."
    chef "Vous savez ce que ça veut dire ? Eh oui, très juste : il faut nous préparer à une guerre, non seulement physique, mais aussi idéologique."
    chef "Ils nous menacent, mais nous saurons répondre. C'est pour cela qu'il faut rétablir un service militaire obligatoire !"
    chef "Nos alliés pourront nous aider à nous réarmer, mais ne craignez rien, c'est seulement à titre préventif, hein !!"
    chef "Réfléchissez bien. Votre vote peut sauver le pays d'un anéantissement comme nous n'en avons jamais connu auparavant."
    chef "Ah oui, et j'oubliais... votre vote peut aussi déterminer VOTRE avenir."
    chef "Comme on dit... votez bien !!"
    hide chef

    menu:
        "{b}Rétablir le service militaire obligatoire et lancer un vaste programme de réarmement national.{/b}"
        "Oui":
            $ fascho += 1
            $ loi = True
            $ lois.append("militaire")
            $ lois_status.append("oui")
            jump scene_apres_vote_4
        "Non":
            $ loi = False
            $ lois.append("militaire")
            $ lois_status.append("non")
            jump scene_apres_vote_4

return