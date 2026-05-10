label scene_maison_6_2:
    # play music "music_maison.mp3"

    scene maison

    if(not loi) or (loi and fascho <=2):
        show partenaire at right
        partenaire "La présidente est revenue te parler ? Ho… mais qu'est-ce qu'il se passe au parlement ?"
        partenaire "Il y avait du personnel de la milice pour la protéger ? J'entends que le climat est tendu en ce moment, mais ce n'est pas sa garde personnelle… c'est pas ce que l'on avait voté !"
        partenaire "Je sais qu'il se passe des choses… tu sais, j'ai encore contact avec mes anciens collègues… Je préfère ne pas trop t'en dire."
        partenaire "Protège-toi, je ne veux pas qu'il t'arrive quelque chose. Par contre, donne-moi plus de détails ! Tu sais que j'adore le thé !"

    elif loi and fascho == 3:
        show partenaire at right
        partenaire "La présidente t'a remercié personnellement ? Woaow… c'est incroyable !"
        partenaire "Elle est venue te parler des avantages que tu pourrais avoir ? C'est plutôt sympa de sa part, par contre j'avoue que l'histoire de la garde personnelle, c'est surprenant."
        partenaire "Je vois que cela te fait plaisir, c'est bien. Des banquets et limousines personnelles ?? Quel luxe !"
        Partenaire "Si tu continues ainsi ? Dis-m'en plus, tu sais que j'adore les histoires…"
    
    elif loi and fascho >=4 :
        show partenaire at right 
        partenaire "Je m'attendais à ce que tu rentres plus tôt. Il a vraiment duré longtemps ce repas…"
        partenaire "La présidente t'a remercié personnellement ? Woaow… c'est incroyable ! Je te félicite, j'imagine que cela devait être vraiment chouette comme soirée…"
        partenaire "C'est dommage que les +1 ne soient pas acceptés. J'aurais aimé… voir ce qui se passe à ces soirées."
        partenaire "Tu me racontes ? Tu sais que j'adore les histoires…"
    
    hide partenaire 

    menu : 
        "Donner plus d'informations sur la soirée.":
            $ fascho +=1
            jump scene_maison_7
        
        "S'excuser et aller se coucher." :
            jump scene_maison_7


    
    
            

    

return
