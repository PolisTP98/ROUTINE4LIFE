/*
==========================================================================================================================================================

-	Autor: Isaac Abdiel Sánchez López.
-	Fecha de creación: 04/11/2025.
-	Fecha de la última actualización: 04/11/2025.
-	Título: Nodo maestro.
-	Descripción: En este archivo se une toda la estructura de la base de datos.

==========================================================================================================================================================
*/


-- Borrar base de datos
:r "C:\Users\isaac_eosrxfr\OneDrive\Desktop\ROUTINE4LIFE_DB\Scripts\01_Base\01_BorrarBaseDeDatos.sql"

-- Carpeta 01_Base
:r "C:\Users\isaac_eosrxfr\OneDrive\Desktop\ROUTINE4LIFE_DB\Scripts\01_Base\02_CrearBaseDeDatos.sql"
:r "C:\Users\isaac_eosrxfr\OneDrive\Desktop\ROUTINE4LIFE_DB\Scripts\01_Base\03_CrearEsquemas.sql"

-- Carpeta 02_Tablas
:r "C:\Users\isaac_eosrxfr\OneDrive\Desktop\ROUTINE4LIFE_DB\Scripts\02_Tablas\01_Catalogos.sql"
:r "C:\Users\isaac_eosrxfr\OneDrive\Desktop\ROUTINE4LIFE_DB\Scripts\02_Tablas\02_TablasPrincipales.sql"
:r "C:\Users\isaac_eosrxfr\OneDrive\Desktop\ROUTINE4LIFE_DB\Scripts\02_Tablas\03_Auditorias.sql"
:r "C:\Users\isaac_eosrxfr\OneDrive\Desktop\ROUTINE4LIFE_DB\Scripts\02_Tablas\04_TablasPacientes.sql"

-- Carpeta 03_ProcedimientosAlmacenados

-- > Carpeta 01_Catalogos
:r "C:\Users\isaac_eosrxfr\OneDrive\Desktop\ROUTINE4LIFE_DB\Scripts\03_ProcedimientosAlmacenados\01_Catalogos\01_InsertarRegistros.sql"
:r "C:\Users\isaac_eosrxfr\OneDrive\Desktop\ROUTINE4LIFE_DB\Scripts\03_ProcedimientosAlmacenados\01_Catalogos\02_ActualizarRegistros.sql"
:r "C:\Users\isaac_eosrxfr\OneDrive\Desktop\ROUTINE4LIFE_DB\Scripts\03_ProcedimientosAlmacenados\01_Catalogos\03_EliminarRegistros.sql"

-- > Carpeta 02_TablasPrincipales
:r "C:\Users\isaac_eosrxfr\OneDrive\Desktop\ROUTINE4LIFE_DB\Scripts\03_ProcedimientosAlmacenados\02_TablasPrincipales\01_InsertarRegistros.sql"
:r "C:\Users\isaac_eosrxfr\OneDrive\Desktop\ROUTINE4LIFE_DB\Scripts\03_ProcedimientosAlmacenados\02_TablasPrincipales\02_ActualizarRegistros.sql"
:r "C:\Users\isaac_eosrxfr\OneDrive\Desktop\ROUTINE4LIFE_DB\Scripts\03_ProcedimientosAlmacenados\02_TablasPrincipales\03_EliminarRegistros.sql"
:r "C:\Users\isaac_eosrxfr\OneDrive\Desktop\ROUTINE4LIFE_DB\Scripts\03_ProcedimientosAlmacenados\02_TablasPrincipales\04_SuspenderMedicos.sql"
:r "C:\Users\isaac_eosrxfr\OneDrive\Desktop\ROUTINE4LIFE_DB\Scripts\03_ProcedimientosAlmacenados\02_TablasPrincipales\05_ReactivarRegistros.sql"
:r "C:\Users\isaac_eosrxfr\OneDrive\Desktop\ROUTINE4LIFE_DB\Scripts\03_ProcedimientosAlmacenados\02_TablasPrincipales\06_InsertarPacientes.sql"
:r "C:\Users\isaac_eosrxfr\OneDrive\Desktop\ROUTINE4LIFE_DB\Scripts\03_ProcedimientosAlmacenados\02_TablasPrincipales\07_ActualizarPacientes.sql"
:r "C:\Users\isaac_eosrxfr\OneDrive\Desktop\ROUTINE4LIFE_DB\Scripts\03_ProcedimientosAlmacenados\02_TablasPrincipales\08_EliminarPacientes.sql"
:r "C:\Users\isaac_eosrxfr\OneDrive\Desktop\ROUTINE4LIFE_DB\Scripts\03_ProcedimientosAlmacenados\02_TablasPrincipales\09_SuspenderPacientes.sql"
:r "C:\Users\isaac_eosrxfr\OneDrive\Desktop\ROUTINE4LIFE_DB\Scripts\03_ProcedimientosAlmacenados\02_TablasPrincipales\10_ReactivarPacientes.sql"

