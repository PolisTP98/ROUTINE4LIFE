-- PROCEDIMIENTO ALMACENADO r4l.usp_insertar_sexos
go
create or alter procedure r4l.usp_insertar_sexos
    @nombre nvarchar(20)
as
begin
    set nocount on;
    begin try
        insert into r4l.sexos(nombre)
        values(@nombre);
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al insertar sexo: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_insertar_continentes
go
create or alter procedure r4l.usp_insertar_continentes
    @nombre nvarchar(20)
as
begin
    set nocount on;
    begin try
        insert into r4l.continentes(nombre)
        values(@nombre);
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al insertar continente: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_insertar_paises
go
create or alter procedure r4l.usp_insertar_paises
    @id_continente int,
    @nombre nvarchar(50),
    @codigo_iso char(3),
    @codigo_telefonico varchar(6)
as
begin
    set nocount on;
    begin try
        insert into r4l.paises(id_continente, nombre, codigo_iso, codigo_telefonico)
        values(@id_continente, @nombre, @codigo_iso, @codigo_telefonico);
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al insertar país: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_insertar_comidas
go
create or alter procedure r4l.usp_insertar_comidas
    @nombre nvarchar(20)
as
begin
    set nocount on;
    begin try
        insert into r4l.comidas(nombre)
        values(@nombre);
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al insertar comida: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_insertar_roles_usuarios
go
create or alter procedure r4l.usp_insertar_roles_usuarios
    @nombre nvarchar(20)
as
begin
    set nocount on;
    begin try
        insert into r4l.roles_usuarios(nombre)
        values(@nombre);
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al insertar rol de usuario: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_insertar_estatus_usuarios
go
create or alter procedure r4l.usp_insertar_estatus_usuarios
    @nombre nvarchar(20),
    @descripcion nvarchar(100) = null
as
begin
    set nocount on;
    begin try
        insert into r4l.estatus_usuarios(nombre, descripcion)
        values(@nombre, @descripcion);
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al insertar estatus de usuario: %s', 16, 1, @mensaje_error);
    end catch
end;
go