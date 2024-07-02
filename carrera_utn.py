import pygame
import colores
from datos import lista
from funciones import *
pygame.init()
ANCHO_VENTANA = 1280
ALTO_VENTANA = 720

#crear una fuente
dict_fuentes={
    "fuente" : pygame.font.SysFont("Arial",30),
    "fuente_respuestas" : pygame.font.SysFont("Arial",20),
    "fuente_boost" : pygame.font.SysFont("Arial",10)
}
#props estado_de_juego



    
estado_de_juego = { 
    "pregunta" : "",
    "tema" : "",
    "score" : 0,
    "respuesta_a" : "",
    "respuesta_b" : "",
    "respuesta_c" : "",
    "contador" : 0,
    "respuesta_apretada" : "",
    "flag_siguiente_pregunta" : False,
    "flag_primera_ejecucion" : True,
    "respuestas_visibles" : False,
    "pos_personaje" : [0,0],
    "indice_pos_personaje" : 0,
    "segundos" : "5",
    "fin_tiempo" : False,
    "nombre_jugador" : "",
    "mostrar_scores":False,
    "guardado":False,
    "vista" : "juego",
    "lista_preguntas" : [],
    "lista_temas" : [],
    "lista_respuesta_a" : [],
    "lista_respuesta_b" : [],
    "lista_respuesta_c" : [],
    "lista_correctas" : []
}

for e_lista in lista:
    estado_de_juego["lista_preguntas"].append(e_lista["pregunta"])
    estado_de_juego["lista_temas"].append(e_lista["tema"])
    estado_de_juego["lista_respuesta_a"].append(e_lista["a"])
    estado_de_juego["lista_respuesta_b"].append(e_lista["b"])
    estado_de_juego["lista_respuesta_c"].append(e_lista["c"])
    estado_de_juego["lista_correctas"].append(e_lista["correcta"])

#casillas
DIFERENCIA = 80
DIFERENCIA_ALTO = 100
ANCHO_CASILLA = 75
ALTO_CASILLA = 75
INICIO = (300,340,75,75)
FIN = (INICIO[0],INICIO[1]+DIFERENCIA_ALTO,75,75)
#9x2
lista_casillas = [INICIO,(INICIO[0]+DIFERENCIA,INICIO[1],ANCHO_CASILLA,ALTO_CASILLA),
                    (INICIO[0]+DIFERENCIA*2,INICIO[1],ANCHO_CASILLA,ALTO_CASILLA),
                  (INICIO[0]+DIFERENCIA*3,INICIO[1],ANCHO_CASILLA,ALTO_CASILLA),
                  (INICIO[0]+DIFERENCIA*4,INICIO[1],ANCHO_CASILLA,ALTO_CASILLA),
                  (INICIO[0]+DIFERENCIA*5,INICIO[1],ANCHO_CASILLA,ALTO_CASILLA),
                  (INICIO[0]+DIFERENCIA*6,INICIO[1],ANCHO_CASILLA,ALTO_CASILLA),
                  (INICIO[0]+DIFERENCIA*7,INICIO[1],ANCHO_CASILLA,ALTO_CASILLA),
                  (INICIO[0]+DIFERENCIA*8,INICIO[1],ANCHO_CASILLA,ALTO_CASILLA),
                  (INICIO[0]+DIFERENCIA*8,INICIO[1] + DIFERENCIA_ALTO ,ANCHO_CASILLA,ALTO_CASILLA),
                  (INICIO[0]+DIFERENCIA*7,INICIO[1] + DIFERENCIA_ALTO ,ANCHO_CASILLA,ALTO_CASILLA),
                  (INICIO[0]+DIFERENCIA*6,INICIO[1] + DIFERENCIA_ALTO ,ANCHO_CASILLA,ALTO_CASILLA),
                  (INICIO[0]+DIFERENCIA*5,INICIO[1] + DIFERENCIA_ALTO ,ANCHO_CASILLA,ALTO_CASILLA),
                  (INICIO[0]+DIFERENCIA*4,INICIO[1] + DIFERENCIA_ALTO ,ANCHO_CASILLA,ALTO_CASILLA),
                  (INICIO[0]+DIFERENCIA*3,INICIO[1] + DIFERENCIA_ALTO ,ANCHO_CASILLA,ALTO_CASILLA),
                  (INICIO[0]+DIFERENCIA*2,INICIO[1] + DIFERENCIA_ALTO ,ANCHO_CASILLA,ALTO_CASILLA),
                  (INICIO[0]+DIFERENCIA,INICIO[1] + DIFERENCIA_ALTO ,ANCHO_CASILLA,ALTO_CASILLA),
                  FIN]
casillas_especiales = [{"numero":6,"boost":1},
                       {"numero":13,"boost":-1}]

#posiciones botones
    
