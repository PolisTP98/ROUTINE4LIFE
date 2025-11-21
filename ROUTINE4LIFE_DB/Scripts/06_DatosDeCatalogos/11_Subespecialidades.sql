/*
==========================================================================================================================================================

-	Autor: Isaac Abdiel Sánchez López.
-	Fecha de creación: 06/11/2025.
-	Fecha de la última actualización: 07/11/2025.
-	Título: Datos de catálogo.
-	Descripción: En este archivo se insertan los datos de la tabla catálogo "subespecialidades".

==========================================================================================================================================================
*/


GO
-- Alergología (1)
EXEC r4l.sp_insert_subespecialidad 1, 'Alergia e Inmunología Clínica';
EXEC r4l.sp_insert_subespecialidad 1, 'Alergia Respiratoria';
EXEC r4l.sp_insert_subespecialidad 1, 'Alergia Pediátrica';

-- Anestesiología (2)
EXEC r4l.sp_insert_subespecialidad 2, 'Anestesia Cardiovascular';
EXEC r4l.sp_insert_subespecialidad 2, 'Anestesia Pediátrica';
EXEC r4l.sp_insert_subespecialidad 2, 'Anestesia Obstétrica';
EXEC r4l.sp_insert_subespecialidad 2, 'Anestesia Regional y del Dolor';

-- Angiología (3)
EXEC r4l.sp_insert_subespecialidad 3, 'Cirugía Endovascular';
EXEC r4l.sp_insert_subespecialidad 3, 'Flebología';
EXEC r4l.sp_insert_subespecialidad 3, 'Linfología';

-- Cardiología (4)
EXEC r4l.sp_insert_subespecialidad 4, 'Cardiología Intervencionista';
EXEC r4l.sp_insert_subespecialidad 4, 'Electrofisiología';
EXEC r4l.sp_insert_subespecialidad 4, 'Cardiología Pediátrica';
EXEC r4l.sp_insert_subespecialidad 4, 'Ecocardiografía';

-- Cirugía general (5)
EXEC r4l.sp_insert_subespecialidad 5, 'Cirugía Laparoscópica';
EXEC r4l.sp_insert_subespecialidad 5, 'Cirugía Oncológica';
EXEC r4l.sp_insert_subespecialidad 5, 'Cirugía de Trauma y Urgencias';

-- Cirugía plástica y reconstructiva (6)
EXEC r4l.sp_insert_subespecialidad 6, 'Cirugía Estética';
EXEC r4l.sp_insert_subespecialidad 6, 'Cirugía Reconstructiva';
EXEC r4l.sp_insert_subespecialidad 6, 'Microcirugía';

-- Cirugía torácica (7)
EXEC r4l.sp_insert_subespecialidad 7, 'Cirugía de Pulmón';
EXEC r4l.sp_insert_subespecialidad 7, 'Cirugía Esofágica';
EXEC r4l.sp_insert_subespecialidad 7, 'Cirugía Mediastinal';

-- Cirugía vascular (8)
EXEC r4l.sp_insert_subespecialidad 8, 'Cirugía Arterial';
EXEC r4l.sp_insert_subespecialidad 8, 'Cirugía Venosa';
EXEC r4l.sp_insert_subespecialidad 8, 'Angioplastia';

-- Dermatología (9)
EXEC r4l.sp_insert_subespecialidad 9, 'Dermatología Pediátrica';
EXEC r4l.sp_insert_subespecialidad 9, 'Dermatopatología';
EXEC r4l.sp_insert_subespecialidad 9, 'Dermatooncología';
EXEC r4l.sp_insert_subespecialidad 9, 'Tricología';

-- Endocrinología (10)
EXEC r4l.sp_insert_subespecialidad 10, 'Endocrinología Pediátrica';
EXEC r4l.sp_insert_subespecialidad 10, 'Diabetología';
EXEC r4l.sp_insert_subespecialidad 10, 'Neuroendocrinología';

-- Epidemiología (11)
EXEC r4l.sp_insert_subespecialidad 11, 'Epidemiología Hospitalaria';
EXEC r4l.sp_insert_subespecialidad 11, 'Epidemiología de Campo';
EXEC r4l.sp_insert_subespecialidad 11, 'Epidemiología Molecular';

