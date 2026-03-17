-- INSERTAR REGISTROS EN TABLA CATÁLOGO r4l.presentaciones_medicamentos
exec r4l.usp_insertar_presentaciones_medicamentos @nombre = 'Tableta';
exec r4l.usp_insertar_presentaciones_medicamentos @nombre = 'Cápsula';
exec r4l.usp_insertar_presentaciones_medicamentos @nombre = 'Solución inyectable';
exec r4l.usp_insertar_presentaciones_medicamentos @nombre = 'Pluma inyectable';
exec r4l.usp_insertar_presentaciones_medicamentos @nombre = 'Vial';
exec r4l.usp_insertar_presentaciones_medicamentos @nombre = 'Ampolla';
exec r4l.usp_insertar_presentaciones_medicamentos @nombre = 'Jarabe';
exec r4l.usp_insertar_presentaciones_medicamentos @nombre = 'Polvo';



-- INSERTAR REGISTROS EN TABLA CATÁLOGO r4l.unidades_medida
exec r4l.usp_insertar_unidades_medida @nombre = 'mg';
exec r4l.usp_insertar_unidades_medida @nombre = 'g';
exec r4l.usp_insertar_unidades_medida @nombre = 'mcg';
exec r4l.usp_insertar_unidades_medida @nombre = 'ml';
exec r4l.usp_insertar_unidades_medida @nombre = 'UI';
exec r4l.usp_insertar_unidades_medida @nombre = 'mg/dL';
exec r4l.usp_insertar_unidades_medida @nombre = 'mmol/L';
exec r4l.usp_insertar_unidades_medida @nombre = '%';
exec r4l.usp_insertar_unidades_medida @nombre = 'mmHg';
exec r4l.usp_insertar_unidades_medida @nombre = 'lpm';
exec r4l.usp_insertar_unidades_medida @nombre = 'cm';
exec r4l.usp_insertar_unidades_medida @nombre = 'kg';



-- INSERTAR REGISTROS EN TABLA CATÁLOGO r4l.tipos_diabetes
exec r4l.usp_insertar_tipos_diabetes @nombre = 'Tipo 1';
exec r4l.usp_insertar_tipos_diabetes @nombre = 'Tipo 2';
exec r4l.usp_insertar_tipos_diabetes @nombre = 'Gestacional';
exec r4l.usp_insertar_tipos_diabetes @nombre = 'MODY';
exec r4l.usp_insertar_tipos_diabetes @nombre = 'LADA';
exec r4l.usp_insertar_tipos_diabetes @nombre = 'Secundaria';
exec r4l.usp_insertar_tipos_diabetes @nombre = 'Neonatal';
exec r4l.usp_insertar_tipos_diabetes @nombre = 'Inducida por fármacos';



-- INSERTAR REGISTROS EN TABLA CATÁLOGO r4l.sintomas_diabetes

-- SÍNTOMAS CLÁSICOS DE DIABETES
exec r4l.usp_insertar_sintomas_diabetes @nombre = 'Poliuria', @descripcion = 'Orina frecuente y abundante';
exec r4l.usp_insertar_sintomas_diabetes @nombre = 'Polidipsia', @descripcion = 'Sed excesiva';
exec r4l.usp_insertar_sintomas_diabetes @nombre = 'Polifagia', @descripcion = 'Hambre excesiva';
exec r4l.usp_insertar_sintomas_diabetes @nombre = 'Pérdida de peso inexplicable', @descripcion = 'Bajar de peso sin razón aparente';
exec r4l.usp_insertar_sintomas_diabetes @nombre = 'Fatiga', @descripcion = 'Cansancio constante';
exec r4l.usp_insertar_sintomas_diabetes @nombre = 'Visión borrosa', @descripcion = 'Dificultad para enfocar la vista';
exec r4l.usp_insertar_sintomas_diabetes @nombre = 'Cicatrización lenta', @descripcion = 'Heridas que tardan en sanar';
exec r4l.usp_insertar_sintomas_diabetes @nombre = 'Infecciones frecuentes', @descripcion = 'Infecciones urinarias, de piel o encías';

