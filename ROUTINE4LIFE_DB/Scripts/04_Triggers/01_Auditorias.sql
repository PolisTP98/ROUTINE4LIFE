/*
==========================================================================================================================================================

-	Autor: Isaac Abdiel Sánchez López.
-	Fecha de creación: 03/11/2025.
-	Fecha de la última actualización: 03/11/2025.
-	Título: Triggers de auditorías.
-	Descripción: En este archivo se crean los TRIGGERS para llenar las tablas de auditorías cuando se detecte un cambio en una tabla principal de la
	base de datos.

==========================================================================================================================================================
*/


-- TRIGGER medico_personal
GO
CREATE OR ALTER TRIGGER r4l.trg_aud_medico_personal
ON r4l.medico_personal
AFTER INSERT, UPDATE, DELETE
AS
BEGIN
    SET NOCOUNT ON;
    DECLARE @usuario NVARCHAR(100) = SYSTEM_USER;

    -- INSERT
    INSERT INTO r4l.aud_medico_personal(id_medico, accion, usuario, datos_nuevos)
    SELECT i.id_medico, 'I', @usuario, (SELECT i.* FOR JSON PATH)
    FROM inserted i;

    -- DELETE
    INSERT INTO r4l.aud_medico_personal(id_medico, accion, usuario, datos_anteriores)
    SELECT d.id_medico, 'D', @usuario, (SELECT d.* FOR JSON PATH)
    FROM deleted d;

    -- UPDATE
    INSERT INTO r4l.aud_medico_personal(id_medico, accion, usuario, datos_anteriores, datos_nuevos)
    SELECT i.id_medico, 'U', @usuario, (SELECT d.* FOR JSON PATH), (SELECT i.* FOR JSON PATH)
    FROM inserted i
    INNER JOIN deleted d ON i.id_medico = d.id_medico;
END;
GO

-- TRIGGER medico_laboral
GO
CREATE OR ALTER TRIGGER r4l.trg_aud_medico_laboral
ON r4l.medico_laboral
AFTER INSERT, UPDATE, DELETE
AS
BEGIN
    SET NOCOUNT ON;
    DECLARE @usuario NVARCHAR(100) = SYSTEM_USER;

    INSERT INTO r4l.aud_medico_laboral(id_medico, accion, usuario, datos_nuevos)
    SELECT i.id_medico, 'I', @usuario, (SELECT i.* FOR JSON PATH) FROM inserted i;

    INSERT INTO r4l.aud_medico_laboral(id_medico, accion, usuario, datos_anteriores)
    SELECT d.id_medico, 'D', @usuario, (SELECT d.* FOR JSON PATH) FROM deleted d;

    INSERT INTO r4l.aud_medico_laboral(id_medico, accion, usuario, datos_anteriores, datos_nuevos)
    SELECT i.id_medico, 'U', @usuario, (SELECT d.* FOR JSON PATH), (SELECT i.* FOR JSON PATH)
    FROM inserted i
    INNER JOIN deleted d ON i.id_medico = d.id_medico;
END;
GO

-- TRIGGER historial_salarial
GO
CREATE OR ALTER TRIGGER r4l.trg_aud_historial_salarial
ON r4l.historial_salarial
AFTER INSERT, UPDATE, DELETE
AS
BEGIN
    SET NOCOUNT ON;
    DECLARE @usuario NVARCHAR(100) = SYSTEM_USER;

    INSERT INTO r4l.aud_historial_salarial(id_historial, accion, usuario, datos_nuevos)
    SELECT i.id_historial, 'I', @usuario, (SELECT i.* FOR JSON PATH) FROM inserted i;

    INSERT INTO r4l.aud_historial_salarial(id_historial, accion, usuario, datos_anteriores)
    SELECT d.id_historial, 'D', @usuario, (SELECT d.* FOR JSON PATH) FROM deleted d;

    INSERT INTO r4l.aud_historial_salarial(id_historial, accion, usuario, datos_anteriores, datos_nuevos)
    SELECT i.id_historial, 'U', @usuario, (SELECT d.* FOR JSON PATH), (SELECT i.* FOR JSON PATH)
    FROM inserted i
    INNER JOIN deleted d ON i.id_historial = d.id_historial;
END;
GO