-- Gastroenterología (12)
EXEC r4l.sp_insert_subespecialidad 12, 'Endoscopía Digestiva';
EXEC r4l.sp_insert_subespecialidad 12, 'Hepatología';
EXEC r4l.sp_insert_subespecialidad 12, 'Gastroenterología Pediátrica';

-- Geriatría (13)
EXEC r4l.sp_insert_subespecialidad 13, 'Geriatría Clínica';
EXEC r4l.sp_insert_subespecialidad 13, 'Medicina Paliativa del Adulto Mayor';
EXEC r4l.sp_insert_subespecialidad 13, 'Neurogeriatría';

-- Ginecología y obstetricia (14)
EXEC r4l.sp_insert_subespecialidad 14, 'Medicina Materno Fetal';
EXEC r4l.sp_insert_subespecialidad 14, 'Ginecología Oncológica';
EXEC r4l.sp_insert_subespecialidad 14, 'Biología de la Reproducción Humana';
EXEC r4l.sp_insert_subespecialidad 14, 'Uroginecología';

-- Hematología (15)
EXEC r4l.sp_insert_subespecialidad 15, 'Hematología Pediátrica';
EXEC r4l.sp_insert_subespecialidad 15, 'Hemostasia y Trombosis';
EXEC r4l.sp_insert_subespecialidad 15, 'Oncohematología';

-- Infectología (16)
EXEC r4l.sp_insert_subespecialidad 16, 'Infectología Pediátrica';
EXEC r4l.sp_insert_subespecialidad 16, 'Infecciones Nosocomiales';
EXEC r4l.sp_insert_subespecialidad 16, 'Infecciones Tropicales';

-- Medicina del deporte (17)
EXEC r4l.sp_insert_subespecialidad 17, 'Traumatología Deportiva';
EXEC r4l.sp_insert_subespecialidad 17, 'Rehabilitación Deportiva';
EXEC r4l.sp_insert_subespecialidad 17, 'Nutrición Deportiva';

-- Medicina de urgencias (18)
EXEC r4l.sp_insert_subespecialidad 18, 'Emergencias Cardiovasculares';
EXEC r4l.sp_insert_subespecialidad 18, 'Emergencias Pediátricas';
EXEC r4l.sp_insert_subespecialidad 18, 'Medicina de Desastres';

-- Medicina familiar (19)
EXEC r4l.sp_insert_subespecialidad 19, 'Salud Comunitaria';
EXEC r4l.sp_insert_subespecialidad 19, 'Atención Integral del Adulto Mayor';
EXEC r4l.sp_insert_subespecialidad 19, 'Medicina Preventiva Familiar';

-- Medicina física y rehabilitación (20)
EXEC r4l.sp_insert_subespecialidad 20, 'Rehabilitación Neurológica';
EXEC r4l.sp_insert_subespecialidad 20, 'Rehabilitación Musculoesquelética';
EXEC r4l.sp_insert_subespecialidad 20, 'Rehabilitación Pediátrica';

-- Medicina interna (21)
EXEC r4l.sp_insert_subespecialidad 21, 'Nefrología Clínica';
EXEC r4l.sp_insert_subespecialidad 21, 'Endocrinología Clínica';
EXEC r4l.sp_insert_subespecialidad 21, 'Reumatología Clínica';

-- Nefrología (22)
EXEC r4l.sp_insert_subespecialidad 22, 'Nefrología Pediátrica';
EXEC r4l.sp_insert_subespecialidad 22, 'Trasplante Renal';
EXEC r4l.sp_insert_subespecialidad 22, 'Diálisis y Hemodiálisis';

-- Neonatología (23)
EXEC r4l.sp_insert_subespecialidad 23, 'Cuidado Intensivo Neonatal';
EXEC r4l.sp_insert_subespecialidad 23, 'Nutrición Neonatal';
EXEC r4l.sp_insert_subespecialidad 23, 'Reanimación Neonatal';