# pos_siguiente_pregunta = (300,20,300,100)
ANCHO_RESPUESTA = ANCHO_VENTANA / 6
ALTO_RESPUESTA = 100
POS_CUADRO_RESPUESTAS = (300,30,950,250)
pos_comenzar = (ANCHO_VENTANA*0.5-300,570,220,100)
pos_terminar = (ANCHO_VENTANA*0.5+100,570,200,100)
pos_respuesta_A = (ANCHO_RESPUESTA*2,ALTO_RESPUESTA,ANCHO_RESPUESTA-10,100)
pos_respuesta_B = (ANCHO_RESPUESTA*3,ALTO_RESPUESTA,ANCHO_RESPUESTA-10,100)
pos_respuesta_C = (ANCHO_RESPUESTA*4,ALTO_RESPUESTA,ANCHO_RESPUESTA-10,100)


#posiciones de variables
pos_score = (ANCHO_RESPUESTA*5+20,100)
pos_score_variable = (ANCHO_RESPUESTA*5+20,150)
pos_tiempo = (ANCHO_RESPUESTA*5+20,200)
pos_tiempo_variable = (ANCHO_RESPUESTA*5+20,250)
pos_tema = (ANCHO_RESPUESTA*2,220)
pos_pregunta = (ANCHO_RESPUESTA*2,50)
pos_avanza = casillas_especiales[0]["numero"]
pos_retrocede = casillas_especiales[1]["numero"]

dict_textos={
    "TEXTO_SCORE" :{"texto": dict_fuentes["fuente"].render(str("SCORE"),True,colores.BLACK),"pos":pos_score},
    "TEXTO_COMENZAR" :{"texto": dict_fuentes["fuente"].render(str("COMENZAR"),True,colores.BLACK),"pos":(pos_comenzar[0]+20,
                                                                                        pos_comenzar[1]+30)},
    "TEXTO_TERMINAR" :{"texto": dict_fuentes["fuente"].render(str("TERMINAR"),True,colores.BLACK),"pos":(pos_terminar[0]+20,
                                                                                        600)},
    "TEXTO_TIEMPO" :{"texto": dict_fuentes["fuente"].render(str("TIEMPO"),True,colores.BLACK),"pos":pos_tiempo},
    "TEXTO_AVANZA" :{"texto": dict_fuentes["fuente_boost"].render(str("Avanza 1"),True,colores.BLACK),"pos":pos_avanza},
    "TEXTO_RETROCEDE" :{"texto": dict_fuentes["fuente_boost"].render(str("Retrocede 1"),True,colores.BLACK),"pos":pos_retrocede},
    "texto_tema":{"texto" :  dict_fuentes["fuente"].render(str("tema"),True,colores.COLOR_AMARILLO),"pos":pos_tema},
    "texto_pregunta":{"texto" :  dict_fuentes["fuente"].render(str("pregunta"),True,colores.BLACK),"pos":pos_pregunta},
    "texto_score_variable":{"texto" : dict_fuentes["fuente"].render(str(estado_de_juego["score"]),True,colores.BLACK),"pos":pos_score_variable},
    "texto_tiempo_variable":{"texto" :  dict_fuentes["fuente"].render(str(estado_de_juego["segundos"]),True,colores.BLACK),"pos":pos_tiempo_variable},
    "texto_respuesta_a":{"texto" : dict_fuentes["fuente_respuestas"].render(str("A"),True,colores.COLOR_AMARILLO),"pos":pos_respuesta_A},
    "texto_respuesta_b":{"texto" : dict_fuentes["fuente_respuestas"].render(str("B"),True,colores.COLOR_AMARILLO),"pos":pos_respuesta_B},
    "texto_respuesta_c":{"texto" : dict_fuentes["fuente_respuestas"].render(str("C"),True,colores.COLOR_AMARILLO),"pos":pos_respuesta_C},
    "CUADRO_RESPUESTAS":{"texto":"","pos":POS_CUADRO_RESPUESTAS},
    "CUADRO_COMENZAR":{"texto":"","pos":pos_comenzar},
    "CUADRO_TERMINAR":{"texto":"","pos":pos_terminar},
    "CUADRO_RESPUESTA_A":{"texto":"","pos":pos_respuesta_A},
    "CUADRO_RESPUESTA_B":{"texto":"","pos":pos_respuesta_B},
    "CUADRO_RESPUESTA_C":{"texto":"","pos":pos_respuesta_C}
}





    

    

#timer
timer_segundos = pygame.USEREVENT
pygame.time.set_timer(timer_segundos,1000)





#crear la pantalla
pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("Carrera UTN")

