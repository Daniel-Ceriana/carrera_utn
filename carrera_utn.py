import pygame
import colores
from datos import lista
from funciones import *
pygame.init()
ANCHO_VENTANA = 1280
ALTO_VENTANA = 720

#crear una fuente
fuente = pygame.font.SysFont("Arial",30)
fuente_respuestas = pygame.font.SysFont("Arial",20)
fuente_boost = pygame.font.SysFont("Arial",10)
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
    "guardado":False
}

TEXTO_SCORE = fuente.render(str("SCORE"),True,colores.BLACK)
TEXTO_COMENZAR = fuente.render(str("COMENZAR"),True,colores.BLACK)
TEXTO_TERMINAR = fuente.render(str("TERMINAR"),True,colores.BLACK)
TEXTO_TIEMPO = fuente.render(str("TIEMPO"),True,colores.BLACK)

TEXTO_AVANZA = fuente_boost.render(str("Avanza 1"),True,colores.BLACK)
TEXTO_RETROCEDE = fuente_boost.render(str("Retrocede 1"),True,colores.BLACK)

dict_textos={
    "texto_tema" : fuente.render(str("tema"),True,colores.COLOR_AMARILLO),
    "texto_pregunta" : fuente.render(str("pregunta"),True,colores.BLACK),
    "texto_score_variable" : fuente.render(str(estado_de_juego["score"]),True,colores.BLACK),
    "texto_tiempo_variable" : fuente.render(str(estado_de_juego["segundos"]),True,colores.BLACK),
    "texto_respuesta_a" : fuente_respuestas.render(str("A"),True,colores.COLOR_AMARILLO),
    "texto_respuesta_b" : fuente_respuestas.render(str("B"),True,colores.COLOR_AMARILLO),
    "texto_respuesta_c" : fuente_respuestas.render(str("C"),True,colores.COLOR_AMARILLO)
}




lista_preguntas = []
lista_temas = []
lista_respuesta_a = []
lista_respuesta_b = []
lista_respuesta_c = []
lista_correctas = []
for e_lista in lista:
    lista_preguntas.append(e_lista["pregunta"])
    lista_temas.append(e_lista["tema"])
    lista_respuesta_a.append(e_lista["a"])
    lista_respuesta_b.append(e_lista["b"])
    lista_respuesta_c.append(e_lista["c"])
    lista_correctas.append(e_lista["correcta"])
    
#personaje
personaje = pygame.image.load("personaje.png")
personaje = pygame.transform.scale(personaje,(100,100))
    
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
#timer
timer_segundos = pygame.USEREVENT
pygame.time.set_timer(timer_segundos,1000)
#cargar logo
imagen = pygame.image.load("logo_carrera_de_mente.png")
imagen = pygame.transform.scale(imagen,(200,200))
imagen_utn = pygame.image.load("Logo-utn.png")
imagen_utn = pygame.transform.scale(imagen_utn,(90,45))



#posiciones botones
    
# pos_siguiente_pregunta = (300,20,300,100)
pos_comenzar = (ANCHO_VENTANA*0.5-300,570,220,100)
pos_terminar = (ANCHO_VENTANA*0.5+100,570,200,100)
ANCHO_RESPUESTA = ANCHO_VENTANA / 6
ALTO_RESPUESTA = 100
pos_respuesta_A = (ANCHO_RESPUESTA*2,ALTO_RESPUESTA,ANCHO_RESPUESTA-10,100)
pos_respuesta_B = (ANCHO_RESPUESTA*3,ALTO_RESPUESTA,ANCHO_RESPUESTA-10,100)
pos_respuesta_C = (ANCHO_RESPUESTA*4,ALTO_RESPUESTA,ANCHO_RESPUESTA-10,100)
POS_CUADRO_RESPUESTAS = (300,30,950,250)


