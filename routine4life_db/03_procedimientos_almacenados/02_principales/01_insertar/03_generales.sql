-- PROCEDIMIENTO ALMACENADO r4l.usp_insertar_usuarios
go
create or alter procedure r4l.usp_insertar_usuarios
    @id_rol int, 
    @id_medico int = null, 
    @id_paciente int = null, 
    @contrasena nvarchar(255)
as
begin
    set nocount on;
    begin try
        if(@id_medico is null and @id_paciente is null) or (@id_medico is not null and @id_paciente is not null)
        begin
            raiserror('Debe especificar exactamente un id_medico o un id_paciente.', 16, 1);
            return;
        end

        insert into r4l.usuarios(
            id_rol, id_medico, id_paciente, contrasena, fecha_registro
        )
        values(
            @id_rol, @id_medico, @id_paciente, @contrasena, cast(getdate() as date)
        );
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al insertar usuario: %s', 16, 1, @mensaje_error);
    end catch
end;
go