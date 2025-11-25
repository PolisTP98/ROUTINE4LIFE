/*
==========================================================================================================================================================

-	Autor: Isaac Abdiel Sánchez López.
-	Fecha de creación: 06/11/2025.
-	Fecha de la última actualización: 07/11/2025.
-	Título: Datos de catálogo.
-	Descripción: En este archivo se insertan los datos de la tabla catálogo "roles_usuarios".

==========================================================================================================================================================
*/


GO
EXEC r4l.sp_insert_rol_usuario 'Médico administrador';
EXEC r4l.sp_insert_rol_usuario 'Médico';
EXEC r4l.sp_insert_rol_usuario 'Paciente';
GO