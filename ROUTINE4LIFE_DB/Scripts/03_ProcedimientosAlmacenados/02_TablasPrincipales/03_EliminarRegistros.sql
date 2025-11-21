/*
==========================================================================================================================================================

-	Autor: Isaac Abdiel Sánchez López.
-	Fecha de creación: 04/11/2025.
-	Fecha de la última actualización: 06/11/2025.
-	Título: Procedimientos almacenados para eliminar registros.
-	Descripción: En este archivo se crean los procedimientos almacenados para eliminar registros de manera lógica de las tablas principales de la base de
	datos.

==========================================================================================================================================================
*/


-- STORED_PROCEDURE delete_medico_personal
GO
CREATE OR ALTER PROCEDURE r4l.sp_delete_medico_personal
    @id_medico INT
AS
BEGIN
    UPDATE r4l.medico_personal
    SET id_estatus = 2,
		fecha_eliminacion = GETDATE()
    WHERE id_medico = @id_medico AND id_estatus <> 2;

	UPDATE r4l.medico_laboral
    SET id_estatus = 2,
		fecha_eliminacion = GETDATE()
    WHERE id_medico = @id_medico AND id_estatus <> 2;
END;
GO

-- STORED_PROCEDURE delete_medico_laboral
GO
CREATE OR ALTER PROCEDURE r4l.sp_delete_medico_laboral
    @id_medico INT
AS
BEGIN
    UPDATE r4l.medico_laboral
    SET id_estatus = 2,
		fecha_eliminacion = GETDATE()
    WHERE id_medico = @id_medico AND id_estatus <> 2;
END;
GO

-- STORED_PROCEDURE delete_historial_salarial
GO
CREATE OR ALTER PROCEDURE r4l.sp_delete_historial_salarial
    @id_historial INT
AS
BEGIN
    UPDATE r4l.historial_salarial
    SET id_estatus = 2,
		fecha_eliminacion = GETDATE()
    WHERE id_historial = @id_historial AND id_estatus <> 2;
END;
GO

-- STORED_PROCEDURE delete_especialidad_medico
GO
CREATE OR ALTER PROCEDURE r4l.sp_delete_especialidad_medico
    @id_especialidad_medico INT
AS
BEGIN
    UPDATE r4l.especialidades_medico
    SET id_estatus = 2,
		fecha_eliminacion = GETDATE()
    WHERE id_especialidad_medico = @id_especialidad_medico AND id_estatus <> 2;

	UPDATE r4l.subespecialidades_medico
    SET id_estatus = 2,
		fecha_eliminacion = GETDATE()
    WHERE id_especialidad_medico = @id_especialidad_medico AND id_estatus <> 2;
END;
GO

-- STORED_PROCEDURE delete_subespecialidad_medico
GO
CREATE OR ALTER PROCEDURE r4l.sp_delete_subespecialidad_medico
    @id_subespecialidad_medico INT
AS
BEGIN
	UPDATE r4l.subespecialidades_medico
    SET id_estatus = 2,
		fecha_eliminacion = GETDATE()
    WHERE id_subespecialidad_medico = @id_subespecialidad_medico AND id_estatus <> 2;
END;
GO

-- STORED_PROCEDURE delete_curso
GO
CREATE OR ALTER PROCEDURE r4l.sp_delete_curso
    @id_curso INT
AS
BEGIN
    UPDATE r4l.cursos
    SET id_estatus = 2,
		fecha_eliminacion = GETDATE()
    WHERE id_curso = @id_curso AND id_estatus <> 2;
END;
GO

-- STORED_PROCEDURE delete_curso_medico
GO
CREATE OR ALTER PROCEDURE r4l.sp_delete_curso_medico
    @id_medico INT,
	@id_curso INT
AS
BEGIN
    UPDATE r4l.cursos_medico
    SET id_estatus = 2,
		fecha_eliminacion = GETDATE()
    WHERE id_medico = @id_medico AND 
		  id_curso = @id_curso AND
		  id_estatus <> 2;
END;
GO

-- STORED_PROCEDURE delete_procedimiento_medico
GO
CREATE OR ALTER PROCEDURE r4l.sp_delete_procedimiento_medico
	@id_medico INT,
	@id_procedimiento INT
AS
BEGIN
    UPDATE r4l.procedimientos_medico
    SET id_estatus = 2,
		fecha_eliminacion = GETDATE()
    WHERE id_medico = @id_medico AND
		  id_procedimiento = @id_procedimiento AND
		  id_estatus <> 2;
END;
GO

