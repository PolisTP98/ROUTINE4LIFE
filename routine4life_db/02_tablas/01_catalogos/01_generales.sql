go

-- ALMACENA LOS TIPOS DE SEXOS DE LOS SERES HUMANOS (HOMBRE, MUJER, INTERSEXUAL)
if object_id('r4l.sexos', 'u') is null
begin
    create table r4l.sexos(
        id_sexo int identity(1, 1) primary key, 
        nombre nvarchar(20) not null, 
        constraint uq_nombre_sexo unique(nombre)
    );
end

-- ALMACENA LOS CONTINENTES (ÁFRICA, ASIA, OCEANÍA, ETC.)
if object_id('r4l.continentes', 'u') is null
begin
    create table r4l.continentes(
        id_continente int identity(1, 1) primary key, 
        nombre nvarchar(20) not null, 
        constraint uq_nombre_continente unique(nombre)
    );
end

-- ALMACENA LOS PAÍSES, SUS CÓDIGOS ISO Y PREFIJOS TELEFÓNICOS (ASOCIADOS A UN CONTINENTE)
if object_id('r4l.paises', 'u') is null
begin
    create table r4l.paises(
        id_pais int identity(1, 1) primary key, 
        id_continente int not null, 
        nombre nvarchar(50) not null, 
        codigo_iso char(3) not null, 
        codigo_telefonico varchar(6) not null, 
        constraint fk_continente_pais foreign key(id_continente) 
            references r4l.continentes(id_continente) 
            on delete cascade 
            on update cascade, 
        constraint uq_nombre_pais unique(nombre), 
        constraint uq_codigo_iso_pais unique(codigo_iso)
        /*
        constraint ck_pais_codigo_iso check(codigo_iso like '[A-Z][A-Z][A-Z]'), 
        constraint ck_pais_codigo_telefonico check(
            codigo_telefonico like '+%' and len(codigo_telefonico) between 2 and 6
        )
        */
    );
    create index ix_paises_id_continente on r4l.paises(id_continente);
end

-- ALMACENA LAS COMIDAS DEL DÍA (DESAYUNO, COMIDA, CENA, ETC.)
if object_id('r4l.comidas', 'u') is null
begin
    create table r4l.comidas(
        id_comida int identity(1, 1) primary key, 
        nombre nvarchar(20) not null, 
        constraint uq_nombre_comida unique(nombre)
    );
end

-- ALMACENA LOS ROLES DE LOS USUARIOS EN EL SISTEMA (MÉDICO ADMINISTRADOR, MÉDICO, USUARIO, ETC.)
if object_id('r4l.roles_usuarios', 'u') is null
begin
    create table r4l.roles_usuarios(
        id_rol int identity(1, 1) primary key, 
        nombre nvarchar(20) not null, 
        constraint uq_nombre_rol unique(nombre)
    );
end

-- ALMACENA LOS ESTATUS DE LOS USUARIOS EN EL SISTEMA (ACTIVO, INACTIVO, SUSPENDIDO, ETC.)
if object_id('r4l.estatus_usuarios', 'u') is null
begin
    create table r4l.estatus_usuarios(
        id_estatus_usuario int identity(1, 1) primary key, 
        nombre nvarchar(20) not null, 
        descripcion nvarchar(100), 
        constraint uq_nombre_estatus_usuario unique(nombre)
    );
end
go