# Contexto: Presentación QA — Review Ejecutiva Farmacity Group

## Propósito

Este repositorio existe para mantener una secuencia ejecutiva de slides que ayude a Gonzalo Estevez a presentar el valor del equipo QA ante owners, sponsors y stakeholders, sin caer en listados de tickets ni dashboards técnicos.

La intención no es explorar diseños nuevos en cada iteración. La intención actual es conservar una estructura estable y actualizar datos, métricas, copy breve y casos destacados con el menor costo posible.

## Arquitectura vigente

La review vigente se compone de `3` slides horizontales:

- `slider-01.html`
- `slider-02.html`
- `slider-03.html`

`slider-q1.html` ya no es el artefacto principal. Queda como referencia histórica y base del split que originó `slider-01` y `slider-02`.

Canvas vigente por slide:

- `1440x840`

## Rol de cada slide

### Slide 01

Archivo:

`slider-01.html`

Objetivo:

Mostrar cómo QA acompañó el ritmo de delivery, las mejoras y los frentes de innovación del trimestre.

Bloques estables:

- KPI strip superior
- panel de mix por sprint
- panel de cobertura por formato
- `3` cards de cierre

### Slide 02

Archivo:

`slider-02.html`

Objetivo:

Mostrar cómo QA interceptó riesgo, gestionó bugs y sostuvo control operativo durante el trimestre.

Bloques estables:

- KPI strip superior
- panel de bugs por sprint
- panel doble de formato y prioridad
- `4` cards de bugs destacados

### Slide 03

Archivo:

`slider-03.html`

Objetivo:

Mostrar el comportamiento de la ticketera TeAyudo, separando el peso de Post Venta del resto de la plataforma y destacando las incidencias más repetidas por mes.

Bloques estables:

- resumen principal de ticketera
- strip de estado operativo
- `section.months-grid` con `3` cards mensuales
- panel final de prácticas de carga

## Sistema visual vigente

Este proyecto ya tiene una línea visual definida. No debería rediseñarse salvo pedido explícito.

Principios visuales actuales:

- fondo blanco limpio
- lenguaje ejecutivo
- contenedores blancos con borde sutil y radio amplio
- tipografía `Montserrat`
- color principal `#211274`
- uso de colores de apoyo solo para jerarquía puntual
- lectura rápida y poco texto visible

Paleta base:

- `#211274`
- `#5ba698`
- `#d7d8d8`
- `#ff3131`
- `#00dd88`
- `#49a5ef`
- `#ffd359`
- `#ffffff`

## Regla principal de mantenimiento

La estructura y el diseño base deben considerarse estables.

Primero se actualizan:

- números
- porcentajes
- labels
- notas breves
- casos destacados

Solo después, y si realmente hace falta, se toca layout.

La expectativa para futuras iteraciones es:

`cambiar datos antes que rediseñar bloques`

## Fuentes de datos actuales

Fuentes principales:

- `docs/jira-cvs/Jira (Q1).csv`
- `docs/jira-cvs/Jira-mejoras (Q1).csv`
- `docs/jira-cvs/Jira-error (Q1).csv`
- `docs/contexto/q1_metrics_baseline.md`
- `docs/story/q1-data-team.md`
- `docs/contexto/teayudo_ticketera_q1.json`

Fuente visual transitoria para `slider-03`:

- `docs/capturas/slider-03.png`

Orden de prioridad si aparecen contradicciones:

1. `docs/jira-cvs/*.csv`
2. `docs/story/*`
3. `docs/contexto/*`
4. capturas

## Caveats metodológicos

- El export principal trae `10` columnas `Sprint` duplicadas. Q1 se define leyendo todas.
- `Campo personalizado (Criticidad)` está vacío. `Prioridad` se usa como proxy de criticidad.
- `Tiempo Trabajado` está incompleto. Las horas visibles deben presentarse como `horas registradas en Jira`.
- La pertenencia al trimestre se define por presencia del ticket en sprints Q1, aunque el cierre ocurra después.
- `Capacity (Q1).csv` sigue siendo exploratorio.
- `slider-03` usa datos normalizados manualmente desde captura. Eso sirve para mantenimiento simple, pero sigue siendo deuda técnica si el slide pasa a actualizarse con frecuencia.

## Métricas vigentes por slide

### Slide 01

- Tareas / User Stories: `177`
- Prioridad alta:
  - `Highest`: `12`
  - `High`: `28`
- Horas registradas QA: `511.7 h`
- Mejoras cerradas: `94`
- Mix por sprint:
  - Sprint 1: `43` = `24` mejoras / `14` bugs / `5` innovación
  - Sprint 2: `59` = `23` mejoras / `23` bugs / `13` innovación
  - Sprint 3: `75` = `47` mejoras / `25` bugs / `3` innovación
- Cobertura por formato:
  - GetTheLook: `27`
  - Cross: `26`
  - Farmacity: `17`
  - TheFoodMarket: `15`
  - Simplicity: `9`
- Completitud mensual:
  - Enero: `44%`
  - Febrero: `52%`
  - Marzo: `60%`

### Slide 02

- Bugs Q1: `59`
- Resolución: `100%`
- Prioridad alta:
  - `Highest`: `7`
  - `High`: `10`
- Pico por sprint: `23`
- Bugs por sprint:
  - Sprint 1: `14`
  - Sprint 2: `23`
  - Sprint 3: `22`
- Bugs por formato:
  - Farmacity: `24`
  - GetTheLook: `14`
  - Simplicity: `12`
  - TheFoodMarket: `9`
- Prioridad en Jira:
  - Medium: `17`
  - High: `10`
  - Highest: `7`
  - Low: `1`

### Slide 03

- Tickets totales: `181`
- Post Venta: `93` (`51,4%`)
- Resto plataforma: `88` (`48,6%`)
- Estado operativo:
  - Tickets: `88`
  - Abiertos: `29`
  - En espera: `29`
  - Cerrados: `30`
  - Tiempo promedio de resolución: `18d`
- Top incidencias:
  - Enero: `27` tickets / `20` incidentes
  - Febrero: `25` tickets / `17` incidentes
  - Marzo: `36` tickets / `29` incidentes

## Narrativa actual

Slide 01:

- QA acompañó volumen, prioridad alta e innovación

Slide 02:

- QA interceptó riesgo y sostuvo control de bugs

Slide 03:

- la ticketera deja una lectura operativa separada entre Post Venta y resto plataforma

Las slides deben sentirse como una sola secuencia, no como piezas aisladas.

## Estado documental

`docs/contexto/slide_design_system.md` no existe hoy en el repositorio.

Hasta que exista, el sistema vigente queda documentado en:

- este archivo
- `docs/contexto/slide_maintenance_system.md`
- `AGENTS.md`

## Validación esperada

- servir por HTTP local antes de usar Playwright
- validar `slider-01.html`, `slider-02.html` y `slider-03.html` en `1440x840`
- revisar jerarquía visual, legibilidad, clipping y consistencia entre slides
- verificar métricas y casos contra las fuentes antes de cerrar cambios