-- TRIGGER especialidades_medico
GO
CREATE OR ALTER TRIGGER r4l.trg_aud_especialidades_medico
ON r4l.especialidades_medico
AFTER INSERT, UPDATE, DELETE
AS
BEGIN
    SET NOCOUNT ON;
    DECLARE @usuario NVARCHAR(100) = SYSTEM_USER;

    INSERT INTO r4l.aud_especialidades_medico(id_especialidad, accion, usuario, datos_nuevos)
    SELECT i.id_especialidad, 'I', @usuario, (SELECT i.* FOR JSON PATH) FROM inserted i;

    INSERT INTO r4l.aud_especialidades_medico(id_especialidad, accion, usuario, datos_anteriores)
    SELECT d.id_especialidad, 'D', @usuario, (SELECT d.* FOR JSON PATH) FROM deleted d;

    INSERT INTO r4l.aud_especialidades_medico(id_especialidad, accion, usuario, datos_anteriores, datos_nuevos)
    SELECT i.id_especialidad, 'U', @usuario, (SELECT d.* FOR JSON PATH), (SELECT i.* FOR JSON PATH)
    FROM inserted i
    INNER JOIN deleted d ON i.id_especialidad = d.id_especialidad;
END;
GO

-- TRIGGER subespecialidades_medico
GO
CREATE OR ALTER TRIGGER r4l.trg_aud_subespecialidades_medico
ON r4l.subespecialidades_medico
AFTER INSERT, UPDATE, DELETE
AS
BEGIN
    SET NOCOUNT ON;
    DECLARE @usuario NVARCHAR(100) = SYSTEM_USER;

    INSERT INTO r4l.aud_subespecialidades_medico(id_subespecialidad, accion, usuario, datos_nuevos)
    SELECT i.id_subespecialidad, 'I', @usuario, (SELECT i.* FOR JSON PATH) FROM inserted i;

    INSERT INTO r4l.aud_subespecialidades_medico(id_subespecialidad, accion, usuario, datos_anteriores)
    SELECT d.id_subespecialidad, 'D', @usuario, (SELECT d.* FOR JSON PATH) FROM deleted d;

    INSERT INTO r4l.aud_subespecialidades_medico(id_subespecialidad, accion, usuario, datos_anteriores, datos_nuevos)
    SELECT i.id_subespecialidad, 'U', @usuario, (SELECT d.* FOR JSON PATH), (SELECT i.* FOR JSON PATH)
    FROM inserted i
    INNER JOIN deleted d ON i.id_subespecialidad = d.id_subespecialidad;
END;
GO

-- TRIGGER cursos
GO
CREATE OR ALTER TRIGGER r4l.trg_aud_cursos
ON r4l.cursos
AFTER INSERT, UPDATE, DELETE
AS
BEGIN
    SET NOCOUNT ON;
    DECLARE @usuario NVARCHAR(100) = SYSTEM_USER;

    INSERT INTO r4l.aud_cursos(id_curso, accion, usuario, datos_nuevos)
    SELECT i.id_curso, 'I', @usuario, (SELECT i.* FOR JSON PATH) FROM inserted i;

    INSERT INTO r4l.aud_cursos(id_curso, accion, usuario, datos_anteriores)
    SELECT d.id_curso, 'D', @usuario, (SELECT d.* FOR JSON PATH) FROM deleted d;

    INSERT INTO r4l.aud_cursos(id_curso, accion, usuario, datos_anteriores, datos_nuevos)
    SELECT i.id_curso, 'U', @usuario, (SELECT d.* FOR JSON PATH), (SELECT i.* FOR JSON PATH)
    FROM inserted i
    INNER JOIN deleted d ON i.id_curso = d.id_curso;
END;
GO

-- TRIGGER procedimientos_medico
GO
CREATE OR ALTER TRIGGER r4l.trg_aud_procedimientos_medico
ON r4l.procedimientos_medico
AFTER INSERT, UPDATE, DELETE
AS
BEGIN
    SET NOCOUNT ON;
    DECLARE @usuario NVARCHAR(100) = SYSTEM_USER;

    INSERT INTO r4l.aud_procedimientos_medico(id_procedimiento, accion, usuario, datos_nuevos)
    SELECT i.id_procedimiento, 'I', @usuario, (SELECT i.* FOR JSON PATH) FROM inserted i;

    INSERT INTO r4l.aud_procedimientos_medico(id_procedimiento, accion, usuario, datos_anteriores)
    SELECT d.id_procedimiento, 'D', @usuario, (SELECT d.* FOR JSON PATH) FROM deleted d;

    INSERT INTO r4l.aud_procedimientos_medico(id_procedimiento, accion, usuario, datos_anteriores, datos_nuevos)
    SELECT i.id_procedimiento, 'U', @usuario, (SELECT d.* FOR JSON PATH), (SELECT i.* FOR JSON PATH)
    FROM inserted i
    INNER JOIN deleted d ON i.id_procedimiento = d.id_procedimiento;
