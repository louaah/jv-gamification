label scene_oui_3:
    # play music "music_maison.mp3"

    scene parlement

    if fascho >= 2:
        show pote at right
        pote "Vous voyez, quand on veut on peut !  Continuez comme cela et je parlerais de vous à la présidente au prochaine votation !"

        jump scene_maison_5_2

    
    
    
    elif fascho >=3: 
        show pote at right

        pote "Quel honneur de faire partie de vos collègues camarades. Je vous présente Miormia Geloni, notre chère présidente."

        show chef at left
        chef "Bonjour Camarade, Potofasho m’a parlé de vous en haute estime. Il a bon espoir pour votre future carrière, il faut dire qu’elle est impeccable jusqu’à présent .Au prochaine votation, nous organisons un repas pour nos plus fidèle partisant. Continuez ainsi etvous serez le bienvenu."

        jump scene maison_5_2

return