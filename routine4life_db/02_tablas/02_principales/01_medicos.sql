go

-- ALMACENA LA INFORMACIÓN PERSONAL DE LOS MÉDICOS
if object_id('r4l.datos_personales_medico', 'u') is null
begin
    create table r4l.datos_personales_medico(
        id_medico int identity(1, 1) primary key, 
        id_sexo int not null, 
        id_pais int not null, 
        nombre_completo nvarchar(255) not null, 
        fecha_nacimiento date not null, 
        telefono varchar(20) not null, 
        fecha_hora_registro datetime2(0) not null, 
        fecha_hora_eliminacion datetime2(0), 
        constraint fk_sexo_medico foreign key(id_sexo) 
            references r4l.sexos(id_sexo), 
        constraint fk_pais_medico foreign key(id_pais) 
            references r4l.paises(id_pais), 
        constraint uq_telefono_medico unique(telefono)
        /*
        constraint ck_fecha_nacimiento_medico check(fecha_nacimiento <= getdate()), 
        constraint ck_telefono_medico check(telefono like '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]%')
        */
    );
    create index ix_datos_personales_medico_id_sexo on r4l.datos_personales_medico(id_sexo);
    create index ix_datos_personales_medico_id_pais on r4l.datos_personales_medico(id_pais);
end

-- ALMACENA LA INFORMACIÓN LABORAL DE LOS MÉDICOS
if object_id('r4l.medicos', 'u') is null
begin
    create table r4l.medicos(
        id_medico int primary key, 
        id_rol int not null, 
        id_especialidad int not null, 
        id_estatus_usuario int not null, 
        codigo nvarchar(20) not null, 
        cedula_profesional nvarchar(30) not null, 
        email varchar(255) not null, 
        rfc varchar(13) not null, 
        constraint fk_datos_personales_medico foreign key(id_medico) 
            references r4l.datos_personales_medico(id_medico) 
            on delete cascade 
            on update cascade, 
        constraint fk_rol_medico foreign key(id_rol) 
            references r4l.roles_usuarios(id_rol), 
        constraint fk_especialidad_medico foreign key(id_especialidad) 
            references r4l.especialidades_medicas(id_especialidad), 
        constraint fk_estatus_medico foreign key(id_estatus_usuario) 
            references r4l.estatus_usuarios(id_estatus_usuario), 
        constraint uq_codigo_medico unique(codigo), 
        constraint uq_cedula_medico unique(cedula_profesional), 
        constraint uq_email_medico unique(email), 
        constraint uq_rfc_medico unique(rfc)
        /*
        constraint ck_email_medico check(email like '%_@__%.__%'), 
        constraint ck_rfc_medico check(rfc like '[A-Z&Ñ]{3,4}[0-9]{6}[A-Z0-9]{3}')
        */
    );
    create index ix_medicos_id_rol on r4l.medicos(id_rol);
    create index ix_medicos_id_especialidad on r4l.medicos(id_especialidad);
    create index ix_medicos_id_estatus_usuario on r4l.medicos(id_estatus_usuario);
end

-- ALMACENA LOS HORARIOS DE ATENCIÓN DE LOS MÉDICOS
if object_id('r4l.horarios_medicos', 'u') is null
begin
    create table r4l.horarios_medicos(
        id_horario int identity(1, 1) primary key, 
        id_medico int not null, 
        dia_semana tinyint not null, 
        hora_inicio time(0) not null, 
        hora_fin time(0) not null, 
        activo bit not null, 
        constraint fk_medico_horario foreign key(id_medico) 
            references r4l.medicos(id_medico)
        /*
        constraint ck_dia_semana check(dia_semana between 1 and 7), 
        constraint ck_horario check(hora_fin > hora_inicio
        */
    );
    create index ix_horarios_medicos_id_medico on r4l.horarios_medicos(id_medico);
    create index ix_horarios_medicos_dia_semana on r4l.horarios_medicos(dia_semana);
end

