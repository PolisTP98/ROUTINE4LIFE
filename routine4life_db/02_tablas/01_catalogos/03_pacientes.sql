go

-- ALMACENA LOS TIPOS DE REGISTROS QUE UN PACIENTE PUEDE REALIZAR PARA EL MONITOREO DE SU DIABETES (GLUCOSA, CETONAS, PRESIÓN, ETC.)
if object_id('r4l.tipos_registros', 'u') is null
begin
    create table r4l.tipos_registros(
        id_tipo_registro int identity(1, 1) primary key, 
        id_unidad int not null, 
        nombre nvarchar(50) not null, 
        descripcion nvarchar(255), 
        constraint fk_unidad_registro foreign key(id_unidad) 
            references r4l.unidades_medida(id_unidad), 
        constraint uq_nombre_registro unique(nombre)
    );
    create index ix_tipos_registros_id_unidad on r4l.tipos_registros(id_unidad);
end
go