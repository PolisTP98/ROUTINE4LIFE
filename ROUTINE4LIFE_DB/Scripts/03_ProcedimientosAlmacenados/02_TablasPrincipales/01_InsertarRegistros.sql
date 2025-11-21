/*
==========================================================================================================================================================

-	Autor: Isaac Abdiel Sánchez López.
-	Fecha de creación: 04/11/2025.
-	Fecha de la última actualización: 06/11/2025.
-	Título: Procedimientos almacenados para insertar registros.
-	Descripción: En este archivo se crean los procedimientos almacenados para insertar registros en las tablas principales de la base de datos.

==========================================================================================================================================================
*/


-- STORED_PROCEDURE insert_medico_personal
GO
CREATE OR ALTER PROCEDURE r4l.sp_insert_medico_personal
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
    INSERT INTO r4l.medico_personal(id_sexo, id_pais, id_documento, numero_identificacion, nombres, apellido_paterno, apellido_materno, fecha_nacimiento, telefono, email_personal, rfc, direccion)
    VALUES(@id_sexo, @id_pais, @id_documento, @numero_identificacion, @nombres, @apellido_paterno, @apellido_materno, @fecha_nacimiento, @telefono, @email_personal, @rfc, @direccion);
END;
GO

-- STORED_PROCEDURE insert_medico_laboral
GO
CREATE OR ALTER PROCEDURE r4l.sp_insert_medico_laboral
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
    INSERT INTO r4l.medico_laboral(id_medico, id_sucursal, id_departamento, id_contrato, fecha_inicio, fecha_fin, anios_experiencia, nss)
    VALUES(@id_medico, @id_sucursal, @id_departamento, @id_contrato, @fecha_inicio, @fecha_fin, @anios_experiencia, @nss);
END;
GO

-- STORED_PROCEDURE insert_historial_salarial
GO
CREATE OR ALTER PROCEDURE r4l.sp_insert_historial_salarial
    @id_medico INT,
    @fecha_inicio DATE,
    @fecha_fin DATE = NULL,
    @salario DECIMAL(10,2)
AS
BEGIN
    INSERT INTO r4l.historial_salarial(id_medico, fecha_inicio, fecha_fin, salario)
    VALUES(@id_medico, @fecha_inicio, @fecha_fin, @salario);
END;
GO

-- STORED_PROCEDURE insert_especialidad_medico
GO
CREATE OR ALTER PROCEDURE r4l.sp_insert_especialidad_medico
    @id_medico INT,
    @id_especialidad INT,
	@institucion_graduacion NVARCHAR(255),
	@cedula_profesional NVARCHAR(50)
AS
BEGIN
    INSERT INTO r4l.especialidades_medico(id_medico, id_especialidad, institucion_graduacion, cedula_profesional)
    VALUES(@id_medico, @id_especialidad, @institucion_graduacion, @cedula_profesional);
END;
GO

-- STORED_PROCEDURE insert_subespecialidad_medico
GO
CREATE OR ALTER PROCEDURE r4l.sp_insert_subespecialidad_medico
    @id_especialidad_medico INT,
    @id_subespecialidad INT
AS
BEGIN
    INSERT INTO r4l.subespecialidades_medico(id_especialidad_medico, id_subespecialidad)
    VALUES(@id_especialidad_medico, @id_subespecialidad);
END;
GO

-- STORED_PROCEDURE insert_curso
GO
CREATE OR ALTER PROCEDURE r4l.sp_insert_curso
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
    INSERT INTO r4l.cursos(fecha_inicio, fecha_fin, nombre, curso_interno, institucion, duracion_horas, certificado, descripcion, url_certificado)
    VALUES(@fecha_inicio, @fecha_fin, @nombre, @curso_interno, @institucion, @duracion_horas, @certificado, @descripcion, @url_certificado);
END;
GO

-- STORED_PROCEDURE insert_curso_medico
GO
CREATE OR ALTER PROCEDURE r4l.sp_insert_curso_medico
    @id_medico INT,
    @id_curso INT,
	@id_resultado INT,
    @observaciones NVARCHAR(255) = NULL
AS
BEGIN
    INSERT INTO r4l.cursos_medico(id_medico, id_curso, id_resultado, observaciones)
    VALUES(@id_medico, @id_curso, @id_resultado, @observaciones);
END;
GO

-- STORED_PROCEDURE insert_procedimiento_medico
GO
CREATE OR ALTER PROCEDURE r4l.sp_insert_procedimiento_medico
    @id_medico INT,
	@id_procedimiento INT
AS
BEGIN
    INSERT INTO r4l.procedimientos_medico(id_medico, id_procedimiento)
    VALUES(@id_medico, @id_procedimiento);
END;
GO

-- STORED_PROCEDURE insert_hospital_anterior
GO
CREATE OR ALTER PROCEDURE r4l.sp_insert_hospital_anterior
	@id_pais INT,
    @nombre NVARCHAR(255),
    @direccion NVARCHAR(255),
    @telefono VARCHAR(13)
AS
BEGIN
    INSERT INTO r4l.hospitales_anteriores(id_pais, nombre, direccion, telefono)
    VALUES(@id_pais, @nombre, @direccion, @telefono);
END;
GO

-- STORED_PROCEDURE insert_hospital_anterior_medico
GO
CREATE OR ALTER PROCEDURE r4l.sp_insert_hospital_anterior_medico
    @id_medico INT,
    @id_hospital INT,
    @fecha_inicio DATE,
    @fecha_fin DATE
AS
BEGIN
    INSERT INTO r4l.hospitales_anteriores_medico(id_medico, id_hospital, fecha_inicio, fecha_fin)
    VALUES(@id_medico, @id_hospital, @fecha_inicio, @fecha_fin);
