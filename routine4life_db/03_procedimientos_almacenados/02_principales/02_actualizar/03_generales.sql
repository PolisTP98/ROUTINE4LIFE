-- PROCEDIMIENTO ALMACENADO r4l.usp_actualizar_usuarios
go
create or alter procedure r4l.usp_actualizar_usuarios
    @id_usuario int, 
    @contrasena nvarchar(255)
as
begin
    set nocount on;
    begin try
        update r4l.usuarios 
        set contrasena = @contrasena 
        where id_usuario = @id_usuario;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al actualizar contraseña del usuario: %s', 16, 1, @mensaje_error);
    end catch
end;
go