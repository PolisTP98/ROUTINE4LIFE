-- INSERTAR REGISTROS EN TABLA CATÁLOGO r4l.sexos
exec r4l.usp_insertar_sexos @nombre = 'Hombre';
exec r4l.usp_insertar_sexos @nombre = 'Mujer';
exec r4l.usp_insertar_sexos @nombre = 'Intersexual';
exec r4l.usp_insertar_sexos @nombre = 'No binario';
exec r4l.usp_insertar_sexos @nombre = 'Prefiero no decirlo';



-- INSERTAR REGISTROS EN TABLA CATÁLOGO r4l.continentes
exec r4l.usp_insertar_continentes @nombre = 'África';
exec r4l.usp_insertar_continentes @nombre = 'América';
exec r4l.usp_insertar_continentes @nombre = 'Antártida';
exec r4l.usp_insertar_continentes @nombre = 'Asia';
exec r4l.usp_insertar_continentes @nombre = 'Europa';
exec r4l.usp_insertar_continentes @nombre = 'Oceanía';



-- INSERTAR REGISTROS EN TABLA CATÁLOGO r4l.paises

-- ÁFRICA
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Angola', @codigo_iso = 'AGO', @codigo_telefonico = '+244';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Argelia', @codigo_iso = 'DZA', @codigo_telefonico = '+213';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Benín', @codigo_iso = 'BEN', @codigo_telefonico = '+229';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Botsuana', @codigo_iso = 'BWA', @codigo_telefonico = '+267';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Burkina Faso', @codigo_iso = 'BFA', @codigo_telefonico = '+226';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Burundi', @codigo_iso = 'BDI', @codigo_telefonico = '+257';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Cabo Verde', @codigo_iso = 'CPV', @codigo_telefonico = '+238';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Camerún', @codigo_iso = 'CMR', @codigo_telefonico = '+237';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Chad', @codigo_iso = 'TCD', @codigo_telefonico = '+235';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Comoras', @codigo_iso = 'COM', @codigo_telefonico = '+269';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Costa de Marfil', @codigo_iso = 'CIV', @codigo_telefonico = '+225';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Egipto', @codigo_iso = 'EGY', @codigo_telefonico = '+20';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Eritrea', @codigo_iso = 'ERI', @codigo_telefonico = '+291';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Esuatini', @codigo_iso = 'SWZ', @codigo_telefonico = '+268';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Etiopía', @codigo_iso = 'ETH', @codigo_telefonico = '+251';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Gabón', @codigo_iso = 'GAB', @codigo_telefonico = '+241';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Gambia', @codigo_iso = 'GMB', @codigo_telefonico = '+220';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Ghana', @codigo_iso = 'GHA', @codigo_telefonico = '+233';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Guinea', @codigo_iso = 'GIN', @codigo_telefonico = '+224';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Guinea-Bisáu', @codigo_iso = 'GNB', @codigo_telefonico = '+245';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Guinea Ecuatorial', @codigo_iso = 'GNQ', @codigo_telefonico = '+240';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Kenia', @codigo_iso = 'KEN', @codigo_telefonico = '+254';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Lesoto', @codigo_iso = 'LSO', @codigo_telefonico = '+266';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Liberia', @codigo_iso = 'LBR', @codigo_telefonico = '+231';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Libia', @codigo_iso = 'LBY', @codigo_telefonico = '+218';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Madagascar', @codigo_iso = 'MDG', @codigo_telefonico = '+261';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Malaui', @codigo_iso = 'MWI', @codigo_telefonico = '+265';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Malí', @codigo_iso = 'MLI', @codigo_telefonico = '+223';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Marruecos', @codigo_iso = 'MAR', @codigo_telefonico = '+212';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Mauricio', @codigo_iso = 'MUS', @codigo_telefonico = '+230';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Mauritania', @codigo_iso = 'MRT', @codigo_telefonico = '+222';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Mozambique', @codigo_iso = 'MOZ', @codigo_telefonico = '+258';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Namibia', @codigo_iso = 'NAM', @codigo_telefonico = '+264';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Níger', @codigo_iso = 'NER', @codigo_telefonico = '+227';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Nigeria', @codigo_iso = 'NGA', @codigo_telefonico = '+234';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'República Centroafricana', @codigo_iso = 'CAF', @codigo_telefonico = '+236';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'República del Congo', @codigo_iso = 'COG', @codigo_telefonico = '+242';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'República Democrática del Congo', @codigo_iso = 'COD', @codigo_telefonico = '+243';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Ruanda', @codigo_iso = 'RWA', @codigo_telefonico = '+250';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Santo Tomé y Príncipe', @codigo_iso = 'STP', @codigo_telefonico = '+239';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Senegal', @codigo_iso = 'SEN', @codigo_telefonico = '+221';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Seychelles', @codigo_iso = 'SYC', @codigo_telefonico = '+248';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Sierra Leona', @codigo_iso = 'SLE', @codigo_telefonico = '+232';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Somalia', @codigo_iso = 'SOM', @codigo_telefonico = '+252';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Sudáfrica', @codigo_iso = 'ZAF', @codigo_telefonico = '+27';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Sudán', @codigo_iso = 'SDN', @codigo_telefonico = '+249';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Sudán del Sur', @codigo_iso = 'SSD', @codigo_telefonico = '+211';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Tanzania', @codigo_iso = 'TZA', @codigo_telefonico = '+255';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Togo', @codigo_iso = 'TGO', @codigo_telefonico = '+228';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Túnez', @codigo_iso = 'TUN', @codigo_telefonico = '+216';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Uganda', @codigo_iso = 'UGA', @codigo_telefonico = '+256';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Yibuti', @codigo_iso = 'DJI', @codigo_telefonico = '+253';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Zambia', @codigo_iso = 'ZMB', @codigo_telefonico = '+260';
exec r4l.usp_insertar_paises @id_continente = 1, @nombre = 'Zimbabue', @codigo_iso = 'ZWE', @codigo_telefonico = '+263';

