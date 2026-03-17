go
if not exists(select 1 from sys.databases where name = 'routine4life')
begin
    create database routine4life;
end
go

use routine4life;
select db_name() as current_database;
go