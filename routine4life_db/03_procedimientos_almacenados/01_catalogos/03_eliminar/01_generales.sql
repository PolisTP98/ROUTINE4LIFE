-- PROCEDIMIENTO ALMACENADO r4l.usp_eliminar_sexos
go
create or alter procedure r4l.usp_eliminar_sexos
    @id_sexo int
as
begin
    set nocount on;
    begin try
        delete from r4l.sexos where id_sexo = @id_sexo;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al eliminar sexo: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_eliminar_continentes
go
create or alter procedure r4l.usp_eliminar_continentes
    @id_continente int
as
begin
    set nocount on;
    begin try
        delete from r4l.continentes where id_continente = @id_continente;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al eliminar continente: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_eliminar_paises
go
create or alter procedure r4l.usp_eliminar_paises
    @id_pais int
as
begin
    set nocount on;
    begin try
        delete from r4l.paises where id_pais = @id_pais;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al eliminar país: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_eliminar_comidas
go
create or alter procedure r4l.usp_eliminar_comidas
    @id_comida int
as
begin
    set nocount on;
    begin try
        delete from r4l.comidas where id_comida = @id_comida;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al eliminar comida: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_eliminar_roles_usuarios
go
create or alter procedure r4l.usp_eliminar_roles_usuarios
    @id_rol int
as
begin
    set nocount on;
    begin try
        delete from r4l.roles_usuarios where id_rol = @id_rol;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al eliminar rol de usuario: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_eliminar_estatus_usuarios
go
create or alter procedure r4l.usp_eliminar_estatus_usuarios
    @id_estatus_usuario int
as
begin
    set nocount on;
    begin try
        delete from r4l.estatus_usuarios where id_estatus_usuario = @id_estatus_usuario;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al eliminar estatus de usuario: %s', 16, 1, @mensaje_error);
    end catch
end;
go