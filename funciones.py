from funciones_archivos import *
from copy import deepcopy
def chequear_click_en_rect(posicion_click:tuple,item_rect:tuple):
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
     
def reiniciar_estado_juego(estado_juego:dict,lista_casillas:list):
     '''
     funcion especifica a carrera_utn para reiniciar el estado de juego
     '''
     estado_juego["respuestas_visibles"] = True
     estado_juego["contador"] = 0
     estado_juego["flag_siguiente_pregunta"] = False
     estado_juego["respuesta_apretada"] = ""
     estado_juego["score"] = 0
     estado_juego["segundos"] = '5'
     # estado_juego["pos_personaje"] = list(lista_casillas[0])
     estado_juego["indice_pos_personaje"] = 0
     estado_juego["fin_tiempo"] = False
     
     
def actualizar_textos(estado_juego:dict,listas:dict,fuente,fuente_respuestas,colores,textos):
     '''
     funcion especifica a carrera_utn para actualizar los textos    
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
                         aux_puntajes.append({"nombre":estado_juego["nombre_jugador"],
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