/*
==========================================================================================================================================================

-	Autor: Isaac Abdiel Sánchez López.
-	Fecha de creación: 03/11/2025.
-	Fecha de la última actualización: 03/11/2025.
-	Título: Funciones.
-	Descripción: En este archivo se crean funciones para calcular diversos datos.

==========================================================================================================================================================
*/


GO
CREATE OR ALTER FUNCTION r4l.fn_calcular_edad
(
    @fecha_nacimiento DATE
)
RETURNS TINYINT
AS
BEGIN
    DECLARE @edad TINYINT;

    SET @edad = DATEDIFF(YEAR, @fecha_nacimiento, GETDATE());

    IF MONTH(@fecha_nacimiento) > MONTH(GETDATE())
       OR (MONTH(@fecha_nacimiento) = MONTH(GETDATE()) AND DAY(@fecha_nacimiento) > DAY(GETDATE()))
    BEGIN
        SET @edad = @edad - 1;
    END

    RETURN @edad;
END;
GO

GO
CREATE OR ALTER FUNCTION r4l.fn_calcular_imc
(
    @peso DECIMAL(5, 2),
	@altura DECIMAL(3, 2)
)
RETURNS DECIMAL(5, 2)
AS
BEGIN
	IF @altura <= 0 OR @peso <= 0
        RETURN NULL;

    RETURN @peso / POWER(@altura, 2);
END;
GO