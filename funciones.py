from funciones_archivos import *
from copy import deepcopy
def chequear_click_en_rect(posicion_click:tuple,item_rect:tuple)->bool:
     '''
     chequea que el click haya sido en un area determinada
     Parametros: posicion_click:tuple
                    item_rect:tuple
     Retorno: bool => True si cliquea en el rect, False si no
     '''
     if ((posicion_click[0] > item_rect[0] and 
          posicion_click[0] < item_rect[0]+item_rect[2])
          and (posicion_click[1] > item_rect[1] and 
               posicion_click[1] < item_rect[1] + item_rect[3])):
                    return True
     return False

def cambiar_respuesta_apretada(estado_juego:dict,key_respuesta_apretada:str,
                               respuesta:str,key_flag_siguiente_pregunta:str):
     estado_juego[key_respuesta_apretada] = respuesta
     estado_juego[key_flag_siguiente_pregunta] = True
     
def reiniciar_estado_juego(estado_juego:dict):
     '''
     funcion especifica a carrera_utn para reiniciar el estado de juego
     Parametros: estado_juego:dict => variables de entorno de juego
     Retorno: No
     '''
     estado_juego["respuestas_visibles"] = True
     estado_juego["contador"] = 0
     estado_juego["flag_siguiente_pregunta"] = False
     estado_juego["respuesta_apretada"] = ""
     estado_juego["score"] = 0
     estado_juego["segundos"] = '5'
     estado_juego["indice_pos_personaje"] = 0
     estado_juego["fin_tiempo"] = False
     
     
def actualizar_textos(estado_juego:dict,listas:dict,fuente,fuente_respuestas,colores,textos):
     '''
     funcion especifica a carrera_utn para actualizar los textos
     Parametros: estado_juego:dict => variables de entorno de juego
               listas:dict => 
               fuente => fuente para los render
               fuente_respuestas => fuente para los render de respuesta
               colores => constantes colores
               textos => textos a renderizar
     Retorno: No    
     '''
     estado_juego["pregunta"] = listas["lista_preguntas"][estado_juego["contador"]]
     estado_juego["tema"] = listas["lista_temas"][estado_juego["contador"]]
     estado_juego["respuesta_a"] = listas["lista_respuesta_a"][estado_juego["contador"]]
     estado_juego["respuesta_b"] = listas["lista_respuesta_b"][estado_juego["contador"]]
     estado_juego["respuesta_c"] = listas["lista_respuesta_c"][estado_juego["contador"]]
     textos["texto_tema"] = fuente.render(str(estado_juego["tema"]),True,colores.COLOR_AMARILLO)
     textos["texto_pregunta"] = fuente.render(str(estado_juego["pregunta"]),True,colores.BLACK)
     textos["texto_respuesta_a"] = fuente_respuestas.render(str(estado_juego["respuesta_a"]),True,colores.COLOR_AMARILLO)
     textos["texto_respuesta_b"] = fuente_respuestas.render(str(estado_juego["respuesta_b"]),True,colores.COLOR_AMARILLO)
     textos["texto_respuesta_c"] = fuente_respuestas.render(str(estado_juego["respuesta_c"]),True,colores.COLOR_AMARILLO)
     textos["texto_score_variable"] = fuente.render(str(estado_juego["score"]),True,colores.BLACK)
     textos["texto_tiempo_variable"] = fuente.render(str(estado_juego["segundos"]),True,colores.BLACK)
     
def frenar_juego(estado_juego:dict):
     '''
     funcion especifica a carrera_utn para frenar el estado de juego
     Parametros: estado_juego:dict => variables de entorno de juego
     Retorno: No
     '''
     estado_juego["respuestas_visibles"] = False
     # estado_juego["contador"] = 0
     estado_juego["flag_siguiente_pregunta"] = False
     estado_juego["respuesta_apretada"] = ""
     # estado_juego["score"] = 0
     estado_juego["segundos"] = '5'
     # estado_juego["indice_pos_personaje"] = 0
     estado_juego["fin_tiempo"] = True
     
