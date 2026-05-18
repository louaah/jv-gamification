label scene_maison_6_2:
    # play music "music_maison.mp3"

    scene maison

    if(not loi) or (loi and fascho <=2):
        show partenaire at Position (xalign=0.75, yalign =0.5)

        partenaire "La présidente est revenue te parler ? Qu'est-ce qu'il se passe au parlement ?"
        partenaire "Du personnel de la milice pour la protéger ? Le climat est tendu en ce moment, mais ce n'est pas sa garde personnelle !"
        partenaire "Il se passe des choses… tu sais, j'ai encore contact avec mes anciens collègues… Je préfère ne pas trop t'en dire."
        partenaire "Protège-toi, je ne veux pas qu'il t'arrive quelque chose. Par contre, donne-moi plus de détails ! Tu sais que j'adore le thé !"
        hide partenaire

    elif loi and fascho == 3:
        show partenaire at Position (xalign=0.75, yalign =0.5)

        partenaire "La présidente t'a remercié personnellement ? C'est incroyable !"
        partenaire "Elle est venue te parler des avantages que tu pourrais avoir ? C'est sympa de sa part, par contre l'histoire de la garde personnelle, c'est surprenant."
        partenaire "Tant que cela te fait plaisir, c'est bien. Des banquets et limousines personnelles ?? Quel luxe !"
        Partenaire "Si tu continues ainsi ? Dis-m'en plus, tu sais que j'adore les histoires…"
        hide partenaire

    elif loi and fascho >=4 :
        show partenaire at Position (xalign=0.75, yalign =0.5)

        partenaire "Je m'attendais à ce que tu rentres plus tôt. Il a duré longtemps ce repas…"
        partenaire "La présidente t'a remercié personnellement ? Woaow… c'est incroyable ! Je te félicite, j'imagine que c'était chouette comme soirée…"
        partenaire "C'est dommage que les +1 ne soient pas acceptés. J'aurais aimé voir ce qui se passe à ces soirées..."
        partenaire "Tu me racontes ? Tu sais que j'adore les histoires…"
        hide partenaire 

    menu : 
        "Donner plus d'informations sur la soirée.":
            $ fascho +=1
            jump scene_intermédiaire_4
        
        "S'excuser et aller se coucher." :
            jump scene_intermédiaire_4


    
    
            

    

return
