/*
==========================================================================================================================================================

-	Autor: Isaac Abdiel Sánchez López.
-	Fecha de creación: 01/11/2025.
-	Fecha de la última actualización: 01/11/2025.
-	Título: Crear esquemas.
-	Descripción: En este archivo se crean los esquemas a utilizar en la base de datos.

==========================================================================================================================================================
*/


GO
IF NOT EXISTS (SELECT * FROM sys.schemas WHERE name = 'r4l')
BEGIN
    EXEC('CREATE SCHEMA r4l');
END;
GO