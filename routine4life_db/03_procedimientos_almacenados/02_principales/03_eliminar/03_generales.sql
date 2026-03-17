-- PROCEDIMIENTO ALMACENADO r4l.usp_eliminar_usuarios
go
create or alter procedure r4l.usp_eliminar_usuarios
    @id_usuario int
as
begin
    set nocount on;
    begin try
        update r4l.usuarios 
        set fecha_hora_eliminacion = sysdatetime() 
        where id_usuario = @id_usuario;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al eliminar usuario: %s', 16, 1, @mensaje_error);
    end catch
end;
go