-- Neumología (24)
EXEC r4l.sp_insert_subespecialidad 24, 'Neumología Pediátrica';
EXEC r4l.sp_insert_subespecialidad 24, 'Medicina del Sueño';
EXEC r4l.sp_insert_subespecialidad 24, 'Broncoscopía';

-- Neurología (25)
EXEC r4l.sp_insert_subespecialidad 25, 'Neurología Pediátrica';
EXEC r4l.sp_insert_subespecialidad 25, 'Neurofisiología Clínica';
EXEC r4l.sp_insert_subespecialidad 25, 'Epileptología';
EXEC r4l.sp_insert_subespecialidad 25, 'Cefaleas y Dolor Neurológico';

-- Neurocirugía (26)
EXEC r4l.sp_insert_subespecialidad 26, 'Neurocirugía Pediátrica';
EXEC r4l.sp_insert_subespecialidad 26, 'Neurocirugía Vascular';
EXEC r4l.sp_insert_subespecialidad 26, 'Neurocirugía Oncológica';
EXEC r4l.sp_insert_subespecialidad 26, 'Columna y Nervio Periférico';

-- Nutriología (27)
EXEC r4l.sp_insert_subespecialidad 27, 'Nutrición Clínica';
EXEC r4l.sp_insert_subespecialidad 27, 'Nutrición Parenteral y Enteral';
EXEC r4l.sp_insert_subespecialidad 27, 'Nutrición Comunitaria';

-- Odontología (28)
EXEC r4l.sp_insert_subespecialidad 28, 'Endodoncia';
EXEC r4l.sp_insert_subespecialidad 28, 'Periodoncia';
EXEC r4l.sp_insert_subespecialidad 28, 'Ortodoncia';
EXEC r4l.sp_insert_subespecialidad 28, 'Odontopediatría';

-- Oftalmología (29)
EXEC r4l.sp_insert_subespecialidad 29, 'Oftalmología Pediátrica';
EXEC r4l.sp_insert_subespecialidad 29, 'Retina y Vítreo';
EXEC r4l.sp_insert_subespecialidad 29, 'Glaucoma';
EXEC r4l.sp_insert_subespecialidad 29, 'Córnea y Cirugía Refractiva';

-- Oncología médica (30)
EXEC r4l.sp_insert_subespecialidad 30, 'Oncología Pediátrica';
EXEC r4l.sp_insert_subespecialidad 30, 'Tumores Sólidos';
EXEC r4l.sp_insert_subespecialidad 30, 'Hematología Oncológica';

-- Otorrinolaringología (31)
EXEC r4l.sp_insert_subespecialidad 31, 'Otología y Neurotología';
EXEC r4l.sp_insert_subespecialidad 31, 'Rinología y Cirugía Endoscópica';
EXEC r4l.sp_insert_subespecialidad 31, 'Laringología';
EXEC r4l.sp_insert_subespecialidad 31, 'Otorrinolaringología Pediátrica';

-- Pediatría (32)
EXEC r4l.sp_insert_subespecialidad 32, 'Pediatría de Urgencias';
EXEC r4l.sp_insert_subespecialidad 32, 'Pediatría del Desarrollo';
EXEC r4l.sp_insert_subespecialidad 32, 'Pediatría Intensiva';

-- Psiquiatría (33)
EXEC r4l.sp_insert_subespecialidad 33, 'Psiquiatría Infantil y Adolescente';
EXEC r4l.sp_insert_subespecialidad 33, 'Psiquiatría Geriátrica';
EXEC r4l.sp_insert_subespecialidad 33, 'Psiquiatría de Enlace';
EXEC r4l.sp_insert_subespecialidad 33, 'Psiquiatría Forense';

-- Radiología (34)
EXEC r4l.sp_insert_subespecialidad 34, 'Neurorradiología';
EXEC r4l.sp_insert_subespecialidad 34, 'Radiología Intervencionista';
EXEC r4l.sp_insert_subespecialidad 34, 'Radiología Pediátrica';
EXEC r4l.sp_insert_subespecialidad 34, 'Imagen Mamaria';

-- Reumatología (35)
EXEC r4l.sp_insert_subespecialidad 35, 'Reumatología Pediátrica';
EXEC r4l.sp_insert_subespecialidad 35, 'Enfermedades Autoinmunes';
EXEC r4l.sp_insert_subespecialidad 35, 'Reumatología Clínica Avanzada';

