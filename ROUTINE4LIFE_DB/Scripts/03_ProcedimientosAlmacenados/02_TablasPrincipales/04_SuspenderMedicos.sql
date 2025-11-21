/*
==========================================================================================================================================================

-	Autor: Isaac Abdiel Sánchez López.
-	Fecha de creación: 12/11/2025.
-	Fecha de la última actualización: 12/11/2025.
-	Título: Procedimientos almacenados para suspender médicos.
-	Descripción: En este archivo se crean los procedimientos almacenados para suspender médicos de manera lógica (pausar sus actividades temporalmente).

==========================================================================================================================================================
*/


-- STORED_PROCEDURE suspend_medico_personal
GO
CREATE OR ALTER PROCEDURE r4l.sp_suspend_medico_personal
    @id_medico INT
AS
BEGIN
    UPDATE r4l.medico_personal
    SET id_estatus = 3,
		fecha_suspension = GETDATE()
    WHERE id_medico = @id_medico AND id_estatus <> 3;

	UPDATE r4l.medico_laboral
    SET id_estatus = 3,
		fecha_suspension = GETDATE()
    WHERE id_medico = @id_medico AND id_estatus <> 3;

	UPDATE r4l.usuarios
    SET id_estatus = 3,
		fecha_suspension = GETDATE()
    WHERE id_medico = @id_medico AND id_estatus <> 3;
END;
GO

-- STORED_PROCEDURE suspend_medico_laboral
GO
CREATE OR ALTER PROCEDURE r4l.sp_suspend_medico_laboral
    @id_medico INT
AS
BEGIN
	UPDATE r4l.medico_laboral
    SET id_estatus = 3,
		fecha_suspension = GETDATE()
    WHERE id_medico = @id_medico AND id_estatus <> 3;

	UPDATE r4l.usuarios
    SET id_estatus = 3,
		fecha_suspension = GETDATE()
    WHERE id_medico = @id_medico AND id_estatus <> 3;
END;
GO

-- STORED_PROCEDURE suspend_usuario
GO
CREATE OR ALTER PROCEDURE r4l.sp_suspend_usuario
    @id_medico INT
AS
BEGIN
	UPDATE r4l.usuarios
    SET id_estatus = 3,
		fecha_suspension = GETDATE()
    WHERE id_medico = @id_medico AND id_estatus <> 3;
END;
GO