/*
==========================================================================================================================================================

-	Autor: Isaac Abdiel Sánchez López.
-	Fecha de creación: 01/11/2025.
-	Fecha de la última actualización: 07/11/2025.
-	Título: Tablas catálogo.
-	Descripción: En este archivo se crean las tablas que funcionarán como catálogos en la base de datos, por lo que no se actualizarán frecuentemente.

==========================================================================================================================================================
*/


GO
IF OBJECT_ID('r4l.sexos', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.sexos (
        id_sexo INT IDENTITY(1,1) PRIMARY KEY,
        nombre NVARCHAR(20) NOT NULL
    );
END

IF OBJECT_ID('r4l.roles_usuarios', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.roles_usuarios (
        id_rol INT IDENTITY(1,1) PRIMARY KEY,
        nombre NVARCHAR(50) NOT NULL
    );
END

IF OBJECT_ID('r4l.estatus_usuarios', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.estatus_usuarios (
        id_estatus INT IDENTITY(1,1) PRIMARY KEY,
        nombre NVARCHAR(50) NOT NULL,
		descripcion NVARCHAR(100) NULL
    );
END

IF OBJECT_ID('r4l.continentes', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.continentes (
        id_continente INT IDENTITY(1,1) PRIMARY KEY,
        nombre NVARCHAR(20) NOT NULL
    );
END

IF OBJECT_ID('r4l.paises', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.paises (
        id_pais INT IDENTITY(1,1) PRIMARY KEY,
		id_continente INT NOT NULL,
        nombre NVARCHAR(100) NOT NULL,
		codigo_iso CHAR(5) NOT NULL,
		prefijo_telefonico CHAR(5) NOT NULL,
		FOREIGN KEY(id_continente)
			REFERENCES r4l.continentes(id_continente)
            ON DELETE CASCADE
			ON UPDATE CASCADE
    );
END

IF OBJECT_ID('r4l.documentos_legales', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.documentos_legales (
        id_documento INT IDENTITY(1,1) PRIMARY KEY,
        nombre NVARCHAR(100) NOT NULL
    );
END

IF OBJECT_ID('r4l.sucursales', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.sucursales (
        id_sucursal INT IDENTITY(1,1) PRIMARY KEY,
        nombre NVARCHAR(100) NOT NULL,
		ubicacion NVARCHAR(255) NOT NULL,
		codigo VARCHAR(10) NOT NULL UNIQUE
    );
END

IF OBJECT_ID('r4l.departamentos', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.departamentos (
        id_departamento INT IDENTITY(1,1) PRIMARY KEY,
        nombre NVARCHAR(100) NOT NULL
    );
END

IF OBJECT_ID('r4l.tipos_contratos', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.tipos_contratos (
        id_contrato INT IDENTITY(1,1) PRIMARY KEY,
        nombre NVARCHAR(50) NOT NULL
    );
END

IF OBJECT_ID('r4l.especialidades', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.especialidades (
        id_especialidad INT IDENTITY(1,1) PRIMARY KEY,
        nombre NVARCHAR(100) NOT NULL
    );
END

IF OBJECT_ID('r4l.subespecialidades', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.subespecialidades (
        id_subespecialidad INT IDENTITY(1,1) PRIMARY KEY,
		id_especialidad INT NOT NULL,
        nombre NVARCHAR(100) NOT NULL,
		FOREIGN KEY(id_especialidad)
			REFERENCES r4l.especialidades(id_especialidad)
			ON DELETE CASCADE
			ON UPDATE CASCADE
    );
END

IF OBJECT_ID('r4l.resultados_cursos', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.resultados_cursos (
        id_resultado INT IDENTITY(1,1) PRIMARY KEY,
        nombre NVARCHAR(20) NOT NULL
    );
END


IF OBJECT_ID('r4l.procedimientos', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.procedimientos (
        id_procedimiento INT IDENTITY(1,1) PRIMARY KEY,
        nombre NVARCHAR(255) NOT NULL,
		descripcion NVARCHAR(500) NOT NULL
    );
END

IF OBJECT_ID('r4l.comidas', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.comidas (
        id_comida INT IDENTITY(1,1) PRIMARY KEY,
        nombre NVARCHAR(20) NOT NULL
    );
END
GO