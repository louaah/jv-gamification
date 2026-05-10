label scene_apres_vote_2:

    if loi:
        scene parlement
        if fascho >=2 :
            show pote at right
            pote "Félicitations Camarade ! Je savais que je pouvais compter sur vous, il faudrait que je te présente à la présidente du parti à la prochaine session, elle appréciera rencontrer quelqu'un d'aligné à ses idées !"
        else:
            show pote at right
            pote "Félicitations ! Un choix de qualité, je savais que je pouvais compter sur vous. Les prochaines votations seront importantes, soyez prêt !"

    else:
        scene parlement
        show pote at right
        pote "Alors collègue ? Je vois que ce n'est pas simple pour vous de comprendre les enjeux actuels. Vous devriez commencer à mieux vous renseigner pour les prochaines votations."
    
    jump scene_maison_4
return 