#posiciones de variables
pos_puntaje = (ANCHO_RESPUESTA*5+20,100)
pos_puntaje_variable = (ANCHO_RESPUESTA*5+20,150)
pos_tiempo = (ANCHO_RESPUESTA*5+20,200)
pos_tiempo_variable = (ANCHO_RESPUESTA*5+20,250)
pos_tema = (ANCHO_RESPUESTA*2,220)
pos_pregunta = (ANCHO_RESPUESTA*2,50)
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
            if lista_correctas[estado_de_juego["contador"]] == estado_de_juego["respuesta_apretada"]:
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
                reiniciar_estado_juego(estado_de_juego,lista_casillas)
                if estado_de_juego["flag_primera_ejecucion"]:
                    estado_de_juego["flag_primera_ejecucion"] = False
                estado_de_juego["respuestas_visibles"] = True
            
                
        estado_de_juego["respuesta_apretada"] = ""            
    pantalla.fill(colores.BLUE)
    
    ##control siguiente pregunta
    if estado_de_juego["flag_siguiente_pregunta"]:
        if estado_de_juego["contador"] == len(lista_preguntas)-1:
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

        #realizar todos los cambios de texto
    if not estado_de_juego["flag_primera_ejecucion"]:
        actualizar_textos(estado_de_juego,{
                              "lista_preguntas":lista_preguntas,
                                "lista_temas":lista_temas,
                                "lista_respuesta_a":lista_respuesta_a,
                                "lista_respuesta_b":lista_respuesta_b,
                                "lista_respuesta_c":lista_respuesta_c},
                          fuente,fuente_respuestas,colores,dict_textos)
        
    if not estado_de_juego["fin_tiempo"]:                      
        #botones
            #fijos    
        pygame.draw.rect(pantalla,colores.COLOR_AMARILLO,pos_comenzar)
        pygame.draw.rect(pantalla,colores.COLOR_AMARILLO,pos_terminar)
        pygame.draw.rect(pantalla,colores.SKYBLUE4,POS_CUADRO_RESPUESTAS)
        
        ###casillas
        lista_colores = [colores.ORANGE,colores.GREEN,colores.SKYBLUE4,
                        colores.RED1,colores.VIOLET,colores.ORANGE,
                        colores.YELLOW1,colores.GREEN]
        indice = 0
        for pos in lista_casillas:
            pygame.draw.rect(pantalla,lista_colores[indice],pos)
            indice += 1
            if indice >= len(lista_colores):
                indice = 0
            
            
        #Fundir textos
        pantalla.blit(TEXTO_SCORE,(pos_puntaje))
        pantalla.blit(dict_textos["texto_score_variable"],
                                    (pos_puntaje_variable))
        pantalla.blit(dict_textos["texto_tema"],pos_tema)
        pantalla.blit(dict_textos["texto_pregunta"],pos_pregunta)
        pantalla.blit(TEXTO_TIEMPO,pos_tiempo)
        pantalla.blit(dict_textos["texto_tiempo_variable"],pos_tiempo_variable)
        
        pantalla.blit(TEXTO_AVANZA,lista_casillas[casillas_especiales[0]["numero"]])
        pantalla.blit(TEXTO_RETROCEDE,lista_casillas[casillas_especiales[1]["numero"]])
            #preguntas/respuestas
    
            #botones
        pantalla.blit(TEXTO_COMENZAR,(pos_comenzar[0]+20,
                                            pos_comenzar[1]+30))
        pantalla.blit(TEXTO_TERMINAR,(pos_terminar[0]+20,
                                            600))
                #respuestas
        if estado_de_juego["respuestas_visibles"]:
            pygame.draw.rect(pantalla,colores.COLOR_AMARILLO,pos_respuesta_A,5)
            pantalla.blit(dict_textos["texto_respuesta_a"],(pos_respuesta_A[0]+15
                                        ,pos_respuesta_A[1]+35))
            pygame.draw.rect(pantalla,colores.COLOR_AMARILLO,pos_respuesta_B,5)
            pantalla.blit(dict_textos["texto_respuesta_b"],(pos_respuesta_B[0]+15
                                        ,pos_respuesta_B[1]+35))
            pygame.draw.rect(pantalla,colores.COLOR_AMARILLO,pos_respuesta_C,5)  
            pantalla.blit(dict_textos["texto_respuesta_c"],(pos_respuesta_C[0]+15
                                        ,pos_respuesta_C[1]+35))
        
        pantalla.blit(imagen,(10,10))
        pantalla.blit(imagen_utn,(64,100))
        
        pantalla.blit(personaje,estado_de_juego["pos_personaje"])
    else:
        terminar_juego(estado_de_juego,pygame,pantalla,colores)
    pygame.display.flip()
    
pygame.quit()

