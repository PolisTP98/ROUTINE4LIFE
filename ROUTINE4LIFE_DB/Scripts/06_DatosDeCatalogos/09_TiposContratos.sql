/*
==========================================================================================================================================================

-	Autor: Isaac Abdiel Sánchez López.
-	Fecha de creación: 06/11/2025.
-	Fecha de la última actualización: 07/11/2025.
-	Título: Datos de catálogo.
-	Descripción: En este archivo se insertan los datos de la tabla catálogo "tipos_contratos".

==========================================================================================================================================================
*/


GO
EXEC r4l.sp_insert_tipo_contrato 'Base';
EXEC r4l.sp_insert_tipo_contrato 'Interino';
EXEC r4l.sp_insert_tipo_contrato 'Eventual';
EXEC r4l.sp_insert_tipo_contrato 'Honorarios';
EXEC r4l.sp_insert_tipo_contrato 'Contrato temporal';
EXEC r4l.sp_insert_tipo_contrato 'Contrato por guardias';
EXEC r4l.sp_insert_tipo_contrato 'Residente';
GO