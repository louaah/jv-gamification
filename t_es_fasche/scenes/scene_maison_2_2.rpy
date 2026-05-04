label scene_maison_2_2:
    # play music "music_maison.mp3"

    scene maison
    show parents at left

    parents "Merci pour l’accueil, cela nous fait toujours plaisir d’avoir des choses à fêter dans la famille ! C’était…sympa de découvrir une nouvelle recette ! La prochaine fois, nous vous invitons, c’est normal de vous retourner la faveur. Il se fait tard, encore félicitation pour ton élection !"

    hide parents
    show partenaire at right 

    partenaire "Hahaha, toujours un sacré tact tes parents, on sait de qui tu tiens tes talents en politique. Non, je ne le prends pas mal, je sais qu’on est de génération différente, déjà, ils ont arrêté de me mègenré, c’est un début. Ça viendra avec le temps. Bon j’avoue que le coup du tuperweares pleins de viande, c’est une nouveauté…."
    "Mais c’est vrai que les discussions autour de la table ne sont pas toujours simples. Heureusement que j’ai du caractère pour leur tenir tête. Bon maintenant, qu’ils sont partis, tu peux me raconter dans les détails comment s'est passé ta journée ! "
menu:
    "Parler de la votation":
        $ fascho += 1
        jump scene_maison_3
    "Ne pas parler de la votation":
        $ fascho = 0
        jump scene_maison_3

return