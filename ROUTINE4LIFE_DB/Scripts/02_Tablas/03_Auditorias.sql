/*
==========================================================================================================================================================

-	Autor: Isaac Abdiel Sánchez López.
-	Fecha de creación: 03/11/2025.
-	Fecha de la última actualización: 03/11/2025.
-	Título: Tablas de auditorías.
-	Descripción: En este archivo se crean las tablas de auditorías para registrar las acciones realizadas en las tablas principales de la base de datos.

==========================================================================================================================================================
*/


GO
IF OBJECT_ID('r4l.aud_medico_personal', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.aud_medico_personal (
        id_auditoria INT IDENTITY(1,1) PRIMARY KEY,
        id_medico INT NULL,
        accion CHAR(1) NOT NULL,
        usuario NVARCHAR(100) NULL,
        fecha_accion DATETIME NOT NULL DEFAULT GETDATE(),
        datos_anteriores NVARCHAR(MAX) NULL,
        datos_nuevos NVARCHAR(MAX) NULL
    );
END;

-- medico_laboral
IF OBJECT_ID('r4l.aud_medico_laboral', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.aud_medico_laboral (
        id_auditoria INT IDENTITY(1,1) PRIMARY KEY,
        id_medico INT NULL,
        accion CHAR(1) NOT NULL,
        usuario NVARCHAR(100) NULL,
        fecha_accion DATETIME NOT NULL DEFAULT GETDATE(),
        datos_anteriores NVARCHAR(MAX) NULL,
        datos_nuevos NVARCHAR(MAX) NULL
    );
END;

IF OBJECT_ID('r4l.aud_historial_salarial', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.aud_historial_salarial (
        id_auditoria INT IDENTITY(1,1) PRIMARY KEY,
        id_historial INT NULL,
        accion CHAR(1) NOT NULL,
        usuario NVARCHAR(100) NULL,
        fecha_accion DATETIME NOT NULL DEFAULT GETDATE(),
        datos_anteriores NVARCHAR(MAX) NULL,
        datos_nuevos NVARCHAR(MAX) NULL
    );
END;

IF OBJECT_ID('r4l.aud_especialidades_medico', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.aud_especialidades_medico (
        id_auditoria INT IDENTITY(1,1) PRIMARY KEY,
        id_especialidad INT NULL,
        accion CHAR(1) NOT NULL,
        usuario NVARCHAR(100) NULL,
        fecha_accion DATETIME NOT NULL DEFAULT GETDATE(),
        datos_anteriores NVARCHAR(MAX) NULL,
        datos_nuevos NVARCHAR(MAX) NULL
    );
END;

IF OBJECT_ID('r4l.aud_subespecialidades_medico', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.aud_subespecialidades_medico (
        id_auditoria INT IDENTITY(1,1) PRIMARY KEY,
        id_subespecialidad INT NULL,
        accion CHAR(1) NOT NULL,
        usuario NVARCHAR(100) NULL,
        fecha_accion DATETIME NOT NULL DEFAULT GETDATE(),
        datos_anteriores NVARCHAR(MAX) NULL,
        datos_nuevos NVARCHAR(MAX) NULL
    );
END;

IF OBJECT_ID('r4l.aud_cursos', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.aud_cursos (
        id_auditoria INT IDENTITY(1,1) PRIMARY KEY,
        id_curso INT NULL,
        accion CHAR(1) NOT NULL,
        usuario NVARCHAR(100) NULL,
        fecha_accion DATETIME NOT NULL DEFAULT GETDATE(),
        datos_anteriores NVARCHAR(MAX) NULL,
        datos_nuevos NVARCHAR(MAX) NULL
    );
END;

IF OBJECT_ID('r4l.aud_procedimientos_medico', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.aud_procedimientos_medico (
        id_auditoria INT IDENTITY(1,1) PRIMARY KEY,
        id_procedimiento INT NULL,
        accion CHAR(1) NOT NULL,
        usuario NVARCHAR(100) NULL,
        fecha_accion DATETIME NOT NULL DEFAULT GETDATE(),
        datos_anteriores NVARCHAR(MAX) NULL,
        datos_nuevos NVARCHAR(MAX) NULL
    );
END;

IF OBJECT_ID('r4l.aud_usuarios', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.aud_usuarios (
        id_auditoria INT IDENTITY(1,1) PRIMARY KEY,
        id_medico INT NULL,
        accion CHAR(1) NOT NULL,
        usuario NVARCHAR(100) NULL,
        fecha_accion DATETIME NOT NULL DEFAULT GETDATE(),
        datos_anteriores NVARCHAR(MAX) NULL,
        datos_nuevos NVARCHAR(MAX) NULL
    );
END;

IF OBJECT_ID('r4l.aud_pacientes', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.aud_pacientes (
        id_auditoria INT IDENTITY(1,1) PRIMARY KEY,
        id_paciente INT NULL,
        accion CHAR(1) NOT NULL,
        usuario NVARCHAR(100) NULL,
        fecha_accion DATETIME NOT NULL DEFAULT GETDATE(),
        datos_anteriores NVARCHAR(MAX) NULL,
        datos_nuevos NVARCHAR(MAX) NULL
    );
END;

IF OBJECT_ID('r4l.aud_cita_paciente', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.aud_cita_paciente (
        id_auditoria INT IDENTITY(1,1) PRIMARY KEY,
        id_cita INT NULL,
        accion CHAR(1) NOT NULL,
        usuario NVARCHAR(100) NULL,
        fecha_accion DATETIME NOT NULL DEFAULT GETDATE(),
        datos_anteriores NVARCHAR(MAX) NULL,
        datos_nuevos NVARCHAR(MAX) NULL
    );
END;

IF OBJECT_ID('r4l.aud_sintomas_paciente', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.aud_sintomas_paciente (
        id_auditoria INT IDENTITY(1,1) PRIMARY KEY,
        id_sintoma INT NULL,
        accion CHAR(1) NOT NULL,
        usuario NVARCHAR(100) NULL,
        fecha_accion DATETIME NOT NULL DEFAULT GETDATE(),
        datos_anteriores NVARCHAR(MAX) NULL,
        datos_nuevos NVARCHAR(MAX) NULL
    );
END;

IF OBJECT_ID('r4l.aud_tratamientos_paciente', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.aud_tratamientos_paciente (
        id_auditoria INT IDENTITY(1,1) PRIMARY KEY,
        id_tratamiento INT NULL,
        accion CHAR(1) NOT NULL,
        usuario NVARCHAR(100) NULL,
        fecha_accion DATETIME NOT NULL DEFAULT GETDATE(),
        datos_anteriores NVARCHAR(MAX) NULL,
        datos_nuevos NVARCHAR(MAX) NULL
    );
END;

IF OBJECT_ID('r4l.aud_rutina_ejercicio', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.aud_rutina_ejercicio (
        id_auditoria INT IDENTITY(1,1) PRIMARY KEY,
        id_rutina_ejercicio INT NULL,
        accion CHAR(1) NOT NULL,
        usuario NVARCHAR(100) NULL,
        fecha_accion DATETIME NOT NULL DEFAULT GETDATE(),
        datos_anteriores NVARCHAR(MAX) NULL,
        datos_nuevos NVARCHAR(MAX) NULL
    );
END;

IF OBJECT_ID('r4l.aud_rutina_alimentacion', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.aud_rutina_alimentacion (
        id_auditoria INT IDENTITY(1,1) PRIMARY KEY,
        id_rutina_alimentacion INT NULL,
        accion CHAR(1) NOT NULL,
        usuario NVARCHAR(100) NULL,
        fecha_accion DATETIME NOT NULL DEFAULT GETDATE(),
        datos_anteriores NVARCHAR(MAX) NULL,
        datos_nuevos NVARCHAR(MAX) NULL
    );
END;
GO