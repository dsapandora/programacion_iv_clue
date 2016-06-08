image interrogatorio = "Interrogatorio.png"
image ciudad = "Ciudad.png"
image compu = "Compu.png"
image fin = "Fin.png"
image asesino = "Asesino.png"
image test1 = "Test1.png"
image test2 = "Test2.png"

image detective = "Detective.png"
image detectivePruebas = "DetectivePruebas.png"
image detectiveConfron = "DetectiveConfron.png"
image detectivePensar = "DetectivePensar.png"
image detectiveAja = "DetectiveAja.png"

image art = "Art.png"
image art1 = "Art1.png"

image burt = "Burt.png"
image burt1 = "Burt1.png"
image burt3 = "Burt3.png"

image carl = "Carl.png"
image carl1 = "Carl1.png"

image detectivePensar = "DetectivePensar.png"

define d = Character('Detective', color="#c8ffc8")
define a = Character('Art', color ="#ff0000")
define b = Character('Burt', color ="#0000cd")
define c = Character('Carl', color ="#32cd32")
define n = Character('Niko', color ="#ffff00")

label start:
    scene interrogatorio
    "Hola bienvenidos"

    show detective
    with dissolve

    d "Estamos aqui para aclarar todo sobre el asesinato de Victoria, quien fue encontrada muerta en las afueras del puebo."
    hide detective

    show detectivePruebas
    with dissolve
    d "El cual segun las pruebas fue perpetrado...."
    hide detectivePruebas

    show detectiveConfron
    with dissolve
    d "Por uno de los SOSPECHOZOS AQUI PRESENTES!"
    hide detectiveConfron

    show detectivePensar at right
    with dissolve
    d "A ver por donde comenzamos"
    d "Hay dos testigos que vieron a los sopechosos y a la victima juntos el dia del asesinato"
    hide detectivePensar

    show test2 at right
    with dissolve
    d "El Señor Lopez"

    show test1 at left
    with dissolve
    d "Y la Señora Garcia"

    hide test1
    hide test2
    show detectivePensar at right
    d "Ademas tenemos tres sospechosos"
    hide detectivePensar
    
    scene ciudad
    show art 
    with dissolve
    d "Art"
    hide art

    show burt
    with dissolve
    d "Burt"
    hide burt

    show carl
    with dissolve
    d "Y Por ultimo Carl"
    hide carl
    
    scene interrogatorio
    show detective
    d "A ver Señor Art que nos puede decir"
    hide detective
    show art1 
    with dissolve
    a "Bern es amigo de Victoria"
    a "Pero Carl y Victoria se odiaban a muerte"
    hide art1

    show detective
    with dissolve
    d "Su turno Señor Burt"
    hide detective
    show burt1
    with dissolve
    b "Yo ni siquiera estaba en la ciudad ese dia..."
    b "Y por si fuera poco no conozco a la tal Victoria" 
    hide burt1

    show detective at left
    d "Y usted señor Carl lo veo muy tranquilo"
    hide detective
    show carl1
    with dissolve
    c "Yo soy inocente no se que hago aqui"
    c "En lo unico que puedo ayudar es en decirles que vi a Art y a Burt conduciendo por la ciudad ese dia"
    hide carl1

    show detectivePensar
    d "Vaya que interesante"
    d "Niko Alimentemos nuestra computadora con los datos a ver que nos dice"
    hide detectivePensar

    scene compu
    n "Si Detective ya me adelante, dentro de poco tendremos el nombre de nuestro asesino" 
    
    scene asesino

    python:
        from pyswip import Prolog
        prolog = Prolog()
        prolog.consult('/home/denis/Documentos/asesino.pl')
        asesino = list(prolog.query('murderer(X)'))
        n ("El asesino es %s "%asesino[0]['X'])

    scene interrogatorio
    show detectiveAja at right
    d "Detengan al Sr Burt"
    hide detectiveAja

    show burt3 at left
    with dissolve
    b "Como fue que lo resolvieron.....rayos!"
    hide burt3

    show detective
    with dissolve
    d "No lo veremos por un buen tiempo"
    hide detective
    
    scene fin
    "FIN"

return
