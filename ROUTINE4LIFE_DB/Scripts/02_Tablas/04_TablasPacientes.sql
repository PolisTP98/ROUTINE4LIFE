/*
==========================================================================================================================================================

-	Autor: Isaac Abdiel Sánchez López.
-	Fecha de creación: 02/11/2025.
-	Fecha de la última actualización: 09/11/2025.
-	Título: Tabla fragmentada de usuarios tipo pacienes.
-	Descripción: En este archivo se crea la tabla fragmentada de usuarios tipo pacientes de la base de datos.

==========================================================================================================================================================
*/

GO
IF OBJECT_ID('r4l.pacientes_aplicacion', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.pacientes_aplicacion (
		id_paciente_aplicacion INT IDENTITY(1, 1) PRIMARY KEY,
        id_paciente INT NOT NULL,
		id_sexo INT NOT NULL,
		id_pais INT NOT NULL,
		id_estatus INT NOT NULL DEFAULT 1,
		fecha_eliminacion DATE NULL,
		fecha_suspension DATE NULL,
		fecha_reactivacion DATE NULL,
		fecha_registro DATE NOT NULL DEFAULT GETDATE(),
		nombres NVARCHAR(100) NOT NULL,
		apellido_paterno NVARCHAR(50) NOT NULL,
		apellido_materno NVARCHAR(50) NULL,
		fecha_nacimiento DATE NOT NULL,
		email NVARCHAR(255) NOT NULL,
		FOREIGN KEY(id_paciente)
			REFERENCES r4l.pacientes(id_paciente)
			ON DELETE CASCADE
			ON UPDATE CASCADE,
		FOREIGN KEY(id_sexo)
			REFERENCES r4l.sexos(id_sexo),
		FOREIGN KEY(id_pais)
			REFERENCES r4l.paises(id_pais),
		FOREIGN KEY(id_estatus)
			REFERENCES r4l.estatus_usuarios(id_estatus)
    );
END

IF OBJECT_ID('r4l.usuarios_pacientes', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.usuarios_pacientes (
		id_paciente_aplicacion INT PRIMARY KEY NOT NULL,
		id_rol INT NOT NULL DEFAULT 3,
		id_estatus INT NOT NULL DEFAULT 1,
		fecha_eliminacion DATE NULL,
		fecha_suspension DATE NULL,
		fecha_reactivacion DATE NULL,
		fecha_registro DATE NOT NULL DEFAULT GETDATE(),
		username NVARCHAR(50) NOT NULL,
		email NVARCHAR(255) NOT NULL,
		contrasena_cifrada VARCHAR(255) NOT NULL,
		url_imagen_perfil NVARCHAR(255) NOT NULL,
		FOREIGN KEY(id_paciente_aplicacion)
			REFERENCES r4l.pacientes_aplicacion(id_paciente_aplicacion)
			ON DELETE CASCADE
			ON UPDATE CASCADE,
		FOREIGN KEY(id_rol)
			REFERENCES r4l.roles_usuarios(id_rol),
		FOREIGN KEY(id_estatus)
			REFERENCES r4l.estatus_usuarios(id_estatus),
		CONSTRAINT chk_fechas CHECK(fecha_eliminacion IS NULL OR fecha_eliminacion >= fecha_registro)
	);
END
GO