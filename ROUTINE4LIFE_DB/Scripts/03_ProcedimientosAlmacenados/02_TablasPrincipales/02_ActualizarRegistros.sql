/*
==========================================================================================================================================================

-	Autor: Isaac Abdiel Sánchez López.
-	Fecha de creación: 04/11/2025.
-	Fecha de la última actualización: 06/11/2025.
-	Título: Procedimientos almacenados para actualizar registros.
-	Descripción: En este archivo se crean los procedimientos almacenados para actualizar registros de las tablas principales de la base de datos.

==========================================================================================================================================================
*/


-- STORED_PROCEDURE update_medico_personal
GO
CREATE OR ALTER PROCEDURE r4l.sp_update_medico_personal
    @id_medico INT,
    @id_sexo INT,
    @id_pais INT,
    @id_documento INT,
    @numero_identificacion VARCHAR(50),
    @nombres NVARCHAR(100),
    @apellido_paterno NVARCHAR(50),
    @apellido_materno NVARCHAR(50) = NULL,
    @fecha_nacimiento DATE,
    @telefono VARCHAR(13),
    @email_personal NVARCHAR(255),
    @rfc VARCHAR(13),
    @direccion NVARCHAR(255)
AS
BEGIN
    UPDATE r4l.medico_personal
    SET id_sexo = ISNULL(@id_sexo, id_sexo),
        id_pais = ISNULL(@id_pais, id_pais),
        id_documento = ISNULL(@id_documento, id_documento),
        numero_identificacion = ISNULL(@numero_identificacion, numero_identificacion),
        nombres = ISNULL(@nombres, nombres),
        apellido_paterno = ISNULL(@apellido_paterno, apellido_paterno),
        apellido_materno = ISNULL(@apellido_materno, apellido_materno),
        fecha_nacimiento = ISNULL(@fecha_nacimiento, fecha_nacimiento),
        telefono = ISNULL(@telefono, telefono),
        email_personal = ISNULL(@email_personal, email_personal),
        rfc = ISNULL(@rfc, rfc),
        direccion = ISNULL(@direccion, direccion)
    WHERE id_medico = @id_medico AND id_estatus = 1;
END;
GO

-- STORED_PROCEDURE update_medico_laboral
GO
CREATE OR ALTER PROCEDURE r4l.sp_update_medico_laboral
    @id_medico INT,
    @id_sucursal INT,
    @id_departamento INT,
    @id_contrato INT,
    @fecha_inicio DATE,
    @fecha_fin DATE = NULL,
    @anios_experiencia TINYINT,
    @nss NVARCHAR(50)
AS
BEGIN
    UPDATE r4l.medico_laboral
    SET id_sucursal = ISNULL(@id_sucursal, id_sucursal),
        id_departamento = ISNULL(@id_departamento, id_departamento),
        id_contrato = ISNULL(@id_contrato, id_contrato),
        fecha_inicio = ISNULL(@fecha_inicio, fecha_inicio),
        fecha_fin = ISNULL(@fecha_fin, fecha_fin),
        anios_experiencia = ISNULL(@anios_experiencia, anios_experiencia),
        nss = ISNULL(@nss, nss)
    WHERE id_medico = @id_medico AND id_estatus = 1;
END;
GO

-- STORED_PROCEDURE update_historial_salarial
GO
CREATE OR ALTER PROCEDURE r4l.sp_update_historial_salarial
    @id_historial INT,
    @fecha_inicio DATE,
    @fecha_fin DATE = NULL,
    @salario DECIMAL(10,2)
AS
BEGIN
    UPDATE r4l.historial_salarial
    SET fecha_inicio = ISNULL(@fecha_inicio, fecha_inicio),
        fecha_fin = ISNULL(@fecha_fin, fecha_fin),
        salario = ISNULL(@salario, salario)
    WHERE id_historial = @id_historial AND id_estatus = 1;
END;
GO

-- STORED_PROCEDURE update_especialidad_medico
GO
CREATE OR ALTER PROCEDURE r4l.sp_update_especialidad_medico
    @id_especialidad_medico INT,
    @institucion_graduacion NVARCHAR(255),
    @cedula_profesional NVARCHAR(50)
AS
BEGIN
    UPDATE r4l.especialidades_medico
    SET institucion_graduacion = ISNULL(@institucion_graduacion, institucion_graduacion),
        cedula_profesional = ISNULL(@cedula_profesional, cedula_profesional)
    WHERE id_especialidad_medico = @id_especialidad_medico AND id_estatus = 1;