-- STORED_PROCEDURE delete_hospital_anterior
GO
CREATE OR ALTER PROCEDURE r4l.sp_delete_hospital_anterior
    @id_hospital INT
AS
BEGIN
    UPDATE r4l.hospitales_anteriores
    SET id_estatus = 2,
		fecha_eliminacion = GETDATE()
    WHERE id_hospital = @id_hospital AND id_estatus <> 2;
END;
GO

-- STORED_PROCEDURE delete_hospital_anterior_medico
GO
CREATE OR ALTER PROCEDURE r4l.sp_delete_hospital_anterior_medico
    @id_medico INT,
	@id_hospital INT
AS
BEGIN
    UPDATE r4l.hospitales_anteriores_medico
    SET id_estatus = 2,
		fecha_eliminacion = GETDATE()
    WHERE id_medico = @id_medico AND
		  id_hospital = @id_hospital AND
		  id_estatus <> 2;
END;
GO

-- STORED_PROCEDURE delete_usuario
GO
CREATE OR ALTER PROCEDURE r4l.sp_delete_usuario
    @id_medico INT
AS
BEGIN
    UPDATE r4l.usuarios
    SET id_estatus = 2,
        fecha_eliminacion = GETDATE()
    WHERE id_medico = @id_medico AND id_estatus <> 2;
END;
GO

-- STORED_PROCEDURE delete_paciente
GO
CREATE OR ALTER PROCEDURE r4l.sp_delete_paciente
    @id_paciente INT
AS
BEGIN
    UPDATE r4l.pacientes
    SET id_estatus = 2,
		fecha_eliminacion = GETDATE()
    WHERE id_paciente = @id_paciente AND id_estatus <> 2;
END;
GO

-- STORED_PROCEDURE delete_cita_paciente
GO
CREATE OR ALTER PROCEDURE r4l.sp_delete_cita_paciente
    @id_cita INT
AS
BEGIN
    UPDATE r4l.cita_paciente
    SET id_estatus = 2,
		fecha_eliminacion = GETDATE()
    WHERE id_cita = @id_cita AND id_estatus <> 2;
END;
GO

-- STORED_PROCEDURE delete_sintoma_paciente
GO
CREATE OR ALTER PROCEDURE r4l.sp_delete_sintoma_paciente
    @id_sintoma INT
AS
BEGIN
    UPDATE r4l.sintomas_paciente
    SET id_estatus = 2,
		fecha_eliminacion = GETDATE()
    WHERE id_sintoma = @id_sintoma AND id_estatus <> 2;
END;
GO

-- STORED_PROCEDURE delete_tratamiento_paciente
GO
CREATE OR ALTER PROCEDURE r4l.sp_delete_tratamiento_paciente
    @id_tratamiento INT
AS
BEGIN
    UPDATE r4l.tratamientos_paciente
    SET id_estatus = 2,
		fecha_eliminacion = GETDATE()
    WHERE id_tratamiento = @id_tratamiento AND id_estatus <> 2;
END;
GO

-- STORED_PROCEDURE delete_rutina_ejercicio
GO
CREATE OR ALTER PROCEDURE r4l.sp_delete_rutina_ejercicio
    @id_rutina_ejercicio INT
AS
BEGIN
    UPDATE r4l.rutina_ejercicio
    SET id_estatus = 2,
		fecha_eliminacion = GETDATE()
    WHERE id_rutina_ejercicio = @id_rutina_ejercicio AND id_estatus <> 2;
END;
GO

-- STORED_PROCEDURE delete_rutina_alimentacion
GO
CREATE OR ALTER PROCEDURE r4l.sp_delete_rutina_alimentacion
    @id_rutina_alimentacion INT
AS
BEGIN
    UPDATE r4l.rutina_alimentacion
    SET id_estatus = 2,
		fecha_eliminacion = GETDATE()
    WHERE id_rutina_alimentacion = @id_rutina_alimentacion AND id_estatus <> 2;

	UPDATE r4l.descripcion_rutina
    SET id_estatus = 2,
		fecha_eliminacion = GETDATE()
    WHERE id_rutina_alimentacion = @id_rutina_alimentacion AND id_estatus <> 2;
END;
GO

GO
CREATE OR ALTER PROCEDURE r4l.sp_delete_descripcion_rutina
    @id_rutina_alimentacion INT
AS
BEGIN
	UPDATE r4l.descripcion_rutina
    SET id_estatus = 2,
		fecha_eliminacion = GETDATE()
    WHERE id_rutina_alimentacion = @id_rutina_alimentacion AND id_estatus <> 2;
END;
GO