-- AMÉRICA
exec r4l.usp_insertar_paises @id_continente = 2, @nombre = 'Antigua y Barbuda', @codigo_iso = 'ATG', @codigo_telefonico = '+1-268';
exec r4l.usp_insertar_paises @id_continente = 2, @nombre = 'Argentina', @codigo_iso = 'ARG', @codigo_telefonico = '+54';
exec r4l.usp_insertar_paises @id_continente = 2, @nombre = 'Bahamas', @codigo_iso = 'BHS', @codigo_telefonico = '+1-242';
exec r4l.usp_insertar_paises @id_continente = 2, @nombre = 'Barbados', @codigo_iso = 'BRB', @codigo_telefonico = '+1-246';
exec r4l.usp_insertar_paises @id_continente = 2, @nombre = 'Belice', @codigo_iso = 'BLZ', @codigo_telefonico = '+501';
exec r4l.usp_insertar_paises @id_continente = 2, @nombre = 'Bolivia', @codigo_iso = 'BOL', @codigo_telefonico = '+591';
exec r4l.usp_insertar_paises @id_continente = 2, @nombre = 'Brasil', @codigo_iso = 'BRA', @codigo_telefonico = '+55';
exec r4l.usp_insertar_paises @id_continente = 2, @nombre = 'Canadá', @codigo_iso = 'CAN', @codigo_telefonico = '+1';
exec r4l.usp_insertar_paises @id_continente = 2, @nombre = 'Chile', @codigo_iso = 'CHL', @codigo_telefonico = '+56';
exec r4l.usp_insertar_paises @id_continente = 2, @nombre = 'Colombia', @codigo_iso = 'COL', @codigo_telefonico = '+57';
exec r4l.usp_insertar_paises @id_continente = 2, @nombre = 'Costa Rica', @codigo_iso = 'CRI', @codigo_telefonico = '+506';
exec r4l.usp_insertar_paises @id_continente = 2, @nombre = 'Cuba', @codigo_iso = 'CUB', @codigo_telefonico = '+53';
exec r4l.usp_insertar_paises @id_continente = 2, @nombre = 'Dominica', @codigo_iso = 'DMA', @codigo_telefonico = '+1-767';
exec r4l.usp_insertar_paises @id_continente = 2, @nombre = 'Ecuador', @codigo_iso = 'ECU', @codigo_telefonico = '+593';
exec r4l.usp_insertar_paises @id_continente = 2, @nombre = 'El Salvador', @codigo_iso = 'SLV', @codigo_telefonico = '+503';
exec r4l.usp_insertar_paises @id_continente = 2, @nombre = 'Estados Unidos', @codigo_iso = 'USA', @codigo_telefonico = '+1';
exec r4l.usp_insertar_paises @id_continente = 2, @nombre = 'Granada', @codigo_iso = 'GRD', @codigo_telefonico = '+1-473';
exec r4l.usp_insertar_paises @id_continente = 2, @nombre = 'Guatemala', @codigo_iso = 'GTM', @codigo_telefonico = '+502';
exec r4l.usp_insertar_paises @id_continente = 2, @nombre = 'Guyana', @codigo_iso = 'GUY', @codigo_telefonico = '+592';
exec r4l.usp_insertar_paises @id_continente = 2, @nombre = 'Haití', @codigo_iso = 'HTI', @codigo_telefonico = '+509';
exec r4l.usp_insertar_paises @id_continente = 2, @nombre = 'Honduras', @codigo_iso = 'HND', @codigo_telefonico = '+504';
exec r4l.usp_insertar_paises @id_continente = 2, @nombre = 'Jamaica', @codigo_iso = 'JAM', @codigo_telefonico = '+1-876';
exec r4l.usp_insertar_paises @id_continente = 2, @nombre = 'México', @codigo_iso = 'MEX', @codigo_telefonico = '+52';
exec r4l.usp_insertar_paises @id_continente = 2, @nombre = 'Nicaragua', @codigo_iso = 'NIC', @codigo_telefonico = '+505';
exec r4l.usp_insertar_paises @id_continente = 2, @nombre = 'Panamá', @codigo_iso = 'PAN', @codigo_telefonico = '+507';
exec r4l.usp_insertar_paises @id_continente = 2, @nombre = 'Paraguay', @codigo_iso = 'PRY', @codigo_telefonico = '+595';
exec r4l.usp_insertar_paises @id_continente = 2, @nombre = 'Perú', @codigo_iso = 'PER', @codigo_telefonico = '+51';
exec r4l.usp_insertar_paises @id_continente = 2, @nombre = 'República Dominicana', @codigo_iso = 'DOM', @codigo_telefonico = '+1-809';
exec r4l.usp_insertar_paises @id_continente = 2, @nombre = 'San Cristóbal y Nieves', @codigo_iso = 'KNA', @codigo_telefonico = '+1-869';
exec r4l.usp_insertar_paises @id_continente = 2, @nombre = 'San Vicente y las Granadinas', @codigo_iso = 'VCT', @codigo_telefonico = '+1-784';
exec r4l.usp_insertar_paises @id_continente = 2, @nombre = 'Santa Lucía', @codigo_iso = 'LCA', @codigo_telefonico = '+1-758';
exec r4l.usp_insertar_paises @id_continente = 2, @nombre = 'Surinam', @codigo_iso = 'SUR', @codigo_telefonico = '+597';
exec r4l.usp_insertar_paises @id_continente = 2, @nombre = 'Trinidad y Tobago', @codigo_iso = 'TTO', @codigo_telefonico = '+1-868';
exec r4l.usp_insertar_paises @id_continente = 2, @nombre = 'Uruguay', @codigo_iso = 'URY', @codigo_telefonico = '+598';
exec r4l.usp_insertar_paises @id_continente = 2, @nombre = 'Venezuela', @codigo_iso = 'VEN', @codigo_telefonico = '+58';