/*
-- ALMACENA LAS EXCEPCIONES DE LOS HORARIOS DE ATENCIÓN DE LOS MÉDICOS (VACACIONES, DÍAS FERIADOS, ETC.)
if object_id('r4l.excepciones_horarios', 'u') is null
begin
    create table r4l.excepciones_horarios(
        id_excepcion int identity(1, 1) primary key, 
        id_medico int not null, 
        fecha_excepcion date not null, 
        activo bit not null, 
        motivo nvarchar(255), 
        constraint fk_excepciones_medico foreign key(id_medico) 
            references r4l.medicos(id_medico), 
        constraint uq_excepcion_medico_fecha unique(id_medico, fecha_excepcion)
    );
    create index ix_excepciones_horarios_id_medico on r4l.excepciones_horarios(id_medico);
    create index ix_excepciones_horarios_fecha_excepcion on r4l.excepciones_horarios(fecha_excepcion);
end
*/

-- ALMACENA LA INFORMACIÓN PERSONAL DE LOS PACIENTES
if object_id('r4l.pacientes', 'u') is null
begin
    create table r4l.pacientes(
        id_paciente int identity(1, 1) primary key, 
        id_sexo int not null, 
        id_estatus_usuario int not null, 
        id_tipo_diabetes int, 
        codigo nvarchar(20) not null, 
        nombre_completo nvarchar(255) not null, 
        fecha_nacimiento date not null, 
        fecha_hora_registro datetime2(0) not null, 
        fecha_hora_eliminacion datetime2(0), 
        constraint fk_sexo_paciente foreign key(id_sexo) 
            references r4l.sexos(id_sexo), 
        constraint fk_estatus_paciente foreign key(id_estatus_usuario) 
            references r4l.estatus_usuarios(id_estatus_usuario), 
        constraint fk_tipo_diabetes_paciente foreign key(id_tipo_diabetes) 
            references r4l.tipos_diabetes(id_tipo_diabetes), 
        constraint uq_codigo_paciente unique(codigo)
        /*
        constraint ck_fecha_nacimiento_paciente check(fecha_nacimiento <= getdate())
        */
    );
    create index ix_pacientes_id_sexo on r4l.pacientes(id_sexo);
    create index ix_pacientes_id_estatus_usuario on r4l.pacientes(id_estatus_usuario);
    create index ix_pacientes_id_tipo_diabetes on r4l.pacientes(id_tipo_diabetes);
end

-- ALMACENA LAS CITAS MÉDICAS (AGENDADAS POR PACIENTES O MÉDICOS)
if object_id('r4l.citas_medicas', 'u') is null
begin
    create table r4l.citas_medicas(
        id_cita int identity(1, 1) primary key, 
        id_rol int not null, 
        id_medico int not null, 
        id_paciente int not null, 
        id_estatus_cita int not null, 
        fecha date not null, 
        hora time(0) not null, 
        motivo nvarchar(255), 
        notas nvarchar(255), 
        fecha_hora_solicitud datetime2(0) not null, 
        constraint fk_rol_cita foreign key(id_rol) 
            references r4l.roles_usuarios(id_rol), 
        constraint fk_medico_cita foreign key(id_medico) 
            references r4l.medicos(id_medico), 
        constraint fk_paciente_cita foreign key(id_paciente) 
            references r4l.pacientes(id_paciente), 
        constraint fk_estatus_cita foreign key(id_estatus_cita) 
            references r4l.estatus_citas(id_estatus_cita)
        /*
        constraint ck_fecha_cita check(fecha_cita >= getdate())
        */
    );
    create index ix_citas_medicas_id_medico on r4l.citas_medicas(id_medico);
    create index ix_citas_medicas_id_paciente on r4l.citas_medicas(id_paciente);
    create index ix_citas_medicas_fecha on r4l.citas_medicas(fecha);
    create index ix_citas_medicas_id_estatus_cita on r4l.citas_medicas(id_estatus_cita);
end