END;
GO

-- STORED_PROCEDURE update_subespecialidad_medico
GO
CREATE OR ALTER PROCEDURE r4l.sp_update_subespecialidad_medico
	@id_subespecialidad_medico INT,
    @id_subespecialidad INT
AS
BEGIN
    UPDATE r4l.subespecialidades_medico
    SET id_subespecialidad = ISNULL(@id_subespecialidad, id_subespecialidad)
    WHERE id_subespecialidad_medico = @id_subespecialidad_medico AND id_estatus = 1;
END;
GO

-- STORED_PROCEDURE update_curso
GO
CREATE OR ALTER PROCEDURE r4l.sp_update_curso
    @id_curso INT,
    @fecha_inicio DATE,
    @fecha_fin DATE = NULL,
    @nombre NVARCHAR(255),
    @curso_interno BIT = 0,
    @institucion NVARCHAR(255) = NULL,
    @duracion_horas SMALLINT = NULL,
    @certificado BIT = 0,
    @descripcion NVARCHAR(500) = NULL,
    @url_certificado NVARCHAR(255) = NULL
AS
BEGIN
    UPDATE r4l.cursos
    SET fecha_inicio = ISNULL(@fecha_inicio, fecha_inicio),
        fecha_fin = ISNULL(@fecha_fin, fecha_fin),
        nombre = ISNULL(@nombre, nombre),
        curso_interno = ISNULL(@curso_interno, curso_interno),
        institucion = ISNULL(@institucion, institucion),
        duracion_horas = ISNULL(@duracion_horas, duracion_horas),
        certificado = ISNULL(@certificado, certificado),
        descripcion = ISNULL(@descripcion, descripcion),
        url_certificado = ISNULL(@url_certificado, url_certificado)
    WHERE id_curso = @id_curso AND id_estatus = 1;
END;
GO

-- STORED_PROCEDURE update_curso_medico
GO
CREATE OR ALTER PROCEDURE r4l.sp_update_curso_medico
    @id_medico INT,
    @id_curso INT,
    @id_resultado INT,
    @observaciones NVARCHAR(255)
AS
BEGIN
    UPDATE r4l.cursos_medico
    SET id_resultado = ISNULL(@id_resultado, id_resultado),
        observaciones = ISNULL(@observaciones, observaciones)
    WHERE id_medico = @id_medico AND
		  id_curso = @id_curso AND 
		  id_estatus = 1;
END;
GO

-- STORED_PROCEDURE update_procedimiento_medico
GO
CREATE OR ALTER PROCEDURE r4l.sp_update_procedimiento_medico
    @id_medico INT,
    @id_procedimiento INT,
	@nuevo_id_procedimiento INT
AS
BEGIN
    UPDATE r4l.procedimientos_medico
    SET id_procedimiento = ISNULL(@nuevo_id_procedimiento, id_procedimiento)
    WHERE id_medico = @id_medico AND
		  id_procedimiento = @id_procedimiento AND 
		  id_estatus = 1;
END;
GO

-- STORED_PROCEDURE update_hospital_anterior
GO
CREATE OR ALTER PROCEDURE r4l.sp_update_hospital_anterior
    @id_hospital INT,
    @id_pais INT,
    @nombre NVARCHAR(255),
    @direccion NVARCHAR(255),
    @telefono VARCHAR(13)
AS
BEGIN
    UPDATE r4l.hospitales_anteriores
    SET id_pais = ISNULL(@id_pais, id_pais),
        nombre = ISNULL(@nombre, nombre),
        direccion = ISNULL(@direccion, direccion),
        telefono = ISNULL(@telefono, telefono)
    WHERE id_hospital = @id_hospital AND id_estatus = 1;
END;
GO

-- STORED_PROCEDURE update_hospital_anterior_medico
GO
CREATE OR ALTER PROCEDURE r4l.sp_update_hospital_anterior_medico
    @id_medico INT,
    @id_hospital INT,
    @fecha_inicio DATE,
    @fecha_fin DATE
AS
BEGIN
    UPDATE r4l.hospitales_anteriores_medico
    SET fecha_inicio = ISNULL(@fecha_inicio, fecha_inicio),
        fecha_fin = ISNULL(@fecha_fin, fecha_fin)
    WHERE id_medico = @id_medico AND
		  id_hospital = @id_hospital AND 
		  id_estatus = 1;
END;
GO

