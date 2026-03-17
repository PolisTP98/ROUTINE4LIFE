-- PROCEDIMIENTO ALMACENADO r4l.usp_eliminar_datos_personales_medico
go
create or alter procedure r4l.usp_eliminar_datos_personales_medico
    @id_medico int
as
begin
    set nocount on;
    begin try
        update r4l.datos_personales_medico 
        set fecha_hora_eliminacion = sysdatetime() 
        where id_medico = @id_medico;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al eliminar datos personales del médico: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_eliminar_medicos
go
create or alter procedure r4l.usp_eliminar_medicos
    @id_medico int
as
begin
    set nocount on;
    begin try
        update r4l.medicos 
        set id_estatus_usuario = 2 
        where id_medico = @id_medico;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al eliminar médico: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_eliminar_horarios_medicos
go
create or alter procedure r4l.usp_eliminar_horarios_medicos
    @id_horario int
as
begin
    set nocount on;
    begin try
        update r4l.horarios_medicos 
        set activo = 0 
        where id_horario = @id_horario;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al eliminar horario médico: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_eliminar_pacientes
go
create or alter procedure r4l.usp_eliminar_pacientes
    @id_paciente int
as
begin
    set nocount on;
    begin try
        update r4l.pacientes 
        set id_estatus_usuario = 2, 
            fecha_hora_eliminacion = sysdatetime() 
        where id_paciente = @id_paciente;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al eliminar paciente: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_eliminar_citas_medicas
go
create or alter procedure r4l.usp_eliminar_citas_medicas
    @id_cita int
as
begin
    set nocount on;
    begin try
        update r4l.citas_medicas 
        set id_estatus_cita = 3 
        where id_cita = @id_cita;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al eliminar cita médica: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_eliminar_consultas_medicas
go
create or alter procedure r4l.usp_eliminar_consultas_medicas
    @id_consulta int
as
begin
    set nocount on;
    begin try
        delete from r4l.consultas_medicas where id_consulta = @id_consulta;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al eliminar consulta médica: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_eliminar_sintomas_consulta
go
create or alter procedure r4l.usp_eliminar_sintomas_consulta
    @id_sintoma int
as
begin
    set nocount on;
    begin try
        delete from r4l.sintomas_consulta where id_sintoma = @id_sintoma;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al eliminar síntoma de consulta: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_eliminar_recetas_medicas
go
create or alter procedure r4l.usp_eliminar_recetas_medicas
    @id_receta int
as
begin
    set nocount on;
    begin try
        delete from r4l.recetas_medicas where id_receta = @id_receta;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al eliminar receta médica: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_eliminar_medicamentos_recetados
go
create or alter procedure r4l.usp_eliminar_medicamentos_recetados
    @id_medicamento int
as
begin
    set nocount on;
    begin try
        delete from r4l.medicamentos_recetados where id_medicamento = @id_medicamento;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al eliminar medicamento recetado: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_eliminar_rutinas_recetadas
go
create or alter procedure r4l.usp_eliminar_rutinas_recetadas
    @id_rutina int
as
begin
    set nocount on;
    begin try
        delete from r4l.rutinas_recetadas where id_rutina = @id_rutina;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al eliminar rutina recetada: %s', 16, 1, @mensaje_error);
    end catch
end;
go