-- ALMACENA LAS CONSULTAS MÉDICAS A PARTIR DE LAS CITAS DE LOS PACIENTES
if object_id('r4l.consultas_medicas', 'u') is null
begin
    create table r4l.consultas_medicas(
        id_consulta int identity(1, 1) primary key, 
        id_cita int not null, 
        id_medico int not null, 
        id_paciente int not null, 
        fecha date not null, 
        hora time(0) not null, 
        peso decimal(5, 2), 
        altura smallint, 
        presion_sistolica tinyint, 
        presion_diastolica tinyint, 
        frecuencia_cardiaca tinyint, 
        glucosa_ayunas decimal(5, 2), 
        glucosa_postprandial decimal(5, 2), 
        hemoglobina_glicosilada decimal(4, 2), 
        colesterol_total decimal(5, 2), 
        trigliceridos decimal(5, 2), 
        nivel_insulina decimal(5, 2), 
        notas nvarchar(255), 
        plan_tratamiento nvarchar(max), 
        constraint fk_cita_consulta foreign key(id_cita) 
            references r4l.citas_medicas(id_cita), 
        constraint fk_medico_consulta foreign key(id_medico) 
            references r4l.medicos(id_medico), 
        constraint fk_paciente_consulta foreign key(id_paciente) 
            references r4l.pacientes(id_paciente)
        /*
        constraint ck_peso check(peso > 0 and peso < 300), 
        constraint ck_altura check(altura between 30 and 250), 
        constraint ck_presion_sistolica check(presion_sistolica between 40 and 250), 
        constraint ck_presion_diastolica check(presion_diastolica between 30 and 200), 
        constraint ck_frecuencia_cardiaca check(frecuencia_cardiaca between 20 and 220), 
        constraint ck_glucosa_ayunas check(glucosa_ayunas >= 20 and glucosa_ayunas <= 1000), 
        constraint ck_glucosa_postprandial check(glucosa_postprandial >= 20 and glucosa_postprandial <= 1000), 
        constraint ck_hemoglobina_glicosilada check(hemoglobina_glicosilada between 3 and 20), 
        constraint ck_colesterol_total check(colesterol_total >= 50 and colesterol_total <= 1000), 
        constraint ck_trigliceridos check(trigliceridos >= 20 and trigliceridos <= 5000), 
        constraint ck_nivel_insulina check(nivel_insulina >= 0 and nivel_insulina <= 5000)
        */
    );
    create index ix_consultas_medicas_id_cita on r4l.consultas_medicas(id_cita);
    create index ix_consultas_medicas_id_paciente on r4l.consultas_medicas(id_paciente);
    create index ix_consultas_medicas_id_medico on r4l.consultas_medicas(id_medico);
    create index ix_consultas_medicas_fecha on r4l.consultas_medicas(fecha);
end

/*
-- ALMACENA LOS HISTÓRICOS DE LOS DIAGNÓSTICOS DE DIABETES DE LOS PACIENTES
if object_id('r4l.diagnosticos_pacientes', 'u') is null
begin
    create table r4l.diagnosticos_pacientes(
        id_diagnostico int identity(1, 1) primary key, 
        id_medico int not null, 
        id_paciente int not null, 
        id_tipo_diabetes int not null, 
        id_consulta int not null, 
        fecha date not null, 
        notas nvarchar(255), 
        constraint fk_medico_diagnostico foreign key(id_medico) 
            references r4l.medicos(id_medico), 
        constraint fk_paciente_diagnostico foreign key(id_paciente) 
            references r4l.pacientes(id_paciente), 
        constraint fk_tipo_diabetes_diagnostico foreign key(id_tipo_diabetes) 
            references r4l.tipos_diabetes(id_tipo_diabetes), 
        constraint fk_consulta_diagnostico foreign key(id_consulta) 
            references r4l.consultas_medicas(id_consulta)
        /*
        constraint ck_fecha_diagnostico check(fecha_diagnostico <= getdate())
        */
    );
    create index ix_diagnosticos_pacientes_id_paciente on r4l.diagnosticos_pacientes(id_paciente);
    create index ix_diagnosticos_pacientes_id_consulta on r4l.diagnosticos_pacientes(id_consulta);
    create index ix_diagnosticos_pacientes_fecha on r4l.diagnosticos_pacientes(fecha);
