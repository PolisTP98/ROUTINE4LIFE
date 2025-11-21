/*
==========================================================================================================================================================

-	Autor: Isaac Abdiel Sánchez López.
-	Fecha de creación: 05/11/2025.
-	Fecha de la última actualización: 07/11/2025.
-	Título: Procedimientos almacenados para insertar registros.
-	Descripción: En este archivo se crean los procedimientos almacenados para insertar registros en las tablas catálogo de la base de datos.

==========================================================================================================================================================
*/


-- STORED_PROCEDURE insert_sexo
GO
CREATE OR ALTER PROCEDURE r4l.sp_insert_sexo
    @nombre NVARCHAR(20)
AS
BEGIN
    INSERT INTO r4l.sexos(nombre) VALUES(@nombre);
END;
GO

-- STORED_PROCEDURE insert_rol_usuario
CREATE OR ALTER PROCEDURE r4l.sp_insert_rol_usuario
    @nombre NVARCHAR(50)
AS
BEGIN
    INSERT INTO r4l.roles_usuarios(nombre)
    VALUES(@nombre);
END;
GO

-- STORED_PROCEDURE insert_estatus_usuario
CREATE OR ALTER PROCEDURE r4l.sp_insert_estatus_usuario
    @nombre NVARCHAR(50),
    @descripcion NVARCHAR(100) = NULL
AS
BEGIN
    INSERT INTO r4l.estatus_usuarios(nombre, descripcion)
    VALUES(@nombre, @descripcion);
END;
GO

-- STORED_PROCEDURE insert_continente
GO
CREATE OR ALTER PROCEDURE r4l.sp_insert_continente
    @nombre NVARCHAR(20)
AS
BEGIN
    INSERT INTO r4l.continentes(nombre) VALUES(@nombre);
END;
GO

-- STORED_PROCEDURE insert_pais
GO
CREATE OR ALTER PROCEDURE r4l.sp_insert_pais
	@id_continente INT,
    @nombre NVARCHAR(100),
	@codigo_iso CHAR(5),
	@prefijo_telefonico CHAR(5)
AS
BEGIN
    INSERT INTO r4l.paises(id_continente, nombre, codigo_iso, prefijo_telefonico)
	VALUES(@id_continente, @nombre, @codigo_iso, @prefijo_telefonico);
END;
GO

-- STORED_PROCEDURE insert_documento_legal
GO
CREATE OR ALTER PROCEDURE r4l.sp_insert_documento_legal
    @nombre NVARCHAR(100)
AS
BEGIN
    INSERT INTO r4l.documentos_legales(nombre) VALUES(@nombre);
END;
GO

-- STORED_PROCEDURE insert_sucursal
GO
CREATE OR ALTER PROCEDURE r4l.sp_insert_sucursal
    @nombre NVARCHAR(100),
    @ubicacion NVARCHAR(255),
    @codigo VARCHAR(10)
AS
BEGIN
    INSERT INTO r4l.sucursales(nombre, ubicacion, codigo)
    VALUES(@nombre, @ubicacion, @codigo);
END;
GO

-- STORED_PROCEDURE insert_departamento
GO
CREATE OR ALTER PROCEDURE r4l.sp_insert_departamento
    @nombre NVARCHAR(100)
AS
BEGIN
    INSERT INTO r4l.departamentos(nombre) VALUES(@nombre);
END;
GO

-- STORED_PROCEDURE insert_tipo_contrato
GO
CREATE OR ALTER PROCEDURE r4l.sp_insert_tipo_contrato
    @nombre NVARCHAR(50)
AS
BEGIN
    INSERT INTO r4l.tipos_contratos(nombre) VALUES(@nombre);
END;
GO

-- STORED_PROCEDURE insert_especialidad
GO
CREATE OR ALTER PROCEDURE r4l.sp_insert_especialidad
    @nombre NVARCHAR(100)
AS
BEGIN
    INSERT INTO r4l.especialidades(nombre) VALUES(@nombre);
END;
GO

-- STORED_PROCEDURE insert_subespecialidad
GO
CREATE OR ALTER PROCEDURE r4l.sp_insert_subespecialidad
    @id_especialidad INT,
    @nombre NVARCHAR(100)
AS
BEGIN
    INSERT INTO r4l.subespecialidades(id_especialidad, nombre)
    VALUES(@id_especialidad, @nombre);
END;
GO

-- STORED_PROCEDURE insert_resultado_curso
GO
CREATE OR ALTER PROCEDURE r4l.sp_insert_resultado_curso
    @nombre NVARCHAR(20)
AS
BEGIN
    INSERT INTO r4l.resultados_cursos(nombre) VALUES(@nombre);
END;
GO

-- STORED_PROCEDURE insert_procedimiento
GO
CREATE OR ALTER PROCEDURE r4l.sp_insert_procedimiento
    @nombre NVARCHAR(255),
    @descripcion NVARCHAR(500)
AS
BEGIN
    INSERT INTO r4l.procedimientos(nombre, descripcion)
    VALUES(@nombre, @descripcion);
END;
GO

-- STORED_PROCEDURE insert_comida
GO
CREATE OR ALTER PROCEDURE r4l.sp_insert_comida
    @nombre NVARCHAR(20)
AS
BEGIN
    INSERT INTO r4l.comidas(nombre) VALUES(@nombre);
END;
GO