-- STORED_PROCEDURE update_usuario
GO
CREATE OR ALTER PROCEDURE r4l.sp_update_usuario
    @id_medico INT,
	@id_rol INT,
    @username NVARCHAR(50),
    @email_laboral NVARCHAR(255),
    @contrasena_cifrada VARCHAR(255),
	@url_imagen_perfil NVARCHAR(255)
AS
BEGIN
    UPDATE r4l.usuarios
    SET id_rol = ISNULL(@id_rol, id_rol),
		username = ISNULL(@username, username),
        email_laboral = ISNULL(@email_laboral, email_laboral),
        contrasena_cifrada = ISNULL(@contrasena_cifrada, contrasena_cifrada),
		url_imagen_perfil = ISNULL(@url_imagen_perfil, url_imagen_perfil)
    WHERE id_medico = @id_medico AND id_estatus = 1;
END;
GO

/*
-- STORED_PROCEDURE update_paciente
GO
CREATE OR ALTER PROCEDURE r4l.sp_update_paciente
    @id_paciente INT,
    @id_sexo INT,
    @id_pais INT,
    @nombres NVARCHAR(100),
    @apellido_paterno NVARCHAR(50),
    @apellido_materno NVARCHAR(50) = NULL,
    @fecha_nacimiento DATE
AS
BEGIN
    UPDATE r4l.pacientes
    SET id_sexo = ISNULL(@id_sexo, id_sexo),
        id_pais = ISNULL(@id_pais, id_pais),
        nombres = ISNULL(@nombres, nombres),
        apellido_paterno = ISNULL(@apellido_paterno, apellido_paterno),
        apellido_materno = ISNULL(@apellido_materno, apellido_materno),
        fecha_nacimiento = ISNULL(@fecha_nacimiento, fecha_nacimiento)
    WHERE id_paciente = @id_paciente AND id_estatus = 1;
END;
GO
*/

-- STORED_PROCEDURE update_cita_paciente
GO
CREATE OR ALTER PROCEDURE r4l.sp_update_cita_paciente
    @id_cita INT,
    @id_medico INT,
    @id_paciente INT,
    @fecha_cita DATE,
    @hora_cita TIME,
    @peso DECIMAL(5,2),
    @altura SMALLINT,
    @presion_arterial VARCHAR(10),
    @frecuencia_cardiaca TINYINT,
    @glucosa_ayuno DECIMAL(5,2),
    @glucosa_postprandial DECIMAL(5,2),
    @hba1c DECIMAL(4,2),
    @colesterol_total DECIMAL(5,2),
    @trigliceridos DECIMAL(5,2),
    @insulina_actual DECIMAL(5,2),
    @recomendaciones NVARCHAR(MAX) = NULL,
    @fecha_siguiente_cita DATE = NULL,
    @hora_siguiente_cita TIME = NULL
AS
BEGIN
    UPDATE r4l.cita_paciente
    SET id_medico = ISNULL(@id_medico, id_medico),
        id_paciente = ISNULL(@id_paciente, id_paciente),
        fecha_cita = ISNULL(@fecha_cita, fecha_cita),
        hora_cita = ISNULL(@hora_cita, hora_cita),
        peso = ISNULL(@peso, peso),
        altura = ISNULL(@altura, altura),
        presion_arterial = ISNULL(@presion_arterial, presion_arterial),
        frecuencia_cardiaca = ISNULL(@frecuencia_cardiaca, frecuencia_cardiaca),
        glucosa_ayuno = ISNULL(@glucosa_ayuno, glucosa_ayuno),
        glucosa_postprandial = ISNULL(@glucosa_postprandial, glucosa_postprandial),
        hba1c = ISNULL(@hba1c, hba1c),
        colesterol_total = ISNULL(@colesterol_total, colesterol_total),
        trigliceridos = ISNULL(@trigliceridos, trigliceridos),
        insulina_actual = ISNULL(@insulina_actual, insulina_actual),
        recomendaciones = ISNULL(@recomendaciones, recomendaciones),
        fecha_siguiente_cita = ISNULL(@fecha_siguiente_cita, fecha_siguiente_cita),
        hora_siguiente_cita = ISNULL(@hora_siguiente_cita, hora_siguiente_cita)
    WHERE id_cita = @id_cita AND id_estatus = 1;
END;
GO

-- STORED_PROCEDURE update_sintoma_paciente
GO
CREATE OR ALTER PROCEDURE r4l.sp_update_sintoma_paciente
    @id_sintoma INT,
    @descripcion NVARCHAR(255)
