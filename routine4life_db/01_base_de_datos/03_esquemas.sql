go
if not exists(select * from sys.schemas where name = 'r4l')
begin
    exec sp_executesql N'create schema [r4l]';
end
go