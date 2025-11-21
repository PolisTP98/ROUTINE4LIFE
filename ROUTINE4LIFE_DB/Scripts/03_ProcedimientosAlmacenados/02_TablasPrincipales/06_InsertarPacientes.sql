/*
==========================================================================================================================================================

-	Autor: Isaac Abdiel Sánchez López.
-	Fecha de creación: 04/11/2025.
-	Fecha de la última actualización: 06/11/2025.
-	Título: Procedimientos almacenados para insertar pacientes.
-	Descripción: En este archivo se crean los procedimientos almacenados para insertar pacientes la base de datos.

==========================================================================================================================================================
*/


-- STORED_PROCEDURE insert_paciente_aplicacion
GO
CREATE OR ALTER PROCEDURE r4l.sp_insert_paciente_aplicacion
    @id_paciente INT,
	@id_sexo INT,
    @id_pais INT,
    @nombres NVARCHAR(100),
    @apellido_paterno NVARCHAR(50),
    @apellido_materno NVARCHAR(50) = NULL,
    @fecha_nacimiento DATE
AS
BEGIN
    INSERT INTO r4l.pacientes_aplicacion(id_paciente, id_sexo, id_pais, nombres, apellido_paterno, apellido_materno, fecha_nacimiento)
    VALUES(@id_paciente, @id_sexo, @id_pais, @nombres, @apellido_paterno, @apellido_materno, @fecha_nacimiento);
END;
GO

-- STORED_PROCEDURE insert_usuario_paciente
GO
CREATE OR ALTER PROCEDURE r4l.sp_insert_usuario_paciente
    @id_paciente_aplicacion INT,
    @username NVARCHAR(50),
    @email NVARCHAR(255),
    @contrasena_cifrada VARCHAR(255),
	@url_imagen_perfil NVARCHAR(255)
AS
BEGIN
    INSERT INTO r4l.usuarios_pacientes(id_paciente_aplicacion, username, email, contrasena_cifrada, url_imagen_perfil)
    VALUES(@id_paciente_aplicacion, @username, @email, @contrasena_cifrada, @url_imagen_perfil);
END;
GO