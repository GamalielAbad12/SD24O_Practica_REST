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
    return repo.obtener_calificaciones_alumno_id(id, sesion)


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
    print("Api hace una consulta de las calificaciones con el id de la calificación")
    return repo.obtener_calificaciones_id(id, sesion)


@app.delete("/fotos/{id}")
def eliminar_fotos_id(id:int, sesion:Session=Depends(generador_sesion)):
    print("Api elimina las fotos segun su id")
    fotos_eliminar = repo.obtener_fotos_id(id, sesion)
    if fotos_eliminar is not None: 
        for fotos_id in fotos_eliminar:
            id_alumno = fotos_id.id_alumno
            repo.eliminar_fotos_alumnos_id(id_alumno, sesion)
    
    return {"foto eliminada": "ok"}

@app.delete("/calificaciones/{id}")
def eliminar_clasificaciones_id(id:int, sesion:Session=Depends(generador_sesion)):
    calificaciones_eliminar = repo.obtener_calificaciones_id(id, sesion)
    if calificaciones_eliminar is not None: 
        for calificaciones in calificaciones_eliminar: 
            id_calificacion = calificaciones.id_alumno
            repo.eliminar_calificaciones_alumnos_id(id_calificacion, sesion)
    return {"calificaciones eliminadas": "ok"}

@app.delete("/alumnos/{id}/calificaciones")
def eliminar_calificaciones_alumno_id(id:int, sesion:Session=Depends(generador_sesion)):
    repo.eliminar_calificaciones_alumnos_id(id, sesion)
    return {"calificaciones alumno borradas":"ok"}
            
@app.delete("/alumnos/{id}/fotos")
def eliminar_fotos_alumnos_id(id:int, sesion:Session=Depends(generador_sesion)):
    repo.eliminar_fotos_alumnos_id(id, sesion)
    return {"fotos eliminadas de alumno": "ok"}

@app.delete("/alumnos/{id}")
def eliminar_alumnos_id(id:int, sesion:Session=Depends(generador_sesion)):
    repo.eliminar_calificaciones_alumno_id(id, sesion)
    repo.eliminar_fotos_alumnos_id(id, sesion)
    repo.eliminar_alumnos_id(id, sesion)

    return {"usuario eliminado" : "ok"}