-- Traumatología y ortopedia (36)
EXEC r4l.sp_insert_subespecialidad 36, 'Ortopedia Pediátrica';
EXEC r4l.sp_insert_subespecialidad 36, 'Artroscopía';
EXEC r4l.sp_insert_subespecialidad 36, 'Columna Vertebral';
EXEC r4l.sp_insert_subespecialidad 36, 'Reemplazos Articulares';

-- Urología (37)
EXEC r4l.sp_insert_subespecialidad 37, 'Urología Pediátrica';
EXEC r4l.sp_insert_subespecialidad 37, 'Urología Oncológica';
EXEC r4l.sp_insert_subespecialidad 37, 'Endourología y Laparoscopía';

-- Medicina crítica (38)
EXEC r4l.sp_insert_subespecialidad 38, 'Terapia Intensiva Adultos';
EXEC r4l.sp_insert_subespecialidad 38, 'Terapia Intensiva Pediátrica';
EXEC r4l.sp_insert_subespecialidad 38, 'Terapia Intensiva Cardiovascular';

-- Anatomía patológica (39)
EXEC r4l.sp_insert_subespecialidad 39, 'Patología Quirúrgica';
EXEC r4l.sp_insert_subespecialidad 39, 'Citopatología';
EXEC r4l.sp_insert_subespecialidad 39, 'Patología Molecular';

-- Cirugía cardiovascular (40)
EXEC r4l.sp_insert_subespecialidad 40, 'Cirugía Cardiaca Pediátrica';
EXEC r4l.sp_insert_subespecialidad 40, 'Cirugía Coronaria';
EXEC r4l.sp_insert_subespecialidad 40, 'Cirugía Valvular';
EXEC r4l.sp_insert_subespecialidad 40, 'Cirugía Aórtica';

-- Cirugía maxilofacial (41)
EXEC r4l.sp_insert_subespecialidad 41, 'Cirugía Ortognática';
EXEC r4l.sp_insert_subespecialidad 41, 'Trauma Maxilofacial';
EXEC r4l.sp_insert_subespecialidad 41, 'Cirugía Reconstructiva Facial';

-- Cirugía pediátrica (42)
EXEC r4l.sp_insert_subespecialidad 42, 'Cirugía Neonatal';
EXEC r4l.sp_insert_subespecialidad 42, 'Cirugía Gastrointestinal Pediátrica';
EXEC r4l.sp_insert_subespecialidad 42, 'Cirugía Torácica Pediátrica';

-- Cirugía oncológica (43)
EXEC r4l.sp_insert_subespecialidad 43, 'Oncología Quirúrgica Gastrointestinal';
EXEC r4l.sp_insert_subespecialidad 43, 'Oncología Quirúrgica de Mama';
EXEC r4l.sp_insert_subespecialidad 43, 'Sarcomas y Tejidos Blandos';

-- Cirugía neurológica (44)
EXEC r4l.sp_insert_subespecialidad 44, 'Neurocirugía Funcional';
EXEC r4l.sp_insert_subespecialidad 44, 'Neurocirugía Oncológica';
EXEC r4l.sp_insert_subespecialidad 44, 'Neurocirugía de Columna';

-- Cirugía de cabeza y cuello (45)
EXEC r4l.sp_insert_subespecialidad 45, 'Oncología de Cabeza y Cuello';
EXEC r4l.sp_insert_subespecialidad 45, 'Cirugía Endocrina (Tiroides/Paratiroides)';
EXEC r4l.sp_insert_subespecialidad 45, 'Cirugía Reconstructiva de Cuello';

-- Cirugía de mano (46)
EXEC r4l.sp_insert_subespecialidad 46, 'Microcirugía de Mano';
EXEC r4l.sp_insert_subespecialidad 46, 'Cirugía de Nervio Periférico';
EXEC r4l.sp_insert_subespecialidad 46, 'Trauma de Mano';

-- Cirugía bariátrica (47)
EXEC r4l.sp_insert_subespecialidad 47, 'Cirugía Metabólica';
EXEC r4l.sp_insert_subespecialidad 47, 'Cirugía Laparoscópica Bariátrica';

