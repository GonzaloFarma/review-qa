# Q1 Metrics Baseline

Baseline inicial armado desde `docs/jira-cvs/Jira (Q1).csv` para definir la narrativa de la review Q1.

## Caveats del dataset

- El CSV trae 10 columnas duplicadas llamadas `Sprint`. Hay que leerlas como un conjunto, no como una sola columna.
- `Campo personalizado (Criticidad)` está vacío en todos los registros.
- Para hablar de severidad en esta fase se usa `Prioridad` como proxy.
- El CSV no separa de forma explícita `tareas internas` vs `QA para implementación`; hoy eso queda absorbido mayormente dentro de `Mejora`.
- `Bugs evitados` no existe como campo nativo. Solo puede inferirse, con cautela, a partir del naming o tagging de los bugs.

## Totales Q1

- Total de incidencias en Q1: `132`
- Mejoras: `97` (`73.5%`)
- Bugs: `35` (`26.5%`)
- Incidencias con arrastre entre más de un sprint Q1: `35` (`26.5%`)
- Incidencias resueltas dentro del período Q1: `70`

## Carga por sprint

Métrica: una incidencia cuenta en el sprint si estuvo presente en cualquiera de las columnas `Sprint` asociadas a ese registro.

| Sprint | Total | Mejoras | Bugs | % Bugs |
| --- | ---: | ---: | ---: | ---: |
| Sprint 1 | 52 | 39 | 13 | 25.0% |
| Sprint 2 | 52 | 39 | 13 | 25.0% |
| Sprint 3 | 70 | 55 | 15 | 21.4% |

Lectura inicial:

- Marzo muestra más volumen de trabajo que enero y febrero.
- El mix se mantiene dominado por mejoras, no por bugs.
- El peso relativo de bugs baja levemente en Sprint 3 aunque la carga total sube.

## Cierres por sprint

Métrica: una incidencia cuenta como cerrada en el sprint si `Resuelta` cae dentro de la ventana del sprint.

| Sprint | Cerradas | Mejoras | Bugs |
| --- | ---: | ---: | ---: |
| Sprint 1 | 22 | 15 | 7 |
| Sprint 2 | 20 | 13 | 7 |
| Sprint 3 | 28 | 20 | 8 |

Lectura inicial:

- Sprint 3 muestra la mejor capacidad de cierre del trimestre.
- El nivel de resolución de bugs se mantiene relativamente estable.

## Mix por formato

### Sprint 1

- Farmacity: `15`
- Simplicity: `11`
- Cross: `10`
- TheFoodMarket: `10`
- GetTheLook: `6`

### Sprint 2

- Farmacity: `20`
- TheFoodMarket: `11`
- Simplicity: `9`
- GetTheLook: `7`
- Cross: `5`

### Sprint 3

- TheFoodMarket: `18`
- GetTheLook: `17`
- Farmacity: `16`
- Cross: `14`
- Simplicity: `5`

Lectura inicial:

- El esfuerzo no estuvo concentrado en una sola marca durante todo Q1.
- Sprint 3 muestra una distribución más cargada en TFM, GTL y Cross.

## Bugs por prioridad

Se usa `Prioridad` como proxy de criticidad.

| Prioridad | Bugs |
| --- | ---: |
| Highest | 7 |
| High | 10 |
| Medium | 17 |
| Low | 1 |

Lectura inicial:

- `17` bugs (`48.6%`) fueron `High` o `Highest`.
- Esto habilita una narrativa de control de riesgo, no solo volumen.

## Bugs por formato

| Formato | Bugs |
| --- | ---: |
| Farmacity | 15 |
| TheFoodMarket | 9 |
| Simplicity | 8 |
| GetTheLook | 3 |

## Escapados vs contenidos

Inferencia conservadora:

- `Bug escapado`: el resumen del ticket contiene `PROD` o `Producción`
- `Bug contenido`: bug sin esa marca explícita en el resumen

Resultado:

- Bugs escapados detectables por naming: `5`
- Bugs contenidos antes de producción por inferencia: `30`

Esto da una señal preliminar de contención de `85.7%`, pero no debe venderse como métrica exacta hasta validar el criterio con negocio o con quien exportó Jira.

## Recomendación de narrativa para las slides

### Slide 1

Título sugerido:

`Cómo QA sostuvo la operación y la salida de cambios en Q1`

Bloques sugeridos:

- Hero metrics: carga total Q1, mejoras vs bugs, cierres Q1, arrastre entre sprints
- Mix por sprint: volumen y composición del trabajo
- Distribución por formato: mostrar cobertura del equipo sobre distintas marcas
- Mensaje ejecutivo: el trimestre estuvo dominado por acompañamiento a implementación con control de riesgo sostenido

### Slide 2

Título sugerido:

`Qué riesgo detectó QA antes de impactar al cliente`

Bloques sugeridos:

- Bugs por sprint: carga y cierre
- Bugs por prioridad: proxy de criticidad
- Escapados vs contenidos: con disclaimer metodológico
- Casos destacados: 3 a 4 bugs con redacción de impacto de negocio, no técnica
