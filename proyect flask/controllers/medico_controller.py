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
    @classmethod
    def obtener_medico_por_id(cls, id_medico):
        """Obtener un médico específico por ID - VERSIÓN CORREGIDA"""
        try:
            print(f"DEBUG: Buscando médico con ID: {id_medico}")
            
            query = """
                SELECT 
                    u.id_medico, 
                    u.id_rol, 
                    u.id_estatus, 
                    u.fecha_registro, 
                    u.username, 
                    u.email_laboral, 
                    u.contrasena_cifrada, 
                    u.url_imagen_perfil,
                    mp.nombres, 
                    mp.apellido_paterno, 
                    mp.apellido_materno, 
                    mp.fecha_nacimiento,
                    mp.id_sexo, 
                    mp.id_pais, 
                    mp.id_documento, 
                    mp.numero_identificacion,
                    mp.telefono, 
                    mp.email_personal, 
                    mp.rfc, 
                    mp.direccion
                FROM r4l.usuarios u
                INNER JOIN r4l.medico_personal mp ON u.id_medico = mp.id_medico
                WHERE u.id_medico = ?
            """
            resultado = Database.execute_query(query, (id_medico,))
            
            print(f"DEBUG: Resultado de la consulta: {resultado}")
            
            if resultado and len(resultado) > 0:
                medico = resultado[0]
                print(f"DEBUG: Médico encontrado: ID {medico[0]}, Nombre: {medico[8]} {medico[9]}")
                return medico
            else:
                print(f"DEBUG: No se encontró médico con ID {id_medico}")
                return None
                
        except Exception as e:
            print(f"ERROR obteniendo médico por ID {id_medico}: {str(e)}")
            return None
    @classmethod
    def actualizar_medico(cls, id_medico, datos):
        """Actualizar información del médico en ambas tablas"""
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            
            # Actualizar tabla medico_personal
            update_personal = """
                UPDATE r4l.medico_personal 
                SET id_sexo = ?, id_pais = ?, id_documento = ?, 
                    numero_identificacion = ?, nombres = ?, apellido_paterno = ?, 
                    apellido_materno = ?, fecha_nacimiento = ?, telefono = ?, 
                    email_personal = ?, rfc = ?, direccion = ?
                WHERE id_medico = ?
            """
            cursor.execute(update_personal, (
                datos['id_sexo'], datos['id_pais'], datos['id_documento'],
                datos['numero_identificacion'], datos['nombres'], datos['apellido_paterno'],
                datos['apellido_materno'], datos['fecha_nacimiento'], datos['telefono'],
                datos['email_personal'], datos['rfc'], datos['direccion'], id_medico
            ))
            
            # Actualizar tabla usuarios
            update_usuario = """
                UPDATE r4l.usuarios 
                SET id_rol = ?, email_laboral = ?
                WHERE id_medico = ?
            """
            cursor.execute(update_usuario, (
                datos['id_rol'], datos['email_laboral'], id_medico
            ))
            
            conn.commit()
            conn.close()
            return True
            
        except Exception as e:
            print(f"Error actualizando médico: {e}")
            if conn:
                conn.rollback()
            return False
    @classmethod
    def eliminar_medico(cls, id_medico):
        """Soft delete del médico (cambiar estatus a inactivo)"""
        try:
            query = "UPDATE r4l.usuarios SET id_estatus = 0, fecha_eliminacion = GETDATE() WHERE id_medico = ?"
            Database.execute_query(query, (id_medico,))
            return True
        except Exception as e:
            print(f"Error eliminando médico: {e}")
            return False
    @classmethod
    def obtener_medicos_eliminados(cls):
        """Obtener médicos eliminados (soft delete)"""
        try:
            query = """
                SELECT u.id_medico, u.id_rol, u.fecha_eliminacion, u.username, u.email_laboral,
                    mp.nombres, mp.apellido_paterno, mp.apellido_materno
                FROM r4.usuarios u
                INNER JOIN r4l.medico_personal mp ON u.id_medico = mp.id_medico
                WHERE u.id_estatus = 0
                ORDER BY u.fecha_eliminacion DESC
            """
            return Database.execute_query(query)
        except Exception as e:
            print(f"Error obteniendo médicos eliminados: {e}")
            return []

    @classmethod
    def reactivar_medico(cls, id_medico):
        """Reactivar un médico eliminado"""
        try:
            query = "UPDATE r4l.usuarios SET id_estatus = 1, fecha_reactivacion = GETDATE() WHERE id_medico = ?"
            Database.execute_query(query, (id_medico,))
            return True
        except Exception as e:
            print(f"Error reactivando médico: {e}")
            return False
    @classmethod
    def obtener_roles(cls):
        """Obtener roles de Médico y Administrador - versión simple"""
        try:
            # Consulta directa filtrando los roles que necesitas
            query = """
                SELECT id_rol, nombre_rol 
                FROM r4l.roles_usuarios 
                WHERE nombre_rol IN ('Administrador', 'Médico')
                ORDER BY id_rol
            """
            resultado = Database.execute_query(query)
            
            if resultado:
                print(f"DEBUG: Roles obtenidos: {resultado}")
                return resultado
            else:
                # Si no encuentra, usar valores por defecto
                print("DEBUG: No se encontraron roles, usando valores por defecto")
                return [
                    (1, 'Administrador'),
                    (2, 'Médico')
                ]
                
        except Exception as e:
            print(f"DEBUG: Error en obtener_roles: {e}")
            return [
                (1, 'Administrador'),
                (2, 'Médico')
            ]