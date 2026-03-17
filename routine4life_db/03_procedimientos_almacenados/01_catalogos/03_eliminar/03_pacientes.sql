-- PROCEDIMIENTO ALMACENADO r4l.usp_eliminar_tipos_registros
go
create or alter procedure r4l.usp_eliminar_tipos_registros
    @id_tipo_registro int
as
begin
    set nocount on;
    begin try
        delete from r4l.tipos_registros where id_tipo_registro = @id_tipo_registro;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al eliminar tipo de registro: %s', 16, 1, @mensaje_error);
    end catch
end;
go