-- ASIA
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Afganistán', @codigo_iso = 'AFG', @codigo_telefonico = '+93';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Arabia Saudita', @codigo_iso = 'SAU', @codigo_telefonico = '+966';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Armenia', @codigo_iso = 'ARM', @codigo_telefonico = '+374';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Azerbaiyán', @codigo_iso = 'AZE', @codigo_telefonico = '+994';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Bangladés', @codigo_iso = 'BGD', @codigo_telefonico = '+880';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Baréin', @codigo_iso = 'BHR', @codigo_telefonico = '+973';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Birmania', @codigo_iso = 'MMR', @codigo_telefonico = '+95';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Brunéi', @codigo_iso = 'BRN', @codigo_telefonico = '+673';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Bután', @codigo_iso = 'BTN', @codigo_telefonico = '+975';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Camboya', @codigo_iso = 'KHM', @codigo_telefonico = '+855';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Catar', @codigo_iso = 'QAT', @codigo_telefonico = '+974';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'China', @codigo_iso = 'CHN', @codigo_telefonico = '+86';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Chipre', @codigo_iso = 'CYP', @codigo_telefonico = '+357';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Corea del Norte', @codigo_iso = 'PRK', @codigo_telefonico = '+850';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Corea del Sur', @codigo_iso = 'KOR', @codigo_telefonico = '+82';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Emiratos Árabes Unidos', @codigo_iso = 'ARE', @codigo_telefonico = '+971';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Filipinas', @codigo_iso = 'PHL', @codigo_telefonico = '+63';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Georgia', @codigo_iso = 'GEO', @codigo_telefonico = '+995';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'India', @codigo_iso = 'IND', @codigo_telefonico = '+91';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Indonesia', @codigo_iso = 'IDN', @codigo_telefonico = '+62';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Irak', @codigo_iso = 'IRQ', @codigo_telefonico = '+964';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Irán', @codigo_iso = 'IRN', @codigo_telefonico = '+98';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Israel', @codigo_iso = 'ISR', @codigo_telefonico = '+972';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Japón', @codigo_iso = 'JPN', @codigo_telefonico = '+81';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Jordania', @codigo_iso = 'JOR', @codigo_telefonico = '+962';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Kazajistán', @codigo_iso = 'KAZ', @codigo_telefonico = '+7';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Kirguistán', @codigo_iso = 'KGZ', @codigo_telefonico = '+996';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Kuwait', @codigo_iso = 'KWT', @codigo_telefonico = '+965';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Laos', @codigo_iso = 'LAO', @codigo_telefonico = '+856';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Líbano', @codigo_iso = 'LBN', @codigo_telefonico = '+961';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Malasia', @codigo_iso = 'MYS', @codigo_telefonico = '+60';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Maldivas', @codigo_iso = 'MDV', @codigo_telefonico = '+960';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Mongolia', @codigo_iso = 'MNG', @codigo_telefonico = '+976';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Nepal', @codigo_iso = 'NPL', @codigo_telefonico = '+977';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Omán', @codigo_iso = 'OMN', @codigo_telefonico = '+968';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Pakistán', @codigo_iso = 'PAK', @codigo_telefonico = '+92';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Rusia', @codigo_iso = 'RUS', @codigo_telefonico = '+7';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Singapur', @codigo_iso = 'SGP', @codigo_telefonico = '+65';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Siria', @codigo_iso = 'SYR', @codigo_telefonico = '+963';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Sri Lanka', @codigo_iso = 'LKA', @codigo_telefonico = '+94';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Tailandia', @codigo_iso = 'THA', @codigo_telefonico = '+66';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Tayikistán', @codigo_iso = 'TJK', @codigo_telefonico = '+992';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Timor Oriental', @codigo_iso = 'TLS', @codigo_telefonico = '+670';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Turkmenistán', @codigo_iso = 'TKM', @codigo_telefonico = '+993';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Turquía', @codigo_iso = 'TUR', @codigo_telefonico = '+90';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Uzbekistán', @codigo_iso = 'UZB', @codigo_telefonico = '+998';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Vietnam', @codigo_iso = 'VNM', @codigo_telefonico = '+84';
exec r4l.usp_insertar_paises @id_continente = 4, @nombre = 'Yemen', @codigo_iso = 'YEM', @codigo_telefonico = '+967';

