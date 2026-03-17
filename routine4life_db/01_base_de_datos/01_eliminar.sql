go
if exists(select 1 from sys.databases where name = 'routine4life')
begin
    drop database routine4life;
end
go