AS
BEGIN
    UPDATE r4l.sintomas_paciente
    SET descripcion = ISNULL(@descripcion, descripcion)
    WHERE id_sintoma = @id_sintoma AND id_estatus = 1;
END;
GO

-- STORED_PROCEDURE update_tratamiento_paciente
GO
CREATE OR ALTER PROCEDURE r4l.sp_update_tratamiento_paciente
    @id_tratamiento INT,
    @fecha_inicio DATE,
    @fecha_fin DATE = NULL,
    @medicamento VARCHAR(100),
    @dosis VARCHAR(50),
    @frecuencia VARCHAR(50),
    @duracion VARCHAR(50),
    @observaciones VARCHAR(255),
	@url_imagen_medicamento NVARCHAR(255)
AS
BEGIN
    UPDATE r4l.tratamientos_paciente
    SET fecha_inicio = ISNULL(@fecha_inicio, fecha_inicio),
        fecha_fin = ISNULL(@fecha_fin, fecha_fin),
        medicamento = ISNULL(@medicamento, medicamento),
        dosis = ISNULL(@dosis, dosis),
        frecuencia = ISNULL(@frecuencia, frecuencia),
        duracion = ISNULL(@duracion, duracion),
        observaciones = ISNULL(@observaciones, observaciones),
		url_imagen_medicamento = ISNULL(@url_imagen_medicamento, url_imagen_medicamento)
    WHERE id_tratamiento = @id_tratamiento AND id_estatus = 1;
END;
GO

-- STORED_PROCEDURE update_rutina_ejercicio
GO
CREATE OR ALTER PROCEDURE r4l.sp_update_rutina_ejercicio
    @id_rutina_ejercicio INT,
	@fecha_inicio DATE,
	@fecha_fin DATE = NULL,
	@ejercicio NVARCHAR(100),
	@duracion_minutos SMALLINT,
	@intensidad VARCHAR(50),
	@frecuencia_semanal TINYINT,
	@observaciones VARCHAR(255)
AS
BEGIN
    UPDATE r4l.rutina_ejercicio
    SET fecha_inicio = ISNULL(@fecha_inicio, fecha_inicio),
        fecha_fin = ISNULL(@fecha_fin, fecha_fin),
		ejercicio = ISNULL(@ejercicio, ejercicio),
        duracion_minutos = ISNULL(@duracion_minutos, duracion_minutos),
		intensidad = ISNULL(@intensidad, intensidad),
        frecuencia_semanal = ISNULL(@frecuencia_semanal, frecuencia_semanal),
        observaciones = ISNULL(@observaciones, observaciones)
    WHERE id_rutina_ejercicio = @id_rutina_ejercicio AND id_estatus = 1;
END;
GO

-- STORED_PROCEDURE update_rutina_alimentacion
GO
CREATE OR ALTER PROCEDURE r4l.sp_update_rutina_alimentacion
    @id_rutina_alimentacion INT,
	@id_comida INT,
	@fecha_inicio DATE,
	@fecha_fin DATE = NULL,
	@platillo NVARCHAR(100),
	@calorias_aprox SMALLINT,
	@duracion_dias SMALLINT,
	@observaciones VARCHAR(255) = NULL,
	@url_imagen_platillo NVARCHAR(255)
AS
BEGIN
    UPDATE r4l.rutina_alimentacion
    SET id_comida = ISNULL(@id_comida, id_comida),
		fecha_inicio = ISNULL(@fecha_inicio, fecha_inicio),
        fecha_fin = ISNULL(@fecha_fin, fecha_fin),
		platillo = ISNULL(@platillo, platillo),
		calorias_aprox = ISNULL(@calorias_aprox, calorias_aprox),
        duracion_dias = ISNULL(@duracion_dias, duracion_dias),
        observaciones = ISNULL(@observaciones, observaciones),
		url_imagen_platillo = ISNULL(@url_imagen_platillo, url_imagen_platillo)
    WHERE id_rutina_alimentacion = @id_rutina_alimentacion AND id_estatus = 1;
END;
GO

-- STORED_PROCEDURE update_descripcion_rutina
GO
CREATE OR ALTER PROCEDURE r4l.sp_update_descripcion_rutina
	@id_rutina_alimentacion INT,
	@descripcion VARCHAR(MAX)
AS
BEGIN
	UPDATE r4l.descripcion_rutina
    SET descripcion = ISNULL(@descripcion, descripcion)
    WHERE id_rutina_alimentacion = @id_rutina_alimentacion AND id_estatus = 1;
END;
GO