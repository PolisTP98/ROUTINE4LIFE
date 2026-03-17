-- UTILIZAR SQLCMD Mode PARA EJECUTAR LOS SCRIPTS DE LA CREACIÓN DEL MODELO DE LA BASE DE DATOS EN ORDEN DESCENDENTE

-- ..\routine4life_db\



-- 01_base_de_datos\
:r "D:\databases\university\routine4life_db\01_base_de_datos\01_eliminar.sql"
:r "D:\databases\university\routine4life_db\01_base_de_datos\02_crear.sql"
:r "D:\databases\university\routine4life_db\01_base_de_datos\03_esquemas.sql"



-- 02_tablas\

-- 01_catalogos\
:r "D:\databases\university\routine4life_db\02_tablas\01_catalogos\01_generales.sql"
:r "D:\databases\university\routine4life_db\02_tablas\01_catalogos\02_medicos.sql"
:r "D:\databases\university\routine4life_db\02_tablas\01_catalogos\03_pacientes.sql"

-- 02_principales\
:r "D:\databases\university\routine4life_db\02_tablas\02_principales\01_medicos.sql"
:r "D:\databases\university\routine4life_db\02_tablas\02_principales\02_pacientes.sql"
:r "D:\databases\university\routine4life_db\02_tablas\02_principales\03_generales.sql"

-- 03_auditorias\
:r "D:\databases\university\routine4life_db\02_tablas\03_auditorias\01_generales.sql"



-- 03_procedimientos_almacenados\

-- 01_catalogos\

-- 01_insertar\
:r "D:\databases\university\routine4life_db\03_procedimientos_almacenados\01_catalogos\01_insertar\01_generales.sql"
:r "D:\databases\university\routine4life_db\03_procedimientos_almacenados\01_catalogos\01_insertar\02_medicos.sql"
:r "D:\databases\university\routine4life_db\03_procedimientos_almacenados\01_catalogos\01_insertar\03_pacientes.sql"

-- 02_actualizar\
:r "D:\databases\university\routine4life_db\03_procedimientos_almacenados\01_catalogos\02_actualizar\01_generales.sql"
:r "D:\databases\university\routine4life_db\03_procedimientos_almacenados\01_catalogos\02_actualizar\02_medicos.sql"
:r "D:\databases\university\routine4life_db\03_procedimientos_almacenados\01_catalogos\02_actualizar\03_pacientes.sql"

-- 03_eliminar\
:r "D:\databases\university\routine4life_db\03_procedimientos_almacenados\01_catalogos\03_eliminar\01_generales.sql"
:r "D:\databases\university\routine4life_db\03_procedimientos_almacenados\01_catalogos\03_eliminar\02_medicos.sql"
:r "D:\databases\university\routine4life_db\03_procedimientos_almacenados\01_catalogos\03_eliminar\03_pacientes.sql"

-- 02_principales\

-- 01_insertar\
:r "D:\databases\university\routine4life_db\03_procedimientos_almacenados\02_principales\01_insertar\01_medicos.sql"
:r "D:\databases\university\routine4life_db\03_procedimientos_almacenados\02_principales\01_insertar\02_pacientes.sql"
:r "D:\databases\university\routine4life_db\03_procedimientos_almacenados\02_principales\01_insertar\03_generales.sql"

-- 02_actualizar\
:r "D:\databases\university\routine4life_db\03_procedimientos_almacenados\02_principales\02_actualizar\01_medicos.sql"
:r "D:\databases\university\routine4life_db\03_procedimientos_almacenados\02_principales\02_actualizar\02_pacientes.sql"
:r "D:\databases\university\routine4life_db\03_procedimientos_almacenados\02_principales\02_actualizar\03_generales.sql"

-- 03_eliminar\
:r "D:\databases\university\routine4life_db\03_procedimientos_almacenados\02_principales\03_eliminar\01_medicos.sql"
:r "D:\databases\university\routine4life_db\03_procedimientos_almacenados\02_principales\03_eliminar\02_pacientes.sql"
:r "D:\databases\university\routine4life_db\03_procedimientos_almacenados\02_principales\03_eliminar\03_generales.sql"



-- 04_triggers
:r "D:\databases\university\routine4life_db\04_triggers\01_auditorias.sql"



-- 05_datos_de_catalogos
:r "D:\databases\university\routine4life_db\05_datos_de_catalogos\01_generales.sql"
:r "D:\databases\university\routine4life_db\05_datos_de_catalogos\02_medicos.sql"
:r "D:\databases\university\routine4life_db\05_datos_de_catalogos\03_pacientes.sql"