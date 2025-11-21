/*
==========================================================================================================================================================

-	Autor: Isaac Abdiel Sánchez López.
-	Fecha de creación: 12/11/2025.
-	Fecha de la última actualización: 12/11/2025.
-	Título: Procedimientos almacenados para suspender pacientes.
-	Descripción: En este archivo se crean los procedimientos almacenados para suspender pacientes de manera lógica (pausar sus actividades temporalmente).

==========================================================================================================================================================
*/


-- STORED_PROCEDURE suspend_paciente
GO
CREATE OR ALTER PROCEDURE r4l.sp_suspend_paciente
    @id_paciente_aplicacion INT
AS
BEGIN
    UPDATE r4l.pacientes_aplicacion
    SET id_estatus = 3,
		fecha_suspension = GETDATE()
    WHERE id_paciente_aplicacion = @id_paciente_aplicacion AND id_estatus <> 3;

	UPDATE r4l.usuarios_pacientes
    SET id_estatus = 3,
		fecha_suspension = GETDATE()
    WHERE id_paciente_aplicacion = @id_paciente_aplicacion AND id_estatus <> 3;
END;
GO

-- STORED_PROCEDURE suspend_usuario_paciente
GO
CREATE OR ALTER PROCEDURE r4l.sp_suspend_usuario_paciente
    @id_paciente_aplicacion INT
AS
BEGIN
	UPDATE r4l.usuarios_pacientes
    SET id_estatus = 3,
		fecha_suspension = GETDATE()
    WHERE id_paciente_aplicacion = @id_paciente_aplicacion AND id_estatus <> 3;
END;
GO