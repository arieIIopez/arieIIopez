# Revisión curada de videos de prensa sin correspondencia

Este archivo clasifica los videos que el cruce automático no pudo resolver con suficiente confianza. No modifica `prensa.csv`: sólo organiza la cola de verificación.

- candidato_nuevo_fuerte: **10**
- alternativa_confirmada: **6**
- candidato_nuevo: **5**
- probable_alternativa: **5**
- requiere_revision: **3**
- posible_segunda_aparicion_mismo_medio: **2**
- sin_datos: **1**
- candidato_fuera_prensa_o_nuevo: **1**

## Criterio

- **alternativa_confirmada**: mismo hecho/medio ya catalogado; conservar como enlace audiovisual secundario.
- **probable_alternativa**: alta probabilidad de corresponder a una fila existente, pero falta comparar contenido.
- **candidato_nuevo_fuerte**: título/medio señalan una aparición separada que merece incorporarse cuando se confirme la fecha.
- **candidato_nuevo**: posible aparición nueva, todavía con menos evidencia contextual.
- **posible_segunda_aparicion_mismo_medio**: mismo hecho y medio, pero podría ser otra emisión/programa.
- **candidato_fuera_prensa_o_nuevo**: contenido audiovisual relevante cuya taxonomía debe decidirse.
- **requiere_revision / sin_datos**: evidencia insuficiente.

## Candidatos nuevos prioritarios

- [Car fire at Santa Isabel Metro station: Affected train is 50 years old](https://www.youtube.com/watch?v=MRthnyOPgw0) — Teletrece. Video oficial de Teletrece sobre incendio en Metro/Santa Isabel; el catálogo tiene el evento en otros medios pero no esta pieza de Teletrece.
- [¿Por qué FALTAN más micros? El ESTUDIO que CUESTIONA al ministro Louis De Grange | #TurnoEnVivo](https://www.youtube.com/watch?v=5dGMB_IPaeY) — Turno. Aparición identificada en Turno sobre recorte de buses; el catálogo contiene el estudio en Contrapoder, que es otro medio.
- [Entrevista en Radio ADN respecto al transporte público, trenes y ciclovías](https://www.youtube.com/watch?v=4ZjCe7eLxps) — Ariel López. Entrevista explícita en Radio ADN sobre transporte público, trenes y ciclovías; no hay coincidencia inequívoca en el catálogo.
- [Pasajeros ciegos no pueden salir de la estación Universidad de Chile por falta de accesibilidad](https://www.youtube.com/watch?v=zZnNwRWO-lA) — Ariel López. Tema de accesibilidad: pasajeros ciegos sin salida en estación Universidad de Chile; no existe fila equivalente clara.
- [Entrevista en Mega por mala señalización en AVO](https://www.youtube.com/watch?v=3kBjdT_W1Ls) — Ariel López. Entrevista identificada en Mega por señalización deficiente en AVO; el catálogo tiene Chilevisión sobre señalética, no esta aparición en Mega.
- [Chileans report driving complications due to errors in highway signage](https://www.youtube.com/watch?v=XC_g7fkwJlI) — Meganoticias. Video oficial de Meganoticias sobre errores de señalización; probablemente es la contraparte oficial del clip 3kBjdT_W1Ls.
- [Entrevista en Radio Biobio por proyecto de mejoramiento de la Av. España en Valparaíso](https://www.youtube.com/watch?v=-zvmYIR3JiA) — Ariel López. Entrevista explícita en Radio Bío Bío sobre mejoramiento de Av. España en Valparaíso; no hay fila equivalente clara.
- [Entrevista en Tu día por rebaja del TAG e 50% en AVO](https://www.youtube.com/watch?v=eqzU13J7s9U) — Ariel López. Entrevista en Tu Día/Canal 13 por rebaja del TAG en AVO; tema distinto de la fila AVO sugerida automáticamente.
- [Entrevista en Canal 13, en el programa Tu día respecto a congestión y agua en AVO](https://www.youtube.com/watch?v=jeUvxR1P2_Q) — Ariel López. Entrevista en Tu Día/Canal 13 sobre congestión y agua en AVO; puede ser cobertura adicional no individualizada.
- [Entrevista en Radio Biobio por fallas en Túnel Ramal del Mapocho de AVO](https://www.youtube.com/watch?v=1fKVxuIqbbI) — Ariel López. Entrevista explícita en Radio Bío Bío por fallas del Túnel Ramal Mapocho AVO; no hay fila equivalente de ese medio.

## Evidencia externa ya confirmada

- La entrevista sobre modernización de taxis colectivos tiene nota original de Radio Bío Bío del 18-02-2026 y ya existe en el catálogo; el video de la playlist queda como enlace audiovisual alternativo.
- La búsqueda de metadata individual por `yt-dlp` desde GitHub Actions fue bloqueada por YouTube (0/33 recuperados); por eso no se asignan fechas inferidas a los demás candidatos.
