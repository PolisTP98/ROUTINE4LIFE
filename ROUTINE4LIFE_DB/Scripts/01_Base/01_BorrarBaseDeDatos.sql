GO
IF EXISTS (SELECT 1 FROM sys.databases WHERE name = 'routine4life')
BEGIN
    DROP DATABASE routine4life;
END
GO