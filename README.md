# Bowling_Game_Kata
This repository is focused on creation of the Bowling Game's kata. This Kata consist of Create a program, which, given a valid sequence of rolls for one line of American Ten-Pin Bowling, produces the total score for the game. This Kata is from "Panel de Actividades" to do from Programming subject

 ## Bowling Game Kata DDD

 ### Dominio del problema: Conseguir la puntuación total del juego a partir de una secuencia valida de una partida de Bowling Game

### Lógica del negocio o reglas del juego. El programa que, dada una secuencia válida de rollos para una línea de American Ten-Pin Bowling,produce la puntuación total del juego. Este es un resumen de las reglas del juego:

1.  Cada juego , o "línea" de bolos, incluye diez turnos o " marcos " para el jugador de bolos. En cada cuadro, el jugador de bolos tiene hasta dos intentos para derribar todos los bolos .

2.  Si en dos intentos, no logra derribarlos a todos, su puntaje para ese marco es el número total de pinesderribado en sus dos intentos.

3.  Si en dos intentos los derriba a todos, esto se llama " repuesto " y su puntuación para el cuadro es diezmás el número de bolos derribados en su próximo lanzamiento (en su próximo turno ).

4.  Si en su primer intento en el marco derriba todos los pines, esto se llama un " golpe ". Su turno ha terminadoy su puntuación para el cuadro es diez más el total simple de los pines derribados en sus próximos dosrollos .

5.  Si obtiene un repuesto o strike en el último (décimo) cuadro , el lanzador puede lanzar uno o dos másbolas de bonificación , respectivamente. - Estos lanzamientos de bonificación se toman como parte del mismo turno. Si el bonotira derribar todos los pines, el proceso no se repite: los lanzamientos de bonificación solo se utilizan paracalcular la puntuación del fotograma final.

6.  La puntuación del juego es el total de todas las puntuaciones de fotogramas .Requisitos funcionales: qué NO hace el programa. Aquí hay algunas cosas que el programa no hará:
 No comprobaremos rollos válidos.
 No verificaremos el número correcto de rollos y marcos.
 No proporcionaremos puntajes para marcos intermedios

## Vocabulario del Dominio

### Game
Tenpin bowling is a type of bowling in which a bowler rolls a bowling ball down a wood or synthetic lane toward ten pins 
### Frames
Unit measuring the number of turns a bowler has in a game. There are 10 frames in a bowling game and bowlers get two throws, or attempts, to knock over the pins during each frame.
### Pins
Are the target of the bowling ball in various bowling games
### Game Score
It's the total score of a Bowling Game
### Spare
Knocking down the remaining pins on the second throw.
### Strike
Knocking over all 10 pins on the first throw.
### Open Frame
A turn in which the bowler fails to get a strike or spare.
