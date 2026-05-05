label scene_oui_2:
    # play music "music_maison.mp3"

    scene parlement

    if fascho >= 2:
        show pote at right
        pote "Félicitations Camarade !  Je savais que je pouvais compter sur vous, il faudrait que je te présente à la présidente du partie à la prochaine session, elle appréciera rencontrer quelqu’un d'aligné à ces idées ! "
        jump scene_maison_4
    
    
    
    elif fascho >= 1: 
        show pote at right

        pote "Félicitations ! Un choix de qualité, je savais que je pouvais compter sur vous. Les prochaines votations seront importantes, soyez prêt !"
        jump scene_maison_4
   
hide pote


return