label scene_maison_2:
    # play music "music_maison.mp3"

    scene maison
    show partenaire at right

    partenaire "Hey Amour ! Alors ce premier jour ? Tu as survécu-e?"
    "Tu arrives pile à temps, tes parents sont censés arriver dans 10 minutes. Oui, non , t'inquiète pas, j’ai fait une recette végétarienne et pas végan, ça ne les empêchera pas de râler tu sais. Donc bon, un peu plus, un peu moins…Je veux bien faire des compromis, mais faut pas abuser non plus. "
    "Allez, va te doucher avant qu’ils arrivent, ça sent que tu as bossé dur aujourd’hui !"

    show parents at left

    parents "Ha mais quel charisme sur cette affiche ! Tu m’étonnes que tout le monde ait voté pour toi. Nous sommes extrêmement fiers !"
    "Oui, avec tout ce travail maintenant tu dois être fatigué-e, ça va tu manges bien? Je t’ai ramené un tupperwares de bœuf wegllinton. "
    "Non, mais je sais que tu manges plus trop de viande…mais cela ne t’as jamais dérangé quand tu vivais à la maison…et tu as besoin d’énergie pour changer le pays!"

    partenaire "ha je ne vous avais pas entendu, alors comment cela fait d’avoir un enfant au parlement?"

    parents "Ha bah une fierté bien sûr, qui de mieux pour représenter notre pays? Avec un tel soutien, notre présidente va pouvoir faire du bon travail !"

    partenaire "Oui, c’est sûr qu’il y’a du boulot, mais ses idées me laissent parfois assez sceptiques… Elle a tendance à se concentrer seulement sur le sommet de l’Iceberg le reste."

    parents "On ne peut pas s’occuper de tout quand le pays est en crise comme aujourd’hui ! Il faut protéger notre pays des différentes menaces. C’est la priorité !"

    partenaire "Oui, mais il ne faut pas oublier de soutenir le peuple non plus ! Ha, le repas est prêt, nous allons pouvoir passer à table."





    # menu:
    #     "Choix 1":
    #         $ fascho += 1
    #         $ loi = True
    #
    #     "Choix 2":
    #         $ loi = False
    jump scene_maison2_2
    

return