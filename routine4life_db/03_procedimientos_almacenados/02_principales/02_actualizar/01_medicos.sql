-- PROCEDIMIENTO ALMACENADO r4l.usp_actualizar_datos_personales_medico
go
create or alter procedure r4l.usp_actualizar_datos_personales_medico
    @id_medico int, 
    @id_sexo int = null, 
    @id_pais int = null, 
    @nombre_completo nvarchar(255) = null, 
    @fecha_nacimiento date = null, 
    @telefono varchar(20) = null
as
begin
    set nocount on;
    begin try
        update r4l.datos_personales_medico 
        set id_sexo = coalesce(@id_sexo, id_sexo), 
            id_pais = coalesce(@id_pais, id_pais), 
            nombre_completo = coalesce(@nombre_completo, nombre_completo), 
            fecha_nacimiento = coalesce(@fecha_nacimiento, fecha_nacimiento), 
            telefono = coalesce(@telefono, telefono) 
            where id_medico = @id_medico;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al actualizar datos personales del médico: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_actualizar_medicos
go
create or alter procedure r4l.usp_actualizar_medicos
    @id_medico int, 
    @id_rol int = null, 
    @id_especialidad int = null, 
    @id_estatus_usuario int = null, 
    @codigo nvarchar(20) = null, 
    @cedula_profesional nvarchar(30) = null, 
    @email varchar(255) = null, 
    @rfc varchar(13) = null
as
begin
    set nocount on;
    begin try
        update r4l.medicos 
        set id_rol = coalesce(@id_rol, id_rol), 
            id_especialidad = coalesce(@id_especialidad, id_especialidad), 
            id_estatus_usuario = coalesce(@id_estatus_usuario, id_estatus_usuario), 
            codigo = coalesce(@codigo, codigo), 
            cedula_profesional = coalesce(@cedula_profesional, cedula_profesional), 
            email = coalesce(@email, email), 
            rfc = coalesce(@rfc, rfc) 
        where id_medico = @id_medico;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al actualizar médico: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_actualizar_horarios_medicos
go
create or alter procedure r4l.usp_actualizar_horarios_medicos
    @id_horario int, 
    @id_medico int = null, 
    @dia_semana tinyint = null, 
    @hora_inicio time(0) = null, 
    @hora_fin time(0) = null, 
    @activo bit = null
as
begin
    set nocount on;
    begin try
        update r4l.horarios_medicos 
        set id_medico = coalesce(@id_medico, id_medico), 
            dia_semana = coalesce(@dia_semana, dia_semana), 
            hora_inicio = coalesce(@hora_inicio, hora_inicio), 
            hora_fin = coalesce(@hora_fin, hora_fin), 
            activo = coalesce(@activo, activo) 
        where id_horario = @id_horario;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al actualizar horario médico: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_actualizar_pacientes
go
create or alter procedure r4l.usp_actualizar_pacientes
    @id_paciente int, 
    @id_sexo int = null, 
    @id_estatus_usuario int = null, 
    @id_tipo_diabetes int = null, 
    @codigo nvarchar(20) = null, 
    @nombre_completo nvarchar(255) = null, 
    @fecha_nacimiento date = null
as
begin
    set nocount on;
    begin try
        update r4l.pacientes 
        set id_sexo = coalesce(@id_sexo, id_sexo), 
            id_estatus_usuario = coalesce(@id_estatus_usuario, id_estatus_usuario), 
            id_tipo_diabetes = coalesce(@id_tipo_diabetes, id_tipo_diabetes), 
            codigo = coalesce(@codigo, codigo), 
            nombre_completo = coalesce(@nombre_completo, nombre_completo), 
            fecha_nacimiento = coalesce(@fecha_nacimiento, fecha_nacimiento) 
        where id_paciente = @id_paciente;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al actualizar paciente: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_actualizar_citas_medicas
go
create or alter procedure r4l.usp_actualizar_citas_medicas
    @id_cita int, 
    @id_rol int = null, 
    @id_medico int = null, 
    @id_paciente int = null, 
    @id_estatus_cita int = null, 
    @fecha date = null, 
    @hora time(0) = null, 
    @motivo nvarchar(255) = null, 
    @notas nvarchar(255) = null
as
begin
    set nocount on;
    begin try
        update r4l.citas_medicas 
        set id_rol = coalesce(@id_rol, id_rol), 
            id_medico = coalesce(@id_medico, id_medico), 
            id_paciente = coalesce(@id_paciente, id_paciente), 
            id_estatus_cita = coalesce(@id_estatus_cita, id_estatus_cita), 
            fecha = coalesce(@fecha, fecha), 
            hora = coalesce(@hora, hora), 
            motivo = coalesce(@motivo, motivo), 
            notas = coalesce(@notas, notas) 
        where id_cita = @id_cita;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al actualizar cita médica: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_actualizar_consultas_medicas
