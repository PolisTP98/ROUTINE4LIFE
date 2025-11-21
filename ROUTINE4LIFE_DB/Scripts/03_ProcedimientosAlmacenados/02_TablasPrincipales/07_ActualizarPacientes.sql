/*
==========================================================================================================================================================

-	Autor: Isaac Abdiel Sánchez López.
-	Fecha de creación: 04/11/2025.
-	Fecha de la última actualización: 06/11/2025.
-	Título: Procedimientos almacenados para actualizar pacientes.
-	Descripción: En este archivo se crean los procedimientos almacenados para actualizar pacientes en la base de datos.

==========================================================================================================================================================
*/


-- STORED_PROCEDURE update_paciente_aplicacion
GO
CREATE OR ALTER PROCEDURE r4l.sp_update_paciente_aplicacion
	@id_paciente_aplicacion INT,
    @id_sexo INT,
    @id_pais INT,
    @nombres NVARCHAR(100),
    @apellido_paterno NVARCHAR(50),
    @apellido_materno NVARCHAR(50) = NULL,
    @fecha_nacimiento DATE
AS
BEGIN
    UPDATE r4l.pacientes_aplicacion
    SET id_sexo = ISNULL(@id_sexo, id_sexo),
        id_pais = ISNULL(@id_pais, id_pais),
        nombres = ISNULL(@nombres, nombres),
        apellido_paterno = ISNULL(@apellido_paterno, apellido_paterno),
        apellido_materno = ISNULL(@apellido_materno, apellido_materno),
        fecha_nacimiento = ISNULL(@fecha_nacimiento, fecha_nacimiento)
    WHERE id_paciente_aplicacion = @id_paciente_aplicacion AND id_estatus = 1;
END;
GO

-- STORED_PROCEDURE update_usuario_paciente
GO
CREATE OR ALTER PROCEDURE r4l.sp_update_usuario_paciente
    @id_paciente_aplicacion INT,
    @username NVARCHAR(50),
    @email NVARCHAR(255),
    @contrasena_cifrada VARCHAR(255),
	@url_imagen_perfil NVARCHAR(255)
AS
BEGIN
    UPDATE r4l.usuarios_pacientes
    SET username = ISNULL(@username, username),
        email = ISNULL(@email, email),
        contrasena_cifrada = ISNULL(@contrasena_cifrada, contrasena_cifrada),
		url_imagen_perfil = ISNULL(@url_imagen_perfil, url_imagen_perfil)
    WHERE id_paciente_aplicacion = @id_paciente_aplicacion AND id_estatus = 1;
END;
GO