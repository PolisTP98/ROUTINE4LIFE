/*
==========================================================================================================================================================

-	Autor: Isaac Abdiel Sánchez López.
-	Fecha de creación: 06/11/2025.
-	Fecha de la última actualización: 06/11/2025.
-	Título: Procedimientos almacenados para eliminar registros.
-	Descripción: En este archivo se crean los procedimientos almacenados para eliminar registros de manera lógica de las tablas catálogo de la base de
	datos.

==========================================================================================================================================================
*/


-- STORED_PROCEDURE delete_sexo
GO
CREATE OR ALTER PROCEDURE r4l.sp_delete_sexo
    @id_sexo INT
AS
BEGIN
    DELETE FROM r4l.sexos
    WHERE id_sexo = @id_sexo;
END;
GO

-- STORED_PROCEDURE delete_rol_usuario
GO
CREATE OR ALTER PROCEDURE r4l.sp_delete_rol_usuario
    @id_rol INT
AS
BEGIN
    DELETE FROM r4l.roles_usuarios
    WHERE id_rol = @id_rol;
END;
GO

-- STORED_PROCEDURE delete_estatus_usuario
GO
CREATE OR ALTER PROCEDURE r4l.sp_delete_estatus_usuario
    @id_estatus INT
AS
BEGIN
    DELETE FROM r4l.estatus_usuarios
    WHERE id_estatus = @id_estatus;
END;
GO

-- STORED_PROCEDURE delete_continente
GO
CREATE OR ALTER PROCEDURE r4l.sp_delete_continente
    @id_continente INT
AS
BEGIN
    DELETE FROM r4l.continentes
    WHERE id_continente = @id_continente;
END;
GO

-- STORED_PROCEDURE delete_pais
GO
CREATE OR ALTER PROCEDURE r4l.sp_delete_pais
    @id_pais INT
AS
BEGIN
    DELETE FROM r4l.paises
    WHERE id_pais = @id_pais;
END;
GO

-- STORED_PROCEDURE delete_documento_legal
GO
CREATE OR ALTER PROCEDURE r4l.sp_delete_documento_legal
    @id_documento INT
AS
BEGIN
    DELETE FROM r4l.documentos_legales
    WHERE id_documento = @id_documento;
END;
GO

-- STORED_PROCEDURE delete_sucursal
GO
CREATE OR ALTER PROCEDURE r4l.sp_delete_sucursal
    @id_sucursal INT
AS
BEGIN
    DELETE FROM r4l.sucursales
    WHERE id_sucursal = @id_sucursal;
END;
GO

-- STORED_PROCEDURE delete_departamento
GO
CREATE OR ALTER PROCEDURE r4l.sp_delete_departamento
    @id_departamento INT
AS
BEGIN
    DELETE FROM r4l.departamentos
    WHERE id_departamento = @id_departamento;
END;
GO

-- STORED_PROCEDURE delete_tipo_contrato
GO
CREATE OR ALTER PROCEDURE r4l.sp_delete_tipo_contrato
    @id_contrato INT
AS
BEGIN
    DELETE FROM r4l.tipos_contratos
    WHERE id_contrato = @id_contrato;
END;
GO

-- STORED_PROCEDURE delete_especialidad
GO
CREATE OR ALTER PROCEDURE r4l.sp_delete_especialidad
    @id_especialidad INT
AS
BEGIN
    DELETE FROM r4l.especialidades
    WHERE id_especialidad = @id_especialidad;
END;
GO

-- STORED_PROCEDURE delete_subespecialidad
GO
CREATE OR ALTER PROCEDURE r4l.sp_delete_subespecialidad
    @id_subespecialidad INT
AS
BEGIN
    DELETE FROM r4l.subespecialidades
    WHERE id_subespecialidad = @id_subespecialidad;
END;
GO

-- STORED_PROCEDURE delete_resultado_curso
GO
CREATE OR ALTER PROCEDURE r4l.sp_delete_resultado_curso
    @id_resultado INT
AS
BEGIN
    DELETE FROM r4l.resultados_cursos
    WHERE id_resultado = @id_resultado;
END;
GO

-- STORED_PROCEDURE delete_procedimiento
GO
CREATE OR ALTER PROCEDURE r4l.sp_delete_procedimiento
    @id_procedimiento INT
AS
BEGIN
    DELETE FROM r4l.procedimientos
    WHERE id_procedimiento = @id_procedimiento;
END;
GO

-- STORED_PROCEDURE delete_comida
GO
CREATE OR ALTER PROCEDURE r4l.sp_delete_comida
    @id_comida INT
AS
BEGIN
    DELETE FROM r4l.comidas
    WHERE id_comida = @id_comida;
END;
GO