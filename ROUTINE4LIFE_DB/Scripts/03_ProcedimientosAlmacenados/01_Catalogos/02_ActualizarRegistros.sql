/*
==========================================================================================================================================================

-	Autor: Isaac Abdiel Sánchez López.
-	Fecha de creación: 06/11/2025.
-	Fecha de la última actualización: 07/11/2025.
-	Título: Procedimientos almacenados para actualizar registros.
-	Descripción: En este archivo se crean los procedimientos almacenados para actualizar registros de las tablas catálogo de la base de datos.

==========================================================================================================================================================
*/


-- STORED_PROCEDURE update_sexo
GO
CREATE OR ALTER PROCEDURE r4l.sp_update_sexo
    @id_sexo INT,
    @nombre NVARCHAR(20)
AS
BEGIN
    UPDATE r4l.sexos
    SET nombre = ISNULL(@nombre, nombre)
    WHERE id_sexo = @id_sexo;
END;
GO

-- STORED_PROCEDURE update_rol_usuario
GO
CREATE OR ALTER PROCEDURE r4l.sp_update_rol_usuario
    @id_rol INT,
    @nombre NVARCHAR(50)
AS
BEGIN
    UPDATE r4l.roles_usuarios
    SET nombre = ISNULL(@nombre, nombre)
    WHERE id_rol = @id_rol;
END;
GO

-- STORED_PROCEDURE update_estatus_usuario
GO
CREATE OR ALTER PROCEDURE r4l.sp_update_estatus_usuario
    @id_estatus INT,
    @nombre NVARCHAR(50),
    @descripcion NVARCHAR(100)
AS
BEGIN
    UPDATE r4l.estatus_usuarios
    SET nombre = ISNULL(@nombre, nombre),
        descripcion = ISNULL(@descripcion, descripcion)
    WHERE id_estatus = @id_estatus;
END;
GO

-- STORED_PROCEDURE update_continente
GO
CREATE OR ALTER PROCEDURE r4l.sp_update_continente
    @id_continente INT,
    @nombre NVARCHAR(20)
AS
BEGIN
    UPDATE r4l.continentes
    SET nombre = ISNULL(@nombre, nombre)
    WHERE id_continente = @id_continente;
END;
GO

-- STORED_PROCEDURE update_pais
GO
CREATE OR ALTER PROCEDURE r4l.sp_update_pais
    @id_pais INT,
    @id_continente INT,
    @nombre NVARCHAR(100),
    @codigo_iso CHAR(5),
    @prefijo_telefonico CHAR(5)
AS
BEGIN
    UPDATE r4l.paises
    SET id_continente = ISNULL(@id_continente, id_continente),
        nombre = ISNULL(@nombre, nombre),
        codigo_iso = ISNULL(@codigo_iso, codigo_iso),
        prefijo_telefonico = ISNULL(@prefijo_telefonico, prefijo_telefonico)
    WHERE id_pais = @id_pais;
END;
GO

-- STORED_PROCEDURE update_documento_legal
GO
CREATE OR ALTER PROCEDURE r4l.sp_update_documento_legal
    @id_documento INT,
    @nombre NVARCHAR(100)
AS
BEGIN
    UPDATE r4l.documentos_legales
    SET nombre = ISNULL(@nombre, nombre)
    WHERE id_documento = @id_documento;
END;
GO

-- STORED_PROCEDURE update_sucursal
GO
CREATE OR ALTER PROCEDURE r4l.sp_update_sucursal
    @id_sucursal INT,
    @nombre NVARCHAR(100),
    @ubicacion NVARCHAR(255),
    @codigo VARCHAR(10)
AS
BEGIN
    UPDATE r4l.sucursales
    SET nombre = ISNULL(@nombre, nombre),
        ubicacion = ISNULL(@ubicacion, ubicacion),
        codigo = ISNULL(@codigo, codigo)
    WHERE id_sucursal = @id_sucursal;
END;
GO

-- STORED_PROCEDURE update_departamento
GO
CREATE OR ALTER PROCEDURE r4l.sp_update_departamento
    @id_departamento INT,
    @nombre NVARCHAR(100)
AS
BEGIN
    UPDATE r4l.departamentos
    SET nombre = ISNULL(@nombre, nombre)
    WHERE id_departamento = @id_departamento;
END;
GO

-- STORED_PROCEDURE update_tipo_contrato
GO
CREATE OR ALTER PROCEDURE r4l.sp_update_tipo_contrato
    @id_contrato INT,
    @nombre NVARCHAR(50)
AS
BEGIN
    UPDATE r4l.tipos_contratos
    SET nombre = ISNULL(@nombre, nombre)
    WHERE id_contrato = @id_contrato;
END;
GO

-- STORED_PROCEDURE update_especialidad
GO
CREATE OR ALTER PROCEDURE r4l.sp_update_especialidad
    @id_especialidad INT,
    @nombre NVARCHAR(100)
AS
BEGIN
    UPDATE r4l.especialidades
    SET nombre = ISNULL(@nombre, nombre)
    WHERE id_especialidad = @id_especialidad;
END;
GO

-- STORED_PROCEDURE update_subespecialidad
GO
CREATE OR ALTER PROCEDURE r4l.sp_update_subespecialidad
    @id_subespecialidad INT,
    @id_especialidad INT,
    @nombre NVARCHAR(100)
AS
BEGIN
    UPDATE r4l.subespecialidades
    SET id_especialidad = ISNULL(@id_especialidad, id_especialidad),
        nombre = ISNULL(@nombre, nombre)
    WHERE id_subespecialidad = @id_subespecialidad;
END;
GO

-- STORED_PROCEDURE update_resultado_curso
GO
CREATE OR ALTER PROCEDURE r4l.sp_update_resultado_curso
    @id_resultado INT,
    @nombre NVARCHAR(20)
AS
BEGIN
    UPDATE r4l.resultados_cursos
    SET nombre = ISNULL(@nombre, nombre)
    WHERE id_resultado = @id_resultado;
END;
GO

-- STORED_PROCEDURE update_procedimiento
GO
CREATE OR ALTER PROCEDURE r4l.sp_update_procedimiento
    @id_procedimiento INT,
    @nombre NVARCHAR(255),
    @descripcion NVARCHAR(500)
AS
BEGIN
    UPDATE r4l.procedimientos
    SET nombre = ISNULL(@nombre, nombre),
        descripcion = ISNULL(@descripcion, descripcion)
    WHERE id_procedimiento = @id_procedimiento;
END;
GO

-- STORED_PROCEDURE update_comida
GO
CREATE OR ALTER PROCEDURE r4l.sp_update_comida
    @id_comida INT,
    @nombre NVARCHAR(20)
AS
BEGIN
    UPDATE r4l.comidas
    SET nombre = ISNULL(@nombre, nombre)
    WHERE id_comida = @id_comida;
END;
GO