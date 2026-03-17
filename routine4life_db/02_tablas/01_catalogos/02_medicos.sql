go

-- ALMACENA LAS SUCURSALES HOSPITALARIAS CON SU CÓDIGO, NOMBRE Y URL DE LA UBICACIÓN
if object_id('r4l.sucursales_hospitalarias', 'u') is null
begin
    create table r4l.sucursales_hospitalarias(
        id_sucursal int identity(1, 1) primary key, 
        codigo varchar(20) not null, 
        nombre nvarchar(50) not null, 
        url_ubicacion nvarchar(255) not null, 
        constraint uq_codigo_sucursal unique(codigo)
        /*
        constraint ck_sucursal_url check(
            url_ubicacion like 'http://%' or url_ubicacion like 'https://%'
        )
        */
    );
end

-- ALMACENA LAS PRESENTACIONES DE LOS MEDICAMENTOS (TABLETA, JARABE, INYECCIÓN, ETC.)
if object_id('r4l.presentaciones_medicamentos', 'u') is null
begin
    create table r4l.presentaciones_medicamentos(
        id_presentacion int identity(1, 1) primary key, 
        nombre nvarchar(20) not null, 
        constraint uq_nombre_presentacion unique(nombre)
    );
end

-- ALMACENA LAS UNIDADES DE MEDIDA DE LOS MEDICAMENTOS (mg, ml, mg/dL, ETC.)
if object_id('r4l.unidades_medida', 'u') is null
begin
    create table r4l.unidades_medida(
        id_unidad int identity(1, 1) primary key, 
        nombre nvarchar(10) not null, 
        constraint uq_nombre_unidad unique(nombre)
    );
end

-- ALMACENA LOS TIPOS DE DIABETES (TIPO 1, TIPO 2, GESTACIONAL)
if object_id('r4l.tipos_diabetes', 'u') is null
begin
    create table r4l.tipos_diabetes(
        id_tipo_diabetes int identity(1, 1) primary key, 
        nombre nvarchar(20) not null, 
        constraint uq_nombre_diabetes unique(nombre)
    );
end

-- ALMACENA LOS SÍNTOMAS COMÚNES DE LA DIABETES (ORINA RECURRENTE, SED EXCESIVA, ETC.)
if object_id('r4l.sintomas_diabetes', 'u') is null
begin
    create table r4l.sintomas_diabetes(
        id_sintoma_diabetes int identity(1, 1) primary key, 
        nombre nvarchar(50) not null, 
        descripcion nvarchar(255), 
        constraint uq_nombre_sintoma unique(nombre)
    );
end

-- ALMACENA LOS MEDICAMENTOS PARA LA DIABETES CON SU NOMBRE, CONCENTRACIÓN, PRESENTACIÓN Y UNIDAD DE MEDIDA
if object_id('r4l.medicamentos_diabetes', 'u') is null
begin
    create table r4l.medicamentos_diabetes(
        id_medicamento_diabetes int identity(1, 1) primary key, 
        id_presentacion int not null, 
        id_unidad int not null, 
        nombre nvarchar(50) not null, 
        concentracion int not null, 
        descripcion nvarchar(255), 
        constraint fk_presentacion_medicamento foreign key(id_presentacion) 
            references r4l.presentaciones_medicamentos(id_presentacion), 
        constraint fk_unidad_medicamento foreign key(id_unidad) 
            references r4l.unidades_medida(id_unidad), 
        constraint uq_medicamento_diabetes unique(nombre, concentracion, id_presentacion, id_unidad)
        /*
        constraint ck_medicamento_concentracion check(concentracion > 0)
        */
    );
    create index ix_medicamentos_diabetes_id_presentacion on r4l.medicamentos_diabetes(id_presentacion);
    create index ix_medicamentos_diabetes_id_unidad on r4l.medicamentos_diabetes(id_unidad);
end

-- ALMACENA LOS TIPOS DE RUTINAS PARA EL TRATAMIENTO DE LA DIABETES (ALIMENTICIA, EJERCICIO, DESCANSO, ETC.)
if object_id('r4l.tipos_rutinas', 'u') is null
begin
    create table r4l.tipos_rutinas(
        id_tipo_rutina int identity(1, 1) primary key, 
        nombre nvarchar(50) not null, 
        descripcion nvarchar(255), 
        constraint uq_nombre_rutina unique(nombre)
    );
end

-- ALMACENA LOS ESTADOS DE LAS CITAS MÉDICAS (PROGRAMADA, CONFIRMADA, CANCELADA, ETC.)
if object_id('r4l.estatus_citas', 'u') is null
begin
    create table r4l.estatus_citas(
        id_estatus_cita int identity(1, 1) primary key, 
        nombre nvarchar(20) not null, 
        constraint uq_nombre_estatus_cita unique(nombre)
    );
end

-- ALMACENA LAS ESPECIALIDADES MÉDICAS (CARDIOLOGÍA, ENDOCRINOLOGÍA, ETC.)
if object_id('r4l.especialidades_medicas', 'u') is null
begin
    create table r4l.especialidades_medicas(
        id_especialidad int identity(1, 1) primary key, 
        nombre nvarchar(50) not null, 
        descripcion nvarchar(255), 
        constraint uq_nombre_especialidad unique(nombre)
    );
end
go