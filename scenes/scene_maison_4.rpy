label scene_maison_4:
    # play music "music_maison.mp3"

    scene maison
    show partenaire at right

    partenaire "Alors cette votation ?"
    partenaire "Cela ne doit pas être facile de devoir prendre de telles décisions. Je me dis heureusement que tu travailles déjà au parlement, comme ça tu pourras à nouveau être élu avec ce nouveau texte."
    partenaire "Je comprends le besoin d’avoir des personnes compétentes, mais un peu moins que l’on ne puisse plus ouvrir de nouveau parti politique."

    hide partenaire




    menu:
        "Parler de l'ami du parlement":
            $ fascho += 1
            jump scene_maison_5
            
        "Ne pas parler de l'ami du parlement ":
            jump scene_maison_5
            

    

return