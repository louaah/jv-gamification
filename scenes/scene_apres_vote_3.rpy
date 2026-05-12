label scene_apres_vote_3:
    # Ici avec l'asset il faudrait dans tout les cas que la présidetne soit à coté de potofasho sinon le scripts marche pas le jours d'après.

    if loi:
        scene parlement
        if fascho >=3 :
            show pote at right
            pote "Quel honneur de faire partie de vos collègues, camarade. Je vous présente Miormia Geloni, notre chère présidente."
            hide pote
            show chef at left
            chef  "Bonjour Camarade, Potofasho m'a parlé de vous en haute estime. Il a bon espoir pour votre future carrière, elle est impeccable jusqu'à présent."
            chef " Continuez ainsi et vous serez le bienvenu au repas pour nos plus fidèles partisans"
            hide chef
        else:
            show pote at right
            pote "Vous voyez, quand on veut on peut ! Continuez comme cela et je parlerai de vous à la présidente à la prochaine votation !"
            hide pote
    
    else:
        scene parlement
        if fascho >=2:
            show pote at right
            pote "Camarade ? Je suis surpris par votre choix, cela ne vous ressemble pas ! J'espère que vous ne referez pas une erreur aussi bête aux prochaines votations."
            hide pote 
        else:
            show pote at right
            pote "Je peux comprendre les fois précédentes, mais votre incompréhension des enjeux semble devenir systématique, collègue… Si j'étais vous, je ferais attention à mes décisions..."
            hide pote
    
    jump scene_maison_5_2
return 
