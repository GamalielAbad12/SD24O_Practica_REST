from fastapi import FastAPI, Depends;
from sqlalchemy.orm import Session
from orm.config import generador_sesion
import orm.repo as repo

app = FastAPI()

@app.get("/")
def bienvenida():
    respuesta = {
        "Todo está bien" : "El servidor ha sido levantado"
    }
    return respuesta


@app.get("/alumnos")
def obtener_alumnos(sesion:Session=Depends(generador_sesion)):
    print("Api hace una consulta de usuarios")
    return repo.obtener_alumnos(sesion) 

@app.get("/alumnos/{id}")
def obtener_alumnos_id(id:int, sesion: Session=Depends(generador_sesion)):
    print("Api hace una consulta de usuarios por id")
    return repo.obtener_alumnos_id(id,sesion)


@app.get("/alumnos/{id}/calificaciones")
def obtener_calificaciones_alumnos_id(id:int, sesion: Session=Depends(generador_sesion)):
    print("Api hace una consulta de las calificaciones por id de alumno")
    return repo.obtener_calificaciones_alumnos_id(id, sesion)


@app.get("/alumnos/{id}/fotos")
def obtener_fotos_alumnos_id(id:int, sesion:Session=Depends(generador_sesion)):
    print("Api hace una consulta de las fotos del alumno por id de alumno")
    return repo.obtener_fotos_alumnos_id(id, sesion)


@app.get("/fotos/{id}")
def obtener_fotos_id(id:int, sesion:Session=Depends(generador_sesion)):
    print("Api hace una consulta de las fotos con el id de la foto")
    return repo.obtener_fotos_id(id, sesion)


@app.get("/calificaciones/{id}")
def obtener_calificaciones_id(id:int, sesion:Session=Depends(generador_sesion)):
    print("Api hace una consulta de las calificaciones con el id de la calificacion")
    return 


"""
@app.delete("/fotos/{id}")
def eliminar_fotos_id(id:int):

@app.delete("/calificaciones/{id}")
def eliminar_clasificaciones_id(id:int):

@app.delete("/alumnos/{id}/calificaciones)

@app.delete("/alumnos/{id}/fotos")
def eliminar_fotos_alumnos_id(id:int):

@app.delete("/alumnos/{id}")
def eliminar_alumnos_id(id:int):

"""