END;
GO

-- STORED_PROCEDURE insert_usuario
GO
CREATE OR ALTER PROCEDURE r4l.sp_insert_usuario
    @id_medico INT,
	@id_rol INT,
    @username NVARCHAR(50),
    @email_laboral NVARCHAR(255),
    @contrasena_cifrada VARCHAR(255),
	@url_imagen_perfil NVARCHAR(255)
AS
BEGIN
    INSERT INTO r4l.usuarios(id_medico, id_rol, username, email_laboral, contrasena_cifrada, url_imagen_perfil)
    VALUES(@id_medico, @id_rol, @username, @email_laboral, @contrasena_cifrada, @url_imagen_perfil);
END;
GO

-- STORED_PROCEDURE insert_paciente
GO
CREATE OR ALTER PROCEDURE r4l.sp_insert_paciente
    @id_sexo INT,
    @id_pais INT,
    @nombres NVARCHAR(100),
    @apellido_paterno NVARCHAR(50),
    @apellido_materno NVARCHAR(50) = NULL,
    @fecha_nacimiento DATE
AS
BEGIN
    INSERT INTO r4l.pacientes(id_sexo, id_pais, nombres, apellido_paterno, apellido_materno, fecha_nacimiento)
    VALUES(@id_sexo, @id_pais, @nombres, @apellido_paterno, @apellido_materno, @fecha_nacimiento);
END;
GO

-- STORED_PROCEDURE insert_cita_paciente
GO
CREATE OR ALTER PROCEDURE r4l.sp_insert_cita_paciente
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
    INSERT INTO r4l.cita_paciente(id_medico, id_paciente, fecha_cita, hora_cita, peso, altura, presion_arterial, frecuencia_cardiaca, glucosa_ayuno, glucosa_postprandial, hba1c, colesterol_total, trigliceridos, insulina_actual, recomendaciones, fecha_siguiente_cita, hora_siguiente_cita)
    VALUES(@id_medico, @id_paciente, @fecha_cita, @hora_cita, @peso, @altura, @presion_arterial, @frecuencia_cardiaca, @glucosa_ayuno, @glucosa_postprandial, @hba1c, @colesterol_total, @trigliceridos, @insulina_actual, @recomendaciones, @fecha_siguiente_cita, @hora_siguiente_cita);
END;
GO

-- STORED_PROCEDURE insert_sintoma_paciente
GO
CREATE OR ALTER PROCEDURE r4l.sp_insert_sintoma_paciente
    @id_cita INT,
    @descripcion NVARCHAR(255)
AS
BEGIN
    INSERT INTO r4l.sintomas_paciente(id_cita, descripcion)
    VALUES(@id_cita, @descripcion);
END;
GO

-- STORED_PROCEDURE insert_tratamiento_paciente
GO
CREATE OR ALTER PROCEDURE r4l.sp_insert_tratamiento_paciente
    @id_cita INT,
	@fecha_inicio DATE,
	@fecha_fin DATE = NULL,
	@medicamento NVARCHAR(100),
	@concentracion VARCHAR(20),
	@dosis VARCHAR(50),
	@frecuencia VARCHAR(50),
	@duracion VARCHAR(50),
	@observaciones VARCHAR(255) = NULL,
	@url_imagen_medicamento NVARCHAR(255)
AS
BEGIN
    INSERT INTO r4l.tratamientos_paciente(id_cita, fecha_inicio, fecha_fin, medicamento, concentracion, dosis, frecuencia, duracion, observaciones, url_imagen_medicamento)
    VALUES(@id_cita, @fecha_inicio, @fecha_fin, @medicamento, @concentracion, @dosis, @frecuencia, @duracion, @observaciones, @url_imagen_medicamento);
END;
GO

-- STORED_PROCEDURE insert_rutina_ejercicio
GO
CREATE OR ALTER PROCEDURE r4l.sp_insert_rutina_ejercicio
	@id_cita INT,
	@fecha_inicio DATE,
	@fecha_fin DATE = NULL,
	@ejercicio NVARCHAR(100),
	@duracion_minutos SMALLINT,
	@intensidad VARCHAR(50),
	@frecuencia_semanal TINYINT,
	@observaciones VARCHAR(255) = NULL
AS
BEGIN
    INSERT INTO r4l.rutina_ejercicio(id_cita, fecha_inicio, fecha_fin, ejercicio, duracion_minutos, frecuencia_semanal, intensidad, observaciones)
    VALUES(@id_cita, @fecha_inicio, @fecha_fin, @ejercicio, @duracion_minutos, @frecuencia_semanal, @intensidad, @observaciones);
END;
GO

-- STORED_PROCEDURE insert_rutina_alimentacion
GO
CREATE OR ALTER PROCEDURE r4l.sp_insert_rutina_alimentacion
	@id_cita INT,
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
    INSERT INTO r4l.rutina_alimentacion(id_cita, id_comida, fecha_inicio, fecha_fin, platillo, calorias_aprox, duracion_dias, observaciones, url_imagen_platillo)
    VALUES(@id_cita, @id_comida, @fecha_inicio, @fecha_fin, @platillo, @calorias_aprox, @duracion_dias, @observaciones, @url_imagen_platillo);
END;
GO

-- STORED_PROCEDURE insert_descripcion_rutina
GO
CREATE OR ALTER PROCEDURE r4l.sp_insert_descripcion_rutina
	@id_rutina_alimentacion INT,
	@descripcion VARCHAR(MAX)
AS
BEGIN
    INSERT INTO r4l.descripcion_rutina(id_rutina_alimentacion, descripcion)
    VALUES(@id_rutina_alimentacion, @descripcion);
END;
GO