end
*/

-- ALMACENA LOS SÍNTOMAS REPORTADOS DURANTE LAS CONSULTAS MÉDICAS
if object_id('r4l.sintomas_consulta', 'u') is null
begin
    create table r4l.sintomas_consulta(
        id_sintoma int identity(1, 1) primary key, 
        id_consulta int not null, 
        id_sintoma_diabetes int not null, 
        intensidad tinyint, 
        duracion nvarchar(50), 
        notas nvarchar(255), 
        constraint fk_consulta_sintoma foreign key(id_consulta) 
            references r4l.consultas_medicas(id_consulta), 
        constraint fk_sintoma_consulta foreign key(id_sintoma_diabetes) 
            references r4l.sintomas_diabetes(id_sintoma_diabetes)
        /*
        constraint ck_intensidad_sintoma check(intensidad between 1 and 10)
        */
    );
    create index ix_sintomas_consulta_id_consulta on r4l.sintomas_consulta(id_consulta);
    create index ix_sintomas_consulta_id_sintoma_diabetes on r4l.sintomas_consulta(id_sintoma_diabetes);
end

-- ALMACENA LAS RECETAS MÉDICAS DERIVADAS DE LAS CONSULTAS
if object_id('r4l.recetas_medicas', 'u') is null
begin
    create table r4l.recetas_medicas(
        id_receta int identity(1, 1) primary key, 
        id_consulta int not null, 
        fecha date not null, 
        hora time(0) not null, 
        instrucciones_generales nvarchar(255), 
        url_pdf nvarchar(255), 
        constraint fk_consulta_receta foreign key(id_consulta) 
            references r4l.consultas_medicas(id_consulta)
        /*
        constraint chk_url_pdf check(
            url_pdf like 'http://%' or url_pdf like 'https://%' or url_pdf is null
        )
        */
    );
    create index ix_recetas_medicas_id_consulta on r4l.recetas_medicas(id_consulta);
end

-- ALMACENA LOS MEDICAMENTOS RECETADOS
if object_id('r4l.medicamentos_recetados', 'u') is null
begin
    create table r4l.medicamentos_recetados(
        id_medicamento int identity(1, 1) primary key, 
        id_receta int not null, 
        id_medicamento_diabetes int not null, 
        dosis nvarchar(50) not null, 
        frecuencia nvarchar(50) not null, 
        duracion nvarchar(50), 
        instrucciones_adicionales nvarchar(500), 
        constraint fk_receta_medicamento foreign key(id_receta) 
            references r4l.recetas_medicas(id_receta), 
        constraint fk_medicamento_recetado foreign key(id_medicamento_diabetes) 
            references r4l.medicamentos_diabetes(id_medicamento_diabetes)
    );
    create index ix_medicamentos_recetados_id_receta on r4l.medicamentos_recetados(id_receta);
end

-- ALMACENA LOS DETALLES DE LAS RUTINAS DE AUTOCUIDADO RECETADAS
if object_id('r4l.rutinas_recetadas', 'u') is null
begin
    create table r4l.rutinas_recetadas(
        id_rutina int identity(1, 1) primary key, 
        id_receta int not null, 
        id_tipo_rutina int not null, 
        id_comida int null, 
        descripcion nvarchar(500) not null, 
        frecuencia nvarchar(50), 
        duracion nvarchar(50), 
        notas nvarchar(255), 
        constraint fk_receta_rutina foreign key(id_receta) 
            references r4l.recetas_medicas(id_receta), 
        constraint fk_tipo_rutina foreign key(id_tipo_rutina) 
            references r4l.tipos_rutinas(id_tipo_rutina), 
        constraint fk_comida_rutina foreign key(id_comida) 
            references r4l.comidas(id_comida)
    );
    create index ix_rutinas_recetadas_id_receta on r4l.rutinas_recetadas(id_receta);
end
go