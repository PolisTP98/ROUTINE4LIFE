from flask import request, flash, session
from models.database import Database

class PacienteController:
    @staticmethod
    def obtener_sexos():
        try:
            return Database.execute_query("SELECT id_sexo, nombre FROM r4l.sexos ORDER BY id_sexo")
        except Exception as e:
            print(f"DEBUG: Error al obtener sexos: {e}")
            return [
                (1, 'Masculino'),
                (2, 'Femenino'), 
                (3, 'Intersexual')
            ]

    @staticmethod
    def obtener_paises():
        try:
            # Obtener países más comunes primero, luego el resto
            paises_comunes = Database.execute_query("""
                SELECT id_pais, nombre 
                FROM r4l.paises 
                WHERE nombre IN ('México', 'Estados Unidos', 'Colombia', 'Argentina', 'España', 'Chile', 'Perú', 'Brasil')
                ORDER BY 
                    CASE 
                        WHEN nombre = 'México' THEN 1
                        WHEN nombre = 'Estados Unidos' THEN 2
                        ELSE 3
                    END,
                    nombre
            """)
            
            otros_paises = Database.execute_query("""
                SELECT id_pais, nombre 
                FROM r4l.paises 
                WHERE nombre NOT IN ('México', 'Estados Unidos', 'Colombia', 'Argentina', 'España', 'Chile', 'Perú', 'Brasil')
                ORDER BY nombre
            """)
            
            return paises_comunes + otros_paises
            
        except Exception as e:
            print(f"DEBUG: Error al obtener países: {e}")
            # Si falla, obtener todos ordenados alfabéticamente
            return Database.execute_query("SELECT id_pais, nombre FROM r4l.paises ORDER BY nombre")

    @staticmethod
    def agregar_paciente(datos):
        try:
            print(f"DEBUG: Iniciando agregar_paciente con datos: {datos}")
            
            # Verificar si existe el procedimiento almacenado
            try:
                procedimientos = Database.execute_query("SELECT name FROM sys.procedures WHERE name = 'sp_insert_paciente'")
                usar_sp = bool(procedimientos)
                print(f"DEBUG: Procedimiento sp_insert_paciente encontrado: {usar_sp}")
            except Exception as e:
                print(f"DEBUG: Error al verificar procedimiento: {e}")
                usar_sp = False
            
            if usar_sp:
                # Usar procedimiento almacenado
                query = "EXEC r4l.sp_insert_paciente @id_sexo = ?, @id_pais = ?, @nombres = ?, @apellido_paterno = ?, @apellido_materno = ?, @fecha_nacimiento = ?"
                print("DEBUG: Usando procedimiento almacenado")
            else:
                # Usar INSERT directo
                query = """
                    INSERT INTO r4l.pacientes (
                        id_sexo, id_pais, id_estatus,
                        nombres, apellido_paterno, apellido_materno, fecha_nacimiento
                    ) VALUES (?, ?, 1, ?, ?, ?, ?)
                """
                print("DEBUG: Usando INSERT directo")
            
            # Preparar parámetros
            apellido_materno = datos['apellido_materno'] if datos['apellido_materno'] else ''
            
            params = (
                int(datos['id_sexo']),
                int(datos['id_pais']),
                datos['nombres'],
                datos['apellido_paterno'],
                apellido_materno,
                datos['fecha_nacimiento']
            )
            
            print(f"DEBUG: Query a ejecutar: {query}")
            print(f"DEBUG: Parámetros: {params}")
            
            # Ejecutar la consulta
            result = Database.execute_query(query, params)
            print(f"DEBUG: Consulta ejecutada. Resultado: {result}")
            
            # Verificar inmediatamente si se insertó
            print("DEBUG: Verificando inserción en la base de datos...")
            paciente_verificado = Database.execute_query("""
                SELECT TOP 1 id_paciente, nombres, apellido_paterno 
                FROM r4l.pacientes 
                WHERE nombres = ? AND apellido_paterno = ?
                ORDER BY id_paciente DESC
            """, (datos['nombres'], datos['apellido_paterno']))
            
            if paciente_verificado:
                print(f"DEBUG: Paciente verificado después de insertar: {paciente_verificado[0]}")
            else:
                print("DEBUG: ERROR - No se encontró el paciente después de insertar")
                
            return result
                
        except Exception as e:
            print(f"DEBUG: Error en agregar_paciente: {str(e)}")
            import traceback
            print(f"DEBUG: Traceback completo: {traceback.format_exc()}")
            raise Exception(f"Error al agregar paciente: {str(e)}")

    @staticmethod
    def obtener_pacientes():
        try:
            pacientes = Database.execute_query("""
                SELECT 
                    p.id_paciente,
                    p.nombres,
                    p.apellido_paterno,
                    p.apellido_materno,
                    CONVERT(varchar, p.fecha_nacimiento, 103) as fecha_nacimiento,
                    s.nombre as sexo,
                    pa.nombre as pais,
                    CONVERT(varchar, p.fecha_registro, 103) as fecha_registro
                FROM r4l.pacientes p
                LEFT JOIN r4l.sexos s ON p.id_sexo = s.id_sexo
                LEFT JOIN r4l.paises pa ON p.id_pais = pa.id_pais
                WHERE p.id_estatus = 1
                ORDER BY p.fecha_registro DESC
            """)
            print(f"DEBUG: Pacientes obtenidos: {len(pacientes)}")
            for i, paciente in enumerate(pacientes):
                print(f"DEBUG: Paciente {i+1}: {paciente}")
            return pacientes
        except Exception as e:
            print(f"DEBUG: Error en obtener_pacientes: {e}")
            # Si falla el JOIN, hacer consulta simple
            try:
                pacientes = Database.execute_query("""
                    SELECT 
                        id_paciente,
                        nombres,
                        apellido_paterno,
                        apellido_materno,
                        CONVERT(varchar, fecha_nacimiento, 103) as fecha_nacimiento,
                        id_sexo,
                        id_pais,
                        CONVERT(varchar, fecha_registro, 103) as fecha_registro
                    FROM r4l.pacientes 
                    WHERE id_estatus = 1
                    ORDER BY fecha_registro DESC
                """)
                print(f"DEBUG: Pacientes obtenidos (sin JOIN): {len(pacientes)}")
                return pacientes
            except Exception as e2:
                print(f"DEBUG: Error en consulta simple: {e2}")
                return []

    @staticmethod
    def buscar_paciente_por_id(id_paciente):
        try:
            resultado = Database.execute_query("""
                SELECT * FROM r4l.pacientes WHERE id_paciente = ? AND id_estatus = 1
            """, (id_paciente,))
            return resultado[0] if resultado else None
        except Exception as e:
            raise Exception(f"Error al buscar paciente: {str(e)}")
    @staticmethod
    def eliminar_paciente(id_paciente):
        """
        Soft Delete - Marca el paciente como inactivo (id_estatus = 2)
        """
        try:
            print(f"DEBUG: Realizando soft delete del paciente ID: {id_paciente}")
            
            # Verificar si existe la columna fecha_eliminacion
            try:
                # Intentar con fecha_eliminacion
                query = """
                    UPDATE r4l.pacientes 
                    SET id_estatus = 2, 
                        fecha_eliminacion = GETDATE() 
                    WHERE id_paciente = ?
                """
            except:
                # Si no existe fecha_eliminacion, usar solo id_estatus
                query = """
                    UPDATE r4l.pacientes 
                    SET id_estatus = 2
                    WHERE id_paciente = ?
                """
            
            result = Database.execute_query(query, (id_paciente,))
            print(f"DEBUG: Soft delete ejecutado. Filas afectadas: {result}")
            
            return result
        except Exception as e:
            print(f"DEBUG: Error en eliminar_paciente: {str(e)}")
            raise Exception(f"Error al eliminar paciente: {str(e)}")

    @staticmethod
    def reactivar_paciente(id_paciente):
        """
        Reactivar un paciente que estaba marcado como eliminado
        """
        try:
            print(f"DEBUG: Reactivando paciente ID: {id_paciente}")
            
            query = """
                UPDATE r4l.pacientes 
                SET id_estatus = 1
                WHERE id_paciente = ?
            """
            
            result = Database.execute_query(query, (id_paciente,))
            print(f"DEBUG: Paciente reactivado. Filas afectadas: {result}")
            
            return result
        except Exception as e:
            print(f"DEBUG: Error en reactivar_paciente: {str(e)}")
            raise Exception(f"Error al reactivar paciente: {str(e)}")

    @staticmethod
    def obtener_pacientes_eliminados():
        """
        Obtener lista de pacientes marcados como eliminados (para admin)
        """
        try:
            pacientes = Database.execute_query("""
                SELECT 
                    p.id_paciente,
                    p.nombres,
                    p.apellido_paterno,
                    p.apellido_materno,
                    CONVERT(varchar, p.fecha_nacimiento, 103) as fecha_nacimiento,
                    s.nombre as sexo,
                    pa.nombre as pais,
                    CONVERT(varchar, p.fecha_registro, 103) as fecha_registro
                FROM r4l.pacientes p
                LEFT JOIN r4l.sexos s ON p.id_sexo = s.id_sexo
                LEFT JOIN r4l.paises pa ON p.id_pais = pa.id_pais
                WHERE p.id_estatus = 2  -- Pacientes eliminados
                ORDER BY p.fecha_registro DESC
            """)
            print(f"DEBUG: Pacientes eliminados obtenidos: {len(pacientes)}")
            return pacientes
        except Exception as e:
            print(f"DEBUG: Error en obtener_pacientes_eliminados: {e}")
            return []
        
    @staticmethod
    def obtener_paciente_por_id(id_paciente):
        """Obtiene un paciente específico para editar"""
        try:
            print(f"DEBUG: Buscando paciente con ID: {id_paciente}")
            
            paciente = Database.execute_query("""
                SELECT 
                    id_paciente, 
                    id_sexo, 
                    id_pais,
                    nombres, 
                    apellido_paterno, 
                    apellido_materno, 
                    CONVERT(varchar, fecha_nacimiento, 23) as fecha_nacimiento
                FROM r4l.pacientes 
                WHERE id_paciente = ? AND id_estatus = 1
            """, (id_paciente,))
            
            if paciente:
                print(f"DEBUG: Paciente encontrado: {paciente[0]}")
                return paciente[0]
            else:
                print(f"DEBUG: Paciente no encontrado con ID: {id_paciente}")
                return None
                
        except Exception as e:
            print(f"DEBUG: Error en obtener_paciente_por_id: {str(e)}")
            raise e
    
    @staticmethod
    def actualizar_paciente(id_paciente, datos):
        """Actualiza un paciente existente"""
        try:
            print(f"DEBUG: Actualizando paciente ID: {id_paciente} con datos: {datos}")
            
            query = """
                UPDATE r4l.pacientes 
                SET id_sexo = ?, 
                    id_pais = ?,
                    nombres = ?, 
                    apellido_paterno = ?, 
                    apellido_materno = ?, 
                    fecha_nacimiento = ?
                WHERE id_paciente = ? AND id_estatus = 1
            """
            
            apellido_materno = datos['apellido_materno'] if datos['apellido_materno'] else ''
            
            params = (
                int(datos['id_sexo']),
                int(datos['id_pais']),
                datos['nombres'],
                datos['apellido_paterno'],
                apellido_materno,
                datos['fecha_nacimiento'],
                id_paciente
            )
            
            print(f"DEBUG: Ejecutando UPDATE: {query}")
            print(f"DEBUG: Parámetros: {params}")
            
            result = Database.execute_query(query, params)
            print(f"DEBUG: Paciente actualizado. Filas afectadas: {result}")
            
            return result
                
        except Exception as e:
            print(f"DEBUG: Error en actualizar_paciente: {str(e)}")
            raise e