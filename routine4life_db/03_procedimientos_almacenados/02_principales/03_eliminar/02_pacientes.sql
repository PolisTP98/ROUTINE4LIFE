-- PROCEDIMIENTO ALMACENADO r4l.usp_eliminar_pacientes_aplicacion
go
create or alter procedure r4l.usp_eliminar_pacientes_aplicacion
    @id_paciente int
as
begin
    set nocount on;
    begin try
        update r4l.pacientes_aplicacion 
        set id_estatus_usuario = 2, 
            fecha_hora_eliminacion = sysdatetime() 
        where id_paciente = @id_paciente;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al eliminar paciente de aplicación: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_eliminar_registros_paciente
go
create or alter procedure r4l.usp_eliminar_registros_paciente
    @id_registro int
as
begin
    set nocount on;
    begin try
        delete from r4l.registros_paciente where id_registro = @id_registro;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al eliminar registro de paciente: %s', 16, 1, @mensaje_error);
    end catch
end;
go