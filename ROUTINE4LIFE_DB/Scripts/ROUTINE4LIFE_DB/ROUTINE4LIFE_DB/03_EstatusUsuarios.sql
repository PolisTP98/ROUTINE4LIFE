/*
==========================================================================================================================================================

-	Autor: Isaac Abdiel Sánchez López.
-	Fecha de creación: 06/11/2025.
-	Fecha de la última actualización: 07/11/2025.
-	Título: Datos de catálogo.
-	Descripción: En este archivo se insertan los datos de la tabla catálogo "estatus_usuarios".

==========================================================================================================================================================
*/


GO
EXEC r4l.sp_insert_estatus_usuario 'Activo';
EXEC r4l.sp_insert_estatus_usuario 'Inactivo';
EXEC r4l.sp_insert_estatus_usuario 'Suspendido';
GO