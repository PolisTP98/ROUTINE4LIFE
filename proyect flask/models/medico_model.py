# models/medico_model.py
class MedicoModel:
    def __init__(self, db_connection):
        self.db = db_connection
    
    def validar_datos_medico(self, datos):
        """Valida los datos del médico y retorna (es_valido, errores)"""
        errores = {}
        
        # Validar nombre
        if not datos.get('nombre', '').strip():
            errores['nombre'] = 'El nombre es obligatorio'
        elif len(datos['nombre'].strip()) < 2:
            errores['nombre'] = 'El nombre debe tener al menos 2 caracteres'
        elif not self._es_texto_valido(datos['nombre']):
            errores['nombre'] = 'El nombre solo puede contener letras y espacios'
        
        # Validar apellido paterno
        if not datos.get('apellido_paterno', '').strip():
            errores['apellido_paterno'] = 'El apellido paterno es obligatorio'
        
        # Validar email
        email = datos.get('email', '').strip()
        if not email:
            errores['email'] = 'El email es obligatorio'
        elif not self._validar_email(email):
            errores['email'] = 'El formato del email no es válido'
        elif self._email_existe(email, datos.get('id')):
            errores['email'] = 'Este email ya está registrado'
        
        # Validar teléfono
        telefono = datos.get('telefono', '').strip()
        if telefono and not self._validar_telefono(telefono):
            errores['telefono'] = 'El teléfono debe tener 10 dígitos'
        
        # Validar código
        codigo = datos.get('codigo', '').strip()
        if not codigo:
            errores['codigo'] = 'El código/matrícula es obligatorio'
        elif self._codigo_existe(codigo, datos.get('id')):
            errores['codigo'] = 'Este código ya está registrado'
        
        return len(errores) == 0, errores
    
    def _validar_email(self, email):
        """Valida formato de email"""
        import re
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(patron, email))
    
    def _validar_telefono(self, telefono):
        """Valida formato de teléfono"""
        import re
        telefono_limpio = re.sub(r'[\s\-\(\)]', '', telefono)
        return telefono_limpio.isdigit() and len(telefono_limpio) == 10
    
    def _es_texto_valido(self, texto):
        """Valida que el texto solo contenga letras y espacios"""
        import re
        return bool(re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', texto.strip()))
    
    def _email_existe(self, email, id_medico=None):
        """Verifica si el email ya existe (excluyendo el médico actual)"""
        cursor = self.db.cursor()
        if id_medico:
            cursor.execute("SELECT id FROM medicos WHERE email = ? AND id != ?", (email, id_medico))
        else:
            cursor.execute("SELECT id FROM medicos WHERE email = ?", (email,))
        return cursor.fetchone() is not None
    
    def _codigo_existe(self, codigo, id_medico=None):
        """Verifica si el código ya existe (excluyendo el médico actual)"""
        cursor = self.db.cursor()
        if id_medico:
            cursor.execute("SELECT id FROM medicos WHERE codigo = ? AND id != ?", (codigo, id_medico))
        else:
            cursor.execute("SELECT id FROM medicos WHERE codigo = ?", (codigo,))
        return cursor.fetchone() is not None
    
    def crear_medico(self, datos):
        """Crea un nuevo médico en la base de datos"""
        cursor = self.db.cursor()
        cursor.execute("""
            INSERT INTO medicos (nombre, apellido_paterno, apellido_materno, email, telefono, codigo, genero, especialidad)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            datos['nombre'],
            datos['apellido_paterno'],
            datos['apellido_materno'],
            datos['email'],
            datos['telefono'],
            datos['codigo'],
            datos['genero'],
            datos.get('especialidad', '')
        ))
        self.db.commit()
        return cursor.lastrowid
    
    def actualizar_medico(self, id_medico, datos):
        """Actualiza un médico existente"""
        cursor = self.db.cursor()
        cursor.execute("""
            UPDATE medicos 
            SET nombre = ?, apellido_paterno = ?, apellido_materno = ?, 
                email = ?, telefono = ?, codigo = ?, genero = ?, especialidad = ?
            WHERE id = ?
        """, (
            datos['nombre'],
            datos['apellido_paterno'],
            datos['apellido_materno'],
            datos['email'],
            datos['telefono'],
            datos['codigo'],
            datos['genero'],
            datos.get('especialidad', ''),
            id_medico
        ))
        self.db.commit()