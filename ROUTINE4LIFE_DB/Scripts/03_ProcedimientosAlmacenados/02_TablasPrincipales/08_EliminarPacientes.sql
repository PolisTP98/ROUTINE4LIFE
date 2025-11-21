/*
==========================================================================================================================================================

-	Autor: Isaac Abdiel Sánchez López.
-	Fecha de creación: 12/11/2025.
-	Fecha de la última actualización: 12/11/2025.
-	Título: Procedimientos almacenados para eliminar pacientes.
-	Descripción: En este archivo se crean los procedimientos almacenados para eliminar pacientes de manera lógica de la base de datos.

==========================================================================================================================================================
*/


-- STORED_PROCEDURE suspend_paciente
GO
CREATE OR ALTER PROCEDURE r4l.sp_suspend_paciente
    @id_paciente INT
AS
BEGIN
    UPDATE r4l.pacientes
    SET id_estatus = 2,
		fecha_eliminacion = GETDATE()
    WHERE id_paciente = @id_paciente AND id_estatus <> 2;
END;
GO

-- STORED_PROCEDURE suspend_paciente_aplicacion
GO
CREATE OR ALTER PROCEDURE r4l.sp_suspend_paciente_aplicacion
    @id_paciente_aplicacion INT
AS
BEGIN
    UPDATE r4l.pacientes_aplicacion
    SET id_estatus = 2,
		fecha_eliminacion = GETDATE()
    WHERE id_paciente_aplicacion = @id_paciente_aplicacion AND id_estatus <> 2;

	UPDATE r4l.usuarios_pacientes
    SET id_estatus = 2,
		fecha_eliminacion = GETDATE()
    WHERE id_paciente_aplicacion = @id_paciente_aplicacion AND id_estatus <> 2;
END;
GO

-- STORED_PROCEDURE suspend_usuario_paciente
GO
CREATE OR ALTER PROCEDURE r4l.sp_suspend_usuario_paciente
    @id_paciente_aplicacion INT
AS
BEGIN
	UPDATE r4l.usuarios_pacientes
    SET id_estatus = 2,
		fecha_eliminacion = GETDATE()
    WHERE id_paciente_aplicacion = @id_paciente_aplicacion AND id_estatus <> 2;
END;
GO