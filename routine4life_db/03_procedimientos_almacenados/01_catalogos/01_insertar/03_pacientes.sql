-- PROCEDIMIENTO ALMACENADO r4l.usp_insertar_tipos_registros
go
create or alter procedure r4l.usp_insertar_tipos_registros
    @id_unidad int,
    @nombre nvarchar(50),
    @descripcion nvarchar(255) = null
as
begin
    set nocount on;
    begin try
        insert into r4l.tipos_registros(id_unidad, nombre, descripcion)
        values(@id_unidad, @nombre, @descripcion);
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al insertar tipo de registro: %s', 16, 1, @mensaje_error);
    end catch
end;
go