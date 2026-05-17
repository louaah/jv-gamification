label scene_apres_vote_2:

    if loi:
        scene parlement
        if fascho >=2 :
            show pote at Position (xalign=0.75, yalign =0.5)
            pote "Félicitations Camarade ! Je savais que je pouvais compter sur vous!"
            pote "Je te présenterai à la présidente du parti à la prochaine session, elle appréciera rencontrer quelqu'un d'aligné à ses idées !"
            hide pote
        else:
            show pote at Position (xalign=0.75, yalign =0.5)
            pote "Félicitations ! Un choix de qualité, je savais que je pouvais compter sur vous. Les prochaines votations seront importantes, soyez prêt !"
            hide pote
    else:
        scene parlement
        show pote at Position (xalign=0.75, yalign =0.5)
        pote "Collègue ? Je vois que ce n'est pas simple pour vous de comprendre les enjeux actuels. Vous devriez mieux vous renseigner pour les prochaines votations."
        hide pote
    jump scene_maison_4
return 
