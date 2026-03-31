#personnage 

define joueur = ("joueur") 
define partenaire = ("partenaire")
define mère = ("mère")
define père = ("père")
define oncle = ("oncle")
define pote = ("pote")
define chef = ("chef")
define vielle_dame = ("vieille dame")

#variable 
default fascho = 0 
default loi = False

#images 
image parlement = "parlement.png"
image ville = "ville.png"
image maison = "maison.png"
image partenaire = "partenaire.png"
image mere = "mere.png"
image pere = "pere.png"
image oncle = "oncle.png"
image pote = "pote.png"
image chef = "chef.png"
image vieille_dame = "vieille_dame.png"

#menu principal

#screen main_menu ():
    #add "image_bg.png"

    #vbox:
        #xalign 0.5
        #yalign 0.5

    #"T'es faché ?"
        #textbutton "oui" action Start()
        #textbutton "non" action Start()

label start : 
    #musique 
    #play music "music_maison.mp3"

    #scène 
    scene maison

    #personnages
    show partenaire at right

    #Narration 
    partenaire "Hey, mais tu es déjà debout? Le stress a fini par monter alors ! "
    "Viens, vu que tu es en avance, profites que je te fasse un café. J’en reviens toujours pas que tu travailles au parlement depuis les dernières élections. Même si je ne comprends pas ton choix d’être dans un parti centriste, je serais toujours là pour te soutenir dans tes projets !"
    "Nous avons vraiment besoin de personnes investies pour faire avancer les choses, la crise économique n’a pas l'air de diminuer. J’ai vu que les stats du chômage ont encore augmenté ce mois-ci et qu’il commence à y’avoir des files d’attente devant les supermarchés….je n’imaginais pas que le fait que notre monnaie perde de la valeur aurait autant de conséquences dans notre quotidien…."
    "J’espère que tu vas pouvoir rapidement faire bouger les choses, la précarité est vraiment en train d'augmenter. J’ai encore entendu parler de coupe budgétaire au travail… j’espère qu’ils ne vont pas refaire une vague de licenciement."
    "Bref ! Je ne veux pas te casser le moral avec mes histoires, surtout que toi, contrairement à moi, tu peux vraiment avoir un impact sur la situation. On se retrouve ce soir avec tes parents pour fêter ce premier jour !"

jump scene_ville 

label scene_ville : 
    #musique 
    #play music "music_ville.mp3"

    #scène 
    scene ville

    #narration 
    "bla bla bla"

    #choix 
    #menu: 
        #""
        #$ fascho +=1 
        #$ loi =
        #""
        #$ loi =

jump scene_parlement

label scene_parlement :
    #musique 
    #play "music_parlement.mp3"

    #scene 
    scene parlement

    #personnages
    show chef at left
    show parlement at right

    #narration 
    #""
    #chef ""
    #pote ""

    #choix
    #menu:
        #""
        #$ fascho +=1
        #$ loi =

        #""
        #$ loi =

jump scene_ville_1

label scene_ville_1: 
    #musique 
    #play music "music_ville.mp3"

    #scène 
    scene ville

    #narration 
    "bla bla bla"

    #choix 
    #menu: 
        #""
        #$ fascho +=1 
        #$ loi =
        #""
        #$ loi =

jump scene_maison_1

label scene_maison_1 : 
    #musique 
    #play music "music_maison.mp3"

    #scène 
    scene maison

    #personnages
    show partenaire at right

    #Narration 
    partenaire ""

    #choix 
    #menu : 
        #""
        #$ fascho +=1
        #$ loi =
        #""
        #$ loi =

jump scene_ville_2