-- EUROPA
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Albania', @codigo_iso = 'ALB', @codigo_telefonico = '+355';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Alemania', @codigo_iso = 'DEU', @codigo_telefonico = '+49';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Andorra', @codigo_iso = 'AND', @codigo_telefonico = '+376';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Austria', @codigo_iso = 'AUT', @codigo_telefonico = '+43';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Bélgica', @codigo_iso = 'BEL', @codigo_telefonico = '+32';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Bielorrusia', @codigo_iso = 'BLR', @codigo_telefonico = '+375';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Bosnia y Herzegovina', @codigo_iso = 'BIH', @codigo_telefonico = '+387';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Bulgaria', @codigo_iso = 'BGR', @codigo_telefonico = '+359';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Croacia', @codigo_iso = 'HRV', @codigo_telefonico = '+385';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Dinamarca', @codigo_iso = 'DNK', @codigo_telefonico = '+45';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Eslovaquia', @codigo_iso = 'SVK', @codigo_telefonico = '+421';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Eslovenia', @codigo_iso = 'SVN', @codigo_telefonico = '+386';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'España', @codigo_iso = 'ESP', @codigo_telefonico = '+34';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Estonia', @codigo_iso = 'EST', @codigo_telefonico = '+372';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Finlandia', @codigo_iso = 'FIN', @codigo_telefonico = '+358';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Francia', @codigo_iso = 'FRA', @codigo_telefonico = '+33';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Grecia', @codigo_iso = 'GRC', @codigo_telefonico = '+30';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Hungría', @codigo_iso = 'HUN', @codigo_telefonico = '+36';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Irlanda', @codigo_iso = 'IRL', @codigo_telefonico = '+353';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Islandia', @codigo_iso = 'ISL', @codigo_telefonico = '+354';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Italia', @codigo_iso = 'ITA', @codigo_telefonico = '+39';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Kosovo', @codigo_iso = 'XKX', @codigo_telefonico = '+383';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Letonia', @codigo_iso = 'LVA', @codigo_telefonico = '+371';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Liechtenstein', @codigo_iso = 'LIE', @codigo_telefonico = '+423';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Lituania', @codigo_iso = 'LTU', @codigo_telefonico = '+370';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Luxemburgo', @codigo_iso = 'LUX', @codigo_telefonico = '+352';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Macedonia del Norte', @codigo_iso = 'MKD', @codigo_telefonico = '+389';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Malta', @codigo_iso = 'MLT', @codigo_telefonico = '+356';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Moldavia', @codigo_iso = 'MDA', @codigo_telefonico = '+373';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Mónaco', @codigo_iso = 'MCO', @codigo_telefonico = '+377';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Montenegro', @codigo_iso = 'MNE', @codigo_telefonico = '+382';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Noruega', @codigo_iso = 'NOR', @codigo_telefonico = '+47';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Países Bajos', @codigo_iso = 'NLD', @codigo_telefonico = '+31';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Polonia', @codigo_iso = 'POL', @codigo_telefonico = '+48';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Portugal', @codigo_iso = 'PRT', @codigo_telefonico = '+351';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Reino Unido', @codigo_iso = 'GBR', @codigo_telefonico = '+44';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'República Checa', @codigo_iso = 'CZE', @codigo_telefonico = '+420';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Rumania', @codigo_iso = 'ROU', @codigo_telefonico = '+40';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'San Marino', @codigo_iso = 'SMR', @codigo_telefonico = '+378';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Serbia', @codigo_iso = 'SRB', @codigo_telefonico = '+381';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Suecia', @codigo_iso = 'SWE', @codigo_telefonico = '+46';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Suiza', @codigo_iso = 'CHE', @codigo_telefonico = '+41';
exec r4l.usp_insertar_paises @id_continente = 5, @nombre = 'Ucrania', @codigo_iso = 'UKR', @codigo_telefonico = '+380';

