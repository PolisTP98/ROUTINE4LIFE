/*
==========================================================================================================================================================

-	Autor: Isaac Abdiel Sánchez López.
-	Fecha de creación: 06/11/2025.
-	Fecha de la última actualización: 07/11/2025.
-	Título: Datos de catálogo.
-	Descripción: En este archivo se insertan los datos de la tabla catálogo "resultados_cursos".

==========================================================================================================================================================
*/


GO
EXEC r4l.sp_insert_resultado_curso 'Aprobado';
EXEC r4l.sp_insert_resultado_curso 'Reprobado';
EXEC r4l.sp_insert_resultado_curso 'En curso';
EXEC r4l.sp_insert_resultado_curso 'Pendiente';
GO