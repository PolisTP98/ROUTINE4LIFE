go

-- ALMACENA LOS USUARIOS DEL SISTEMA CON SU NOMBRE, CONTRASEÑA Y URL DE SU FOTO DE PERFIL
if object_id('r4l.usuarios', 'u') is null
begin
    create table r4l.usuarios(
        id_usuario int identity(1, 1) primary key, 
        id_rol int not null, 
        id_medico int null, 
        id_paciente int null, 
        contrasena nvarchar(255) not null, 
        fecha_registro date not null, 
        fecha_hora_eliminacion datetime2(0), 
        constraint fk_rol_usuario foreign key(id_rol) 
            references r4l.roles_usuarios(id_rol), 
        constraint fk_medico_usuario foreign key(id_medico) 
            references r4l.medicos(id_medico), 
        constraint fk_paciente_usuario foreign key(id_paciente) 
            references r4l.pacientes(id_paciente), 
        constraint uq_id_medico unique(id_medico), 
        constraint uq_id_paciente unique(id_paciente), 
        constraint ck_tipo_usuario check(
            (id_medico is not null and id_paciente is null) or 
            (id_medico is null and id_paciente is not null)
        )
    );
    create index ix_usuarios_id_medico on r4l.usuarios(id_medico);
    create index ix_usuarios_id_paciente on r4l.usuarios(id_paciente);
end
go