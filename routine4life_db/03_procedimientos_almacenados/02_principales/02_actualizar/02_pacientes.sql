-- PROCEDIMIENTO ALMACENADO r4l.usp_actualizar_pacientes_aplicacion
go
create or alter procedure r4l.usp_actualizar_pacientes_aplicacion
    @id_paciente int, 
    @id_sexo int = null, 
    @id_pais int = null, 
    @id_estatus_usuario int = null, 
    @nombre_completo nvarchar(255) = null, 
    @fecha_nacimiento date = null, 
    @email varchar(255) = null, 
    @telefono varchar(20) = null
as
begin
    set nocount on;
    begin try
        update r4l.pacientes_aplicacion 
        set id_sexo = coalesce(@id_sexo, id_sexo), 
            id_pais = coalesce(@id_pais, id_pais), 
            id_estatus_usuario = coalesce(@id_estatus_usuario, id_estatus_usuario), 
            nombre_completo = coalesce(@nombre_completo, nombre_completo), 
            fecha_nacimiento = coalesce(@fecha_nacimiento, fecha_nacimiento), 
            email = coalesce(@email, email), 
            telefono = coalesce(@telefono, telefono) 
        where id_paciente = @id_paciente;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al actualizar paciente de aplicación: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_actualizar_registros_paciente
go
create or alter procedure r4l.usp_actualizar_registros_paciente
    @id_registro int, 
    @id_paciente int = null, 
    @id_tipo_registro int = null, 
    @fecha date = null, 
    @hora time(0) = null, 
    @valor decimal(10, 2) = null, 
    @unidad_alternativa nvarchar(20) = null, 
    @notas nvarchar(255) = null
as
begin
    set nocount on;
    begin try
        update r4l.registros_paciente 
        set id_paciente = coalesce(@id_paciente, id_paciente), 
            id_tipo_registro = coalesce(@id_tipo_registro, id_tipo_registro), 
            fecha = coalesce(@fecha, fecha), 
            hora = coalesce(@hora, hora), 
            valor = coalesce(@valor, valor), 
            unidad_alternativa = coalesce(@unidad_alternativa, unidad_alternativa), 
            notas = coalesce(@notas, notas) 
        where id_registro = @id_registro;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al actualizar registro de paciente: %s', 16, 1, @mensaje_error);
    end catch
end;
go