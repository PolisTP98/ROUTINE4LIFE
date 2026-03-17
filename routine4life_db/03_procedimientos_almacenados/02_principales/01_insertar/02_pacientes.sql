-- PROCEDIMIENTO ALMACENADO r4l.usp_insertar_pacientes_aplicacion
go
create or alter procedure r4l.usp_insertar_pacientes_aplicacion
    @id_paciente int, 
    @id_sexo int, 
    @id_pais int, 
    @nombre_completo nvarchar(255), 
    @fecha_nacimiento date, 
    @email varchar(255), 
    @telefono varchar(20), 
    @id_estatus_usuario int = 1
as
begin
    set nocount on;
    begin try
        insert into r4l.pacientes_aplicacion(
            id_paciente, id_sexo, id_pais, id_estatus_usuario, nombre_completo, 
            fecha_nacimiento, email, telefono, fecha_registro
        )
        values(
            @id_paciente, @id_sexo, @id_pais, @id_estatus_usuario, @nombre_completo, 
            @fecha_nacimiento, @email, @telefono, cast(getdate() as date)
        );
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al insertar paciente de aplicación: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_insertar_registros_paciente
go
create or alter procedure r4l.usp_insertar_registros_paciente
    @id_paciente int, 
    @id_tipo_registro int, 
    @fecha date, 
    @hora time(0), 
    @valor decimal(10, 2), 
    @unidad_alternativa nvarchar(20) = null, 
    @notas nvarchar(255) = null
as
begin
    set nocount on;
    begin try
        insert into r4l.registros_paciente(
            id_paciente, id_tipo_registro, fecha, hora, valor, unidad_alternativa, notas
        )
        values(
            @id_paciente, @id_tipo_registro, @fecha, @hora, @valor, @unidad_alternativa, @notas
        );
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al insertar registro de paciente: %s', 16, 1, @mensaje_error);
    end catch
end;
go