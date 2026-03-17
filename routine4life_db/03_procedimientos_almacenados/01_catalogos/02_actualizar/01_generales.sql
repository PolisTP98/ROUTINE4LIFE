-- PROCEDIMIENTO ALMACENADO r4l.usp_actualizar_sexos
go
create or alter procedure r4l.usp_actualizar_sexos
    @id_sexo int,
    @nombre nvarchar(20) = null
as
begin
    set nocount on;
    begin try
        update r4l.sexos
        set nombre = coalesce(@nombre, nombre)
        where id_sexo = @id_sexo;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al actualizar sexo: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_actualizar_continentes
go
create or alter procedure r4l.usp_actualizar_continentes
    @id_continente int,
    @nombre nvarchar(20) = null
as
begin
    set nocount on;
    begin try
        update r4l.continentes
        set nombre = coalesce(@nombre, nombre)
        where id_continente = @id_continente;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al actualizar continente: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_actualizar_paises
go
create or alter procedure r4l.usp_actualizar_paises
    @id_pais int,
    @id_continente int = null,
    @nombre nvarchar(50) = null,
    @codigo_iso char(3) = null,
    @codigo_telefonico varchar(6) = null
as
begin
    set nocount on;
    begin try
        update r4l.paises
        set id_continente = coalesce(@id_continente, id_continente),
            nombre = coalesce(@nombre, nombre),
            codigo_iso = coalesce(@codigo_iso, codigo_iso),
            codigo_telefonico = coalesce(@codigo_telefonico, codigo_telefonico)
        where id_pais = @id_pais;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al actualizar país: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_actualizar_comidas
go
create or alter procedure r4l.usp_actualizar_comidas
    @id_comida int,
    @nombre nvarchar(20) = null
as
begin
    set nocount on;
    begin try
        update r4l.comidas
        set nombre = coalesce(@nombre, nombre)
        where id_comida = @id_comida;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al actualizar comida: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_actualizar_roles_usuarios
go
create or alter procedure r4l.usp_actualizar_roles_usuarios
    @id_rol int,
    @nombre nvarchar(20) = null
as
begin
    set nocount on;
    begin try
        update r4l.roles_usuarios
        set nombre = coalesce(@nombre, nombre)
        where id_rol = @id_rol;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al actualizar rol de usuario: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_actualizar_estatus_usuarios
go
create or alter procedure r4l.usp_actualizar_estatus_usuarios
    @id_estatus_usuario int,
    @nombre nvarchar(20) = null,
    @descripcion nvarchar(100) = null
as
begin
    set nocount on;
    begin try
        update r4l.estatus_usuarios
        set nombre = coalesce(@nombre, nombre),
            descripcion = case 
                when @descripcion is not null then @descripcion 
                else descripcion 
            end
        where id_estatus_usuario = @id_estatus_usuario;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al actualizar estatus de usuario: %s', 16, 1, @mensaje_error);
    end catch
end;
go