-- Coloproctología (48)
EXEC r4l.sp_insert_subespecialidad 48, 'Cirugía Colorrectal';
EXEC r4l.sp_insert_subespecialidad 48, 'Proctología Avanzada';
EXEC r4l.sp_insert_subespecialidad 48, 'Enfermedad Inflamatoria Intestinal';

-- Angiología y cirugía vascular (49)
EXEC r4l.sp_insert_subespecialidad 49, 'Cirugía Endovascular';
EXEC r4l.sp_insert_subespecialidad 49, 'Flebología';
EXEC r4l.sp_insert_subespecialidad 49, 'Linfología';

-- Medicina nuclear (50)
EXEC r4l.sp_insert_subespecialidad 50, 'PET/CT';
EXEC r4l.sp_insert_subespecialidad 50, 'Terapia con Radioisótopos';
EXEC r4l.sp_insert_subespecialidad 50, 'Imagen Molecular';

-- Dermatopatología (51)
EXEC r4l.sp_insert_subespecialidad 51, 'Dermatopatología Quirúrgica';
EXEC r4l.sp_insert_subespecialidad 51, 'Dermatopatología Oncológica';
EXEC r4l.sp_insert_subespecialidad 51, 'Micología Médica';

-- Foniatría (52)
EXEC r4l.sp_insert_subespecialidad 52, 'Foniatría Pediátrica';
EXEC r4l.sp_insert_subespecialidad 52, 'Rehabilitación de la Voz';
EXEC r4l.sp_insert_subespecialidad 52, 'Trastornos del Lenguaje y Comunicación';

-- Gastroenterología pediátrica (53)
EXEC r4l.sp_insert_subespecialidad 53, 'Nutrición Pediátrica';
EXEC r4l.sp_insert_subespecialidad 53, 'Hepatología Pediátrica';
EXEC r4l.sp_insert_subespecialidad 53, 'Gastroenterología Endoscópica Pediátrica';

-- Ginecología oncológica (54)
EXEC r4l.sp_insert_subespecialidad 54, 'Cirugía Oncológica Ginecológica';
EXEC r4l.sp_insert_subespecialidad 54, 'Oncología de Mama';
EXEC r4l.sp_insert_subespecialidad 54, 'Oncología Reproductiva';

-- Hepatología (55)
EXEC r4l.sp_insert_subespecialidad 55, 'Trasplante Hepático';
EXEC r4l.sp_insert_subespecialidad 55, 'Hepatología Clínica';
EXEC r4l.sp_insert_subespecialidad 55, 'Enfermedad Hepática Autoinmune';

-- Inmunología clínica (56)
EXEC r4l.sp_insert_subespecialidad 56, 'Alergia e Inmunología Pediátrica';
EXEC r4l.sp_insert_subespecialidad 56, 'Inmunodeficiencias Primarias';
EXEC r4l.sp_insert_subespecialidad 56, 'Autoinmunidad Clínica';

-- Medicina crítica (57)
EXEC r4l.sp_insert_subespecialidad 57, 'Terapia Intensiva Respiratoria';
EXEC r4l.sp_insert_subespecialidad 57, 'Shock y Sepsis';
EXEC r4l.sp_insert_subespecialidad 57, 'Cuidados Intensivos Neurológicos';

-- Medicina del sueño (58)
EXEC r4l.sp_insert_subespecialidad 58, 'Trastornos Respiratorios del Sueño';
EXEC r4l.sp_insert_subespecialidad 58, 'Insomnio y Cronobiología';
EXEC r4l.sp_insert_subespecialidad 58, 'Narcolepsia y Trastornos Neurológicos del Sueño';

-- Medicina forense (59)
EXEC r4l.sp_insert_subespecialidad 59, 'Tanatología Forense';
EXEC r4l.sp_insert_subespecialidad 59, 'Criminalística Médica';
EXEC r4l.sp_insert_subespecialidad 59, 'Toxicología Forense';

