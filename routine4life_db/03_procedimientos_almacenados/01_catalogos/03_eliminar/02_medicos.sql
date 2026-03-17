-- PROCEDIMIENTO ALMACENADO r4l.usp_eliminar_sucursales_hospitalarias
go
create or alter procedure r4l.usp_eliminar_sucursales_hospitalarias
    @id_sucursal int
as
begin
    set nocount on;
    begin try
        delete from r4l.sucursales_hospitalarias where id_sucursal = @id_sucursal;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al eliminar sucursal hospitalaria: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_eliminar_presentaciones_medicamentos
go
create or alter procedure r4l.usp_eliminar_presentaciones_medicamentos
    @id_presentacion int
as
begin
    set nocount on;
    begin try
        delete from r4l.presentaciones_medicamentos where id_presentacion = @id_presentacion;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al eliminar presentación de medicamento: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_eliminar_unidades_medida
go
create or alter procedure r4l.usp_eliminar_unidades_medida
    @id_unidad int
as
begin
    set nocount on;
    begin try
        delete from r4l.unidades_medida where id_unidad = @id_unidad;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al eliminar unidad de medida: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_eliminar_tipos_diabetes
go
create or alter procedure r4l.usp_eliminar_tipos_diabetes
    @id_tipo_diabetes int
as
begin
    set nocount on;
    begin try
        delete from r4l.tipos_diabetes where id_tipo_diabetes = @id_tipo_diabetes;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al eliminar tipo de diabetes: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_eliminar_sintomas_diabetes
go
create or alter procedure r4l.usp_eliminar_sintomas_diabetes
    @id_sintoma_diabetes int
as
begin
    set nocount on;
    begin try
        delete from r4l.sintomas_diabetes where id_sintoma_diabetes = @id_sintoma_diabetes;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al eliminar síntoma de diabetes: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_eliminar_medicamentos_diabetes
go
create or alter procedure r4l.usp_eliminar_medicamentos_diabetes
    @id_medicamento_diabetes int
as
begin
    set nocount on;
    begin try
        delete from r4l.medicamentos_diabetes where id_medicamento_diabetes = @id_medicamento_diabetes;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al eliminar medicamento para diabetes: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_eliminar_tipos_rutinas
go
create or alter procedure r4l.usp_eliminar_tipos_rutinas
    @id_tipo_rutina int
as
begin
    set nocount on;
    begin try
        delete from r4l.tipos_rutinas where id_tipo_rutina = @id_tipo_rutina;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al eliminar tipo de rutina: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_eliminar_estatus_citas
go
create or alter procedure r4l.usp_eliminar_estatus_citas
    @id_estatus_cita int
as
begin
    set nocount on;
    begin try
        delete from r4l.estatus_citas where id_estatus_cita = @id_estatus_cita;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al eliminar estatus de cita: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_eliminar_especialidades_medicas
go
create or alter procedure r4l.usp_eliminar_especialidades_medicas
    @id_especialidad int
as
begin
    set nocount on;
    begin try
        delete from r4l.especialidades_medicas where id_especialidad = @id_especialidad;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al eliminar especialidad médica: %s', 16, 1, @mensaje_error);
    end catch
end;
go