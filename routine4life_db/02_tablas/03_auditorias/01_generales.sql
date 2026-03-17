go

-- TABLA DE AUDITORÍA GENERAL
if object_id('r4l.auditorias', 'u') is null
begin
    create table r4l.auditorias(
        id_auditoria int identity(1, 1) primary key, 
        tabla_afectada nvarchar(50) not null, 
        accion char(1) not null, 
        id_registro_afectado int not null, 
        id_usuario int not null, 
        fecha_hora datetime2(0) not null, 
        datos_anteriores nvarchar(max), 
        datos_nuevos nvarchar(max), 
        constraint fk_auditoria_usuario foreign key(id_usuario) 
            references r4l.usuarios(id_usuario)
    );
    create index ix_auditorias_tabla_registro on r4l.auditorias(tabla_afectada, id_registro_afectado);
    create index ix_auditorias_fecha_hora on r4l.auditorias(fecha_hora);
end
go