-- OCEANÍA
exec r4l.usp_insertar_paises @id_continente = 6, @nombre = 'Australia', @codigo_iso = 'AUS', @codigo_telefonico = '+61';
exec r4l.usp_insertar_paises @id_continente = 6, @nombre = 'Fiyi', @codigo_iso = 'FJI', @codigo_telefonico = '+679';
exec r4l.usp_insertar_paises @id_continente = 6, @nombre = 'Islas Marshall', @codigo_iso = 'MHL', @codigo_telefonico = '+692';
exec r4l.usp_insertar_paises @id_continente = 6, @nombre = 'Islas Salomón', @codigo_iso = 'SLB', @codigo_telefonico = '+677';
exec r4l.usp_insertar_paises @id_continente = 6, @nombre = 'Kiribati', @codigo_iso = 'KIR', @codigo_telefonico = '+686';
exec r4l.usp_insertar_paises @id_continente = 6, @nombre = 'Micronesia', @codigo_iso = 'FSM', @codigo_telefonico = '+691';
exec r4l.usp_insertar_paises @id_continente = 6, @nombre = 'Nauru', @codigo_iso = 'NRU', @codigo_telefonico = '+674';
exec r4l.usp_insertar_paises @id_continente = 6, @nombre = 'Nueva Zelanda', @codigo_iso = 'NZL', @codigo_telefonico = '+64';
exec r4l.usp_insertar_paises @id_continente = 6, @nombre = 'Palaos', @codigo_iso = 'PLW', @codigo_telefonico = '+680';
exec r4l.usp_insertar_paises @id_continente = 6, @nombre = 'Papúa Nueva Guinea', @codigo_iso = 'PNG', @codigo_telefonico = '+675';
exec r4l.usp_insertar_paises @id_continente = 6, @nombre = 'Samoa', @codigo_iso = 'WSM', @codigo_telefonico = '+685';
exec r4l.usp_insertar_paises @id_continente = 6, @nombre = 'Tonga', @codigo_iso = 'TON', @codigo_telefonico = '+676';
exec r4l.usp_insertar_paises @id_continente = 6, @nombre = 'Tuvalu', @codigo_iso = 'TUV', @codigo_telefonico = '+688';
exec r4l.usp_insertar_paises @id_continente = 6, @nombre = 'Vanuatu', @codigo_iso = 'VUT', @codigo_telefonico = '+678';



