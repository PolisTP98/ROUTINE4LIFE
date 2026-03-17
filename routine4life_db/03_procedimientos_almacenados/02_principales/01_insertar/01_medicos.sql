-- PROCEDIMIENTO ALMACENADO r4l.usp_insertar_datos_personales_medico
go
create or alter procedure r4l.usp_insertar_datos_personales_medico
    @id_sexo int, 
    @id_pais int, 
    @nombre_completo nvarchar(255), 
    @fecha_nacimiento date, 
    @telefono varchar(20)
as
begin
    set nocount on;
    begin try
        insert into r4l.datos_personales_medico(
            id_sexo, id_pais, nombre_completo, fecha_nacimiento, telefono, fecha_hora_registro
        )
        values(
            @id_sexo, @id_pais, @nombre_completo, @fecha_nacimiento, @telefono, sysdatetime()
        );
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al insertar datos personales del médico: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_insertar_medicos
go
create or alter procedure r4l.usp_insertar_medicos
    @id_medico int, 
    @id_rol int, 
    @id_especialidad int, 
    @id_estatus_usuario int = 1, 
    @codigo nvarchar(20), 
    @cedula_profesional nvarchar(30), 
    @email varchar(255), 
    @rfc varchar(13)
as
begin
    set nocount on;
    begin try
        insert into r4l.medicos(
            id_medico, id_rol, id_especialidad, id_estatus_usuario, codigo, cedula_profesional, email, rfc
        )
        values(
            @id_medico, @id_rol, @id_especialidad, @id_estatus_usuario, @codigo, @cedula_profesional, @email, @rfc
        );
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al insertar médico: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_insertar_horarios_medicos
go
create or alter procedure r4l.usp_insertar_horarios_medicos
    @id_medico int, 
    @dia_semana tinyint, 
    @hora_inicio time(0), 
    @hora_fin time(0), 
    @activo bit
as
begin
    set nocount on;
    begin try
        insert into r4l.horarios_medicos(id_medico, dia_semana, hora_inicio, hora_fin, activo)
        values(@id_medico, @dia_semana, @hora_inicio, @hora_fin, @activo);
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al insertar horario médico: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_insertar_pacientes
go
create or alter procedure r4l.usp_insertar_pacientes
    @id_sexo int, 
    @id_estatus_usuario int = 1, 
    @id_tipo_diabetes int = null, 
    @codigo nvarchar(20), 
    @nombre_completo nvarchar(255), 
    @fecha_nacimiento date
as
begin
    set nocount on;
    begin try
        insert into r4l.pacientes(
            id_sexo, id_estatus_usuario, id_tipo_diabetes, codigo, nombre_completo, fecha_nacimiento, fecha_hora_registro
        )
        values(
            @id_sexo, @id_estatus_usuario, @id_tipo_diabetes, @codigo, @nombre_completo, @fecha_nacimiento, sysdatetime()
        );
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al insertar paciente: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_insertar_citas_medicas
go
create or alter procedure r4l.usp_insertar_citas_medicas
    @id_rol int, 
    @id_medico int, 
    @id_paciente int, 
    @id_estatus_cita int = 1, 
    @fecha date, 
    @hora time(0), 
    @motivo nvarchar(255) = null, 
    @notas nvarchar(255) = null
as
begin
    set nocount on;
    begin try
        insert into r4l.citas_medicas(
            id_rol, id_medico, id_paciente, id_estatus_cita, fecha, hora, motivo, notas, fecha_hora_solicitud
        )
        values(
            @id_rol, @id_medico, @id_paciente, @id_estatus_cita, @fecha, @hora, @motivo, @notas, sysdatetime()
        );
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al insertar cita médica: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_insertar_consultas_medicas
go
create or alter procedure r4l.usp_insertar_consultas_medicas
    @id_cita int, 
    @id_medico int, 
    @id_paciente int, 
    @fecha date = null, 
    @hora time(0) = null, 
    @peso decimal(5, 2) = null, 
    @altura smallint = null, 
    @presion_sistolica tinyint = null, 
    @presion_diastolica tinyint = null, 
    @frecuencia_cardiaca tinyint = null, 
    @glucosa_ayunas decimal(5, 2) = null, 
    @glucosa_postprandial decimal(5, 2) = null, 
    @hemoglobina_glicosilada decimal(4, 2) = null, 
    @colesterol_total decimal(5, 2) = null, 
    @trigliceridos decimal(5, 2) = null, 
    @nivel_insulina decimal(5, 2) = null, 
    @notas nvarchar(255) = null, 
    @plan_tratamiento nvarchar(max) = null