-- Medicina paliativa (60)
EXEC r4l.sp_insert_subespecialidad 60, 'Cuidados Paliativos Pediátricos';
EXEC r4l.sp_insert_subespecialidad 60, 'Control del Dolor';
EXEC r4l.sp_insert_subespecialidad 60, 'Paliación Oncológica Avanzada';

-- Medicina tropical (61)
EXEC r4l.sp_insert_subespecialidad 61, 'Parasitología Clínica';
EXEC r4l.sp_insert_subespecialidad 61, 'Enfermedades Transmitidas por Vectores';
EXEC r4l.sp_insert_subespecialidad 61, 'Epidemiología Tropical';

-- Microbiología (62)
EXEC r4l.sp_insert_subespecialidad 62, 'Bacteriología Clínica';
EXEC r4l.sp_insert_subespecialidad 62, 'Virología Médica';
EXEC r4l.sp_insert_subespecialidad 62, 'Micología Clínica';

-- Neurofisiología clínica (63)
EXEC r4l.sp_insert_subespecialidad 63, 'Electroencefalografía Avanzada';
EXEC r4l.sp_insert_subespecialidad 63, 'Electromiografía y Conducción Nerviosa';
EXEC r4l.sp_insert_subespecialidad 63, 'Monitoreo Neurofisiológico Intraoperatorio';

-- Neuropediatría (64)
EXEC r4l.sp_insert_subespecialidad 64, 'Neurometabólicas y Enfermedades Raras';
EXEC r4l.sp_insert_subespecialidad 64, 'Epileptología Pediátrica';
EXEC r4l.sp_insert_subespecialidad 64, 'Neurodesarrollo';

-- Oncohematología (65)
EXEC r4l.sp_insert_subespecialidad 65, 'Leucemias y Linfomas';
EXEC r4l.sp_insert_subespecialidad 65, 'Trasplante de Médula Ósea';
EXEC r4l.sp_insert_subespecialidad 65, 'Hemato-Oncología Pediátrica';

-- Oncología radioterápica (66)
EXEC r4l.sp_insert_subespecialidad 66, 'Radioterapia Pediátrica';
EXEC r4l.sp_insert_subespecialidad 66, 'Radioterapia de Alta Precisión';
EXEC r4l.sp_insert_subespecialidad 66, 'Braquiterapia Oncológica';

-- Otoneurología (67)
EXEC r4l.sp_insert_subespecialidad 67, 'Vértigo y Trastornos del Equilibrio';
EXEC r4l.sp_insert_subespecialidad 67, 'Hipoacusia y Audición';
EXEC r4l.sp_insert_subespecialidad 67, 'Trastornos Vestibulares Centrales';

-- Patología clínica (68)
EXEC r4l.sp_insert_subespecialidad 68, 'Hematopatología';
EXEC r4l.sp_insert_subespecialidad 68, 'Biología Molecular Diagnóstica';
EXEC r4l.sp_insert_subespecialidad 68, 'Inmunopatología';

-- Psicología médica (69)
EXEC r4l.sp_insert_subespecialidad 69, 'Psicología de la Salud';
EXEC r4l.sp_insert_subespecialidad 69, 'Psicooncología';
EXEC r4l.sp_insert_subespecialidad 69, 'Psicología Hospitalaria';

-- Rehabilitación neurológica (70)
EXEC r4l.sp_insert_subespecialidad 70, 'Rehabilitación de Lesiones Medulares';
EXEC r4l.sp_insert_subespecialidad 70, 'Rehabilitación Post-Ictus';
EXEC r4l.sp_insert_subespecialidad 70, 'Rehabilitación Neurocognitiva';

-- Reumatología pediátrica (71)
EXEC r4l.sp_insert_subespecialidad 71, 'Enfermedades Autoinmunes Pediátricas';
EXEC r4l.sp_insert_subespecialidad 71, 'Artritis Idiopática Juvenil';
EXEC r4l.sp_insert_subespecialidad 71, 'Vasculitis Pediátricas';

-- Toxicología clínica (72)
EXEC r4l.sp_insert_subespecialidad 72, 'Toxicología de Urgencias';
EXEC r4l.sp_insert_subespecialidad 72, 'Toxicología Ambiental y Laboral';
EXEC r4l.sp_insert_subespecialidad 72, 'Toxicología Farmacológica';

