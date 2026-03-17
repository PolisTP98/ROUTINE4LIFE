go

-- ALMACENA LA INFORMACIÓN PERSONAL DE LOS PACIENTES EN LA APLICACIÓN MÓVIL
if object_id('r4l.pacientes_aplicacion', 'u') is null
begin
    create table r4l.pacientes_aplicacion(
        id_paciente int primary key, 
        id_sexo int not null, 
        id_pais int not null, 
        id_estatus_usuario int not null, 
        nombre_completo nvarchar(255) not null, 
        fecha_nacimiento date not null, 
        email varchar(255) not null, 
        telefono varchar(20) not null, 
        fecha_registro date not null, 
        fecha_hora_eliminacion datetime2(0), 
        constraint fk_pacientes foreign key(id_paciente) 
            references r4l.pacientes(id_paciente) 
            on delete cascade 
            on update cascade, 
        constraint fk_pais_paciente foreign key(id_pais) 
            references r4l.paises(id_pais), 
        constraint fk_sexo_paciente_aplicacion foreign key(id_sexo) 
            references r4l.sexos(id_sexo), 
        constraint fk_estatus_paciente_aplicacion foreign key(id_estatus_usuario) 
            references r4l.estatus_usuarios(id_estatus_usuario), 
        constraint uq_email_paciente unique(email), 
        constraint uq_telefono_paciente unique(telefono)
        /*
        constraint ck_fecha_nacimiento_paciente check(fecha_nacimiento <= getdate()), 
        constraint ck_email_paciente check(email like '%_@__%.__%'), 
        constraint ck_telefono_paciente check(telefono like '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]%')
        */
    );
    create index ix_pacientes_aplicacion_id_sexo on r4l.pacientes_aplicacion(id_sexo);
    create index ix_pacientes_aplicacion_id_pais on r4l.pacientes_aplicacion(id_pais);
    create index ix_pacientes_aplicacion_id_estatus_usuario on r4l.pacientes_aplicacion(id_estatus_usuario);
end

-- ALMACENA LOS REGISTROS REALIZADOS POR LOS PACIENTES PARA MONITOREAR EL AVANCE CONTRA SU DIABETES DESDE SU HOGAR
if object_id('r4l.registros_paciente', 'u') is null
begin
    create table r4l.registros_paciente(
        id_registro int identity(1, 1) primary key, 
        id_paciente int not null, 
        id_tipo_registro int not null, 
        fecha date not null, 
        hora time(0) not null, 
        valor decimal(10, 2) not null, 
        unidad_alternativa nvarchar(20), 
        notas nvarchar(255), 
        constraint fk_paciente_registro foreign key(id_paciente) 
            references r4l.pacientes(id_paciente), 
        constraint fk_tipo_registro foreign key(id_tipo_registro) 
            references r4l.tipos_registros(id_tipo_registro)
        /*
        constraint chk_valor_medicion check(valor_medicion >= 0)
        */
    );
    create index ix_registros_paciente_id_paciente on r4l.registros_paciente(id_paciente);
    create index ix_registros_paciente_id_tipo_registro on r4l.registros_paciente(id_tipo_registro);
    create index ix_registros_paciente_fecha on r4l.registros_paciente(fecha);
end
go