-- INSERTAR REGISTROS EN TABLA CATÁLOGO r4l.comidas
exec r4l.usp_insertar_comidas @nombre = 'Desayuno';
exec r4l.usp_insertar_comidas @nombre = 'Comida';
exec r4l.usp_insertar_comidas @nombre = 'Cena';
exec r4l.usp_insertar_comidas @nombre = 'Merienda matutina';
exec r4l.usp_insertar_comidas @nombre = 'Merienda vespertina';
exec r4l.usp_insertar_comidas @nombre = 'Colación nocturna';
exec r4l.usp_insertar_comidas @nombre = 'Ayunas';
exec r4l.usp_insertar_comidas @nombre = 'Post-entrenamiento';
exec r4l.usp_insertar_comidas @nombre = 'Pre-entrenamiento';
exec r4l.usp_insertar_comidas @nombre = 'Antes de dormir';



-- INSERTAR REGISTROS EN TABLA CATÁLOGO r4l.roles_usuarios
exec r4l.usp_insertar_roles_usuarios @nombre = 'Médico administrador';
exec r4l.usp_insertar_roles_usuarios @nombre = 'Médico';
exec r4l.usp_insertar_roles_usuarios @nombre = 'Paciente';
exec r4l.usp_insertar_roles_usuarios @nombre = 'Enfermero';
exec r4l.usp_insertar_roles_usuarios @nombre = 'Recepcionista';



-- INSERTAR REGISTROS EN TABLA CATÁLOGO r4l.estatus_usuarios
exec r4l.usp_insertar_estatus_usuarios @nombre = 'Activo', @descripcion = 'Usuario con acceso completo al sistema';
exec r4l.usp_insertar_estatus_usuarios @nombre = 'Inactivo', @descripcion = 'Usuario dado de baja del sistema';
exec r4l.usp_insertar_estatus_usuarios @nombre = 'Suspendido', @descripcion = 'Usuario temporalmente sin acceso por incumplimiento';
exec r4l.usp_insertar_estatus_usuarios @nombre = 'Bloqueado', @descripcion = 'Usuario bloqueado por intentos fallidos';