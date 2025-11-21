/*
==========================================================================================================================================================

-	Autor: Isaac Abdiel Sánchez López.
-	Fecha de creación: 01/11/2025.
-	Fecha de la última actualización: 04/11/2025.
-	Título: Crear base de datos.
-	Descripción: En este archivo se crea y usa la base de datos "routine4life".

==========================================================================================================================================================
*/


GO
IF NOT EXISTS (SELECT 1 FROM sys.databases WHERE name = 'routine4life')
BEGIN
    CREATE DATABASE routine4life;
END
GO

GO
USE routine4life;
SELECT DB_NAME() AS BaseActual;
GO