def mostrar_puntajes(lista_puntajes:list,pygame,pantalla,colores):
     '''
     Mostrar los puntajes en pantalla
     Parametros:  lista_puntajes => lista con todos los puntajes
               pygame => objeto pygame
               pantalla => lugar donde pintar
               colores => constantes colores
     Retorno:
     '''
     alto_base_puntajes = 200
     POS_PUNTAJES = [400,100,100,100]
     pos_puntajes = [800,alto_base_puntajes,100,100]
     POS_NOMBRES = [400,alto_base_puntajes,100,100]
     
     
     fuente = pygame.font.SysFont("Arial",30)
     
     PUNTAJES = fuente.render(str("PUNTAJES"),True,colores.BLACK)
     pantalla.blit(PUNTAJES,POS_PUNTAJES)

     
     if len(lista_puntajes)>0:
          for item in lista_puntajes:
               nombre = fuente.render(str(item["nombre"]),True,colores.BLACK)
               score = fuente.render(str(item["score"]),True,colores.BLACK)
               pantalla.blit(nombre,POS_NOMBRES)
               pantalla.blit(score,pos_puntajes)
               pos_puntajes[1] += 50
               POS_NOMBRES[1] += 50
               
def terminar_juego(estado_juego:dict,pygame,pantalla,colores):
     '''
     termina el juego y guarda el score
     Parametros: estado_juego:dict => variables de entorno de juego
               pygame => objeto pygame
               pantalla => lugar donde pintar
               colores => constantes colores

     Retorno: No
     '''
     aux_guardar_ordenado = []
     
     fuente = pygame.font.SysFont("Arial",30)
     TEXTO_FINALIZADO = fuente.render(str("JUEGO FINALIZADO, SU PUNTAJE:"),True,colores.BLACK)
     PUNTAJE_FINALIZADO = fuente.render(str(estado_juego["score"]),True,colores.BLACK)
     TEXTO_INGRESE_NOMBRE = fuente.render(str("Ingrese su nombre:"),True,colores.BLACK)
     TEXTO_NOMBRE = fuente.render(str(estado_juego["nombre_jugador"]),True,colores.BLACK)
     

     POS_FINALIZADO = (100,100,100,100)
     POS_PUNTAJE_FINALIZADO = (800,100)
     POS_INGRESE_NOMBRE = (500,400)
     POS_INGRESE_NOMBRE_VARIABLE = (550,500)
     if not estado_juego["mostrar_scores"]:
          # pos_texto_finalizado
          pygame.draw.rect(pantalla,colores.COLOR_AMARILLO,(
               POS_INGRESE_NOMBRE_VARIABLE[0]-75,
               POS_INGRESE_NOMBRE_VARIABLE[1]-30,
               300,100),5)
          pantalla.blit(TEXTO_FINALIZADO,POS_FINALIZADO)
          pantalla.blit(PUNTAJE_FINALIZADO,POS_PUNTAJE_FINALIZADO)
          pantalla.blit(TEXTO_INGRESE_NOMBRE,POS_INGRESE_NOMBRE)
          pantalla.blit(TEXTO_NOMBRE,POS_INGRESE_NOMBRE_VARIABLE)
     else:
          try:
               puntajes = leer_json_lista("scores.json")
          except:
               print('Ocurrio un error al leer el archivo de scores')
          if not estado_juego["guardado"]:
               try:
                    if puntajes:
                         aux_puntajes = deepcopy(puntajes)
                         if len(estado_juego["nombre_jugador"])>0:
                              aux_puntajes.append({"nombre":estado_juego["nombre_jugador"],
                                                  "score":estado_juego["score"]})
                         else:
                              aux_puntajes.append({"nombre":"NOMBRE_DESCONOCIDO",
                              "score":estado_juego["score"]})
                         aux_puntajes.sort(key=lambda item : int(item["score"]), reverse=True)
                         i = 0
                         for item in aux_puntajes:
                              if i < 10:
                                   aux_guardar_ordenado.append(item)
                              i += 1
                         guardar_json_lista("scores.json",aux_guardar_ordenado)
                         estado_juego["guardado"] = True
               except:
                 print('Ocurrio un error al guardar el archivo de scores')
          else:
               mostrar_puntajes(puntajes,pygame,pantalla,colores)   
                 
               

     
     
     
def verificar_casilla_especial(estado_juego:list,lista_casillas_especiales:list):
     '''
     devuelve el boost, si es 0 es porque no tiene
     '''
     boost = 0
     pos_personaje = estado_juego["indice_pos_personaje"]
     for item in lista_casillas_especiales:
          if pos_personaje == item["numero"]:
               boost = item["boost"]
     return boost

def mostrar_textos(pantalla,textos):
    for key in textos.keys():
        pantalla.blit(textos[key]["texto"],textos[key]["pos"])
    
