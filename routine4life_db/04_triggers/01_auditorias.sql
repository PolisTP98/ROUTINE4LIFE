-- TRIGGER PARA r4l.citas_medicas
go
create or alter trigger r4l.utg_auditorias_citas_medicas
on r4l.citas_medicas
after insert, update, delete
as
begin
    set nocount on;
    declare @usuario_actual int = convert(int, session_context(N'usuario_id'));
    if @usuario_actual is null set @usuario_actual = 1;

    if exists(select 1 from inserted) and not exists(select 1 from deleted)
    begin
        insert into r4l.auditorias(tabla_afectada, accion, id_registro_afectado, id_usuario, fecha_hora, datos_nuevos)
        select 'citas_medicas', 'i', i.id_cita, @usuario_actual, sysdatetime(), 
            (select i.* for json path, without_array_wrapper)
        from inserted i;
    end

    if exists(select 1 from deleted) and not exists(select 1 from inserted)
    begin
        insert into r4l.auditorias(tabla_afectada, accion, id_registro_afectado, id_usuario, fecha_hora, datos_anteriores)
        select 'citas_medicas', 'd', d.id_cita, @usuario_actual, sysdatetime(), 
            (select d.* for json path, without_array_wrapper)
        from deleted d;
    end

    if exists(select 1 from inserted) and exists(select 1 from deleted)
    begin
        insert into r4l.auditorias(tabla_afectada, accion, id_registro_afectado, id_usuario, fecha_hora, datos_anteriores, datos_nuevos)
        select 'citas_medicas', 'u', i.id_cita, @usuario_actual, sysdatetime(), 
            (select d.* for json path, without_array_wrapper), 
            (select i.* for json path, without_array_wrapper)
        from inserted i
        inner join deleted d on i.id_cita = d.id_cita;
    end
end;
go

-- TRIGGER PARA r4l.recetas_medicas
go
create or alter trigger r4l.utg_auditorias_recetas_medicas
on r4l.recetas_medicas
after insert, update, delete
as
begin
    set nocount on;
    declare @usuario_actual int = convert(int, session_context(N'usuario_id'));
    if @usuario_actual is null set @usuario_actual = 1;

    if exists(select 1 from inserted) and not exists(select 1 from deleted)
    begin
        insert into r4l.auditorias(tabla_afectada, accion, id_registro_afectado, id_usuario, fecha_hora, datos_nuevos)
        select 'recetas_medicas', 'i', i.id_receta, @usuario_actual, sysdatetime(), 
            (select i.* for json path, without_array_wrapper)
        from inserted i;
    end

    if exists(select 1 from deleted) and not exists(select 1 from inserted)
    begin
        insert into r4l.auditorias(tabla_afectada, accion, id_registro_afectado, id_usuario, fecha_hora, datos_anteriores)
        select 'recetas_medicas', 'd', d.id_receta, @usuario_actual, sysdatetime(), 
            (select d.* for json path, without_array_wrapper)
        from deleted d;
    end

    if exists(select 1 from inserted) and exists(select 1 from deleted)
    begin
        insert into r4l.auditorias(tabla_afectada, accion, id_registro_afectado, id_usuario, fecha_hora, datos_anteriores, datos_nuevos)
        select 'recetas_medicas', 'u', i.id_receta, @usuario_actual, sysdatetime(), 
            (select d.* for json path, without_array_wrapper), 
            (select i.* for json path, without_array_wrapper)
        from inserted i
        inner join deleted d on i.id_receta = d.id_receta;
    end
end;
go

-- TRIGGER PARA r4l.pacientes
go
create or alter trigger r4l.utg_auditorias_pacientes
on r4l.pacientes
after insert, update, delete
as
begin
    set nocount on;
    declare @usuario_actual int = convert(int, session_context(N'usuario_id'));
    if @usuario_actual is null set @usuario_actual = 1;

    if exists(select 1 from inserted) and not exists(select 1 from deleted)
    begin
        insert into r4l.auditorias(tabla_afectada, accion, id_registro_afectado, id_usuario, fecha_hora, datos_nuevos)
        select 'pacientes', 'i', i.id_paciente, @usuario_actual, sysdatetime(), 
            (select i.* for json path, without_array_wrapper)
        from inserted i;
    end

    if exists(select 1 from deleted) and not exists(select 1 from inserted)
    begin
        insert into r4l.auditorias(tabla_afectada, accion, id_registro_afectado, id_usuario, fecha_hora, datos_anteriores)
        select 'pacientes', 'd', d.id_paciente, @usuario_actual, sysdatetime(), 
            (select d.* for json path, without_array_wrapper)
        from deleted d;
    end

    if exists(select 1 from inserted) and exists(select 1 from deleted)
    begin
        insert into r4l.auditorias(tabla_afectada, accion, id_registro_afectado, id_usuario, fecha_hora, datos_anteriores, datos_nuevos)
        select 'pacientes', 'u', i.id_paciente, @usuario_actual, sysdatetime(), 
            (select d.* for json path, without_array_wrapper), 
            (select i.* for json path, without_array_wrapper)
        from inserted i
        inner join deleted d on i.id_paciente = d.id_paciente;
    end
