from pydantic import BaseModel

class alumnoBase(BaseModel):
    nombre: str
    edad: int
    domicilio: str 
    carrera: str 
    trimestre: str
    email: str
    password: str

class calificacionBase(BaseModel):
    uea: str
    calificacion: str

class fotoBase(BaseModel):
    titulo: str
    descripcion: str