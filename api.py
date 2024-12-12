from fastapi import FastAPI, Depends;
from sqlalchemy.orm import Session
from orm.config import generador_sesion
import orm.repo as repo
import orm.esquemas as esquemas

app = FastAPI()

# Ruta raíz que devuelve un mensaje de bienvenida    
@app.get("/")
def bienvenida():
    respuesta = {
        "Todo está bien" : "El servidor ha sido levantado"
    }
    return respuesta

# Devuelve la lista de todos los alumnos
@app.get("/alumnos")
def obtener_alumnos(sesion:Session=Depends(generador_sesion)):
    print("Api hace una consulta de usuarios")
    return repo.obtener_alumnos(sesion) 

# Devuelve un alumno específico por su ID
@app.get("/alumnos/{id}")
def obtener_alumnos_id(id:int, sesion: Session=Depends(generador_sesion)):
    print("Api hace una consulta de usuarios por id")
    return repo.obtener_alumnos_id(id,sesion)

# Devuelve las calificaciones de un alumno específico por su ID
@app.get("/alumnos/{id}/calificaciones")
def obtener_calificaciones_alumnos_id(id:int, sesion: Session=Depends(generador_sesion)):
    print("Api hace una consulta de las calificaciones por id de alumno")
    return repo.obtener_calificaciones_alumnos_id(id, sesion)

# Devuelve las fotos de un alumno específico por su ID
@app.get("/alumnos/{id}/fotos")
def obtener_fotos_alumnos_id(id:int, sesion:Session=Depends(generador_sesion)):
    print("Api hace una consulta de las fotos del alumno por id de alumno")
    return repo.obtener_fotos_alumnos_id(id, sesion)

# Devuelve una foto específica por su ID
@app.get("/fotos/{id}")
def obtener_fotos_id(id:int, sesion:Session=Depends(generador_sesion)):
    print("Api hace una consulta de las fotos con el id de la foto")
    return repo.obtener_fotos_id(id, sesion)

# Devuelve una calificación específica por su ID
@app.get("/calificaciones/{id}")
def obtener_calificaciones_id(id:int, sesion:Session=Depends(generador_sesion)):
    print("Api hace una consulta de las calificaciones con el id de la calificación")
    return repo.obtener_calificaciones_id(id, sesion)

# Elimina una foto específica por su ID
@app.delete("/fotos/{id}")
def eliminar_fotos_id(id:int, sesion:Session=Depends(generador_sesion)):
    print("Api elimina las fotos por id")
    return repo.eliminar_fotos_id(id, sesion)
    
# Elimina una calificación específica por su ID
@app.delete("/calificaciones/{id}")
def eliminar_calificaciones_id(id:int, sesion:Session=Depends(generador_sesion)):
    print("Api eleimina la calificacion por id")
    return repo.eliminar_calificaciones_id(id, sesion)

# Elimina todas las calificaciones de un alumno específico por su ID
@app.delete("/alumnos/{id}/calificaciones")
def eliminar_calificaciones_alumnos_id(id:int, sesion:Session=Depends(generador_sesion)):
    return repo.eliminar_calificaciones_alumnos_id(id, sesion)
    
# Elimina todas las fotos de un alumno específico por su ID
@app.delete("/alumnos/{id}/fotos")
def eliminar_fotos_alumnos_id(id:int, sesion:Session=Depends(generador_sesion)):
    return repo.eliminar_fotos_alumnos_id(id, sesion)

# Elimina un alumno específico por su ID
@app.delete("/alumnos/{id}")
def eliminar_alumnos_id(id:int, sesion:Session=Depends(generador_sesion)):
    return repo.eliminar_alumnos_id(id, sesion)

@app.post("/alumnos")
def agregar_alumnos(nuevo_alumno: esquemas.alumnoBase, sesion: Session=Depends(generador_sesion)):
    return repo.agregar_alumnos(nuevo_alumno, sesion)

@app.put("/alumnos/{id}")
def actualizar_alumno_id(id:int, alumno_actu: esquemas.alumnoBase, sesion: Session=Depends(generador_sesion)):
    return repo.actualizar_alumnos_id(id, alumno_actu, sesion)

@app.post("/alumnos/{id}/calificaciones")
def agregar_calificacion_alumno_id(id:int, nueva_calificacion: esquemas.calificacionBase, sesion: Session=Depends(generador_sesion)):
    return repo.agregar_calificacion_alumno_id(id, nueva_calificacion, sesion)

@app.put("/calificaciones/{id}")
def actualizar_calificaciones_id(id:int, calificacion_actu: esquemas.calificacionBase, sesion: Session=Depends(generador_sesion)):
    return repo.actualizar_calificaciones_id(id, calificacion_actu, sesion)

@app.post("/alumnos/{id}/fotos")
def agregar_fotos_alumnos_id(id:int, nueva_fotos: esquemas.fotoBase, sesion: Session=Depends(generador_sesion)):
    return repo.agregar_fotos_alumnos_id(id, nueva_fotos, sesion)

@app.put("/fotos/{id}")
def actualizar_fotos_id(id:int, foto_actu: esquemas.fotoBase, sesion: Session=Depends(generador_sesion)):
    return repo.actualizar_fotos_id(id, foto_actu, sesion)