as
begin
    set nocount on;
    declare @fecha_actual date = cast(getdate() as date);
    declare @hora_actual time(0) = cast(sysdatetime() as time(0));
    
    begin try
        insert into r4l.consultas_medicas(
            id_cita, id_medico, id_paciente, fecha, hora, peso, altura, presion_sistolica, 
            presion_diastolica, frecuencia_cardiaca, glucosa_ayunas, glucosa_postprandial, 
            hemoglobina_glicosilada, colesterol_total, trigliceridos, nivel_insulina, notas, plan_tratamiento
        )
        values(
            @id_cita, @id_medico, @id_paciente, 
            isnull(@fecha, @fecha_actual), 
            isnull(@hora, @hora_actual), 
            @peso, @altura, @presion_sistolica, @presion_diastolica, @frecuencia_cardiaca, 
            @glucosa_ayunas, @glucosa_postprandial, @hemoglobina_glicosilada, 
            @colesterol_total, @trigliceridos, @nivel_insulina, @notas, @plan_tratamiento
        );
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al insertar consulta médica: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_insertar_sintomas_consulta
go
create or alter procedure r4l.usp_insertar_sintomas_consulta
    @id_consulta int, 
    @id_sintoma_diabetes int, 
    @intensidad tinyint = null, 
    @duracion nvarchar(50) = null, 
    @notas nvarchar(255) = null
as
begin
    set nocount on;
    begin try
        insert into r4l.sintomas_consulta(id_consulta, id_sintoma_diabetes, intensidad, duracion, notas)
        values(@id_consulta, @id_sintoma_diabetes, @intensidad, @duracion, @notas);
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al insertar síntoma de consulta: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_insertar_recetas_medicas
go
create or alter procedure r4l.usp_insertar_recetas_medicas
    @id_consulta int, 
    @fecha date, 
    @hora time(0), 
    @instrucciones_generales nvarchar(255) = null, 
    @url_pdf nvarchar(255) = null
as
begin
    set nocount on;
    begin try
        insert into r4l.recetas_medicas(id_consulta, fecha, hora, instrucciones_generales, url_pdf)
        values(@id_consulta, @fecha, @hora, @instrucciones_generales, @url_pdf);
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al insertar receta médica: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_insertar_medicamentos_recetados
go
create or alter procedure r4l.usp_insertar_medicamentos_recetados
    @id_receta int, 
    @id_medicamento_diabetes int, 
    @dosis nvarchar(50), 
    @frecuencia nvarchar(50), 
    @duracion nvarchar(50) = null, 
    @instrucciones_adicionales nvarchar(500) = null
as
begin
    set nocount on;
    begin try
        insert into r4l.medicamentos_recetados(id_receta, id_medicamento_diabetes, dosis, frecuencia, duracion, instrucciones_adicionales)
        values(@id_receta, @id_medicamento_diabetes, @dosis, @frecuencia, @duracion, @instrucciones_adicionales);
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al insertar medicamento recetado: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_insertar_rutinas_recetadas
go
create or alter procedure r4l.usp_insertar_rutinas_recetadas
    @id_receta int, 
    @id_tipo_rutina int, 
    @id_comida int = null, 
    @descripcion nvarchar(500), 
    @frecuencia nvarchar(50) = null, 
    @duracion nvarchar(50) = null, 
    @notas nvarchar(255) = null
as
begin
    set nocount on;
    begin try
        insert into r4l.rutinas_recetadas(id_receta, id_tipo_rutina, id_comida, descripcion, frecuencia, duracion, notas)
        values(@id_receta, @id_tipo_rutina, @id_comida, @descripcion, @frecuencia, @duracion, @notas);
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al insertar rutina recetada: %s', 16, 1, @mensaje_error);
    end catch
end;
go