from flask import request, flash, session
from models.database import Database

class MedicoController:
    @staticmethod
    def obtener_medicos():
        try:
            return Database.execute_query("""
                SELECT 
                    m.id_medico,
                    m.nombres,
                    m.apellido_paterno,
                    m.apellido_materno,
                    m.numero_identificacion,
                    m.email_personal,
                    m.telefono,
                    s.nombre as sexo,
                    CONVERT(varchar, m.fecha_registro, 103) as fecha_registro
                FROM r4l.medico_personal m
                LEFT JOIN r4l.sexos s ON m.id_sexo = s.id_sexo
                WHERE m.id_estatus = 1
                ORDER BY m.fecha_registro DESC
            """)
        except Exception as e:
            print(f"DEBUG: Error al obtener médicos: {e}")
            return []

    @staticmethod
    def agregar_medico(datos):
        try:
            print(f"DEBUG: Agregando médico con datos: {datos}")
            
            # Usar el procedimiento almacenado sp_insert_medico_personal
            query = "EXEC r4l.sp_insert_medico_personal @id_sexo = ?, @id_pais = ?, @id_documento = ?, @numero_identificacion = ?, @nombres = ?, @apellido_paterno = ?, @apellido_materno = ?, @fecha_nacimiento = ?, @telefono = ?, @email_personal = ?, @rfc = ?, @direccion = ?"
            
            params = (
                int(datos['id_sexo']),
                int(datos['id_pais']),
                int(datos['id_documento']),
                datos['numero_identificacion'],
                datos['nombres'],
                datos['apellido_paterno'],
                datos.get('apellido_materno', ''),
                datos['fecha_nacimiento'],
                datos['telefono'],
                datos['email_personal'],
                datos.get('rfc', ''),
                datos.get('direccion', '')
            )
            
            print(f"DEBUG: Ejecutando SP médico con parámetros: {params}")
            result = Database.execute_query(query, params)
            print(f"DEBUG: SP médico ejecutado exitosamente")
            
            return result
                
        except Exception as e:
            print(f"DEBUG: Error en agregar_medico: {str(e)}")
            raise Exception(f"Error al agregar médico: {str(e)}")

    @staticmethod
    def obtener_documentos_legales():
        try:
            return Database.execute_query("SELECT id_documento, nombre FROM r4l.documentos_legales WHERE id_estatus = 1")
        except Exception as e:
            print(f"DEBUG: Error al obtener documentos: {e}")
            return [(1, 'CURP'), (2, 'Pasaporte'), (3, 'Licencia')]