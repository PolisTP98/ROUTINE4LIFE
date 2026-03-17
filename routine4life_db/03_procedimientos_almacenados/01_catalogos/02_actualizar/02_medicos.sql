-- PROCEDIMIENTO ALMACENADO r4l.usp_actualizar_tipos_diabetes
go
create or alter procedure r4l.usp_actualizar_tipos_diabetes
    @id_tipo_diabetes int,
    @nombre nvarchar(20) = null
as
begin
    set nocount on;
    begin try
        update r4l.tipos_diabetes
        set nombre = coalesce(@nombre, nombre)
        where id_tipo_diabetes = @id_tipo_diabetes;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al actualizar tipo de diabetes: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_actualizar_sintomas_diabetes
go
create or alter procedure r4l.usp_actualizar_sintomas_diabetes
    @id_sintoma_diabetes int,
    @nombre nvarchar(50) = null,
    @descripcion nvarchar(255) = null
as
begin
    set nocount on;
    begin try
        update r4l.sintomas_diabetes
        set nombre = coalesce(@nombre, nombre),
            descripcion = case 
                when @descripcion is not null then @descripcion 
                else descripcion 
            end
        where id_sintoma_diabetes = @id_sintoma_diabetes;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al actualizar síntoma de diabetes: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_actualizar_medicamentos_diabetes
go
create or alter procedure r4l.usp_actualizar_medicamentos_diabetes
    @id_medicamento_diabetes int,
    @id_presentacion int = null,
    @id_unidad int = null,
    @nombre nvarchar(50) = null,
    @concentracion int = null,
    @descripcion nvarchar(255) = null
as
begin
    set nocount on;
    begin try
        update r4l.medicamentos_diabetes
        set id_presentacion = coalesce(@id_presentacion, id_presentacion),
            id_unidad = coalesce(@id_unidad, id_unidad),
            nombre = coalesce(@nombre, nombre),
            concentracion = coalesce(@concentracion, concentracion),
            descripcion = case 
                when @descripcion is not null then @descripcion 
                else descripcion 
            end
        where id_medicamento_diabetes = @id_medicamento_diabetes;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al actualizar medicamento para diabetes: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_actualizar_tipos_rutinas
go
create or alter procedure r4l.usp_actualizar_tipos_rutinas
    @id_tipo_rutina int,
    @nombre nvarchar(50) = null,
    @descripcion nvarchar(255) = null
as
begin
    set nocount on;
    begin try
        update r4l.tipos_rutinas
        set nombre = coalesce(@nombre, nombre),
            descripcion = case 
                when @descripcion is not null then @descripcion 
                else descripcion 
            end
        where id_tipo_rutina = @id_tipo_rutina;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al actualizar tipo de rutina: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_actualizar_estatus_citas
go
create or alter procedure r4l.usp_actualizar_estatus_citas
    @id_estatus_cita int,
    @nombre nvarchar(20) = null
as
begin
    set nocount on;
    begin try
        update r4l.estatus_citas
        set nombre = coalesce(@nombre, nombre)
        where id_estatus_cita = @id_estatus_cita;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al actualizar estatus de cita: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_actualizar_especialidades_medicas
go
create or alter procedure r4l.usp_actualizar_especialidades_medicas
    @id_especialidad int,
    @nombre nvarchar(50) = null,
    @descripcion nvarchar(255) = null
as
begin
    set nocount on;
    begin try
        update r4l.especialidades_medicas
        set nombre = coalesce(@nombre, nombre),
            descripcion = case 
                when @descripcion is not null then @descripcion 
                else descripcion 
            end
        where id_especialidad = @id_especialidad;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al actualizar especialidad médica: %s', 16, 1, @mensaje_error);
    end catch
end;
go