-- SÍNTOMAS DE HIPERGLUCEMIA
exec r4l.usp_insertar_sintomas_diabetes @nombre = 'Náuseas', @descripcion = 'Sensación de malestar estomacal';
exec r4l.usp_insertar_sintomas_diabetes @nombre = 'Vómito', @descripcion = 'Expulsión violenta del contenido estomacal';
exec r4l.usp_insertar_sintomas_diabetes @nombre = 'Dolor abdominal', @descripcion = 'Dolor en el área del estómago';
exec r4l.usp_insertar_sintomas_diabetes @nombre = 'Aliento afrutado', @descripcion = 'Olor dulce en el aliento (cetonas)';
exec r4l.usp_insertar_sintomas_diabetes @nombre = 'Confusión', @descripcion = 'Dificultad para pensar con claridad';
exec r4l.usp_insertar_sintomas_diabetes @nombre = 'Pérdida del conocimiento', @descripcion = 'Desmayo o inconsciencia';

-- SÍNTOMAS DE HIPOGLUCEMIA
exec r4l.usp_insertar_sintomas_diabetes @nombre = 'Temblores', @descripcion = 'Sacudidas o movimientos involuntarios';
exec r4l.usp_insertar_sintomas_diabetes @nombre = 'Sudoración fría', @descripcion = 'Transpiración sin calor';
exec r4l.usp_insertar_sintomas_diabetes @nombre = 'Palpitaciones', @descripcion = 'Corazón acelerado';
exec r4l.usp_insertar_sintomas_diabetes @nombre = 'Mareos', @descripcion = 'Sensación de desvanecimiento';
exec r4l.usp_insertar_sintomas_diabetes @nombre = 'Debilidad', @descripcion = 'Falta de fuerza';
exec r4l.usp_insertar_sintomas_diabetes @nombre = 'Irritabilidad', @descripcion = 'Mal humor o nerviosismo';
exec r4l.usp_insertar_sintomas_diabetes @nombre = 'Hormigueo', @descripcion = 'Sensación de alfileres en labios o dedos';

-- COMPLICACIONES CRÓNICAS
exec r4l.usp_insertar_sintomas_diabetes @nombre = 'Hormigueo en pies', @descripcion = 'Neuropatía diabética periférica';
exec r4l.usp_insertar_sintomas_diabetes @nombre = 'Entumecimiento', @descripcion = 'Pérdida de sensibilidad en extremidades';
exec r4l.usp_insertar_sintomas_diabetes @nombre = 'Dolor al caminar', @descripcion = 'Claudicación intermitente';
exec r4l.usp_insertar_sintomas_diabetes @nombre = 'Úlceras en pies', @descripcion = 'Heridas que no cicatrizan';



-- INSERTAR REGISTROS EN LA TABLA CATÁLOGO r4l.medicamentos_diabetes
exec r4l.usp_insertar_medicamentos_diabetes @id_presentacion = 1, @id_unidad = 1, @nombre = 'Metformina', @concentracion = 500, @descripcion = 'Tableta de 500 mg';
exec r4l.usp_insertar_medicamentos_diabetes @id_presentacion = 1, @id_unidad = 1, @nombre = 'Metformina', @concentracion = 850, @descripcion = 'Tableta de 850 mg';
exec r4l.usp_insertar_medicamentos_diabetes @id_presentacion = 1, @id_unidad = 1, @nombre = 'Glibenclamida', @concentracion = 5, @descripcion = 'Tableta de 5 mg';
exec r4l.usp_insertar_medicamentos_diabetes @id_presentacion = 1, @id_unidad = 1, @nombre = 'Glimepirida', @concentracion = 2, @descripcion = 'Tableta de 2 mg';
exec r4l.usp_insertar_medicamentos_diabetes @id_presentacion = 1, @id_unidad = 1, @nombre = 'Sitagliptina', @concentracion = 100, @descripcion = 'Tableta de 100 mg';
exec r4l.usp_insertar_medicamentos_diabetes @id_presentacion = 1, @id_unidad = 1, @nombre = 'Empagliflozina', @concentracion = 25, @descripcion = 'Tableta de 25 mg';
exec r4l.usp_insertar_medicamentos_diabetes @id_presentacion = 4, @id_unidad = 5, @nombre = 'Insulina Glargina', @concentracion = 100, @descripcion = 'Pluma precargada 100 UI/ml, 3 ml';
exec r4l.usp_insertar_medicamentos_diabetes @id_presentacion = 4, @id_unidad = 5, @nombre = 'Insulina Aspart', @concentracion = 100, @descripcion = 'Pluma precargada 100 UI/ml, 3 ml';
exec r4l.usp_insertar_medicamentos_diabetes @id_presentacion = 4, @id_unidad = 5, @nombre = 'Insulina NPH', @concentracion = 100, @descripcion = 'Pluma precargada 100 UI/ml, 3 ml';
exec r4l.usp_insertar_medicamentos_diabetes @id_presentacion = 4, @id_unidad = 3, @nombre = 'Exenatida', @concentracion = 10, @descripcion = 'Pluma para inyección de 10 mcg/dosis';