end;
go

-- TRIGGER PARA r4l.medicos
go
create or alter trigger r4l.utg_auditorias_medicos
on r4l.medicos
after insert, update, delete
as
begin
    set nocount on;
    declare @usuario_actual int = convert(int, session_context(N'usuario_id'));
    if @usuario_actual is null set @usuario_actual = 1;

    if exists(select 1 from inserted) and not exists(select 1 from deleted)
    begin
        insert into r4l.auditorias(tabla_afectada, accion, id_registro_afectado, id_usuario, fecha_hora, datos_nuevos)
        select 'medicos', 'i', i.id_medico, @usuario_actual, sysdatetime(), 
            (select i.* for json path, without_array_wrapper)
        from inserted i;
    end

    if exists(select 1 from deleted) and not exists(select 1 from inserted)
    begin
        insert into r4l.auditorias(tabla_afectada, accion, id_registro_afectado, id_usuario, fecha_hora, datos_anteriores)
        select 'medicos', 'd', d.id_medico, @usuario_actual, sysdatetime(), 
            (select d.* for json path, without_array_wrapper)
        from deleted d;
    end

    if exists(select 1 from inserted) and exists(select 1 from deleted)
    begin
        insert into r4l.auditorias(tabla_afectada, accion, id_registro_afectado, id_usuario, fecha_hora, datos_anteriores, datos_nuevos)
        select 'medicos', 'u', i.id_medico, @usuario_actual, sysdatetime(), 
            (select d.* for json path, without_array_wrapper), 
            (select i.* for json path, without_array_wrapper)
        from inserted i
        inner join deleted d on i.id_medico = d.id_medico;
    end
end;
go

-- TRIGGER PARA r4l.usuarios
go
create or alter trigger r4l.utg_auditorias_usuarios
on r4l.usuarios
after insert, update, delete
as
begin
    set nocount on;
    declare @usuario_actual int = convert(int, session_context(N'usuario_id'));
    if @usuario_actual is null set @usuario_actual = 1;

    if exists(select 1 from inserted) and not exists(select 1 from deleted)
    begin
        insert into r4l.auditorias(tabla_afectada, accion, id_registro_afectado, id_usuario, fecha_hora, datos_nuevos)
        select 'usuarios', 'i', i.id_usuario, @usuario_actual, sysdatetime(), 
            (select i.* for json path, without_array_wrapper)
        from inserted i;
    end

    if exists(select 1 from deleted) and not exists(select 1 from inserted)
    begin
        insert into r4l.auditorias(tabla_afectada, accion, id_registro_afectado, id_usuario, fecha_hora, datos_anteriores)
        select 'usuarios', 'd', d.id_usuario, @usuario_actual, sysdatetime(), 
            (select d.* for json path, without_array_wrapper)
        from deleted d;
    end

    if exists(select 1 from inserted) and exists(select 1 from deleted)
    begin
        insert into r4l.auditorias(tabla_afectada, accion, id_registro_afectado, id_usuario, fecha_hora, datos_anteriores, datos_nuevos)
        select 'usuarios', 'u', i.id_usuario, @usuario_actual, sysdatetime(), 
            (select d.* for json path, without_array_wrapper), 
            (select i.* for json path, without_array_wrapper)
        from inserted i
        inner join deleted d on i.id_usuario = d.id_usuario;
    end
end;
go

-- TRIGGER PARA r4l.consultas_medicas
go
create or alter trigger r4l.utg_auditorias_consultas_medicas
on r4l.consultas_medicas
after insert, update, delete
as
begin
    set nocount on;
    declare @usuario_actual int = convert(int, session_context(N'usuario_id'));
    if @usuario_actual is null set @usuario_actual = 1;

    if exists(select 1 from inserted) and not exists(select 1 from deleted)
    begin
        insert into r4l.auditorias(tabla_afectada, accion, id_registro_afectado, id_usuario, fecha_hora, datos_nuevos)
        select 'consultas_medicas', 'i', i.id_consulta, @usuario_actual, sysdatetime(), 
            (select i.* for json path, without_array_wrapper)
        from inserted i;
    end

    if exists(select 1 from deleted) and not exists(select 1 from inserted)
    begin
        insert into r4l.auditorias(tabla_afectada, accion, id_registro_afectado, id_usuario, fecha_hora, datos_anteriores)
        select 'consultas_medicas', 'd', d.id_consulta, @usuario_actual, sysdatetime(), 
            (select d.* for json path, without_array_wrapper)
        from deleted d;
    end

    if exists(select 1 from inserted) and exists(select 1 from deleted)
    begin
        insert into r4l.auditorias(tabla_afectada, accion, id_registro_afectado, id_usuario, fecha_hora, datos_anteriores, datos_nuevos)
        select 'consultas_medicas', 'u', i.id_consulta, @usuario_actual, sysdatetime(), 
            (select d.* for json path, without_array_wrapper), 
            (select i.* for json path, without_array_wrapper)
        from inserted i
        inner join deleted d on i.id_consulta = d.id_consulta;
    end
end;
go