def mostrar_juego(estado_de_juego,pygame,pantalla,colores,
                  dict_textos,lista_casillas,dict_fuentes):
     print("asasda")
             #realizar todos los cambios de texto
     if not estado_de_juego["flag_primera_ejecucion"]:
          actualizar_textos(estado_de_juego,{
                              "lista_preguntas":estado_de_juego["lista_preguntas"],
                                "lista_temas":estado_de_juego["lista_temas"],
                                "lista_respuesta_a":estado_de_juego["lista_respuesta_a"],
                                "lista_respuesta_b":estado_de_juego["lista_respuesta_b"],
                                "lista_respuesta_c":estado_de_juego["lista_respuesta_c"]},
                          dict_fuentes["fuente"],dict_fuentes["fuente_respuestas"],colores,dict_textos)
        
     
     #cargar logo
     imagen = pygame.image.load("logo_carrera_de_mente.png")
     imagen = pygame.transform.scale(imagen,(200,200))
     imagen_utn = pygame.image.load("Logo-utn.png")
     imagen_utn = pygame.transform.scale(imagen_utn,(90,45))
     
     pygame.draw.rect(pantalla,colores.COLOR_AMARILLO,dict_textos["CUADRO_COMENZAR"]["pos"])
     pygame.draw.rect(pantalla,colores.COLOR_AMARILLO,dict_textos["CUADRO_TERMINAR"]["pos"])
     pygame.draw.rect(pantalla,colores.SKYBLUE4,dict_textos["CUADRO_RESPUESTAS"]["pos"])
     
     #personaje
     personaje = pygame.image.load("personaje.png")
     personaje = pygame.transform.scale(personaje,(100,100))
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
     pantalla.blit(dict_textos["TEXTO_SCORE"]["texto"],dict_textos["TEXTO_SCORE"]["pos"])
     pantalla.blit(dict_textos["texto_score_variable"]["texto"],
                                   dict_textos["texto_score_variable"]["pos"])
     pantalla.blit(dict_textos["texto_tema"]["texto"],dict_textos["texto_tema"]["pos"])
     pantalla.blit(dict_textos["texto_pregunta"]["texto"],dict_textos["texto_pregunta"]["pos"])
     pantalla.blit(dict_textos["TEXTO_TIEMPO"]["texto"],dict_textos["TEXTO_TIEMPO"]["pos"])
     pantalla.blit(dict_textos["texto_tiempo_variable"]["texto"],dict_textos["texto_tiempo_variable"]["pos"])
     
     pantalla.blit(dict_textos["TEXTO_AVANZA"]["texto"],dict_textos["TEXTO_AVANZA"]["pos"])
     pantalla.blit(dict_textos["TEXTO_RETROCEDE"]["texto"],dict_textos["TEXTO_RETROCEDE"]["pos"])
          #preguntas/respuestas

          #botones
     pantalla.blit(dict_textos["TEXTO_COMENZAR"]["texto"],
                   dict_textos["TEXTO_COMENZAR"]["pos"])
     pantalla.blit(dict_textos["TEXTO_TERMINAR"]["texto"],
                   dict_textos["TEXTO_TERMINAR"]["pos"])
               #respuestas
     if estado_de_juego["respuestas_visibles"]:
          pygame.draw.rect(pantalla,colores.COLOR_AMARILLO,dict_textos["CUADRO_RESPUESTA_A"]["pos"],5)
          pantalla.blit(dict_textos["texto_respuesta_a"],(dict_textos["texto_respuesta_a"]["pos"][0]+15
                                   ,dict_textos["texto_respuesta_a"]["pos"][1]+35))
          pygame.draw.rect(pantalla,colores.COLOR_AMARILLO,dict_textos["CUADRO_RESPUESTA_B"]["pos"],5)
          pantalla.blit(dict_textos["texto_respuesta_b"],(dict_textos["texto_respuesta_b"]["pos"][0]+15
                                   ,dict_textos["texto_respuesta_b"]["pos"][1]+35))
          pygame.draw.rect(pantalla,colores.COLOR_AMARILLO,dict_textos["CUADRO_RESPUESTA_C"]["pos"],5)  
          pantalla.blit(dict_textos["texto_respuesta_c"],(dict_textos["texto_respuesta_c"]["pos"][0]+15
                                   ,dict_textos["texto_respuesta_c"]["pos"][1]+35))
     
     pantalla.blit(imagen,(10,10))
     pantalla.blit(imagen_utn,(64,100))
     
     pantalla.blit(personaje,estado_de_juego["pos_personaje"])