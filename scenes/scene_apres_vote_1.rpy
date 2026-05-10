label scene_apres_vote_1:

    if loi:
        scene parlement
        show pote at right
        pote "Hey compatriote ! Je savais qu’on était sur la même longueur d’onde. On va enfin pouvoir améliorer rapidement la situation. Ça fait plaisir d’avoir quelqu’un sur qui je peux compter ! "
        hide pote

    else:
        scene parlement
        show pote at right
        pote "Je suis surpris par ton vote, je pensais qu’on était sur la même longueur d’onde. Heureusement, la votation est quand même passée et la présidente va rapidement pouvoir améliorer la situation."
        hide pote

    jump scene_maison_2
return 