-- INSERTAR REGISTROS EN TABLA CATÁLOGO r4l.tipos_rutinas
exec r4l.usp_insertar_tipos_rutinas @nombre = 'Alimenticia', @descripcion = 'Rutinas relacionadas con la dieta y alimentación';
exec r4l.usp_insertar_tipos_rutinas @nombre = 'Ejercicio', @descripcion = 'Rutinas de actividad física y ejercicio';
exec r4l.usp_insertar_tipos_rutinas @nombre = 'Descanso', @descripcion = 'Rutinas de sueño y períodos de descanso';
exec r4l.usp_insertar_tipos_rutinas @nombre = 'Medición', @descripcion = 'Rutinas para medir niveles de glucosa';
exec r4l.usp_insertar_tipos_rutinas @nombre = 'Medicación', @descripcion = 'Rutinas para administración de medicamentos';
exec r4l.usp_insertar_tipos_rutinas @nombre = 'Hidratación', @descripcion = 'Rutinas para consumo de agua y líquidos';
exec r4l.usp_insertar_tipos_rutinas @nombre = 'Cuidado de pies', @descripcion = 'Rutinas para inspección y cuidado de pies';



-- INSERTAR REGISTROS EN TABLA CATÁLOGO r4l.estatus_citas
exec r4l.usp_insertar_estatus_citas @nombre = 'Programada';
exec r4l.usp_insertar_estatus_citas @nombre = 'Confirmada';
exec r4l.usp_insertar_estatus_citas @nombre = 'Cancelada';
exec r4l.usp_insertar_estatus_citas @nombre = 'Completada';
exec r4l.usp_insertar_estatus_citas @nombre = 'Reprogramada';
exec r4l.usp_insertar_estatus_citas @nombre = 'No asistió';



-- INSERTAR REGISTROS EN TABLA CATÁLOGO r4l.especialidades_medicas
exec r4l.usp_insertar_especialidades_medicas @nombre = 'Endocrinología', @descripcion = 'Especialidad enfocada en el sistema endocrino y enfermedades como la diabetes';
exec r4l.usp_insertar_especialidades_medicas @nombre = 'Medicina Interna', @descripcion = 'Atención integral de pacientes adultos con enfermedades crónicas';
exec r4l.usp_insertar_especialidades_medicas @nombre = 'Medicina Familiar', @descripcion = 'Atención primaria y seguimiento de pacientes con diabetes';
exec r4l.usp_insertar_especialidades_medicas @nombre = 'Nutriología', @descripcion = 'Especialidad enfocada en la alimentación y nutrición';
exec r4l.usp_insertar_especialidades_medicas @nombre = 'Cardiología', @descripcion = 'Atención de complicaciones cardiovasculares de la diabetes';
exec r4l.usp_insertar_especialidades_medicas @nombre = 'Nefrología', @descripcion = 'Atención de complicaciones renales de la diabetes';
exec r4l.usp_insertar_especialidades_medicas @nombre = 'Oftalmología', @descripcion = 'Atención de complicaciones oculares de la diabetes';
exec r4l.usp_insertar_especialidades_medicas @nombre = 'Podología', @descripcion = 'Atención y cuidado de pies en pacientes diabéticos';
exec r4l.usp_insertar_especialidades_medicas @nombre = 'Psicología', @descripcion = 'Apoyo emocional y psicológico para pacientes con diabetes';