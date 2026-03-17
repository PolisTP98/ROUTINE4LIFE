-- PROCEDIMIENTO ALMACENADO r4l.usp_actualizar_tipos_registros
go
create or alter procedure r4l.usp_actualizar_tipos_registros
    @id_tipo_registro int,
    @id_unidad int = null,
    @nombre nvarchar(50) = null,
    @descripcion nvarchar(255) = null
as
begin
    set nocount on;
    begin try
        update r4l.tipos_registros
        set id_unidad = coalesce(@id_unidad, id_unidad),
            nombre = coalesce(@nombre, nombre),
            descripcion = case 
                when @descripcion is not null then @descripcion 
                else descripcion 
            end
        where id_tipo_registro = @id_tipo_registro;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al actualizar tipo de registro: %s', 16, 1, @mensaje_error);
    end catch
end;
go