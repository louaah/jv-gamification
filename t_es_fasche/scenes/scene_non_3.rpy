label scene_non_3:
    # play music "music_maison.mp3"

    scene parlement

    if fascho >= 1:
        show pote at right
        pote "Je peux comprendre les fois précédentes, mais votre incompréhension des enjeux semble devenir systématique collègue…Si j’étais vous, je ferais attention à mes décisions."

        jump scene_maison_5_2

    
    
    
    elif fascho >=2: 
        show pote at right

        pote "Camarade? Je suis surpris par votre choix, cela ne vous ressemble pas ! J’espères que vous ne referez pas une erreur aussi bête aux prochaines votations."
        
        jump scene maison_5_2

return