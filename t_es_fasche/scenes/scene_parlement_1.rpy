label scene_parlement_1:
    # play music "music_parlement.mp3"

    scene parlement

    show pote at right
    pote "Bonjour ! J’ai vu que toi aussi c’est ton premier jour, ça va pas trop le stress?"
    "Moi, j’ai pas réussi à fermer l'œil, je suis content de ne pas être le seul à découvrir le parlement, c’est vraiment impressionnant."
    "On est à la fois si nombreux et si peu avec tout ce qu’on doit faire."
    "Avec les conflits dans le monde, notre pays est vraiment en train de payer les pots cassés, il faut vraiment que l’on arrive à faire la différence pour nos électeurs."
    "Il va falloir être réactif et prendre les choses en main ! On doit être rapide si on veut sauver le pouvoir d’achat de la population."

    hide pote 
    show chef at right 
    chef "La votation du jour est a propos de bla bla bla "
    "À votre tour de donner vos avis maintenant en votant oui ou non..."

   

menu:
    "Oui":
        $ fascho += 1
        $ loi = True
        jump scene_oui_1
    "Non":
        $ loi = False
        jump scene_non_1

return