END;
GO

-- TRIGGER usuarios
GO
CREATE OR ALTER TRIGGER r4l.trg_aud_usuarios
ON r4l.usuarios
AFTER INSERT, UPDATE, DELETE
AS
BEGIN
    SET NOCOUNT ON;
    DECLARE @usuario NVARCHAR(100) = SYSTEM_USER;

    INSERT INTO r4l.aud_usuarios(id_medico, accion, usuario, datos_nuevos)
    SELECT i.id_medico, 'I', @usuario, (SELECT i.* FOR JSON PATH) FROM inserted i;

    INSERT INTO r4l.aud_usuarios(id_medico, accion, usuario, datos_anteriores)
    SELECT d.id_medico, 'D', @usuario, (SELECT d.* FOR JSON PATH) FROM deleted d;

    INSERT INTO r4l.aud_usuarios(id_medico, accion, usuario, datos_anteriores, datos_nuevos)
    SELECT i.id_medico, 'U', @usuario, (SELECT d.* FOR JSON PATH), (SELECT i.* FOR JSON PATH)
    FROM inserted i
    INNER JOIN deleted d ON i.id_medico = d.id_medico;
END;
GO

-- TRIGGER pacientes
GO
CREATE OR ALTER TRIGGER r4l.trg_aud_pacientes
ON r4l.pacientes
AFTER INSERT, UPDATE, DELETE
AS
BEGIN
    SET NOCOUNT ON;
    DECLARE @usuario NVARCHAR(100) = SYSTEM_USER;

    INSERT INTO r4l.aud_pacientes(id_paciente, accion, usuario, datos_nuevos)
    SELECT i.id_paciente, 'I', @usuario, (SELECT i.* FOR JSON PATH) FROM inserted i;

    INSERT INTO r4l.aud_pacientes(id_paciente, accion, usuario, datos_anteriores)
    SELECT d.id_paciente, 'D', @usuario, (SELECT d.* FOR JSON PATH) FROM deleted d;

    INSERT INTO r4l.aud_pacientes(id_paciente, accion, usuario, datos_anteriores, datos_nuevos)
    SELECT i.id_paciente, 'U', @usuario, (SELECT d.* FOR JSON PATH), (SELECT i.* FOR JSON PATH)
    FROM inserted i
    INNER JOIN deleted d ON i.id_paciente = d.id_paciente;
END;
GO

-- TRIGGER cita_paciente
GO
CREATE OR ALTER TRIGGER r4l.trg_aud_cita_paciente
ON r4l.cita_paciente
AFTER INSERT, UPDATE, DELETE
AS
BEGIN
    SET NOCOUNT ON;
    DECLARE @usuario NVARCHAR(100) = SYSTEM_USER;

    INSERT INTO r4l.aud_cita_paciente(id_cita, accion, usuario, datos_nuevos)
    SELECT i.id_cita, 'I', @usuario, (SELECT i.* FOR JSON PATH) FROM inserted i;

    INSERT INTO r4l.aud_cita_paciente(id_cita, accion, usuario, datos_anteriores)
    SELECT d.id_cita, 'D', @usuario, (SELECT d.* FOR JSON PATH) FROM deleted d;

    INSERT INTO r4l.aud_cita_paciente(id_cita, accion, usuario, datos_anteriores, datos_nuevos)
    SELECT i.id_cita, 'U', @usuario, (SELECT d.* FOR JSON PATH), (SELECT i.* FOR JSON PATH)
    FROM inserted i
    INNER JOIN deleted d ON i.id_cita = d.id_cita;
END;
GO

-- TRIGGER sintomas_paciente
GO
CREATE OR ALTER TRIGGER r4l.trg_aud_sintomas_paciente
ON r4l.sintomas_paciente
AFTER INSERT, UPDATE, DELETE
AS
BEGIN
    SET NOCOUNT ON;
    DECLARE @usuario NVARCHAR(100) = SYSTEM_USER;

    INSERT INTO r4l.aud_sintomas_paciente(id_sintoma, accion, usuario, datos_nuevos)
    SELECT i.id_sintoma, 'I', @usuario, (SELECT i.* FOR JSON PATH) FROM inserted i;

    INSERT INTO r4l.aud_sintomas_paciente(id_sintoma, accion, usuario, datos_anteriores)
    SELECT d.id_sintoma, 'D', @usuario, (SELECT d.* FOR JSON PATH) FROM deleted d;

    INSERT INTO r4l.aud_sintomas_paciente(id_sintoma, accion, usuario, datos_anteriores, datos_nuevos)
    SELECT i.id_sintoma, 'U', @usuario, (SELECT d.* FOR JSON PATH), (SELECT i.* FOR JSON PATH)
    FROM inserted i
    INNER JOIN deleted d ON i.id_sintoma = d.id_sintoma;
