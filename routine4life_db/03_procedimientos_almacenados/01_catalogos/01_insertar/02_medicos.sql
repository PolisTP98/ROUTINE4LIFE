-- PROCEDIMIENTO ALMACENADO r4l.usp_insertar_sucursales_hospitalarias
go
create or alter procedure r4l.usp_insertar_sucursales_hospitalarias
    @codigo varchar(20),
    @nombre nvarchar(50),
    @url_ubicacion nvarchar(255)
as
begin
    set nocount on;
    begin try
        insert into r4l.sucursales_hospitalarias(codigo, nombre, url_ubicacion)
        values(@codigo, @nombre, @url_ubicacion);
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al insertar sucursal hospitalaria: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_insertar_presentaciones_medicamentos
go
create or alter procedure r4l.usp_insertar_presentaciones_medicamentos
    @nombre nvarchar(20)
as
begin
    set nocount on;
    begin try
        insert into r4l.presentaciones_medicamentos(nombre)
        values(@nombre);
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al insertar presentación de medicamento: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_insertar_unidades_medida
go
create or alter procedure r4l.usp_insertar_unidades_medida
    @nombre nvarchar(10)
as
begin
    set nocount on;
    begin try
        insert into r4l.unidades_medida(nombre)
        values(@nombre);
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al insertar unidad de medida: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_insertar_tipos_diabetes
go
create or alter procedure r4l.usp_insertar_tipos_diabetes
    @nombre nvarchar(20)
as
begin
    set nocount on;
    begin try
        insert into r4l.tipos_diabetes(nombre)
        values(@nombre);
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al insertar tipo de diabetes: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_insertar_sintomas_diabetes
go
create or alter procedure r4l.usp_insertar_sintomas_diabetes
    @nombre nvarchar(50),
    @descripcion nvarchar(255) = null
as
begin
    set nocount on;
    begin try
        insert into r4l.sintomas_diabetes(nombre, descripcion)
        values(@nombre, @descripcion);
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al insertar síntoma de diabetes: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_insertar_medicamentos_diabetes
go
create or alter procedure r4l.usp_insertar_medicamentos_diabetes
    @id_presentacion int,
    @id_unidad int,
    @nombre nvarchar(50),
    @concentracion int,
    @descripcion nvarchar(255) = null
as
begin
    set nocount on;
    begin try
        insert into r4l.medicamentos_diabetes(id_presentacion, id_unidad, nombre, concentracion, descripcion)
        values(@id_presentacion, @id_unidad, @nombre, @concentracion, @descripcion);
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al insertar medicamento para diabetes: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_insertar_tipos_rutinas
go
create or alter procedure r4l.usp_insertar_tipos_rutinas
    @nombre nvarchar(50),
    @descripcion nvarchar(255) = null
as
begin
    set nocount on;
    begin try
        insert into r4l.tipos_rutinas(nombre, descripcion)
        values(@nombre, @descripcion);
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al insertar tipo de rutina: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_insertar_estatus_citas
go
create or alter procedure r4l.usp_insertar_estatus_citas
    @nombre nvarchar(20)
as
begin
    set nocount on;
    begin try
        insert into r4l.estatus_citas(nombre)
        values(@nombre);
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al insertar estatus de cita: %s', 16, 1, @mensaje_error);
    end catch
end;
go

-- PROCEDIMIENTO ALMACENADO r4l.usp_insertar_especialidades_medicas
go
create or alter procedure r4l.usp_insertar_especialidades_medicas
    @nombre nvarchar(50),
    @descripcion nvarchar(255) = null
as
begin
    set nocount on;
    begin try
        insert into r4l.especialidades_medicas(nombre, descripcion)
        values(@nombre, @descripcion);
    end try
    begin catch
        declare @mensaje_error nvarchar(255) = error_message();
        raiserror('Error al insertar especialidad médica: %s', 16, 1, @mensaje_error);
    end catch
end;
go