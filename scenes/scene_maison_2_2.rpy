label scene_maison_2_2:
    # play music "music_maison.mp3"

    scene maison
    show parents at Position (xalign=0.75, yalign =0.5)

    parents "Cela fait toujours plaisir d’avoir des choses à fêter dans la famille ! C’était…sympa cette nouvelle recette !"
    parents "La prochaine fois, nous vous invitons, c’est normal de vous retourner la faveur !"

    hide parents
    show partenaire at Position (xalign=0.75, yalign =0.5) 

    partenaire "Toujours un sacré tact tes parents, on sait de qui tu tiens tes talents en politique." 
    partenaire "Non, je ne le prends pas mal, déjà, ils ont arrêté de me mègenré. Bon j’avoue que le coup du tuperweares pleins de viande, c’est une nouveauté…."
    partenaire "C’est vrai que les discussions autour de la table ne sont pas simples." 
    partenaire "Maintenant, qu’ils sont partis, racontes les détails comment s'est passé ta journée ! "

    hide partenaire
menu:
    "Raconter sa première journée.":
        $ fascho += 1
        jump scene_scene_intermédiaire_1
    "S'excusez car la soirée a été longue.":
        $ fascho = 0
        jump scene_scene_intermédiaire_1

return