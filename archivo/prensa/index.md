# Archivo de entrevistas y apariciones en prensa

Catálogo histórico de entrevistas, coberturas y apariciones en prensa documentadas por Ariel López en las páginas anuales de `blog.ariellopez.cl`.

Este archivo está deliberadamente separado del README del perfil. La unidad de registro es la **aparición efectiva en un medio**: cuando un mismo hecho fue cubierto por varios medios, cada publicación tiene su propia fila.

## Estado de cobertura

| Año | Registros indexados | Registros declarados en la fuente | Estado |
|---:|---:|---:|---|
| 2026 | 92 | 89 | Completo en blog + 3 hallazgos externos |
| 2025 | 51 | 50 | Completo en blog + 1 hallazgo externo |
| 2024 | 37 | 36 | Completo en blog + 1 hallazgo externo |
| 2023 | 30 | 30 | Completo |
| 2022 | 30 | 24 | Completo en blog + 6 hallazgos externos |
| 2021 | 19 | 14 | Completo en blog + 5 hallazgos externos |
| 2020 | 46 | 46 | Completo |

**Total registrado: 305 apariciones (289 documentadas y curadas desde los índices del blog + 16 hallazgos externos).**

Los años 2021 y 2022 inicialmente no podían verificarse de forma exhaustiva porque Medium no exponía el cuerpo de esas páginas. Posteriormente fueron reconciliados contra copias Markdown suministradas por el autor. Las apariciones verificadas que no figuran en el índice anual se conservan por separado como `hallazgo_externo`, sin alterar el conteo original del blog.

## Criterio

- Fecha: corresponde a la fecha de entrevista/aparición indicada en el archivo anual; cuando el pie o el enlace contiene una fecha distinta, se conserva en `nota`.
- Medio: se normalizan variantes menores de nombre (por ejemplo, Radio Biobío → Radio Bío Bío).
- Título: se conserva el título del archivo anual, incluidas algunas erratas de la fuente.
- Enlace: sólo se incorpora la noticia original o video cuando fue posible resolverlo de manera verificable. Si no, se deja como “Sin URL original documentada”.
- Categoría: `entrevista`, `cobertura` o `columna_opinion`. Esto permitirá separar después las columnas del archivo de entrevistas.
- El CSV [`prensa.csv`](prensa.csv) es la versión estructurada y reutilizable.

## Auditoría audiovisual de YouTube

La playlist de prensa del canal se incorporó como fuente complementaria para recuperar enlaces y detectar apariciones que no estaban claramente resueltas en los índices anuales.

- Videos enumerados en la playlist: **105**.
- Mapeos curados ya versionados contra el catálogo: **37**.
- Videos que aún requieren revisión individual: **33**.
- La prioridad de enlace se mantiene: medio original → video propio/verificado → copia institucional.
- Los videos que parecen corresponder a una fila existente no reemplazan el enlace original del medio; se conservan como evidencia audiovisual complementaria.
- La cola de revisión está en [`youtube_candidates_review.md`](youtube_candidates_review.md) y [`youtube_candidates_review.csv`](youtube_candidates_review.csv).
- El inventario completo del cruce está en [`youtube_playlist.csv`](youtube_playlist.csv) y el reporte automático en [`youtube_match_report.md`](youtube_match_report.md).

La extracción de metadata individual de YouTube desde GitHub Actions fue bloqueada por las protecciones anti-bot de YouTube, por lo que no se asignan fechas inferidas a los candidatos pendientes. Sólo se incorporarán al catálogo principal cuando fecha y medio puedan verificarse por otra fuente.



## 2026

