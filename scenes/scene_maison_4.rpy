label scene_maison_4:
    # play music "music_maison.mp3"

    scene maison
    show partenaire at right

    partenaire "Alors cette votation ?"
    partenaire "Ca doit pas être facile de prendre de telles décisions. Heureusement que tu travailles déjà au parlement, comme ça tu pourras à nouveau être élu avec ce nouveau texte."
    partenaire "Je comprends le besoin d’avoir des personnes compétentes, mais un peu moins que l’on ne puisse plus ouvrir de nouveau parti politique..."
    Partenaire "Tu as à nouveau vu ton collègue? Il a l'aire...intéressant. Il ressemble à quoi?"

    hide partenaire




    menu:
        "Parler de notre pote du parlement":
            $ fascho += 1
            jump scene_maison_5
            
        "Fuir en s'excusant d'un besoin pressant":
            jump scene_maison_5
            

    

return