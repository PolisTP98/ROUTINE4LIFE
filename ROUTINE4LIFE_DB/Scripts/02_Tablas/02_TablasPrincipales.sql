/*
==========================================================================================================================================================

-	Autor: Isaac Abdiel Sánchez López.
-	Fecha de creación: 02/11/2025.
-	Fecha de la última actualización: 09/11/2025.
-	Título: Tablas principales.
-	Descripción: En este archivo se crean las tablas principales de la base de datos.

==========================================================================================================================================================
*/


GO
IF OBJECT_ID('r4l.medico_personal', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.medico_personal (
        id_medico INT IDENTITY(1,1) PRIMARY KEY,
		id_sexo INT NOT NULL,
		id_pais INT NOT NULL,
		id_documento INT NOT NULL,
		id_estatus INT NOT NULL DEFAULT 1,
		fecha_eliminacion DATE NULL,
		fecha_suspension DATE NULL,
		fecha_reactivacion DATE NULL,
		fecha_registro DATE NOT NULL DEFAULT GETDATE(),
		numero_identificacion VARCHAR(50) NOT NULL,
		nombres NVARCHAR(100) NOT NULL,
		apellido_paterno NVARCHAR(50) NOT NULL,
		apellido_materno NVARCHAR(50) NULL,
		fecha_nacimiento DATE NOT NULL,
		telefono VARCHAR(13) NOT NULL,
		email_personal NVARCHAR(255) NOT NULL,
		rfc VARCHAR(13) NOT NULL,
		direccion NVARCHAR(255) NOT NULL,
		FOREIGN KEY(id_estatus)
			REFERENCES r4l.estatus_usuarios(id_estatus),
		FOREIGN KEY(id_sexo)
			REFERENCES r4l.sexos(id_sexo),
		FOREIGN KEY(id_pais)
			REFERENCES r4l.paises(id_pais),
		FOREIGN KEY(id_documento)
			REFERENCES r4l.documentos_legales(id_documento)
    );
END

IF OBJECT_ID('r4l.medico_laboral', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.medico_laboral (
		id_medico INT PRIMARY KEY NOT NULL,
		id_sucursal INT NOT NULL,
		id_departamento INT NOT NULL,
		id_contrato INT NOT NULL,
		id_estatus INT NOT NULL DEFAULT 1,
		fecha_eliminacion DATE NULL,
		fecha_suspension DATE NULL,
		fecha_reactivacion DATE NULL,
		fecha_registro DATE NOT NULL DEFAULT GETDATE(),
		fecha_inicio DATE NOT NULL,
		fecha_fin DATE NULL,
		anios_experiencia TINYINT NOT NULL,
		nss NVARCHAR(50) NOT NULL,
		FOREIGN KEY(id_medico)
			REFERENCES r4l.medico_personal(id_medico)
			ON DELETE CASCADE
			ON UPDATE CASCADE,
		FOREIGN KEY(id_sucursal)
			REFERENCES r4l.sucursales(id_sucursal),
		FOREIGN KEY(id_departamento)
			REFERENCES r4l.departamentos(id_departamento),
		FOREIGN KEY(id_contrato)
			REFERENCES r4l.tipos_contratos(id_contrato),
		FOREIGN KEY(id_estatus)
			REFERENCES r4l.estatus_usuarios(id_estatus),
		CONSTRAINT chk_anios_experiencia CHECK(anios_experiencia >= 0),
        CONSTRAINT chk_fechas_medico_laboral CHECK(fecha_fin IS NULL OR fecha_fin >= fecha_inicio)
	);
END

IF OBJECT_ID('r4l.historial_salarial', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.historial_salarial (
		id_historial INT IDENTITY(1,1) PRIMARY KEY,
		id_medico INT NOT NULL,
		id_estatus INT NOT NULL DEFAULT 1,
		fecha_eliminacion DATE NULL,
		fecha_reactivacion DATE NULL,
		fecha_registro DATE NOT NULL DEFAULT GETDATE(),
		fecha_inicio DATE NOT NULL DEFAULT GETDATE(),
		fecha_fin DATE NULL,
		salario DECIMAL(10, 2) NOT NULL,
		FOREIGN KEY(id_medico)
			REFERENCES r4l.medico_personal(id_medico)
			ON DELETE CASCADE
			ON UPDATE CASCADE,
		FOREIGN KEY(id_estatus)
			REFERENCES r4l.estatus_usuarios(id_estatus),
		CONSTRAINT chk_salario CHECK(salario >= 0),
		CONSTRAINT chk_fechas_historial_salarial CHECK(fecha_fin IS NULL OR fecha_fin >= fecha_inicio)
	);
END

IF OBJECT_ID('r4l.especialidades_medico', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.especialidades_medico (
		id_especialidad_medico INT IDENTITY(1,1) PRIMARY KEY,
		id_medico INT NOT NULL,
		id_especialidad INT NOT NULL,
		id_estatus INT NOT NULL DEFAULT 1,
		fecha_eliminacion DATE NULL,
		fecha_reactivacion DATE NULL,
		fecha_registro DATE NOT NULL DEFAULT GETDATE(),
		institucion_graduacion NVARCHAR(255) NOT NULL,
		cedula_profesional NVARCHAR(50) NOT NULL,
		FOREIGN KEY(id_medico)
			REFERENCES r4l.medico_personal(id_medico)
			ON DELETE CASCADE
			ON UPDATE CASCADE,
		FOREIGN KEY(id_especialidad)
			REFERENCES r4l.especialidades(id_especialidad)
			ON UPDATE CASCADE,
		FOREIGN KEY(id_estatus)
			REFERENCES r4l.estatus_usuarios(id_estatus)
	);
END

IF OBJECT_ID('r4l.subespecialidades_medico', 'U') IS NULL
BEGIN
	CREATE TABLE r4l.subespecialidades_medico (
		id_subespecialidad_medico INT IDENTITY(1,1) PRIMARY KEY,
		id_especialidad_medico INT NOT NULL,
		id_subespecialidad INT NOT NULL,
		id_estatus INT NOT NULL DEFAULT 1,
		fecha_eliminacion DATE NULL,
		fecha_reactivacion DATE NULL,
		fecha_registro DATE NOT NULL DEFAULT GETDATE(),
		FOREIGN KEY(id_especialidad_medico)
			REFERENCES r4l.especialidades_medico(id_especialidad_medico)
			ON DELETE CASCADE
			ON UPDATE CASCADE,
		FOREIGN KEY(id_subespecialidad)
			REFERENCES r4l.subespecialidades(id_subespecialidad),
		FOREIGN KEY(id_estatus)
			REFERENCES r4l.estatus_usuarios(id_estatus)
	);
END

IF OBJECT_ID('r4l.cursos', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.cursos (
        id_curso INT IDENTITY(1,1) PRIMARY KEY,
		id_estatus INT NOT NULL DEFAULT 1,
		fecha_eliminacion DATE NULL,
		fecha_reactivacion DATE NULL,
		fecha_registro DATE NOT NULL DEFAULT GETDATE(),
		fecha_inicio DATE NOT NULL DEFAULT GETDATE(),
        fecha_fin DATE NULL,
        nombre NVARCHAR(255) NOT NULL,
        curso_interno BIT NOT NULL DEFAULT 0,
        institucion NVARCHAR(255) NULL,
        duracion_horas SMALLINT NULL,
        certificado BIT NOT NULL DEFAULT 0,
        descripcion NVARCHAR(500) NULL,
        url_certificado NVARCHAR(255) NULL,
		FOREIGN KEY(id_estatus)
			REFERENCES r4l.estatus_usuarios(id_estatus),
		CONSTRAINT chk_duracion_curso CHECK(duracion_horas IS NULL OR duracion_horas >= 0),
        CONSTRAINT chk_fechas_curso CHECK(fecha_fin IS NULL OR fecha_fin >= fecha_inicio)
    );
END

IF OBJECT_ID('r4l.cursos_medico', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.cursos_medico (
		id_medico INT NOT NULL,
        id_curso INT NOT NULL,
        id_resultado INT NOT NULL,
		id_estatus INT NOT NULL DEFAULT 1,
		fecha_eliminacion DATE NULL,
		fecha_reactivacion DATE NULL,
		fecha_registro DATE NOT NULL DEFAULT GETDATE(),
        observaciones NVARCHAR(255) NULL,
        PRIMARY KEY(id_medico, id_curso),
        FOREIGN KEY(id_medico)
            REFERENCES r4l.medico_personal(id_medico)
            ON UPDATE CASCADE
            ON DELETE CASCADE,
        FOREIGN KEY(id_curso)
            REFERENCES r4l.cursos(id_curso)
            ON UPDATE CASCADE
            ON DELETE CASCADE,
		FOREIGN KEY(id_resultado)
			REFERENCES r4l.resultados_cursos(id_resultado),
		FOREIGN KEY(id_estatus)
			REFERENCES r4l.estatus_usuarios(id_estatus)
	);
END

IF OBJECT_ID('r4l.procedimientos_medico', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.procedimientos_medico (
		id_medico INT NOT NULL,
		id_procedimiento INT NOT NULL,
		id_estatus INT NOT NULL DEFAULT 1,
		fecha_eliminacion DATE NULL,
		fecha_reactivacion DATE NULL,
		fecha_registro DATE NOT NULL DEFAULT GETDATE(),
		PRIMARY KEY(id_medico, id_procedimiento),
		FOREIGN KEY(id_medico)
			REFERENCES r4l.medico_personal(id_medico)
			ON DELETE CASCADE
			ON UPDATE CASCADE,
		FOREIGN KEY(id_procedimiento)
			REFERENCES r4l.procedimientos(id_procedimiento),
		FOREIGN KEY(id_estatus)
			REFERENCES r4l.estatus_usuarios(id_estatus)
	);
END

IF OBJECT_ID('r4l.hospitales_anteriores', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.hospitales_anteriores (
		id_hospital INT IDENTITY(1,1) PRIMARY KEY,
		id_pais INT NOT NULL,
		id_estatus INT NOT NULL DEFAULT 1,
		fecha_eliminacion DATE NULL,
		fecha_reactivacion DATE NULL,
		fecha_registro DATE NOT NULL DEFAULT GETDATE(),
		nombre NVARCHAR(255) NOT NULL,
		direccion NVARCHAR(255) NOT NULL,
		telefono VARCHAR(20) NOT NULL,
		FOREIGN KEY(id_pais)
			REFERENCES r4l.paises(id_pais),
		FOREIGN KEY(id_estatus)
			REFERENCES r4l.estatus_usuarios(id_estatus)
	);
END

IF OBJECT_ID('r4l.hospitales_anteriores_medico', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.hospitales_anteriores_medico (
		id_medico INT NOT NULL,
		id_hospital INT NOT NULL,
		id_estatus INT NOT NULL DEFAULT 1,
		fecha_eliminacion DATE NULL,
		fecha_reactivacion DATE NULL,
		fecha_registro DATE NOT NULL DEFAULT GETDATE(),
		fecha_inicio DATE NOT NULL,
		fecha_fin DATE NOT NULL,
		PRIMARY KEY(id_medico, id_hospital),
		FOREIGN KEY(id_medico)
			REFERENCES r4l.medico_personal(id_medico)
			ON DELETE CASCADE
			ON UPDATE CASCADE,
		FOREIGN KEY(id_hospital)
			REFERENCES r4l.hospitales_anteriores(id_hospital),
		FOREIGN KEY(id_estatus)
			REFERENCES r4l.estatus_usuarios(id_estatus),
		CONSTRAINT chk_fechas_hospital CHECK(fecha_fin >= fecha_inicio)
	);
END

IF OBJECT_ID('r4l.usuarios', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.usuarios (
		id_medico INT PRIMARY KEY NOT NULL,
		id_rol INT NOT NULL,
		id_estatus INT NOT NULL DEFAULT 1,
		fecha_eliminacion DATE NULL,
		fecha_suspension DATE NULL,
		fecha_reactivacion DATE NULL,
		fecha_registro DATE NOT NULL DEFAULT GETDATE(),
		username NVARCHAR(50) NOT NULL,
		email_laboral NVARCHAR(255) NOT NULL,
		contrasena_cifrada VARCHAR(255) NOT NULL,
		url_imagen_perfil NVARCHAR(255) NOT NULL,
		FOREIGN KEY(id_medico)
			REFERENCES r4l.medico_personal(id_medico)
			ON DELETE CASCADE
			ON UPDATE CASCADE,
		FOREIGN KEY(id_rol)
			REFERENCES r4l.roles_usuarios(id_rol),
		FOREIGN KEY(id_estatus)
			REFERENCES r4l.estatus_usuarios(id_estatus),
		CONSTRAINT chk_rol_usuario CHECK(id_rol IN (1, 2)),
		CONSTRAINT chk_fechas_usuario CHECK(fecha_eliminacion IS NULL OR fecha_eliminacion >= fecha_registro)
	);
END

IF OBJECT_ID('r4l.pacientes', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.pacientes (
        id_paciente INT IDENTITY(1,1) PRIMARY KEY,
		id_sexo INT NOT NULL,
		id_pais INT NOT NULL,
		id_estatus INT NOT NULL DEFAULT 1,
		fecha_eliminacion DATE NULL,
		fecha_reactivacion DATE NULL,
		fecha_registro DATE NOT NULL DEFAULT GETDATE(),
		nombres NVARCHAR(100) NOT NULL,
		apellido_paterno NVARCHAR(50) NOT NULL,
		apellido_materno NVARCHAR(50) NULL,
		fecha_nacimiento DATE NOT NULL,
		FOREIGN KEY(id_sexo)
			REFERENCES r4l.sexos(id_sexo),
		FOREIGN KEY(id_pais)
			REFERENCES r4l.paises(id_pais),
		FOREIGN KEY(id_estatus)
			REFERENCES r4l.estatus_usuarios(id_estatus)
    );
END

IF OBJECT_ID('r4l.cita_paciente', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.cita_paciente (
        id_cita INT IDENTITY(1,1) PRIMARY KEY,
		id_medico INT NOT NULL,
		id_paciente INT NOT NULL,
		id_estatus INT NOT NULL DEFAULT 1,
		fecha_eliminacion DATE NULL,
		fecha_reactivacion DATE NULL,
		fecha_registro DATE NOT NULL DEFAULT GETDATE(),
		fecha_cita DATE NOT NULL DEFAULT GETDATE(),
		hora_cita TIME NOT NULL,
		peso DECIMAL(5, 2) NOT NULL,
		altura SMALLINT NOT NULL,
		presion_arterial VARCHAR(10) NOT NULL,
		frecuencia_cardiaca TINYINT NOT NULL,
		glucosa_ayuno DECIMAL(5, 2) NOT NULL,
		glucosa_postprandial DECIMAL(5, 2) NOT NULL,
		hba1c DECIMAL(4, 2) NOT NULL,
		colesterol_total DECIMAL(5, 2) NOT NULL,
		trigliceridos DECIMAL(5, 2) NOT NULL,
		insulina_actual DECIMAL(5, 2) NOT NULL,
		recomendaciones NVARCHAR(MAX) NULL,
		fecha_siguiente_cita DATE NULL,
		hora_siguiente_cita TIME NULL,
		FOREIGN KEY(id_medico)
			REFERENCES r4l.medico_personal(id_medico)
			ON DELETE CASCADE
			ON UPDATE CASCADE,
		FOREIGN KEY(id_paciente)
			REFERENCES r4l.pacientes(id_paciente)
			ON DELETE CASCADE
			ON UPDATE CASCADE,
		FOREIGN KEY(id_estatus)
			REFERENCES r4l.estatus_usuarios(id_estatus),
		CONSTRAINT chk_peso CHECK(peso > 0),
		CONSTRAINT chk_altura CHECK(altura > 0),
		CONSTRAINT chk_frecuencia_cardiaca CHECK(frecuencia_cardiaca > 0),
		CONSTRAINT chk_glucosa_ayuno CHECK(glucosa_ayuno >= 0),
		CONSTRAINT chk_glucosa_postprandial CHECK(glucosa_postprandial >= 0),
		CONSTRAINT chk_hba1c CHECK(hba1c >= 0),
		CONSTRAINT chk_colesterol CHECK(colesterol_total >= 0),
		CONSTRAINT chk_trigliceridos CHECK(trigliceridos >= 0),
		CONSTRAINT chk_insulina CHECK(insulina_actual >= 0),
		CONSTRAINT chk_fechas_cita CHECK(fecha_siguiente_cita IS NULL OR fecha_siguiente_cita >= fecha_cita)
    );
END

IF OBJECT_ID('r4l.sintomas_paciente', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.sintomas_paciente (
		id_sintoma INT IDENTITY(1,1) PRIMARY KEY,
		id_cita INT NOT NULL,
		id_estatus INT NOT NULL DEFAULT 1,
		fecha_eliminacion DATE NULL,
		fecha_reactivacion DATE NULL,
		fecha_registro DATE NOT NULL DEFAULT GETDATE(),
		descripcion NVARCHAR(255) NOT NULL,
		FOREIGN KEY(id_cita)
			REFERENCES r4l.cita_paciente(id_cita)
			ON DELETE CASCADE
			ON UPDATE CASCADE,
		FOREIGN KEY(id_estatus)
			REFERENCES r4l.estatus_usuarios(id_estatus)
	);
END

IF OBJECT_ID('r4l.tratamientos_paciente', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.tratamientos_paciente (
		id_tratamiento INT IDENTITY(1,1) PRIMARY KEY,
		id_cita INT NOT NULL,
		id_estatus INT NOT NULL DEFAULT 1,
		fecha_eliminacion DATE NULL,
		fecha_reactivacion DATE NULL,
		fecha_registro DATE NOT NULL DEFAULT GETDATE(),
		fecha_inicio DATE NOT NULL DEFAULT GETDATE(),
		fecha_fin DATE NULL,
		medicamento NVARCHAR(100) NOT NULL,
		concentracion VARCHAR(20) NOT NULL,
		dosis VARCHAR(50) NOT NULL,
		frecuencia VARCHAR(50) NOT NULL,
		duracion VARCHAR(50) NOT NULL,
		observaciones VARCHAR(255) NULL,
		url_imagen_medicamento NVARCHAR(255) NOT NULL,
		FOREIGN KEY(id_cita)
			REFERENCES r4l.cita_paciente(id_cita)
			ON DELETE CASCADE
			ON UPDATE CASCADE,
		FOREIGN KEY(id_estatus)
			REFERENCES r4l.estatus_usuarios(id_estatus),
		CONSTRAINT chk_fechas_tratamiento CHECK(fecha_fin IS NULL OR fecha_fin >= fecha_inicio)
	);
END

IF OBJECT_ID('r4l.rutina_ejercicio', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.rutina_ejercicio (
		id_rutina_ejercicio INT IDENTITY(1,1) PRIMARY KEY,
		id_cita INT NOT NULL,
		id_estatus INT NOT NULL DEFAULT 1,
		fecha_eliminacion DATE NULL,
		fecha_reactivacion DATE NULL,
		fecha_registro DATE NOT NULL DEFAULT GETDATE(),
		fecha_inicio DATE NOT NULL DEFAULT GETDATE(),
		fecha_fin DATE NULL,
		ejercicio NVARCHAR(100) NOT NULL,
		duracion_minutos SMALLINT NOT NULL,
		intensidad VARCHAR(50) NOT NULL,
		frecuencia_semanal TINYINT NOT NULL,
		observaciones VARCHAR(255) NULL,
		FOREIGN KEY(id_cita)
			REFERENCES r4l.cita_paciente(id_cita)
			ON DELETE CASCADE
			ON UPDATE CASCADE,
			FOREIGN KEY(id_estatus)
			REFERENCES r4l.estatus_usuarios(id_estatus),
		CONSTRAINT chk_fechas_rutina_ejercicio CHECK(fecha_fin IS NULL OR fecha_fin >= fecha_inicio),
		CONSTRAINT chk_duracion_rutina_ejercicio CHECK(duracion_minutos > 0),
		CONSTRAINT chk_frecuencia_rutina_ejercicio CHECK(frecuencia_semanal > 0)
	);
END

IF OBJECT_ID('r4l.rutina_alimentacion', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.rutina_alimentacion (
		id_rutina_alimentacion INT IDENTITY(1,1) PRIMARY KEY,
		id_cita INT NOT NULL,
		id_comida INT NOT NULL,
		id_estatus INT NOT NULL DEFAULT 1,
		fecha_eliminacion DATE NULL,
		fecha_reactivacion DATE NULL,
		fecha_registro DATE NOT NULL DEFAULT GETDATE(),
		fecha_inicio DATE NOT NULL DEFAULT GETDATE(),
		fecha_fin DATE NULL,
		platillo NVARCHAR(100) NOT NULL,
		calorias_aprox SMALLINT NOT NULL,
		duracion_dias SMALLINT NOT NULL,
		observaciones VARCHAR(255) NULL,
		url_imagen_platillo NVARCHAR(255) NOT NULL,
		FOREIGN KEY(id_cita)
			REFERENCES r4l.cita_paciente(id_cita)
			ON DELETE CASCADE
			ON UPDATE CASCADE,
		FOREIGN KEY(id_comida)
			REFERENCES r4l.comidas(id_comida),
		FOREIGN KEY(id_estatus)
			REFERENCES r4l.estatus_usuarios(id_estatus),
		CONSTRAINT chk_calorias CHECK(calorias_aprox >= 0),
		CONSTRAINT chk_fechas_rutina_alimentacion CHECK(fecha_fin IS NULL OR fecha_fin >= fecha_inicio),
		CONSTRAINT chk_duracion_dias CHECK(duracion_dias > 0)
	);
END
GO

IF OBJECT_ID('r4l.descripcion_rutina', 'U') IS NULL
BEGIN
    CREATE TABLE r4l.descripcion_rutina (
		id_rutina_alimentacion INT PRIMARY KEY NOT NULL,
		id_estatus INT NOT NULL DEFAULT 1,
		fecha_eliminacion DATE NULL,
		fecha_reactivacion DATE NULL,
		fecha_registro DATE NOT NULL DEFAULT GETDATE(),
		descripcion VARCHAR(MAX) NOT NULL,
		FOREIGN KEY(id_rutina_alimentacion)
			REFERENCES r4l.rutina_alimentacion(id_rutina_alimentacion)
			ON DELETE CASCADE
			ON UPDATE CASCADE,
		FOREIGN KEY(id_estatus)
			REFERENCES r4l.estatus_usuarios(id_estatus)
	);
END
GO