Fuente anual: [En la prensa 2026](https://blog.ariellopez.cl/en-la-prensa-2026-ab565e1372b4). El contenido fue reconciliado contra una copia de texto suministrada por el autor: 89/89 apariciones efectivas.

| Fecha | Medio | Título | Enlace |
|---|---|---|---|
| 2026-09-23 | Chilevisión | Lanzan plan piloto de agentes anti evasión | [video](https://www.youtube.com/watch?v=LvtEtiMhpFw) |
| 2026-09-21 | Canal 13 | Menos días, pero más muertes en accidentes de tránsito durante las Fiestas Patrias | [video](https://www.t13.cl/videos/nacional/balance-fiestas-patrias-menos-dias-pero-mas-muertes-accidentes-21-9-2026) |
| 2026-09-21 | Chilevisión | Agentes antievasión deberán validar su utilidad | [video](https://www.youtube.com/watch?v=VabJoemqkmQ) |
| 2026-09-20 | Canal 13 | Gobierno negocia con concesionarias para bajar el TAG | [video](https://www.youtube.com/watch?v=qFsSvMTg-n0) |
| 2026-09-04 | T13 | “Aquí eso no se hizo”: Experto expone deficiencia del Metro que propició muerte de pasajero en estación Pajaritos | [original](https://www.t13.cl/amp/noticia/nacional/aqui-eso-no-se-hizo-experto-expone-deficiencia-del-metro-propicio-muerte-4-9-2026) |
| 2026-09-08 | La Tercera | De Grange promete seguir impulsando la electromovilidad en cuenta pública del MTT y expertos cuestionan sus anuncios | [original](https://www.latercera.com/nacional/noticia/de-grange-promete-seguir-impulsando-la-electromovilidad-en-cuenta-publica-del-mtt-y-expertos-cuestionan-sus-anuncios/) |
| 2026-09-03 | Canal 13 | ¿Se pudo evitar la tragedia del Metro? | [video](https://www.youtube.com/watch?v=98e0AedpRQo) |
| 2026-09-02 | Chilevisión | Conflicto sobre ruedas merece más de una vuelta | [video](https://www.youtube.com/watch?v=9uX5UyUwJnU) |
| 2026-08-23 | Chilevisión | Algunas estaciones llevan meses sin ascensor | [video](https://www.youtube.com/watch?v=BCJpRefGsIs) |
| 2026-08-20 | Canal 13 | Quedó atrapada en puerta y micro la arrolló | [video](https://www.t13.cl/videos/nacional/adulta-mayor-quedo-atrapada-puerta-micro-arrollo-quilicura-20-8-2026) |
| 2026-08-14 | La Tercera | A 40 años de la restricción vehicular en Chile: 2026 registra 116 mil citaciones por circular en días indebidos | [original](https://www.latercera.com/nacional/noticia/a-40-anos-de-la-restriccion-vehicular-en-chile-2026-registra-116-mil-citaciones-por-circular-en-dias-indebidos/) |
| 2026-08-04 | El Mercurio | Fallas en trenes más antiguos del Metro hacen crecer dudas sobre su vida útil y mantención | Sin URL original documentada |
| 2026-08-02 | Revista Pedalea | ¿Qué construir primero? EVA: la herramienta que pone orden al rompecabezas de 820 km. | [original](https://revistapedalea.com/que-construir-primero-eva-la-herramienta-que-pone-orden-al-rompecabezas-de-820-km/) |
| 2026-08-01 | The Clinic | El incendio que expuso la otra deuda del Metro: la encapsulada sustancia prohibida que nunca salió de sus trenes más antiguos | [original](https://www.theclinic.cl/2026/08/01/el-incendio-que-expuso-la-otra-deuda-del-metro-la-sustancia-prohibida-que-nunca-salio-de-sus-trenes-mas-antiguos/) |
| 2026-07-31 | El Dínamo | ¿Falla más que antes el Metro de Santiago? Las cifras y lo que hay detrás de los incidentes que afectan a miles de usuarios | [original](https://www.eldinamo.cl/pais/2026/08/01/falla-mas-que-antes-el-metro-de-santiago-las-cifras-y-lo-que-hay-detras-de-los-incidentes-que-afectan-a-miles-de-usuarios/) |
| 2026-07-29 | CNN Chile | Incendio en Metro abre debate sobre renovación de trenes | [video](https://www.youtube.com/watch?v=62EmAiDJwak) |
| 2026-07-29 | La Tercera | Línea de transmisión: el proyecto eléctrico que tendrá a la Avenida Andrés Bello con cortes de tránsito por más de un año | [original](https://www.latercera.com/nacional/noticia/linea-de-transmision-el-proyecto-electrico-que-tendra-a-la-avenida-andres-bello-con-cortes-de-transito-por-mas-de-un-ano/) |
| 2026-07-28 | Canal 13 | ¿Qué provocó el incendio en el Metro? | [video](https://www.youtube.com/watch?v=p5LH7RFvLzM) |
| 2026-07-28 | Latamobility | Chile: Restricciones presupuestarias impulsan la reconversión de buses como alternativa al modelo tradicional de renovación de flotas | [original](https://latamobility.com/chilea-reconversion-buses-alternativa-flotas/) |
| 2026-06-24 | Radio Bío Bío | ¿Prohibir scooter en Chile como se hizo en España? | Sin URL original documentada |
| 2026-06-23 | Experiencia Tech | El desafío de una movilidad inteligente | [video](https://www.youtube.com/watch?v=qiSEBsXfSZM) |
| 2026-06-22 | Canal 13 | Manejó a 264 km/h y quedó en libertad | [video](https://www.t13.cl/videos/nacional/tiene-antecedentes-pestado-ebriedad-desde-2009-hombre-manejo-264-km-quedo-libre-22-6-2026) |
| 2026-06-12 | Radio 13C | Contraloría rechazó las modificaciones a la Ley Uber propuestas por el ministro de transportes | [video](https://www.youtube.com/watch?v=Ne8okX43Tps) |
| 2026-06-10 | TVN | ¿Hay menos frecuencia de buses en Santiago? | [original](https://www.tvn.cl/programas/buenos-dias-a-todos/actualidad/experto-en-transporte-explica-las-razones-de-la-aparente-baja-en-frecuencia-video) |
| 2026-06-08 | Contrapoder | Registro del Congreso revela que exdiputado y actual director nacional de Migraciones gastó casi $10 millones en combustible | [original](https://contrapoderchile.cl/registro-del-congreso-revela-que-exdiputado-y-actual-director-nacional-de-migraciones-gasto-casi-10-millones-en-combustible/) |
| 2026-06-05 | La Tercera | Grandes filas y aglomeraciones en horario peak: ¿por qué Metro tiene pocas boleterías habilitadas? | [original](https://www.latercera.com/nacional/noticia/grandes-filas-y-aglomeraciones-en-horario-peak-por-que-metro-tiene-pocas-boleterias-habilitadas/) |
| 2026-06-03 | Turno | ¿Ha bajado la frecuencia de las micros? | [video](https://www.youtube.com/watch?v=ZaK4vA_PBaU) |
| 2026-06-02 | Canal 13 | Tacos eternos, la pesadilla de Chicureo | [video](https://www.youtube.com/watch?v=Gq86xSXwfds) |
| 2026-06-01 | T13 | No podrán sacar pasaporte ni entrar a estadios: las nuevas sanciones para quienes evadan el transporte público | [original](https://www.t13.cl/noticia/nacional/no-podran-sacar-pasaporte-ni-entrar-estadios-las-nuevas-sanciones-para-quienes-1-6-2026) |
| 2026-06-01 | Publimetro | Endurecen sanciones contra quienes evadan el transporte público: infractores arriesgan perder acceso a pasaporte y estadios | [original](https://www.publimetro.cl/noticias/2026/06/01/endurecen-sanciones-contra-quienes-evadan-el-transporte-publico-infractores-arriesgan-perder-acceso-a-pasaporte-y-estadios/) |
| 2026-05-31 | Chilevisión | Evasiones: Contraloría aprueba duras sanciones | [video](https://www.youtube.com/watch?v=hVc75yWFvW8) |
| 2026-05-29 | El Desconcierto | Ministerio de Transportes en el dardo del gobierno para posible fusión de cartera con Obras Públicas | [original](https://eldesconcierto.cl/actualidad/ministerio-transportes-el-dardo-del-gobierno-posible-fusion-cartera-obras-publicas-n5459191) |
| 2026-05-29 | La Tercera | Tacos kilométricos, tag costoso y triple de población truncan la promesa idílica de una vida tranquila en Chicureo | [original](https://www.latercera.com/nacional/noticia/tacos-kilometricos-tag-costoso-y-alta-densidad-truncan-la-promesa-idilica-de-una-vida-tranquila-en-chicureo/) |
| 2026-05-28 | Chilevisión | Pasajeros de Buin y Talagante pasan 5 horas en el transporte público | [video](https://www.youtube.com/watch?v=P7KINSF0leM) |
| 2026-05-21 | La Tercera | La posibilidad de potenciar el MOP junto al MTT es muy virtuosa: las primeras definiciones del biministro De Grange | [original](https://www.latercera.com/nacional/noticia/la-posibilidad-de-potenciar-el-mop-junto-al-mtt-es-muy-virtuosa-las-primeras-definiciones-del-biministro-de-grange/) |
| 2026-05-18 | La Tercera | Transportes busca extender la vigencia del Certificado de Homologación de autos nuevos en 12 meses | [original](https://www.latercera.com/nacional/noticia/transportes-busca-extender-la-vigencia-del-certificado-de-homologacion-de-autos-nuevos-en-12-meses/) |
| 2026-05-17 | El Desconcierto | Experto revela recortes en micros y fallas ocultas en metro | [video](https://www.youtube.com/watch?v=KI6vFrEK8U0) |
| 2026-05-15 | Radio La Metro | La accesibilidad no se mide en porcentajes de dispositivos dañados, porque un ascensor es parte de una trayectoria, un ascensor dañado corta el trayecto completo | [video](https://www.youtube.com/watch?v=rK62xVOsdHE) |
| 2026-05-15 | The Clinic | Recorte de más de $56 mil millones en Transporte enciende alertas por posibles impactos en buses regionales y electromovilidad | [original](https://www.theclinic.cl/2026/05/15/recorte-de-mas-de-56-mil-millones-en-transporte-enciende-alertas-por-posibles-impactos-en-buses-regionales-y-electromovilidad/) |
| 2026-05-15 | TVN | Metro: récord de escaleras mecánicas y ascensores malos | [video](https://www.tvn.cl/programas/buenos-dias-a-todos/actualidad/record-de-escaleras-mecanicas-y-ascensores-malos-en-estaciones-del-metro-video) |
| 2026-05-13 | Radio ADN | Aumento de flujo y de fallas en el Metro de Santiago | [video](https://www.youtube.com/watch?v=Jb0as9jQhwg) |
| 2026-05-13 | Radio Bío Bío | Metro reconoce aumento en problemas con ascensores y escaleras mecánicas y anuncia más técnicos | [original](https://www.biobiochile.cl/noticias/nacional/region-metropolitana/2026/05/13/metro-reconoce-aumento-en-problemas-con-ascensores-y-escaleras-mecanicas-y-anuncia-mas-tecnicos.shtml) |
| 2026-05-13 | Radio Bío Bío | Aumentan las fallas de escaleras y ascensores en el Metro de Santiago | Sin URL original documentada |
| 2026-05-12 | Chilevisión | Metro, reportan récord de fallas en abril | [video](https://www.youtube.com/watch?v=2KSeM42Nmuw) |
| 2026-05-12 | Doble Espacio | No hay menos buses, pero hay más pasajeros: el alza del combustible golpea al transporte público | [original](https://doble-espacio.uchile.cl/golpea-al-transporte-publico-buses-red/) |
| 2026-05-12 | Mega | 1 de cada 3 estaciones del Metro de Santiago presenta falla | [video](https://www.youtube.com/watch?v=ePOvWnUbPoc) |
| 2026-05-12 | Meganoticias | Récord de fallas en estaciones de Metro | [video](https://www.youtube.com/watch?v=nrhPDMfspWY) |
| 2026-05-11 | CNN Chile | Reportan cifra récord de escaleras mecánicas y ascensores dañados en el Metro de Santiago: Línea 5 es la más afectada | [original](https://www.cnnchile.com/pais/reportan-cifra-record-de-escaleras-mecanicas-y-ascensores-danados-en-el-metro-de-santiago-linea-5-es-la-mas-afectada/) |
| 2026-05-11 | Diario USACH | Más de 40 equipos fuera de servicio: Denuncian aumento de desperfectos en el Metro de Santiago | [original](https://www.diariousach.cl/mas-de-40-equipos-fuera-de-servicio-denuncian-aumento-de-desperfectos-en) |
| 2026-05-11 | La Tercera | Récord de escaleras mecánicas y ascensores malos: la compleja situación que enfrenta el Metro de Santiago | [original](https://www.latercera.com/nacional/noticia/record-de-escaleras-mecanicas-y-ascensores-malos-la-compleja-situacion-que-enfrenta-metro-de-santiago/) |
| 2026-05-10 | Canal 13 | Santiaguinos se niegan a dejar el auto | [video](https://www.youtube.com/watch?v=rcHPTWyjTpI) |
| 2026-05-08 | LUN | Pedro Carcuro aclara agresión en Uber: “Me da miedo que les pueda pasar a otras personas” | [original](https://www.lun.com/Pages/NewsDetail.aspx?EsAviso=0&PaginaId=14&bodyid=0&dt=2026-05-08) |
| 2026-05-07 | Fast Check | Ariel López, experto en transporte público: “Tenemos empresas que sacan menos buses de los que deberían sacar” | Sin URL original documentada |
| 2026-05-06 | Canal 13 | Hay menos micros y el Metro está más lleno? | [video](https://www.youtube.com/watch?v=RJI_peC7eqI) |
| 2026-05-06 | La Tercera | El desafío hoy es el déficit habitaciona: las ciclovías pasan al fondo de las prioridades para el gobierno de Kast | [original](https://www.latercera.com/nacional/noticia/el-desafio-hoy-es-el-deficit-habitacional-como-las-ciclovias-pasaron-al-fondo-de-las-prioridades-para-el-gobierno-de-kast/) |
| 2026-05-04 | Radio ADN | Aumento de flujo de pasajeros en el transporte público tras el aumento del precio de los combustibles | [video](https://www.youtube.com/watch?v=2lUPQiq9jNE) |
| 2026-05-01 | Canal 13 | Gobierno ajusta sistema de transporte | [video](https://www.youtube.com/watch?v=RwBmZkIP4Lo) |
| 2026-04-30 | Teletrece | Fallas en escaleras mecánicas y ascensores del Metro | [video](https://www.t13.cl/videos/nacional/fallas-mecanicas-escaleras-ascensores-metro-30-04-2026) |
| 2026-04-29 | Chilevisión | Mayor falla de escaleras mecánicas en un año | [video](https://www.youtube.com/watch?v=3pOlMiqAvdE) |
| 2026-04-29 | El Desconcierto | Metro de Santiago y sus problemas de accesibilidad: denuncian récord de escaleras mecánicas y ascensores malos | [original](https://eldesconcierto.cl/actualidad/metro-santiago-y-sus-problemas-accesibilidad-denuncian-record-escaleras-mecanicas-ascensores-malos-n5458447?utm_medium=Social&utm_source=Twitter&utm_term=Autofeed) |
| 2026-04-28 | Radio Bío Bío | Reglamento de apps de transporte divide opinión de expertos mientras taxis acusan competencia desigual | [original](https://www.biobiochile.cl/noticias/nacional/chile/2026/04/28/ley-uber-reglamento-de-apps-de-transporte-divide-opiniones-taxis-acusan-desregulacion-y-competencia-desigual.shtml) |
| 2026-04-27 | Radio T13C | Nivelar para abajo: el nuevo reglamento de Ley Uber | [original](https://radio13c.cl/show/corresponsales/episode/corresponsales-26272345) |
| 2026-04-22 | Radio Bío Bío | ¿Menor flujo de buses en Santiago? | [video](https://www.youtube.com/watch?v=fllMdTBe5Bo) |
| 2026-04-20 | Chilevisión | Gobierno evalúa bajar tarifa del TAG | [video](https://www.youtube.com/watch?v=A_F88IWgBLU) |
| 2026-04-19 | Chilevisión | Paraderos llenos: menos micros o más pasajeros | [video](https://www.youtube.com/watch?v=ibpdDmZKBF8) |
| 2026-04-15 | Contrapoder | El estudio que desmiente al Ministerio de Transportes y confirma que hay menos buses en circulación | [original](https://contrapoderchile.cl/el-estudio-que-desmiente-al-ministerio-de-transportes-y-confirma-que-hay-menos-buses-en-circulacion/) |
| 2026-04-12 | Meganoticias | ¿Fin de los buses “oruga” por las noches? | [video](https://www.youtube.com/watch?v=z46NLS0mGhc) |
| 2026-04-10 | LaBot | De Grange y la Ley Uber: ¿un ministro comprometido? | [original](https://robotlabot.substack.com/p/de-grange-y-la-ley-uber-un-ministro) |
| 2026-04-10 | Teletrece | Filas en paraderos ¿hay menos micros en Santiago? | [original](https://www.t13.cl/videos/nacional/filas-paraderos-hay-menos-micros-santiago-10-4-2026) |
| 2026-04-09 | Radio Bío Bío | Expectativa vs realidad: video revela cómo está quedando la vía “semipeatonal” de calle Bandera | [original](https://www.biobiochile.cl/noticias/nacional/region-metropolitana/2026/04/09/expectativa-vs-realidad-video-revela-como-esta-quedando-la-via-semipeatonal-de-calle-bandera.shtml) |
| 2026-04-03 | El Desconcierto | Menos micros fines de semana, noche y sin “orugas”: el recorte del ministro Louis de Grange para recorridos de buses en RM | [original](https://eldesconcierto.cl/reportajes/menos-micros-fines-semana-noche-y-orugas-el-recorte-del-ministro-louis-grange-recorridos-buses-rm-n5457738) |
| 2026-03-24 | Radio ADN | Un bus eléctrico es un 60% más eficiente que uno a diésel | [original](https://www.adnradio.cl/2026/03/24/magister-en-urbanismo-de-la-u-de-chile-un-bus-electrico-es-un-60-mas-eficiente-que-uno-a-diesel/) |
| 2026-03-23 | Chilevisión | El transporte público es más barato que el automóvil | [video](https://www.youtube.com/watch?v=_2EMhZGeBgM) |
| 2026-03-23 | Súbela Radio | ¿Qué implican las reformas del MEPCO en nuestro bolsillo? | [video](https://www.youtube.com/watch?v=qXWV-oAsgg4) |
| 2026-03-22 | TVN | Gobierno descarta reducción de buses operativos de flota Red | [video](https://www.youtube.com/watch?v=hp2iE6qCOek) |
| 2026-03-17 | LUN | Por qué las autopistas están obligadas a brindar seguridad a los usuarios | [original](https://www.lun.com/Pages/NewsDetail.aspx?EsAviso=0&PaginaId=2&bodyid=0&dt=2026-03-18) |
| 2026-03-04 | Canal 13 | Asfaltaron la calle y taparon los desagües | [video](https://www.youtube.com/watch?v=iUWwHhZIM3Y) |
| 2026-03-04 | Radio Bío Bío | Ley Uber: De Grange solicita a Muñoz no publicar reglamento antes del cambio de mando | [original](https://www.biobiochile.cl/noticias/nacional/chile/2026/03/04/ley-uber-de-grange-solicita-a-munoz-no-publicar-reglamento-antes-del-cambio-de-mando.shtml) |
| 2026-03-03 | Radio Bío Bío | Denuncian que reasfaltado de calle Bandera tapó desagües de lluvia: Serviu responde | [original](https://www.biobiochile.cl/noticias/nacional/region-metropolitana/2026/03/03/denuncian-que-reasfaltado-de-calle-bandera-tapo-desagues-de-lluvia-serviu-responde.shtml) |
| 2026-02-23 | Sabes.cl | “No está mal ubicado, solo que las condiciones del caso de Coronel no son las normales”: Experto explica ubicación de polémico paradero de la Ruta 160 | [original](https://sabes.cl/2026/02/23/no-esta-mal-ubicado-solo-que-las-condiciones-del-caso-de-coronel-no-son-las-normales-experto-explica-ubicacion-de-polemico-paradero-de-la-ruta-160/) |
| 2026-02-20 | Radio Bío Bío | Gremios y expertos llaman a reforzar fiscalización de camiones de carga ante tragedia en Renca | [original](https://www.biobiochile.cl/noticias/nacional/region-metropolitana/2026/02/20/gremios-y-expertos-llaman-a-reforzar-fiscalizacion-de-camiones-de-carga-ante-tragedia-en-renca.shtml) |
| 2026-02-18 | Radio Bío Bío | Propuesta de futuro ministro de Transportes de vans como colectivos abre debate sobre modernización | [original](https://www.biobiochile.cl/noticias/nacional/chile/2026/02/18/propuesta-de-futuro-ministro-de-transportes-de-vans-como-colectivos-abre-debate-sobre-modernizacion.shtml) |
| 2026-02-10 | Canal 13 | Usuario se graba abriendo puertas de vagones del Metro de Santiago | [original](https://www.t13.cl/noticia/nacional/tiktoker-peligrosa-maniobra-graba-puertas-metro-10-02-2026) |
| 2026-02-04 | Teletrece | Buscan a ciclista que huyó tras atropellar a mujer | [video](https://www.youtube.com/watch?v=tO7NVNrAp14) |
| 2026-01-29 | Chilevisión | Turistas sorprendidos por respeto vial | [video](https://www.youtube.com/watch?v=Qecg6VEBtqI) |
| 2026-01-28 | Chilevisión | Usuarios en alerta por intenso calor en el Metro | [video](https://www.youtube.com/watch?v=oIzXFLzT1KE) |
| 2026-01-18 | LUN | Diseñadora paga 30.000 por estacionar afuera de su casa y le pasaron dos partes | [original](https://www.lun.com/Pages/NewsDetail.aspx?EsAviso=0&PaginaId=6&bodyid=0&dt=2026-01-18) |
| 2026-01-16 | Canal 13 | Tuneladora del Metro falló y no avanzó más | [original](https://www.t13.cl/noticia/nacional/tuneladora-del-metro-santiago-fallo-no-avanzo-mas-cuanto-se-podria-atrasar-16-1-2026) |
| 2026-01-14 | The Clinic | Expertos advierten que inauguración de línea 7 podría verse retrasada, tras término de contrato entre Metro y empresa tuneladora | [original](https://www.theclinic.cl/2026/01/14/expertos-advierten-que-inauguracion-de-linea-7-podria-verse-retrasada-tras-termino-de-contrato-entre-metro-y-empresa-tuneladora/) |
| 2026-01-07 | LUN | ¿Cierto que es un placer andr por las cajjes despejadas durante el verano en Santiago? | [original](https://www.lun.com/Pages/NewsDetail.aspx?EsAviso=0&PaginaId=2&bodyid=0&dt=2026-01-07) |
| 2026-01-05 | Radio Bío Bío | Kusanovic ve inviable aplicar “Ley Uber” antes del término del actual gobierno y cuestiona su sentido | [original](https://www.biobiochile.cl/noticias/nacional/chile/2026/01/05/kusanovic-ve-inviable-aplicar-la-ley-uber-antes-de-marzo-y-cuestiona-su-sentido.shtml) |

### Hallazgos externos no incluidos en el blog 2026

Esta aparición se encontró mediante búsqueda externa y no figura entre las 89 entradas de la copia suministrada por el autor. Se conserva por separado para ampliar el archivo sin alterar el inventario original del blog.

| Fecha | Medio | Título | Enlace |
|---|---|---|---|
| 2026-07-29 | The Clinic | “Por reacciones inflamatorias”: Médico asegura que personas expuestas a humo con asbesto tras incendio de Metro deben quedar en seguimiento | [original](https://www.theclinic.cl/2026/07/29/por-reacciones-inflamatorias-medico-asegura-que-personas-expuestas-a-humo-con-asbesto-de-metro-deben-quedar-en-seguimiento/) |

> Estado: 2026 queda cerrado respecto del índice entregado (89/89 apariciones). El hallazgo externo se etiqueta como `hallazgo_externo`.

## 2025

Fuente anual: [En la prensa 2025](https://blog.ariellopez.cl/en-la-prensa-2025-e0bdc343bba6). El contenido fue reconciliado contra una copia Markdown suministrada por el autor: 50/50 apariciones efectivas.

| Fecha | Medio | Título | Enlace |
|---|---|---|---|
| 2025-12-27 | Chilevisión | Conductor de scooter muere tras ser colisionado por automovilista en estado de ebriedad | [video](https://www.youtube.com/watch?v=sXHqtI5C3EA) |
| 2025-12-26 | Chilevisión | ¿Qué artículos se pueden subir a un tren? Guardias de EFE arrebatan regalo de navidad a una pasajera en el Biotren | Sin URL original documentada |
| 2025-12-26 | Meganoticias | ¿Qué artículos se pueden subir a un tren? Guardias de EFE arrebatan regalo de navidad a una pasajera en el Biotren | [video](https://www.youtube.com/watch?v=lw-MUEorJZg) |
| 2025-12-17 | Canal 13 | Denuncian aire caliente en los andenes del Metro | [video](https://www.youtube.com/watch?v=g7RCFzoM6bY) |
| 2025-11-06 | The Clinic | Gobierno anuncia tren que unirá Ñuble y Concepción en 90 minutos y será más lento que viajar en bus: “Lo están condenando a morir antes de nacer” | [original](https://www.theclinic.cl/2025/11/06/expertos-debaten-sobre-tiempos-de-traslado-del-tren-chillan-concepcion-lo-estan-condenando-a-morir-antes-de-nacer/) |
| 2025-11-05 | Chilevisión | Señal de tránsito que permite pasar el semáforo con luz roja ilegalmente | [video](https://www.youtube.com/watch?v=8A1s-Z9nRXw) |
| 2025-11-02 | Canal 13 | Vuelven los buses articulados: ahora son eléctricos | [video](https://www.youtube.com/watch?v=3naViTajGPM) |
| 2025-10-14 | Chilevisión | Metro de Santiago bajo la lupa: aumentan fallas internas | [video](https://www.youtube.com/watch?v=sn5ho1ex2lU) |
| 2025-10-13 | Chilevisión | Así es el nuevo cruce entre Vespucio y Ruta 68 | Sin URL original documentada |
| 2025-10-13 | LUN | Nuevo enlace tipo turbina en Vespucio con Ruta 68 | [original](https://www.lun.com/Pages/NewsDetail.aspx?EsAviso=0&PaginaId=15&SupplementId=0&dt=2025-10-13) |
| 2025-10-11 | The Clinic | Caminantes en las vías del Metro: las querellas, millonarios costos y protocolos detrás de un fenómeno masivo que refleja la crisis de salud mental en Chile | [original](https://www.theclinic.cl/2025/10/11/caminantes-en-las-vias-del-metro-las-querellas-millonarios-costos-y-protocolos-detras-de-un-fenomeno-masivo-que-refleja-la-crisis-de-salud-mental-en-chile/) |
| 2025-09-26 | LUN | Visita a la calle en situación de hoyo: ha provocado dos accidentes en un mes | [original](https://www.lun.com/Pages/NewsDetail.aspx?EsAviso=0&PaginaId=6&bodyid=0&dt=2025-09-26) |
| 2025-09-25 | Chilevisión | Señalética confunde a conductores en autopistas | Sin URL original documentada |
| 2025-09-23 | LUN | Seis preguntas innecesarias que salen en el examen escrito de manejo | [original](https://www.lun.com/Pages/NewsDetail.aspx?EsAviso=0&PaginaId=10&bodyid=0&dt=2025-09-23) |
| 2025-09-15 | The Clinic | ¿Guetos verticales se trasladan a La Florida? Experto alerta que decenas de permisos para megaedificios se han aprobado en la comuna desde 2018 | [original](https://www.theclinic.cl/2025/09/15/guetos-verticales-se-trasladan-a-la-florida-experto-alerta-que-decenas-de-permisos-para-megaedificios-se-han-aprobado-en-la-comuna-desde-2018/) |
| 2025-09-05 | LUN | Señalética en las autopistas: “Muchas veces la información aparece demasiado cerca de la salida, con mensajes largos y poco claros” | [original](https://www.lun.com/Pages/NewsDetail.aspx?EsAviso=0&PaginaId=8&bodyid=0&dt=2025-09-05) |
| 2025-09-05 | The Clinic | “Se debe descontaminar”: La preocupante advertencia de experto tras incendio en estación San Joaquín por posible presencia de asbesto en el Metro | [original](https://www.theclinic.cl/2025/09/05/se-debe-descontaminar-la-preocupante-advertencia-de-experto-tras-incendio-en-estacion-san-joaquin-por-posible-presencia-de-asbesto-en-el-metro/) |
| 2025-08-11 | LUN | Venezolanos que viven en Chile eligieron qué les gusta más del país: puras flores para el transporte público nacional | [original](https://www.lun.com/Pages/NewsDetail.aspx?EsAviso=0&PaginaId=17&bodyid=0&dt=2025-08-11) |
| 2025-08-08 | Chilevisión | Vehículos mal estacionados impiden el paso de bomberos | [video](https://www.youtube.com/watch?v=zxNVfifgpdU) |
| 2025-08-08 | El Mercurio de Valparaíso | Proponen ciclovía por Paseo Wheelwright y avenida España | [original](https://www.mercuriovalpo.cl/impresa/2025/08/08/full/cuerpo-principal/7/) |
| 2025-07-31 | Chilevisión | Tobalaba al límite: Acusan colapso en andén | [video](https://www.youtube.com/watch?v=xKTBmdeA4yA) |
| 2025-07-28 | The Clinic | El error de diseño que condenó a la estación Tobalaba al colapso: la falla estructural en los andenes que Metro no anticipó y que sigue sin solución | [original](https://www.theclinic.cl/2025/07/28/el-error-de-diseno-que-condeno-a-la-estacion-tobalaba-al-colapso-la-falla-estructural-en-los-andenes-que-metro-no-anticipo-y-que-sigue-sin-solucion/) |
| 2025-06-21 | The Clinic | 50 años del Metro: ¿Y si retomamos la “elegancia”? | [original](https://www.theclinic.cl/2025/06/21/50-anos-del-metro-y-si-retomamos-la-elegancia/) |
| 2025-06-19 | El Ciudadano | Karol Cariola y las multas del TAG: Ingeniero en transporte aclara que por ley cualquier persona puede pedir una rebaja del 80% | [original](https://www.elciudadano.com/chile/karol-cariola-y-las-multas-del-tag-ingeniero-en-transporte-aclara-que-por-ley-cualquier-persona-puede-pedir-una-rebaja-del-80/06/19/) |
| 2025-06-07 | Chilevisión | APP muestra estado de ascensores de Metro | Sin URL original documentada |
| 2025-06-05 | LUN | Sitio web le avisa cuántas escaleras mecánicas y ascensores del Metro están malos | [original](https://www.lun.com/Pages/NewsDetail.aspx?EsAviso=0&PaginaId=9&bodyid=0&dt=2025-06-05) |
| 2025-05-28 | LUN | Metro culpa a las lluvias por el caos en la Línea 1 este martes | [original](https://www.lun.com/Pages/NewsDetail.aspx?EsAviso=0&PaginaId=2&bodyid=0&dt=2025-05-28) |
| 2025-05-12 | LUN | Claudio Bravo increpó a conductor que lo chocó: “Bájate ahora, vení alcoholizado” | [original](https://www.lun.com/Pages/NewsDetail.aspx?EsAviso=0&PaginaId=2&bodyid=0&dt=2025-05-12) |
| 2025-05-07 | LUN | Ingeniero alerta de la doble contaminación de las sopladoras de hojas | [original](https://www.lun.com/Pages/NewsDetail.aspx?EsAviso=0&PaginaId=6&bodyid=0&dt=2025-05-07) |
| 2025-05-01 | Chilevisión | Medidas de autocuidado peatonal para prevenir accidentes | [video](https://www.youtube.com/watch?v=wo7keUXeX8k) |
| 2025-05-01 | Chilevisión | Dos mujeres mueren atropelladas por bus Red Movilidad | [video](https://www.youtube.com/watch?v=yclmLliDe5I) |
| 2025-04-20 | LUN | Especialistas en transportes cuestionan maniobrabilidad de los buses oruga | [original](https://www.lun.com/Pages/NewsDetail.aspx?BodyId=0&PaginaId=5&dt=2025-04-20) |
| 2025-04-19 | Canal 13 | Quedó atrapada y fue arrastrada por la micro | [video](https://www.youtube.com/watch?v=dIADb_pXgx0) |
| 2025-04-10 | Universidad de Chile | Ariel López: “El problema en Chile es que no se planifica a largo plazo” | [original](https://uchile.cl/noticias/227093/ariel-lopez-alumni-uchile-la-movilidad-es-un-derecho-social-) |
| 2025-04-09 | LUN | Llegó la primera cabina del Teleférico Bicentenario: caben diez personas cómodamente sentadas | [original](https://www.lun.com/Pages/NewsDetail.aspx?EsAviso=0&PaginaId=2&bodyid=0&dt=2025-04-09) |
| 2025-04-07 | The Clinic | Falla en un neumático generó el colapso de Metro que generó caos en Santiago: especialista acusa falta de mantenimiento de los trenes | [original](https://www.theclinic.cl/2025/04/07/falla-en-un-neumatico-genero-el-colapso-de-metro-que-genero-caos-en-santiago-especialista-acusa-falta-de-mantenimiento-de-los-trenes/) |
| 2025-04-04 | Chilevisión | Ascensores de Metro sin servicio hace un año | [video](https://www.youtube.com/watch?v=MaU_9CpTnP4) |
| 2025-03-24 | LUN | Trifulca por cartel hechizo de baja velocidad en Peñaflor: ¿se puede solicitar tránsito lento a la municipalidad? | [original](https://www.lun.com/Pages/NewsDetail.aspx?EsAviso=0&PaginaId=11&bodyid=0&dt=2025-03-25) |
| 2025-03-24 | Revista Pedalea | Las mejoras que trae la nueva Guía de Diseño Vial Ciclo-Inclusivo | [original](https://revistapedalea.com/las-mejoras-que-trae-la-nueva-guia-de-diseno-vial-ciclo-inclusivo/) |
| 2025-03-20 | LUN | Jugada polémica: micro hace añicos el techo de un paradero y deja a los pasajeros con tiritones | [original](https://www.lun.com/Pages/NewsDetail.aspx?EsAviso=0&PaginaId=2&bodyid=0&dt=2025-03-20) |
| 2025-03-18 | Revista Pedalea | Ciclistas de Melipilla en pie de lucha tras eliminación de ciclovía en calle Libertad | [original](https://revistapedalea.com/ciclistas-de-melipilla-en-pie-de-lucha-tras-eliminacion-de-ciclovia-en-calle-libertad/) |
| 2025-03-12 | Chilevisión | Tarifas de saturación en autopistas urbanas | [video](https://www.youtube.com/watch?v=shWGLIKIx9g) |
| 2025-03-11 | LUN | Ahora podrá renovar licencia de conducir en cualquier municipio | [original](https://www.lun.com/Pages/NewsDetail.aspx?EsAviso=0&PaginaId=6&bodyid=0&dt=2025-03-11) |
| 2025-03-08 | LUN | Caminar o no caminar | [original](https://www.lun.com/Pages/NewsDetail.aspx?EsAviso=0&PaginaId=23&bodyid=0&dt=2025-03-08) |
| 2025-03-03 | LUN | Cómo moverse mejor y qué considerar en el tránsito este amenazante primer lunes de marzo | [original](https://www.lun.com/Pages/NewsDetail.aspx?EsAviso=0&PaginaId=18&bodyid=0&dt=2025-03-03) |
| 2025-02-20 | LUN | Análisis físico-técnico al costalazo que se pegó un ciclista en el Marga Marga | [original](https://www.lun.com/Pages/NewsDetail.aspx?EsAviso=0&PaginaId=6&bodyid=0&dt=2025-02-20) |
| 2025-02-11 | Meganoticias | Alerta por accidentes en peajes | [video](https://www.youtube.com/watch?v=GyRzst7C2Fg) |
| 2025-01-31 | LUN | Es en 3D: debuta buscador para encontrar el último sismo ocurrido en suelo chileno | [original](https://www.lun.com/Pages/NewsDetail.aspx?EsAviso=0&PaginaId=2&bodyid=0&dt=2025-01-31) |
| 2025-01-18 | LUN | Greenlight, la inteligencia artificial que busca mejorar la coordinación de los semáforos en Santiago | [original](https://images.lun.com/Pages/NewsDetail.aspx?EsAviso=0&PaginaId=6&bodyid=0&dt=2025-01-18) |
| 2025-01-09 | Radio Bío Bío | Descarrilamiento en L2 del Metro de Santiago | [video](https://www.youtube.com/watch?v=WNm7xF17vWo) |

### Hallazgos externos no incluidos en el blog 2025

Esta aparición se encontró mediante búsqueda externa y no figura en la copia Markdown del índice anual. Se conserva por separado para ampliar el archivo sin alterar el inventario original del blog.

| Fecha | Medio | Título | Enlace |
|---|---|---|---|
| 2025-06-09 | The Clinic | Influencer en silla de ruedas dejó de usar el metro por ascensores malos en la red: "No están siendo accesibles, nos están excluyendo" | [original](https://www.theclinic.cl/2025/06/09/influencer-en-silla-de-ruedas-dejo-de-usar-el-metro-por-ascensores-malos-en-la-red-no-estan-siendo-accesibles-nos-estan-excluyendo/) |

> Estado: 2025 queda cerrado respecto del índice del blog (50/50 apariciones). El hallazgo externo se etiqueta como `hallazgo_externo`.

## 2024

Fuente anual: [En la prensa 2024](https://blog.ariellopez.cl/en-la-prensa-2024-ee71aa3b0fdf). El contenido fue reconciliado contra una copia Markdown suministrada por el autor: 36/36 apariciones efectivas.

| Fecha | Medio | Título | Enlace |
|---|---|---|---|
| 2024-11-30 | LUN | Ahora puede saber dónde está el grifo más cercano | [original](https://www.lun.com/Pages/NewsDetail.aspx?EsAviso=0&PaginaId=8&bodyid=0&dt=2024-11-30) |
| 2024-10-31 | LUN | A juntar paciencia: empieza la remodelación total de Plaza Italia | [original](https://www.lun.com/Pages/NewsDetail.aspx?EsAviso=0&PaginaId=2&bodyid=0&dt=2024-10-31) |
| 2024-10-03 | Consejo de Políticas de Infraestructura (CPI) | Tren Santiago-Valparaíso, por Camila Balbontín y Ariel López | [original](https://www.infraestructurapublica.cl/tren-santiago-valparaiso-por-camila-balbontin-y-ariel-lopez/) |
| 2024-10-02 | El Mercurio de Valparaíso | Tren Santiago-Valparaíso, por Camila Balbontín y Ariel López | [original](https://www.mercuriovalpo.cl/impresa/2024/10/02/full/cuerpo-principal/8/) |
| 2024-09-21 | LUN | Cambio de pista sin señalizar: es la segunda mayor causa de accidentes de tránsito | Sin URL original documentada |
| 2024-09-08 | Meganoticias | Tarifa de saturación en la mira | [video](https://www.youtube.com/watch?v=MDo4-dxOj_Q) |
| 2024-09-07 | LUN | Ingeniero contabilizó todos los puntos donde hubo atropellos el 2023 | [original](https://www.lun.com/Pages/NewsDetail.aspx?EsAviso=0&PaginaId=6&bodyid=0&dt=2024-09-07) |
| 2024-09-03 | LUN | La historia del paso peatonal que deja a los autos machucados en Quilicura | [original](https://www.lun.com/Pages/NewsDetail.aspx?EsAviso=0&PaginaId=4&bodyid=0&dt=2024-09-03) |
| 2024-08-31 | LUN | Expertos analizan qué pasó con el camión sin conductor que chocó en el camino La Pólvora | [original](https://www.lun.com/Pages/NewsDetail.aspx?EsAviso=0&PaginaId=8&bodyid=0&dt=2024-08-31) |
| 2024-08-22 | LUN | Amaro Gómez-Pablos auxilió a jóven que lo chocó: “es un muchacho honorable” | [original](https://www.lun.com/Pages/NewsDetail.aspx?EsAviso=0&PaginaId=34&bodyid=0&dt=2024-08-22) |
| 2024-07-31 | Radio Pauta | Scooters eléctricos: Un problema de educación vial y una ley ambigua | [original](https://www.pauta.cl/ciudad/ciudad-pauta/2024/07/31/scooters-electricos-un-problema-de-educacion-vial-y-una-ley-ambigua.html) |
| 2024-07-16 | El Mercurio | Japón construirá sistema subterráneo de transporte para carga pequeña | [original](https://digital.elmercurio.com/2024/07/16/DCST-B/NM4EVOCO) |
| 2024-07-12 | La Tercera | Agua en las vías, ‘arcos eléctricos’ y aglomeraciones: las principales dificultades en el funcionamiento de Metro en 2024 | [original](https://www.latercera.com/nacional/noticia/agua-en-las-vias-arcos-electricos-y-aglomeraciones-las-principales-dificultades-en-el-funcionamiento-de-metro-en-2024/L2V5MBQ3R5HFNH4FGEEJQK5KUA/) |
| 2024-07-05 | El Mercurio | Disímil balance por el fin de la reversibilidad en Av. Andrés Bello | [copia](https://www.cedeus.cl/disimil-balance-por-el-fin-de-la-reversibilidad-en-av-andres-bello/) |
| 2024-06-29 | Mega | Continúan las filtraciones de agua en AVO por segundo año consecutivo | [video](https://www.youtube.com/watch?v=YkNxjkA2KPQ) |
| 2024-06-29 | Meganoticias | Continúan las filtraciones de agua en AVO por segundo año consecutivo | [video](https://www.youtube.com/watch?v=OHkdD9J4ylg) |
| 2024-06-29 | TVN | Continúan las filtraciones de agua en AVO por segundo año consecutivo | [video](https://www.youtube.com/watch?v=ZJ1JOduGubA) |
| 2024-06-22 | LUN | Las 38 causales de salud con que le pueden negar o reducir la licencia de conducir | [original](https://www.lun.com/Pages/NewsDetail.aspx?EsAviso=0&PaginaId=19&bodyid=0&dt=2024-06-22) |
| 2024-06-21 | Radio Bío Bío | Concón: autoridades informan que diámetro del socavón en Camino Internacional no ha aumentado | [original](https://www.biobiochile.cl/noticias/nacional/region-de-valparaiso/2024/06/21/concon-autoridades-informan-que-diametro-del-socavon-en-camino-internacional-no-ha-aumentado.shtml) |
| 2024-06-04 | Radio ADN | Entrevista en Radio ADN sobre ciclovías y patinetas | [original](https://adnradio.cl/audio/adn_paisadn_20240604_100000_110000/) |
| 2024-05-13 | LUN | Las esquinas donde estarán las estaciones de la línea 8 del Metro | [original](https://www.lun.com/Pages/NewsDetail.aspx?EsAviso=0&PaginaId=13&bodyid=0&dt=2024-05-13) |
| 2024-05-08 | LUN | Parece meme, pero ocurrió en Santiago: cómo se destraba el candado vehicular | [original](https://www.lun.com/Pages/NewsDetail.aspx?EsAviso=0&PaginaId=24&bodyid=0&dt=2024-05-08) |
| 2024-04-29 | LUN | Para conductores ansiosos: prueban semáforos con cuenta regresiva para el cambio de color | [original](https://www.lun.com/Pages/NewsDetail.aspx?EsAviso=0&PaginaId=20&bodyid=0&dt=2024-04-30) |
| 2024-04-04 | Chilevisión | Circuló contra el tránsito y me agrede por decírselo | [original](https://www.chilevision.cl/programas/contigo-en-la-manana/mujeres-agredieron-a-conductor-hombre-acuso-que-venian-contra-el-transito/) |
| 2024-04-04 | Cooperativa | Circuló contra el tránsito y me agrede por decírselo | [original](https://cooperativa.cl/noticias/pais/transportes/automovilistas/roto-de-m-mujer-agredio-a-conductor-que-le-dijo-que-iba-contra-el/2024-04-04/102930.html) |
| 2024-04-04 | La Cuarta | Circuló contra el tránsito y me agrede por decírselo | [original](https://www.lacuarta.com/cronica/noticia/roto-de-mier-tengo-cancer-le-paran-el-carro-por-manejar-contra-el-transito-y-protagoniza-minuto-de-furia/WU3TLAN36VHPBGBQGCXK7ODX3Q/) |
| 2024-04-04 | Publimetro | Circuló contra el tránsito y me agrede por decírselo | [original](https://www.publimetro.cl/social/2024/04/04/roto-de-mierd-tengo-cancer-conductora-en-contra-del-transito-las-emprende-contra-automovilista-a-garabato-limpio/) |
| 2024-04-04 | Radio Bío Bío | Circuló contra el tránsito y me agrede por decírselo | [original](https://www.biobiochile.cl/noticias/nacional/region-metropolitana/2024/04/04/roto-de-mierda-mujer-agrede-e-insulta-a-conductor-tras-circular-contra-el-transito-en-la-florida.shtml) |
| 2024-04-04 | Radio Futuro | Circuló contra el tránsito y me agrede por decírselo | [original](https://www.futuro.cl/2024/04/te-voy-a-hacer-mierda-el-auto-tengo-cancer-mujer-que-iba-contra-el-transito-pierde-el-control-y-arremete-contra-un-conductor/) |
| 2024-04-04 | Radio Imagina | Circuló contra el tránsito y me agrede por decírselo | [original](https://www.radioimagina.cl/2024/04/tengo-cancer-crisis-de-asma-y-me-estai-hue-la-insolita-explicacion-de-mujer-que-iba-contra-el-transito-y-que-termino-con-la-agresion-hacia-un-conductor/) |
| 2024-04-04 | Radio Pudahuel | Circuló contra el tránsito y me agrede por decírselo | [original](https://www.pudahuel.cl/videos/2024/04/dia-de-furia-mujer-que-iba-en-contra-del-transito-se-hace-viral-tras-agredir-a-otro-conductor-no-me-interesa-romper-el-auto-tengo-cancer-y-me-estai-hue/) |
| 2024-03-17 | Radio ADN | Buses de 2 pisos operan en Santiago hace más de una década | [video](https://www.youtube.com/watch?v=_Vx1l5C178M) |
| 2024-03-15 | La Tercera | ¿Dónde están los buses de dos pisos?: la razón detrás de la desaparición de la novedad de los Panamericanos | [original](https://www.latercera.com/la-tercera-pm/noticia/donde-estan-los-buses-de-dos-pisos-la-razon-detras-de-por-que-las-maquinas-desaparecieron-de-las-calles-de-santiago/ZI6STNNZFJFFJLZGTD65ZPIMWY/) |
| 2024-03-13 | La Cuarta | Pudo evitarse: el análisis de un ingeniero en transporte por escolar que falleció atropellada | [original](https://www.lacuarta.com/cronica/noticia/pudo-evitarse-el-analisis-de-un-ingeniero-en-transporte-por-escolar-que-fallecio-atropellada/AJIHLGIP4ZG7RHYAR5DQFYYREA/) |
| 2024-02-03 | LUN | Comienzan desvíos por la construcción de AVO2: Durarán 4 años y 10 meses | [original](https://www.lun.com/Pages/NewsDetail.aspx?EsAviso=0&PaginaId=2&bodyid=0&dt=2024-02-03) |
| 2024-01-28 | LUN | En Antofagasta instalan baldes plásticos en veredas para terminar con autos mal estacionados | [original](https://www.lun.com/Pages/NewsDetail.aspx?EsAviso=0&PaginaId=2&bodyid=0&dt=2024-01-28) |

### Hallazgos externos no incluidos en el blog 2024

Esta aparición fue confirmada mediante búsqueda externa y no figura entre las 36 apariciones del índice anual 2024. Se conserva por separado para ampliar el archivo sin alterar el inventario original del blog.

| Fecha | Medio | Título | Enlace |
|---|---|---|---|
| 2024-07-31 | Radio Pauta | Una ley ambigua y falta de educación vial: los desafíos ante el creciente uso de scooters en Santiago | [original](https://www.pauta.cl/ciudad/2024/07/31/una-ley-ambigua-y-falta-de-educacion-vial-los-desafios-que-evidencian-los-scooters-en-santiago.html) · [video](https://www.youtube.com/watch?v=_Y-C4mD8yJA) |

> Estado: hallazgo externo verificado. La nota original identifica a Ariel López como entrevistado en Ciudad Pauta; el video correspondiente está preservado en la playlist de prensa.

## 2023

Fuente anual: [En la prensa 2023](https://blog.ariellopez.cl/en-la-prensa-e39e770d85d2). El contenido fue reconciliado contra una copia Markdown suministrada por el autor: 30/30 apariciones.

| Fecha | Medio | Título | Enlace |
|---|---|---|---|
| 2023-11-23 | La Tercera | Demanda colectiva, filtraciones y pavimento deformado: los problemas interminables de AVO 1 | [original](https://www.latercera.com/la-tercera-pm/noticia/demanda-colectiva-filtraciones-y-pavimento-deformado-los-problemas-intermibables-de-avo-1/CQUIO6GRJNGB3PREM7LMDR77KI/) |
| 2023-10-15 | El Ciudadano | ¿Es mejor colocarse a la derecha o a ambos lados de las escaleras mecánicas del Metro?: Investigadores chilenos tienen la respuesta | [original](https://www.elciudadano.com/ciencia-tecnologia/es-mejor-colocarse-a-la-derecha-o-a-ambos-lados-de-las-escaleras-mecanicas-del-metro-investigadores-chilenos-tienen-la-respuesta/10/15/) |
| 2023-10-04 | TVN | Las dudas que salpican a la concesionaria | [video](https://www.youtube.com/watch?v=zxLaFZoc9kQ) |
| 2023-10-02 | Canal 13 | Autopista está fuera de norma | Sin URL original documentada |
| 2023-09-29 | TVN / 24 Horas | Tramo de AVO afectado por filtraciones de agua se mantendrá cerrado | [original](https://www.24horas.cl/programas/manana-informativa/experto-reparacion-avo-problemas-agua-norma-mop) |
| 2023-09-28 | Canal 13 | Ordenan cierre de tramo de AVO | [original](https://www.t13.cl/noticia/nacional/ingeniero-filtraciones-vespucio-oriente-tunel-no-cumpliendo-normas-mop-29-9-2023) |
| 2023-09-28 | Canal 13 | Cierran salida en AVO por riesgos para usuarios | [video](https://www.t13.cl/videos/nacional/cierran-salida-avo-por-riesgos-para-usuarios-por-ahora-no-habra-rebajas-costos-28-9-2023) |
| 2023-09-28 | Canal 13 | Filtraciones en Autopista Vespucio Oriente | [video](https://www.youtube.com/watch?v=Ok277EqeA64) |
| 2023-09-28 | LUN | Concesionaria debió cerrar un acceso, Autopista AVO recomienda manejar a 50 km/h en zonas con filtraciones | Sin URL original documentada |
| 2023-09-28 | Radio Bío Bío | “Debió no haberse construido”: Experto explica acumulación de agua en Autopista Vespucio Oriente | [original](https://www.biobiochile.cl/biobiotv/programas/expreso-bio-bio/2023/09/28/debio-no-haberse-construido-experto-explica-acumulacion-de-agua-en-autopista-vespucio-oriente.shtml) |
| 2023-09-27 | El Mercurio | Tren de levitación magnética: Nuevo maglev chino alcanza los 600 km/h | Sin URL original documentada |
| 2023-09-18 | Canal 13 | AVO, especialistas advirtieron que no cumplía exigencias | Sin URL original documentada |
| 2023-09-13 | Chilevisión | Por mal estado de las vías, motoristas en riesgo | [video](https://www.youtube.com/watch?v=57tCgT5581w) |
| 2023-09-11 | Chilevisión | Mujer herida tras disparo a Metrotren Nos | [video](https://www.youtube.com/watch?v=x3vWbpOWQ18) |
| 2023-09-06 | El Mercurio / Emol | Fin de la reversibilidad de la Costanera Andrés Bello: Los profundos cambios en Santiago que gatillaron la histórica medida | [original](https://www.emol.com/noticias/Nacional/2023/09/06/1106403/andres-bellocardenal-reversibilidad.html) |
| 2023-09-06 | LUN | Impactantes videos de conductores que no respetan los cruces ferroviarios | [original](https://www.lun.com/Pages/NewsDetail.aspx?EsAviso=0&PaginaId=6&bodyid=0&dt=2023-09-06) |
| 2023-07-16 | Revista Pedalea | Bicicletas eléctricas: todo lo que debes saber sobre esta tendencia al alza | [original](https://revistapedalea.com/bicicletas-electricas-todo-lo-que-debes-saber-sobre-esta-tendencia-al-alza/) |
| 2023-07-14 | Radio Bío Bío | Autopista al sur: Ruta 5 Santiago-Chillán contabiliza 7.226 accidentes y 392 muertos en cuatro años | [original](https://www.biobiochile.cl/especial/bbcl-investiga/noticias/reportajes/2023/07/14/autopista-al-sur-ruta-5-santiago-chillan-contabiliza-7-226-accidentes-y-392-muertos-en-cuatro-anos.shtml) |
| 2023-06-19 | La Tercera | Nataniel Cox: el peligro de los cruces peatonales no autorizados en plena Alameda | [original](https://www.latercera.com/tendencias/noticia/nataniel-cox-el-peligro-de-los-cruces-peatonales-no-autorizados-en-plena-alameda/QGAQMXD2TBHIBKGZKH23V7F2G4/) |
| 2023-06-14 | LUN | Dos ingenieros explican como deben cruzar los peatones en forma segunra en Alameda con Nataniel | [original](https://www.lun.com/Pages/NewsDetail.aspx?BodyID=0&NewsID=512675&PaginaId=27&dt=2023-06-14) |
| 2023-04-08 | Canal 13 | Pasajeros se suben a tren de Metro que circula con puerta abierta | Sin URL original documentada |
| 2023-04-03 | La Tercera | Gobierno crea Unidad de Movilidad Activa y espera construir 800 km de ciclovías fuera de Santiago | [original](https://www.latercera.com/nacional/noticia/gobierno-crea-unidad-de-movilidad-activa-y-espera-construir-800-kilometros-de-ciclovias-fuera-de-santiago/EEGFE4QFCRHFJHEKWDT2YJ62TE/) |
| 2023-03-28 | La Tercera | Expertos proyectan aglomeraciones en futura estación de Metro con acceso sólo por ascensores | [original](https://www.latercera.com/nacional/noticia/expertos-proyectan-aglomeraciones-en-futura-estacion-de-metro-con-acceso-solo-por-ascensores/JYBST3E6RRBGTHOOXS5YX24VKY/) |
| 2023-03-26 | Canal 13 | Estación del Metro de Santiago únicamente con ascensores | [video](https://www.youtube.com/watch?v=8NubwgkNL6g) |
| 2023-03-20 | El Mercurio / Emol | De qué se trata, beneficiarios y críticas a la nueva ley que rebaja hasta en un 80% las multas por no pago de TAG | [original](https://www.emol.com/noticias/Economia/2023/03/20/1089848/el-beneficio-para-deudores-tag.html) |
| 2023-02-11 | Canal 13 | Controversia por tragaluces en Autopista Central | [video](https://www.youtube.com/watch?v=IK6pkaOqgM0) |
| 2023-01-29 | El Mercurio / Emol | Sólo el 5,9% de las calles del Gran Santiago tiene niveles “excelentes” | [original](https://www.emol.com/noticias/Nacional/2023/01/29/1085247/calles-santiago-niveles-estudio-calidad.html) |
| 2023-01-24 | El Mercurio / Emol | ¿Por Vespucio o llegar hasta estación Del Sol?: Las propuesta para instalar el Metro en Lo Espejo | [original](https://www.emol.com/noticias/Nacional/2023/01/24/1084792/opciones-metro-para-lo-espejo.html) |
| 2023-01-10 | Radio Bío Bío | La pandemia en silencio: cifra de muertos en siniestros viales sigue aumentando año a año | [original](https://www.biobiochile.cl/especial/bbcl-investiga/noticias/reportajes/2023/01/10/la-pandemia-en-silencio-cifra-de-muertos-en-siniestros-viales-sigue-aumentando-ano-a-ano.shtml) |
| 2023-01-08 | El Mercurio | Andrés Bello, Santa Rosa y Pajaritos: expertos anticipan las calles que deberían tener cámaras de control de velocidad | [copia](https://www.cedeus.cl/blog/2023/01/09/de-aprobarse-el-proyecto-cati-andres-bello-santa-rosa-y-pajaritos-expertos-anticipan-las-calles-que-deberian-tener-camaras-de-control-de-velocidad/) |

## 2022

Fuente anual: [En la prensa 2022](https://blog.ariellopez.cl/en-la-prensa-2022-aebe4412f9d5). El contenido fue recuperado directamente desde una copia Markdown suministrada por el autor. El índice del blog contiene 24 apariciones.

### Documentadas en el blog

| Fecha | Medio | Título | Enlace |
|---|---|---|---|
| 2022-11-30 | El Mercurio | Panel de Expertos sugiere alza de $30 en el Transantiago, pero Gobierno mantiene tarifa | [copia](https://www.infraestructurapublica.cl/panel-de-expertos-sugiere-alza-de-30-en-el-transantiago-pero-gobierno-mantiene-tarifa/) |
| 2022-11-18 | El Mercurio | Mandatario hace llamado de atención a parlamentarios de su coalición tras presión para congelar la tarifa de transporte | [original](https://digital.elmercurio.com/2022/11/18/C/K946UC7N) |
| 2022-11-09 | LUN | Así funciona la bicicleta que en cuatro pasos se convierte en su propio candado | [original](https://www.lun.com/Pages/NewsDetail.aspx?dt=2022-11-10&EsAviso=0&PaginaId=20&bodyid=0) |
| 2022-10-16 | CNN Chile | Buses con sensor de ciclistas y peatones | [video](https://www.youtube.com/watch?v=A-H6sjBomWo&t=11s) |
| 2022-09-29 | LUN | Detectan los puntos donde más costalazos se dan los ciclistas en el Cerro San Cristóbal | [copia](https://fing.utem.cl/2022/09/30/detectan-los-puntos-donde-mas-costalazos-se-dan-los-ciclistas-en-el-cerro-san-cristobal/) |
| 2022-08-19 | El Mercurio | Municipios alistan servicio de transporte gratuito para el plebiscito, a la espera de instrucciones de Contraloría | [original](https://digital.elmercurio.com/2022/08/19/N) |
| 2022-08-18 | El Mercurio | Metro: Critican falta de personal tras falla que obligó a cierre de estaciones | [original](https://digital.elmercurio.com/2022/08/18/C) |
| 2022-07-21 | Chilevisión | Conductor ebrio manejó contra el tránsito y mató a padre con su pequeño hijo y otra menor | [original](https://www.chilevision.cl/contigo-en-directo/mejores-momentos/conductor-ebrio-manejo-contra-el-transito-y-mato-a-padre-con-su-pequeno) |
| 2022-06-02 | LUN | ¿Cómo elegir un casco seguro para andar en bici? Tres especialistas cuentan sus datos | [original](https://www.lun.com/Pages/NewsDetail.aspx?dt=2022-06-02&EsAviso=0&PaginaId=30&bodyid=0) |
| 2022-05-22 | Chilevisión | Proyecto Alameda Providencia busca cambiar la cara de la Alameda | Sin URL original/video verificable |
| 2022-05-05 | Radio Bío Bío | Ocupa la vereda y complica a peatones: experto denuncia instalación de reja del Mall Plaza Vespucio | [original](https://www.biobiochile.cl/noticias/nacional/region-metropolitana/2022/05/05/ocupa-la-vereda-y-complica-a-peatones-experto-denuncia-instalacion-de-reja-del-mall-plaza-vespucio.shtml) |
| 2022-05-01 | El Mercurio | Encuesta revela empeoramiento de la percepción ciudadana sobre las ciclovías y el transporte público | [copia](https://noticiasrepositorio.unab.cl/el-mercurio-encuesta-revela-el-empeoramiento-de-la-percepcion-ciudadana-sobre-las-ciclovias-y-el-transporte-publico/) |
| 2022-04-22 | Chilevisión | Mal estado de buses alcanza nivel peligroso | Sin URL original/video verificable |
| 2022-04-22 | El Mercurio | Mal estado de las micros, especialmente en la periferia, alcanza niveles “peligrosos” | Sin URL original/video verificable |
| 2022-04-15 | Chilevisión | Caida de mujer alerta por estado de micros | Sin URL original/video verificable |
| 2022-04-14 | Chilevisión | Kilométrico taco duró más de 12 horas | Sin URL original/video verificable |
| 2022-03-26 | El Mercurio | Propuesta del ministro de Transporte que busca aumentar impuesto a los combustibles abre debate en el sector | Sin URL original/video verificable |
| 2022-03-09 | LUN | Ciclista muere en accidente en céntrica esquina de Santiago | Sin URL original/video verificable |
| 2022-03-07 | Chilevisión | Polémica por mal uso de ciclovía | Sin URL original/video verificable |
| 2022-03-04 | LUN | ¿Por qué hay una larga fila de autosen una ciclovía de Ñuña? | [copia](https://isci.cl/por-que-hay-una-larga-fila-de-autos-en-una-ciclovia-de-nunoa/) |
| 2022-02-11 | Cooperativa | 15 años de Transantiago | Sin URL original/video verificable |
| 2022-02-07 | Revista Pedalea | El bot que evidencia que el transporte público excede la velocidad máxima | [original](https://revistapedalea.com/el-bot-que-evidencia-que-el-transporte-publico-excede-la-velocidad-maxima/) |
| 2022-02-05 | El Mercurio | Plataforma detecta que más de 4 mil micros circularon a exceso de velovidad la última semana | Sin URL original/video verificable |
| 2022-02-04 | The Clinic | Qué ciudad busca el gobierno de Boric: Expertos evalúan a los nuevos ministros Montes, Muñoz y García | [original](https://www.theclinic.cl/2022/02/04/ciudad-boric-expertos-evaluan-ministros-montes-munoz-garcia/) |

### Hallazgos externos no incluidos en el blog 2022

Estas seis apariciones se encontraron durante la reconstrucción web y no figuran en la copia Markdown del índice anual. Se conservan por separado para ampliar el archivo sin alterar el inventario original del blog.

| Fecha | Medio | Título | Enlace |
|---|---|---|---|
| 2022-11-25 | The Clinic | Cuenta de diseños hostiles armó polémica por los asientos del Metro de Santiago | [original](https://www.theclinic.cl/2022/11/25/disenos-hostiles-asientos-metro-de-santiago/amp/) |
| 2022-07-20 | Chilevisión | Acusan a la falta de limitación de las vías como una de las causas de un fatal accidente de tránsito en Quillota | [video](https://noticias.utem.cl/wp-content/uploads/2022/10/Ariel_Lopez-CHV-20-07.mp4) |
| 2022-04-25 | The Clinic | VIDEO. Acusan que Muni de La Florida liderada por Carter decidió cerrar vereda con rejas: adjuntaron metraje del peligroso camino que quedó | [original](https://www.theclinic.cl/2022/04/25/muni-la-florida-liderada-carter-vereda-rejas/) |
| 2022-03-15 | Revista Pedalea | El ministro de las ciudades intermodales | [original](https://revistapedalea.com/el-ministro-de-las-ciudades-intermodales/) |
| 2022-02-05 | Cooperativa | El 65% de buses del Transantiago excedió el límite de velocidad la última semana | [original](https://www.cooperativa.cl/noticias/site/artic/20220205/pags-amp/20220205105711.html) |
| 2022-01-10 | Revista Pedalea | Ariel López: “Los automovilistas saben que no los están fiscalizando” | [original](https://revistapedalea.com/ariel-lopez-mientras-mas-personas-usan-la-bicicleta-la-calle-se-vuelve-mas-segura-para-todos/) |

> Estado: 2022 queda cerrado respecto del índice del blog (24/24 entradas recuperadas). Los hallazgos externos se etiquetan por separado como `hallazgo_externo`. La política de enlaces es: original del medio → video exacto de YouTube → copia institucional verificable → sin enlace.


## 2021

Fuente anual: [En la prensa 2021](https://blog.ariellopez.cl/en-la-prensa-2021-7192a2541e1e). El contenido fue recuperado directamente desde una copia Markdown suministrada por el autor. El índice del blog contiene 14 apariciones.

### Documentadas en el blog

| Fecha | Medio | Título | Enlace |
|---|---|---|---|
| 2021-12-30 | Universidad de Chile | La ley está pensada desde la perspectiva que las calles son para los vehículos y los peatones ni siquiera se consideran | [original](https://uchile.cl/noticias/182993/la-convivencia-vial-en-ciudades-pensadas-prioritariamente-para-autos) |
| 2021-12-25 | Canal 13 | Reversibilidad de Andrés Bello | Sin URL original/video verificable |
| 2021-11-11 | Radio Pauta | Ciclosendas de Emergencia, Premio Sochitran 2021 | [original](https://www.pauta.cl/actualidad/2021/11/13/la-solucion-de-emergencia-para-ciclistas-con-falta-de-ciclovias.html) |
| 2021-11-09 | LUN | Ciclovía de Lyon tendrá sólo un sentido | Sin URL original/video verificable |
| 2021-11-07 | El Mercurio | Urbanistas proponen soluciones por Línea 7 en Parque Forestal: apuntan a usar calzada en obras de ventilación | [copia](https://www.infraestructurapublica.cl/urbanistas-proponen-soluciones-por-linea-7-en-parque-forestal-apuntan-a-usar-calzada-en-obras-de-ventilacion/) |
| 2021-09-27 | Revista Pedalea | Conoce los beneficios y desventajas del nuevo “modo bicicleta” de Google Maps en Chile | [original](https://revistapedalea.com/conoce-los-beneficios-y-desventajas-del-nuevo-modo-bicicleta-de-google-maps-en-chile/) |
| 2021-08-14 | El Mercurio | Expertos debaten sobre el impacto del proyecto de Autopista Costanera Central | [copia](https://www.dii.uchile.cl/wp-content/uploads/2021/08/14-EL-MERCURIO-Expertos-debaten-sobre-el-impacto-del-proyecto-de-autopista-Costanera-Central.pdf) |
| 2021-07-14 | LUN | La historia del hombre que se pasea por Santiago en este biciclo de 1879 | [original](https://www.lun.com/Pages/NewsDetail.aspx?dt=2021-07-14&PaginaId=23&SupplementId=0&BodyId=0) |
| 2021-03-22 | Radio Concierto | Ariel López, Magister en Urbanismo: “mientras menos ciclistas, más accidentes” | [original](https://www.concierto.cl/2021/03/ariel-lopez-magister-en-urbanismo-mientras-menos-ciclistas-mas-accidentes/) |
| 2021-03-17 | El Ciudadano | Muertes de ciclistas en Chile alcanza su cifra más alta en 5 años | [original](https://www.elciudadano.com/chile/nomasciclistasmuertos-muertes-de-ciclistas-en-chile-alcanza-su-cifra-mas-alta-en-5-anos/03/17/) |
| 2021-03-11 | LUN | En Las Condes y Providencia ya debutaron algunas de las nuevas señales de tránsito | [original](https://www.lun.com/Pages/NewsDetail.aspx?dt=2021-03-11&PaginaId=27&bodyid=0) |
| 2021-01-14 | LUN | Video captó a un hombre circulando en scooter al interior de una autopista | Sin URL original/video verificable |
| 2021-01-12 | La Tercera | Muertes en accidentes muestran baja histórica, pero suben ciclistas fallecidos | [original](https://www.latercera.com/nacional/noticia/muertes-en-accidentes-muestran-baja-historica-pero-suben-ciclistas-fallecidos/ZUIR7DYZ25BENGEYVCRND4VCEA/) |
| 2021-01-07 | La Tercera | Nueve mil partes por exceso de velocidad se cursaron en cuatro meses | [original](https://www.latercera.com/nacional/noticia/nueve-mil-partes-por-exceso-de-velocidad-se-cursaron-en-cuatro-meses/MJVXX6AIA5BNFOZDZF745C6SE4/) |

### Hallazgos externos no incluidos en el blog 2021

Estas cinco apariciones se encontraron durante la reconstrucción web y no figuran en la copia Markdown del índice anual. Se conservan por separado para ampliar el archivo sin alterar el inventario original del blog.

| Fecha | Medio | Título | Enlace |
|---|---|---|---|
| 2021-12-23 | Radio Bío Bío | Experto en transportes advierte que Andrés Bello se ha vuelto una vía peligrosa desde hace décadas | [original](https://www.biobiochile.cl/noticias/opinion/entrevistas/2021/12/23/expero-en-transportes-advierte-que-andres-bello-se-ha-vuelto-una-via-peligrosa-desde-hace-decadas.shtml) |
| 2021-12-22 | Vergara 240 / UDP | Muertes de ciclistas: Los puntos críticos de la Ley de Convivencia Vial | [original](https://vergara240.udp.cl/muertes-ciclistas-chile-ley-de-convivencia-vial/) |
| 2021-10-22 | Meganoticias | Semáforo con luz verde en Las Condes apenas duraba 10 segundos: Ingeniero logró que lo reprogramaran | [original](https://www.meganoticias.cl/nacional/355894-semaforo-verde-10-segundos-las-condes-ingeniero-logro-un-cambio-22-10-2021.html) |
| 2021-06-27 | Revista Pedalea | #VeredaNoEsCiclovia: Ciudadanía organizada dice no a la infraestructura deficiente | [original](https://revistapedalea.com/veredanoesciclovia-ciudadania-organizada-dice-no-a-la-infraestructura-deficiente/) |
| 2021-06-25 | La Tercera | Metro reanuda servicio tras interrupción de Línea 4A por falla en estación La Cisterna | [original](https://www.latercera.com/nacional/noticia/metro-presenta-servicio-interrumpido-en-linea-4a-por-falla-en-estacion-la-cisterna/TZRBHJ253NAPXIHMFRV63FXYBU/) |

> Estado: 2021 queda cerrado respecto del índice del blog (14/14 entradas recuperadas). Los hallazgos externos se etiquetan por separado como `hallazgo_externo`.


## 2020

Fuente anual: [En la prensa 2020](https://blog.ariellopez.cl/en-la-prensa-2020-e95ebbc5518c).

| Fecha | Medio | Título | Enlace |
|---|---|---|---|
| 2020-12-24 | Revista Más Deco / La Tercera | La escalada del ciclismo urbano | [original](https://www.latercera.com/masdeco/la-escalada-del-ciclismo-urbano/) |
| 2020-12-09 | El Mercurio | Infraestructura para bicicletas: ¿Se pueden concesionar las ciclovías? | Sin URL original documentada |
| 2020-12-01 | La Tercera | Metro tuvo 26 millones de pasajeros en noviembre, la cifra más alta de la pandemia | Sin URL original documentada |
| 2020-11-27 | Meganoticias | Motociclista muere tras grave colisión | Sin URL original documentada |
| 2020-11-15 | The Clinic | Especialistas y organizaciones encienden las alertas por alarmante cifra en pandemia | [original](https://www.theclinic.cl/2020/11/13/nomasciclistasmuertos-especialistas-y-organizaciones-encienden-las-alertas-por-alarmante-cifra-en-pandemia/) |
| 2020-11-13 | El Dínamo | Las cinco razones tras el dramático aumento de ciclistas fallecidos durante este año | [original](https://www.eldinamo.cl/pais/2020/11/13/aumento-de-ciclistas-fallecidos-durante-este-ano-expertos/) |
| 2020-11-11 | Meganoticias | Un año oscuro para los ciclistas | Sin URL original documentada |
| 2020-11-03 | La Tercera | Aumenta número de ciclistas fallecidos en accidentes de tránsito en pandemia | Sin URL original documentada |
| 2020-10-02 | La Tercera | Desconfinamiento: Suben tiempos de traslado en la Región Metropolitana | Sin URL original documentada |
| 2020-09-26 | La Tercera | Debuta ciclovía de 2,5 km en la ribera del río Mapocho | Sin URL original documentada |
| 2020-09-23 | La Tercera | A casi un año del 18 de Octubre, Metro alista reapertura de toda su red | Sin URL original documentada |
| 2020-08-19 | Tele13 Radio | Propuesta de Ciclovía en el eje Alameda — Providencia | Sin URL original documentada |
| 2020-08-11 | La Tercera | Grupo de expertos propone al gobierno ciclovía para el eje Alameda — Providencia | Sin URL original documentada |
| 2020-08-07 | LUN | Con una bici eléctrica se puede andar hasta 60 km al día y se carga en 3 horas | [original](https://www.lun.com/Pages/NewsDetail.aspx?BodyId=0&PaginaId=19&SupplementId=0&dt=2020-08-08) |
| 2020-08-03 | La Tercera | Viajes en buses y Metro subieron 11% la semana pasada | Sin URL original documentada |
| 2020-07-30 | El Mercurio | Alza de hasta 60% en flujos de comunas en transición pone en riesgo estrategia sanitaria | [original](https://digital.elmercurio.com/2020/07/30/C/JL3QUIK0) |
| 2020-07-28 | La Tercera | Gobierno solicita a empresas flexibilizar los horarios de ingreso, almuerzo y salida | Sin URL original documentada |
| 2020-06-04 | El Mercurio | La dispar distribución de ciclovías frente al aumento de usuarios durante las crisis | Sin URL original documentada |
| 2020-05-20 | La Tercera | Viajes en el transporte público registran la mayor baja de la crisis | [original](https://www.latercera.com/nacional/noticia/viajes-en-el-transporte-publico-registran-la-mayor-baja-de-la-crisis/2SKMYFF4KBEX3MM62QKKZLU2RM/) |
| 2020-05-06 | El Mostrador | Estallido social y pandemia propician que uso de la bicicleta comience a ganarle terreno al automóvil | [original](https://www.elmostrador.cl/cultura/2020/05/06/estallido-social-y-pandemia-propician-que-uso-de-la-bicicleta-comience-a-ganarle-terreno-al-automovil/) |
| 2020-05-06 | LUN | Novedoso sujetador de vasos impide que se derramen líquidos de la bicicleta | [original](http://lun.com/Pages/NewsDetail.aspx?dt=2020-05-06&PaginaId=26&bodyid=0) |
| 2020-05-05 | La Tercera | Baquedano: comercio valora apertura de accesos | Sin URL original documentada |
| 2020-04-25 | El Mercurio | Paseo Bandera, convertido en estacionamiento irregular | Sin URL original documentada |
| 2020-04-01 | La Tercera | Transporte en su semana negra: viajes disminuyen un 81,6% en Santiago | Sin URL original documentada |
| 2020-03-30 | LUN | Ingeniero en transportes le saca trote a su bicicleta que aguanta 100 kilos de carga | [original](https://www.lun.com/Pages/NewsDetail.aspx?PaginaId=17&bodyid=0&dt=2020-03-31) |
| 2020-03-27 | LUN | Tiempos de viaje en La Florida se redujeron hasta 14,8 minutos en la últimos días | [original](https://www.lun.com/Pages/NewsDetail.aspx?PaginaId=30&bodyid=0&dt=2020-03-27) |
| 2020-03-26 | La Tercera | Metro: La Cisterna y Las Rejas concentran los viajes | [original](https://www.latercera.com/nacional/noticia/metro-estaciones-la-cisterna-y-las-rejas-concentran-mayor-afluencia-de-pasajeros-en-la-manana/K4LNIROTVZGOZLOI5SN3R77TFQ/) |
| 2020-03-24 | La Tercera | Metro amplia horario y CPC se compromete a facilitar entradas y salidas | Sin URL original documentada |
| 2020-03-13 | La Tercera | Metro: Suben viajes, pero no a niveles pre estallido | Sin URL original documentada |
| 2020-03-09 | El Mercurio | Licitaciones de futuras líneas 8 y 9 fueron declaradas desiertas en medio de crisis social | Sin URL original documentada |
| 2020-03-07 | La Tercera | Protestas obligan a cerrar 30 estaciones de Metro | Sin URL original documentada |
| 2020-03-06 | La Tercera | Descuento a tercera edad en buses del Transantiago será a través de la tarjeta bip! | Sin URL original documentada |
| 2020-02-28 | LUN | Providencia presenta nuevos semáforos con sistemas antizamarreos | [original](https://www.lun.com/Pages/NewsDetail.aspx?BodyID=0&NewsID=446584&PaginaId=64&dt=2020-02-28) |
| 2020-02-16 | LUN | En India, los semáforos castigan a conductores que bocinean | [original](https://www.lun.com/Pages/NewsDetail.aspx?BodyID=0&PaginaId=18&SupplementId=0&dt=2020-02-16&r=w) |
| 2020-02-15 | LUN | Campaña para que el Metro tenga baños lleva 9600 firmas | [original](https://www.lun.com/Pages/NewsDetail.aspx?BodyID=0&PaginaId=8&SupplementId=0&dt=2020-02-15&r=w) |
| 2020-02-14 | El Mercurio | Expertos plantean subsidios focalizados y otros métodos de pago para abordar evasión | [original](https://digital.elmercurio.com/2020/02/14/C/LS3OD9MH) |
| 2020-02-06 | LUN | ¿Puedo usar un estacionamiento para discapacitados si tengo el pie enyesado? | [original](https://www.lun.com/Pages/NewsDetail.aspx?PaginaId=50&bodyid=0&dt=2020-02-07) |
| 2020-02-01 | La Tercera | Registro de evasores del Transantiago: 26% de los multados ingresó tras el estallido social | [original](https://www.latercera.com/nacional/noticia/registro-evasores-del-transantiago-26-los-multados-ingreso-tras-estallido-social/995502/) |
| 2020-01-29 | La Tercera | Viajes de Metro y buses reputan en diciembre y compensarán a operadores | [original](https://www.latercera.com/nacional/noticia/viajes-metro-buses-repuntan-diciembre-compensaran-operadores/990863/) |
| 2020-01-22 | La Tercera | Gobierno analiza nueva ley para financiar el Transantiago | [original](https://www.latercera.com/nacional/noticia/gobierno-analiza-nueva-ley-financiar-transantiago/982442/) |
| 2020-01-22 | LUN | ¿Funcionan los semáforos portátiles en Providencia con Eliodoro Yáñez? | [original](https://www.lun.com/Pages/NewsDetail.aspx?BodyID=0&PaginaId=36&dt=2020-01-23) |
| 2020-01-15 | La Tercera | Avenidas claves de Providencia tendrán un carril menos por instalación de ciclopistas | [original](https://www.latercera.com/nacional/noticia/avenidas-claves-providencia-tendran-carril-menos-instalacion-ciclopistas/973932/) |
| 2020-01-14 | La Tercera | Obras en La Pirámide generan alta congestión y reclamos entre los usuarios | [original](https://www.latercera.com/nacional/noticia/obras-la-piramide-generan-alta-congestion-reclamos-los-usuarios/972722/) |
| 2020-01-03 | TVN | Ciclistas lideran cifras de accidentes fatales | Sin URL original documentada |
| 2020-01-02 | Radio Bío Bío | Expertos estiman que la evasión en el Transantiago superó el 50% en la última parte del 2019 | [original](https://www.biobiochile.cl/noticias/nacional/region-metropolitana/2020/01/02/expertos-estiman-que-la-evasion-en-el-transantiago-supero-el-50-en-la-ultima-parte-del-2019.shtml) |
| 2020-01-01 | LUN | Trabajos para recuperar cruce del Paradero 14 de La Florida llevan 60% de avance | Sin URL original documentada |

## Fuente audiovisual: YouTube

La playlist de prensa del canal de Ariel López se usa como respaldo audiovisual canónico cuando la URL original del medio no está disponible. El inventario automatizado enumera **105 videos** y se cruza de forma reproducible contra `prensa.csv`.

- Playlist: https://www.youtube.com/playlist?list=PLAzCbyGKyDPBSXrZb5NctMaQwpZPmpUMG
- Inventario generado: `archivo/prensa/youtube_playlist.csv`
- Reporte de cruce: `archivo/prensa/youtube_match_report.md`
- Script: `scripts/sync_youtube_prensa.py`
- Workflow: `.github/workflows/sync-youtube-prensa.yml`

Los enlaces originales de los medios tienen prioridad y nunca son reemplazados por YouTube. Los videos se usan para completar registros sin URL original y para detectar posibles apariciones externas que luego requieren verificación.

## Notas de calidad de datos

El catálogo distingue el registro documental de la interpretación. En particular, algunos años contienen errores tipográficos de fecha o títulos, y algunos encabezados reúnen varias coberturas. Esos casos se normalizan sin ocultarlos: la versión CSV conserva una columna `nota` para documentar la decisión.

La actualización automática desde Medium quedó desactivada porque los runners de GitHub reciben respuestas 403. El workflow sólo valida el catálogo. Los años 2021, 2022, 2023, 2024, 2025 y 2026 fueron reconciliados contra copias de texto/Markdown aportadas por el autor. El estado `hallazgo_externo` identifica apariciones verificadas que no figuran en el índice anual del blog.