END;
GO

-- TRIGGER tratamiento_paciente
GO
CREATE OR ALTER TRIGGER r4l.trg_aud_tratamientos_paciente
ON r4l.tratamientos_paciente
AFTER INSERT, UPDATE, DELETE
AS
BEGIN
    SET NOCOUNT ON;
    DECLARE @usuario NVARCHAR(100) = SYSTEM_USER;

    INSERT INTO r4l.aud_tratamientos_paciente(id_tratamiento, accion, usuario, datos_nuevos)
    SELECT i.id_tratamiento, 'I', @usuario, (SELECT i.* FOR JSON PATH) FROM inserted i;

    INSERT INTO r4l.aud_tratamientos_paciente(id_tratamiento, accion, usuario, datos_anteriores)
    SELECT d.id_tratamiento, 'D', @usuario, (SELECT d.* FOR JSON PATH) FROM deleted d;

    INSERT INTO r4l.aud_tratamientos_paciente(id_tratamiento, accion, usuario, datos_anteriores, datos_nuevos)
    SELECT i.id_tratamiento, 'U', @usuario, (SELECT d.* FOR JSON PATH), (SELECT i.* FOR JSON PATH)
    FROM inserted i
    INNER JOIN deleted d ON i.id_tratamiento = d.id_tratamiento;
END;
GO

-- TRIGGER rutina_ejercicio
GO
CREATE OR ALTER TRIGGER r4l.trg_aud_rutina_ejercicio
ON r4l.rutina_ejercicio
AFTER INSERT, UPDATE, DELETE
AS
BEGIN
    SET NOCOUNT ON;
    DECLARE @usuario NVARCHAR(100) = SYSTEM_USER;

    INSERT INTO r4l.aud_rutina_ejercicio(id_rutina_ejercicio, accion, usuario, datos_nuevos)
    SELECT i.id_rutina_ejercicio, 'I', @usuario, (SELECT i.* FOR JSON PATH) FROM inserted i;

    INSERT INTO r4l.aud_rutina_ejercicio(id_rutina_ejercicio, accion, usuario, datos_anteriores)
    SELECT d.id_rutina_ejercicio, 'D', @usuario, (SELECT d.* FOR JSON PATH) FROM deleted d;

    INSERT INTO r4l.aud_rutina_ejercicio(id_rutina_ejercicio, accion, usuario, datos_anteriores, datos_nuevos)
    SELECT i.id_rutina_ejercicio, 'U', @usuario, (SELECT d.* FOR JSON PATH), (SELECT i.* FOR JSON PATH)
    FROM inserted i
    INNER JOIN deleted d ON i.id_rutina_ejercicio = d.id_rutina_ejercicio;
END;
GO

-- TRIGGER rutina_alimentacion
GO
CREATE OR ALTER TRIGGER r4l.trg_aud_rutina_alimentacion
ON r4l.rutina_alimentacion
AFTER INSERT, UPDATE, DELETE
AS
BEGIN
    SET NOCOUNT ON;
    DECLARE @usuario NVARCHAR(100) = SYSTEM_USER;

    INSERT INTO r4l.aud_rutina_alimentacion(id_rutina_alimentacion, accion, usuario, datos_nuevos)
    SELECT i.id_rutina_alimentacion, 'I', @usuario, (SELECT i.* FOR JSON PATH) FROM inserted i;

    INSERT INTO r4l.aud_rutina_alimentacion(id_rutina_alimentacion, accion, usuario, datos_anteriores)
    SELECT d.id_rutina_alimentacion, 'D', @usuario, (SELECT d.* FOR JSON PATH) FROM deleted d;

    INSERT INTO r4l.aud_rutina_alimentacion(id_rutina_alimentacion, accion, usuario, datos_anteriores, datos_nuevos)
    SELECT i.id_rutina_alimentacion, 'U', @usuario, (SELECT d.* FOR JSON PATH), (SELECT i.* FOR JSON PATH)
    FROM inserted i
    INNER JOIN deleted d ON i.id_rutina_alimentacion = d.id_rutina_alimentacion;
END;
GO