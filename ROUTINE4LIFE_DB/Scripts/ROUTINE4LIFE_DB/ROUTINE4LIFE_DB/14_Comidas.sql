/*
==========================================================================================================================================================

-	Autor: Isaac Abdiel Sánchez López.
-	Fecha de creación: 06/11/2025.
-	Fecha de la última actualización: 07/11/2025.
-	Título: Datos de catálogo.
-	Descripción: En este archivo se insertan los datos de la tabla catálogo "comidas".

==========================================================================================================================================================
*/


GO
EXEC r4l.sp_insert_comida 'Desayuno';
EXEC r4l.sp_insert_comida 'Almuerzo';
EXEC r4l.sp_insert_comida 'Comida';
EXEC r4l.sp_insert_comida 'Merienda';
EXEC r4l.sp_insert_comida 'Cena';
EXEC r4l.sp_insert_comida 'Snack';
EXEC r4l.sp_insert_comida 'Refrigerio';
EXEC r4l.sp_insert_comida 'Postre';
GO