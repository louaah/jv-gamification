label scene_apres_vote_4:

    if loi:
        scene parlement
        if fascho <=2 :
            show chef at right
            chef "Vous avez fini par entendre raison, c'est le bon choix. Nous aimerions pas qu'il vous arrive quelque chose… camarade…"
            hide chef
        elif fascho == 3:
            show chef at right
            chef "Bravo Camarade, nous avons constaté vos efforts, c'est avec plaisir que nous pouvons compter sur vous. Si vous continuez ainsi, vous verrez de réels avantages aux prochaines votations."
            hide chef
        else:
            show chef at left
            chef "Mon ami, quel beau projet nous réalisons ensemble. Potofasho avait raison à votre sujet, vous êtes un de nos plus fidèles partisans. Venez, nous allons fêter la réussite avec le reste de l'équipe, laissez-moi vous remercier personnellement. Vous pourrez bientôt avoir votre propre chauffeur et véhicule. Je vous tiens en… haute estime… personnellement."
            hide chef
    
    else:
        scene parlement
        if fascho <=1:
            show chef at right
            chef "Il est temps que vous vous repreniez en main, c'est le dernier avertissement que vous aurez de notre part. Notre patience a atteint sa limite. Soyez prêt pour les prochaines votations… On aimerait pas qu'il vous arrive quelque chose."
            hide chef 
        elif fascho == 2:
            show chef at right
            chef "Nous avons encore de l'espoir pour vous camarade, à la prochaine votation, ce sera votre dernière occasion de ne pas nous décevoir."
            hide chef
        else:
            show chef at right
            chef "Camarade ? Qu'est-ce qu'il vous arrive ? Ce n'est pas le moment de vous dégonfler. Nous comptons sur vous. C'est votre seul avertissement, vos actions auront des conséquences."
            hide chef
    
    jump scene_maison_6_2
return 