-- Traumatología deportiva (73)
EXEC r4l.sp_insert_subespecialidad 73, 'Lesiones de Rodilla y Hombro';
EXEC r4l.sp_insert_subespecialidad 73, 'Medicina del Deporte Quirúrgica';
EXEC r4l.sp_insert_subespecialidad 73, 'Rehabilitación Deportiva Avanzada';

-- Urología pediátrica (74)
EXEC r4l.sp_insert_subespecialidad 74, 'Malformaciones Genitourinarias';
EXEC r4l.sp_insert_subespecialidad 74, 'Endourología Pediátrica';
EXEC r4l.sp_insert_subespecialidad 74, 'Oncología Urológica Pediátrica';

-- Medicina aeroespacial (75)
EXEC r4l.sp_insert_subespecialidad 75, 'Medicina del Vuelo';
EXEC r4l.sp_insert_subespecialidad 75, 'Fisiología Aeroespacial';
EXEC r4l.sp_insert_subespecialidad 75, 'Medicina de Altura';

-- Medicina hiperbárica (76)
EXEC r4l.sp_insert_subespecialidad 76, 'Tratamiento con Oxígeno Hiperbárico';
EXEC r4l.sp_insert_subespecialidad 76, 'Lesiones por Descompresión';
EXEC r4l.sp_insert_subespecialidad 76, 'Cicatrización y Manejo de Heridas Complejas';

-- Medicina del dolor (77)
EXEC r4l.sp_insert_subespecialidad 77, 'Manejo Intervencionista del Dolor';
EXEC r4l.sp_insert_subespecialidad 77, 'Dolor Crónico Complejo';
EXEC r4l.sp_insert_subespecialidad 77, 'Cuidados Paliativos y Dolor Avanzado';

-- Bioética médica (78)
EXEC r4l.sp_insert_subespecialidad 78, 'Ética Clínica';
EXEC r4l.sp_insert_subespecialidad 78, 'Comités Hospitalarios de Bioética';
EXEC r4l.sp_insert_subespecialidad 78, 'Ética en Investigación Médica';

-- Telemedicina (79)
EXEC r4l.sp_insert_subespecialidad 79, 'Teleconsulta Clínica';
EXEC r4l.sp_insert_subespecialidad 79, 'Teleradiología';
EXEC r4l.sp_insert_subespecialidad 79, 'Telemonitoreo de Pacientes Crónicos';

-- Salud ocupacional (80)
EXEC r4l.sp_insert_subespecialidad 80, 'Higiene Industrial';
EXEC r4l.sp_insert_subespecialidad 80, 'Ergonomía y Biomecánica Laboral';
EXEC r4l.sp_insert_subespecialidad 80, 'Toxicología Laboral';

-- Medicina familiar y comunitaria (81)
EXEC r4l.sp_insert_subespecialidad 81, 'Atención Primaria Avanzada';
EXEC r4l.sp_insert_subespecialidad 81, 'Salud Comunitaria';
EXEC r4l.sp_insert_subespecialidad 81, 'Medicina Preventiva Familiar';

-- Cirugía de trasplantes (82)
EXEC r4l.sp_insert_subespecialidad 82, 'Trasplante Renal';
EXEC r4l.sp_insert_subespecialidad 82, 'Trasplante Hepático';
EXEC r4l.sp_insert_subespecialidad 82, 'Trasplante Cardiaco';

-- Cirugía ortopédica (83)
EXEC r4l.sp_insert_subespecialidad 83, 'Cirugía de Reemplazo Articular';
EXEC r4l.sp_insert_subespecialidad 83, 'Ortopedia Oncológica';
EXEC r4l.sp_insert_subespecialidad 83, 'Trauma Ortopédico Complejo';

-- Cirugía laparoscópica (84)
EXEC r4l.sp_insert_subespecialidad 84, 'Laparoscopía Bariátrica';
EXEC r4l.sp_insert_subespecialidad 84, 'Laparoscopía Oncológica';
EXEC r4l.sp_insert_subespecialidad 84, 'Cirugía Mínimamente Invasiva Avanzada';
GO