go
create or alter procedure r4l.usp_actualizar_consultas_medicas
    @id_consulta int, 
    @id_cita int = null, 
    @id_medico int = null, 
    @id_paciente int = null, 
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
    begin try
        update r4l.consultas_medicas 
        set id_cita = coalesce(@id_cita, id_cita), 
            id_medico = coalesce(@id_medico, id_medico), 
            id_paciente = coalesce(@id_paciente, id_paciente), 
            fecha = coalesce(@fecha, fecha), 
            hora = coalesce(@hora, hora), 
            peso = coalesce(@peso, peso), 
            altura = coalesce(@altura, altura), 
            presion_sistolica = coalesce(@presion_sistolica, presion_sistolica), 
            presion_diastolica = coalesce(@presion_diastolica, presion_diastolica), 
            frecuencia_cardiaca = coalesce(@frecuencia_cardiaca, frecuencia_cardiaca), 
            glucosa_ayunas = coalesce(@glucosa_ayunas, glucosa_ayunas), 
            glucosa_postprandial = coalesce(@glucosa_postprandial, glucosa_postprandial), 
            hemoglobina_glicosilada = coalesce(@hemoglobina_glicosilada, hemoglobina_glicosilada), 
            colesterol_total = coalesce(@colesterol_total, colesterol_total), 
            trigliceridos = coalesce(@trigliceridos, trigliceridos), 
            nivel_insulina = coalesce(@nivel_insulina, nivel_insulina), 
            notas = coalesce(@notas, notas), 
            plan_tratamiento = coalesce(@plan_tratamiento, plan_tratamiento) 
        where id_consulta = @id_consulta;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al actualizar consulta médica: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_actualizar_sintomas_consulta
go
create or alter procedure r4l.usp_actualizar_sintomas_consulta
    @id_sintoma int, 
    @id_consulta int = null, 
    @id_sintoma_diabetes int = null, 
    @intensidad tinyint = null, 
    @duracion nvarchar(50) = null, 
    @notas nvarchar(255) = null
as
begin
    set nocount on;
    begin try
        update r4l.sintomas_consulta 
        set id_consulta = coalesce(@id_consulta, id_consulta), 
            id_sintoma_diabetes = coalesce(@id_sintoma_diabetes, id_sintoma_diabetes), 
            intensidad = coalesce(@intensidad, intensidad), 
            duracion = coalesce(@duracion, duracion), 
            notas = coalesce(@notas, notas) 
        where id_sintoma = @id_sintoma;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al actualizar síntoma de consulta: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_actualizar_recetas_medicas
go
create or alter procedure r4l.usp_actualizar_recetas_medicas
    @id_receta int, 
    @id_consulta int = null, 
    @fecha date = null, 
    @hora time(0) = null, 
    @instrucciones_generales nvarchar(255) = null, 
    @url_pdf nvarchar(255) = null
as
begin
    set nocount on;
    begin try
        update r4l.recetas_medicas 
        set id_consulta = coalesce(@id_consulta, id_consulta), 
            fecha = coalesce(@fecha, fecha), 
            hora = coalesce(@hora, hora), 
            instrucciones_generales = coalesce(@instrucciones_generales, instrucciones_generales), 
            url_pdf = coalesce(@url_pdf, url_pdf) 
        where id_receta = @id_receta;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al actualizar receta médica: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_actualizar_medicamentos_recetados
go
create or alter procedure r4l.usp_actualizar_medicamentos_recetados
    @id_medicamento int, 
    @id_receta int = null, 
    @id_medicamento_diabetes int = null, 
    @dosis nvarchar(50) = null, 
    @frecuencia nvarchar(50) = null, 
    @duracion nvarchar(50) = null, 
    @instrucciones_adicionales nvarchar(500) = null
as
begin
    set nocount on;
    begin try
        update r4l.medicamentos_recetados 
        set id_receta = coalesce(@id_receta, id_receta), 
            id_medicamento_diabetes = coalesce(@id_medicamento_diabetes, id_medicamento_diabetes), 
            dosis = coalesce(@dosis, dosis), 
            frecuencia = coalesce(@frecuencia, frecuencia), 
            duracion = coalesce(@duracion, duracion), 
            instrucciones_adicionales = coalesce(@instrucciones_adicionales, instrucciones_adicionales) 
        where id_medicamento = @id_medicamento;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al actualizar medicamento recetado: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_actualizar_rutinas_recetadas
go
create or alter procedure r4l.usp_actualizar_rutinas_recetadas
    @id_rutina int, 
    @id_receta int = null, 
    @id_tipo_rutina int = null, 
    @id_comida int = null, 
    @descripcion nvarchar(500) = null, 
    @frecuencia nvarchar(50) = null, 
    @duracion nvarchar(50) = null, 
    @notas nvarchar(255) = null
as
begin
    set nocount on;
    begin try
        update r4l.rutinas_recetadas 
        set id_receta = coalesce(@id_receta, id_receta), 
            id_tipo_rutina = coalesce(@id_tipo_rutina, id_tipo_rutina), 
            id_comida = coalesce(@id_comida, id_comida), 
            descripcion = coalesce(@descripcion, descripcion), 
            frecuencia = coalesce(@frecuencia, frecuencia), 
            duracion = coalesce(@duracion, duracion), 
            notas = coalesce(@notas, notas) 
        where id_rutina = @id_rutina;
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al actualizar rutina recetada: %s', 16, 1, @mensaje_error);
    end catch
end;
go