flag_correr = True
while flag_correr:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_correr = False
        if evento.type == pygame.USEREVENT:
            if evento.type == timer_segundos:
                if not estado_de_juego["flag_primera_ejecucion"]:
                    if estado_de_juego["fin_tiempo"] == False:
                        estado_de_juego["segundos"] = int(estado_de_juego["segundos"]) - 1
                    if int(estado_de_juego["segundos"]) == 0:
                        estado_de_juego["flag_siguiente_pregunta"] = True
        if evento.type == pygame.KEYDOWN:
            if estado_de_juego["fin_tiempo"] == True:
                if evento.key == pygame.K_BACKSPACE:
                    estado_de_juego["nombre_jugador"] = estado_de_juego["nombre_jugador"][0:-1]
                    print(estado_de_juego["nombre_jugador"])
                elif evento.key == pygame.K_RETURN:
                    estado_de_juego["mostrar_scores"] = True
                elif estado_de_juego["fin_tiempo"] == True:
                    estado_de_juego["nombre_jugador"] += evento.unicode 
                    print(estado_de_juego["nombre_jugador"])
        if evento.type == pygame.MOUSEBUTTONDOWN:
            
            if chequear_click_en_rect(evento.pos,pos_respuesta_A):
                if estado_de_juego["respuestas_visibles"]: 
                    cambiar_respuesta_apretada(estado_de_juego,"respuesta_apretada",
                                               'a',"flag_siguiente_pregunta")
            elif chequear_click_en_rect(evento.pos,pos_respuesta_B):
                if estado_de_juego["respuestas_visibles"]:
                    cambiar_respuesta_apretada(estado_de_juego,"respuesta_apretada",
                                               'b',"flag_siguiente_pregunta")
            elif chequear_click_en_rect(evento.pos,pos_respuesta_C):
                if estado_de_juego["respuestas_visibles"]:
                    cambiar_respuesta_apretada(estado_de_juego,"respuesta_apretada",
                                               'c',"flag_siguiente_pregunta")
            if estado_de_juego["lista_correctas"][estado_de_juego["contador"]] == estado_de_juego["respuesta_apretada"]:
                estado_de_juego["score"] += 10
                if(estado_de_juego["indice_pos_personaje"] + 2 >= len(lista_casillas)):
                    #fin juego
                    estado_de_juego["indice_pos_personaje"] = len(lista_casillas) - 1
                    frenar_juego(estado_de_juego)
                    print("GANASTE")
                elif verificar_casilla_especial(estado_de_juego,casillas_especiales) != 0 : 
                    # print("pasa por una casilla especial")
                    estado_de_juego["indice_pos_personaje"] += 2
                else:
                    estado_de_juego["indice_pos_personaje"] += 2
            elif estado_de_juego["respuesta_apretada"] != '' :
                if estado_de_juego["indice_pos_personaje"] - 1 <= 0:
                    frenar_juego(estado_de_juego)
                    # terminar_juego(estado_de_juego,pygame,pantalla,colores)
                else:
                    estado_de_juego["indice_pos_personaje"] -= 1
            if chequear_click_en_rect(evento.pos,pos_terminar):
                frenar_juego(estado_de_juego)
                # terminar_juego(estado_de_juego,pygame,pantalla,colores)
            if chequear_click_en_rect(evento.pos,pos_comenzar):
                reiniciar_estado_juego(estado_de_juego)
                if estado_de_juego["flag_primera_ejecucion"]:
                    estado_de_juego["flag_primera_ejecucion"] = False
                estado_de_juego["respuestas_visibles"] = True
            
                
        estado_de_juego["respuesta_apretada"] = ""            
    pantalla.fill(colores.BLUE)
    
    ##control siguiente pregunta
    if estado_de_juego["flag_siguiente_pregunta"]:
        if estado_de_juego["contador"] == len(estado_de_juego["lista_preguntas"])-1:
                frenar_juego(estado_de_juego)
                # terminar_juego(estado_de_juego,pygame,pantalla,colores)

        else:
            estado_de_juego["contador"] += 1
        estado_de_juego["respuesta_apretada"] = "" 
        estado_de_juego["flag_siguiente_pregunta"] = False
        estado_de_juego["segundos"] = "5"

    #movimiento personaje
    boost = verificar_casilla_especial(estado_de_juego,casillas_especiales) 
    estado_de_juego["indice_pos_personaje"] += boost
    estado_de_juego["pos_personaje"] = list(lista_casillas[estado_de_juego["indice_pos_personaje"]])     


# vistas = [{"nombre":"juego"},{"nombre":"nombre"},{"nombre":"puntajes"}]
    print(estado_de_juego["vista"])
    match estado_de_juego["vista"]:
        case "juego":
            mostrar_juego(estado_de_juego,pygame,pantalla,colores,dict_textos,
                          lista_casillas,dict_fuentes)
        case "nombre":
            pass
        case "puntajes":
            pass
    if estado_de_juego["fin_tiempo"]:                          
        terminar_juego(estado_de_juego,pygame,pantalla,colores)
    pygame.display.flip()
    
pygame.quit()