-- Carpeta 04_Triggers
:r "C:\Users\isaac_eosrxfr\OneDrive\Desktop\ROUTINE4LIFE_DB\Scripts\04_Triggers\01_Auditorias.sql"

-- Carpeta 05_Funciones
:r "C:\Users\isaac_eosrxfr\OneDrive\Desktop\ROUTINE4LIFE_DB\Scripts\05_Funciones\01_CalcularDatos.sql"

-- Carpeta 06_DatosCatalogos
:r "C:\Users\isaac_eosrxfr\OneDrive\Desktop\ROUTINE4LIFE_DB\Scripts\06_DatosDeCatalogos\01_Sexos.sql"
:r "C:\Users\isaac_eosrxfr\OneDrive\Desktop\ROUTINE4LIFE_DB\Scripts\06_DatosDeCatalogos\02_RolesUsuarios.sql"
:r "C:\Users\isaac_eosrxfr\OneDrive\Desktop\ROUTINE4LIFE_DB\Scripts\06_DatosDeCatalogos\03_EstatusUsuarios.sql"
:r "C:\Users\isaac_eosrxfr\OneDrive\Desktop\ROUTINE4LIFE_DB\Scripts\06_DatosDeCatalogos\04_Continentes.sql"
:r "C:\Users\isaac_eosrxfr\OneDrive\Desktop\ROUTINE4LIFE_DB\Scripts\06_DatosDeCatalogos\05_Paises.sql"
:r "C:\Users\isaac_eosrxfr\OneDrive\Desktop\ROUTINE4LIFE_DB\Scripts\06_DatosDeCatalogos\06_DocumentosLegales.sql"
:r "C:\Users\isaac_eosrxfr\OneDrive\Desktop\ROUTINE4LIFE_DB\Scripts\06_DatosDeCatalogos\07_Sucursales.sql"
:r "C:\Users\isaac_eosrxfr\OneDrive\Desktop\ROUTINE4LIFE_DB\Scripts\06_DatosDeCatalogos\08_Departamentos.sql"
:r "C:\Users\isaac_eosrxfr\OneDrive\Desktop\ROUTINE4LIFE_DB\Scripts\06_DatosDeCatalogos\09_TiposContratos.sql"
:r "C:\Users\isaac_eosrxfr\OneDrive\Desktop\ROUTINE4LIFE_DB\Scripts\06_DatosDeCatalogos\10_Especialidades.sql"
:r "C:\Users\isaac_eosrxfr\OneDrive\Desktop\ROUTINE4LIFE_DB\Scripts\06_DatosDeCatalogos\11_Subespecialidades.sql"
:r "C:\Users\isaac_eosrxfr\OneDrive\Desktop\ROUTINE4LIFE_DB\Scripts\06_DatosDeCatalogos\12_ResultadosCursos.sql"
:r "C:\Users\isaac_eosrxfr\OneDrive\Desktop\ROUTINE4LIFE_DB\Scripts\06_DatosDeCatalogos\13_Procedimientos.sql"
:r "C:\Users\isaac_eosrxfr\OneDrive\Desktop\ROUTINE4LIFE_DB\Scripts\06_DatosDeCatalogos\14_Comidas.sql"