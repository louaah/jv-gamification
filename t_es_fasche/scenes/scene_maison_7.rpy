label scene_maison_7:
    # play music "music_maison.mp3"

    scene maison

    if(not loi) or (loi and fascho <=2):
        show partenaire at right
        partenaire "C’est le grand jour. Fais attention à toi aujourd’hui. Avec ce qui c’est passé ces derniers mois, cela risque d’être tendu au parlement."
        partenaire "Ne t’inquiète pas pour moi, tu sais, même au “chômage”... je sais très bien m'occuper. On travaille sur quelque chose avec mes anciens collègues."
        partenaire "Vraiment…aujourd’hui, ne prends pas de risque... Je ne veux pas qu’il t'arrive quelque chose…Ne t’approches pas des limousines misent à disposition par la présidente, tu me le promets ?"
    if loi and fascho <=4 :
        partenaire "Il y’a du café prêt dans la cuisine, avec la journée qui t’attend tu vas en avoir besoin. "
        partenaire "Tiens, comment ça se fait que tu aies une limousine le soir et pas le matin qui te transporte?"
        partenaire "Oui…j’ai remarqué que tu terminais tard ces temps…Tu dois vraiment travailler sur des gros projets avec la présidente…"
        partenaire "D’ailleurs aujourd’hui c’est une grande journée, tu devrais te dépêcher. J’ai hâte de te voir rentrer dans ta belle limousine ce soir…"
    
    hide partenaire


    
    jump scene_ville_5
            

    

return
