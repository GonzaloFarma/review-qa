# Sistema de mantenimiento de slides

## Objetivo

Este documento existe para facilitar actualizaciones futuras sin reabrir decisiones de diseño o arquitectura.

La regla base es:

`mantener estructura y actualizar datos`

## Qué se considera estable

Estos elementos no deberían cambiar salvo pedido explícito de rediseño:

- cantidad de slides
- rol narrativo de cada slide
- jerarquía general de bloques
- orden de lectura
- sistema de bordes, radios y contenedores
- tipografía y paleta base

## Qué se considera variable

Estos elementos sí pueden actualizarse con frecuencia:

- números
- porcentajes
- labels cortos
- notas breves
- nombres de cards
- copy ejecutivo de 1 o 2 líneas
- casos destacados

## Mapa de mantenimiento por slide

### `slider-01.html`

Bloques estables:

- KPI strip
- panel de mix por sprint
- panel de cobertura por formato
- `3` cards finales

Normalmente se actualiza:

- KPIs
- valores por sprint
- cobertura por formato
- porcentajes de completitud
- copy de innovación

No tocar por default:

- estructura del panel principal
- orden de cards
- proporciones generales

### `slider-02.html`

Bloques estables:

- KPI strip
- panel de bugs por sprint
- panel doble de formato y prioridad
- `4` cards finales

Normalmente se actualiza:

- KPIs
- valores por sprint
- ranking por formato
- distribución por prioridad
- copy de los casos destacados

No tocar por default:

- estructura del gráfico
- cantidad de cards
- partición izquierda/derecha

### `slider-03.html`

Bloques estables:

- resumen superior
- strip de estado operativo
- `section.months-grid`
- panel final de prácticas

Normalmente se actualiza:

- volumen total
- peso de Post Venta
- estado operativo
- top incidencias por mes
- prácticas finales

No tocar por default:

- estructura de `months-grid`
- jerarquía del resumen superior
- ubicación del panel final

## Flujo recomendado de actualización

1. Identificar qué slide cambia.
2. Confirmar la fuente de datos.
3. Actualizar solo los valores y copys afectados.
4. Revisar si el cambio rompe densidad o legibilidad.
5. Validar visualmente.
6. Documentar solo si cambió una regla estable.

## Fuentes de datos por slide

### Slide 01

- `docs/jira-cvs/Jira (Q1).csv`
- `docs/jira-cvs/Jira-mejoras (Q1).csv`
- `docs/contexto/q1_metrics_baseline.md`
- `docs/story/q1-data-team.md`

### Slide 02

- `docs/jira-cvs/Jira (Q1).csv`
- `docs/jira-cvs/Jira-error (Q1).csv`
- `docs/contexto/q1_metrics_baseline.md`
- `docs/story/q1-data-team.md`

### Slide 03

- `docs/contexto/teayudo_ticketera_q1.json`
- `docs/capturas/slider-03.png`

## Cuándo sí conviene tocar layout

Solo cuando ocurre alguno de estos casos:

- un bloque ya no entra en el canvas
- un cambio de datos vuelve ilegible la slide
- cambia la narrativa ejecutiva del trimestre
- hay pedido explícito de rediseño

Si no pasa eso, la decisión correcta suele ser:

`editar contenido, no rediseñar`
