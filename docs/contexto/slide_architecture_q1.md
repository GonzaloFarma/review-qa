# Arquitectura de Slides Q1

Definición de arquitectura para la review ejecutiva de QA Q1.

## Enfoque elegido

Se descarta un enfoque centrado en fallas de proveedores. La narrativa se apoya en una lógica más ejecutiva:

- `Slide 1`: mostrar cómo QA sostuvo el flujo de cambios del trimestre.
- `Slide 2`: mostrar qué riesgo detectó y contuvo QA antes de impactar al cliente.

Esto permite hablar de calidad en lenguaje de negocio: continuidad operativa, prevención, cobertura y control del riesgo.

## Slide 1

### Pregunta que responde

`¿Dónde estuvo el esfuerzo de QA y qué tan bien acompañó la salida de cambios del trimestre?`

### Mensaje principal

QA operó sobre un trimestre con más volumen en marzo, manteniendo el foco en acompañamiento a implementación y con cobertura distribuida entre marcas y formatos.

### Estructura

1. Hero statement
2. Métricas resumen
3. Evolución de carga por sprint
4. Cobertura por formato
5. Lecturas ejecutivas

### Hero statement sugerido

`QA sostuvo la salida de cambios del trimestre sin convertir el cierre en una dinámica puramente reactiva a bugs.`

### Métricas resumen

- Incidencias acompañadas en Q1: `132`
- Mejoras: `97` (`73.5%`)
- Cierres dentro de Q1: `70`
- Incidencias con arrastre entre sprints: `35`

### Visual principal

Comparativa por sprint con foco en:

- Volumen total
- Mix mejoras vs bugs
- Cierres por sprint

### Visual secundario

Cobertura por formato:

- Farmacity: `39`
- The Food Market: `26`
- Get The Look: `25`
- Cross: `24`
- Simplicity: `18`

### Lecturas ejecutivas

- Marzo tuvo el mayor volumen del trimestre.
- El trabajo estuvo dominado por mejoras, no por gestión reactiva de bugs.
- QA acompañó múltiples frentes al mismo tiempo, no una sola marca.

## Slide 2

### Pregunta que responde

`¿Qué nivel de riesgo detectó QA y cuánto logró contener antes de que impactara al cliente?`

### Mensaje principal

El riesgo existió y fue material, pero QA absorbió la mayor parte antes de que escalara a experiencia visible en producción.

### Estructura

1. Hero statement
2. Métricas resumen de riesgo
3. Bugs por sprint
4. Prioridad como proxy de criticidad
5. Casos de negocio destacados
6. Nota metodológica breve

### Hero statement sugerido

`Casi la mitad de los bugs del trimestre fueron de prioridad alta o crítica, y la mayoría se detectó antes de quedar explícitamente marcada como incidencia de producción.`

### Métricas resumen

- Bugs Q1: `35`
- Bugs `High` + `Highest`: `17`
- Bugs marcados como `PROD` o `Producción` en el resumen: `5`
- Bugs inferidos como contenidos antes de producción: `30`

### Visual principal

Comparativa por sprint con doble lectura:

- Bugs en radar del sprint
- Bugs cerrados dentro del sprint

### Visual secundario

Distribución por prioridad:

- Highest: `7`
- High: `10`
- Medium: `17`
- Low: `1`

Complemento por formato:

- Farmacity: `15`
- The Food Market: `9`
- Simplicity: `8`
- Get The Look: `3`

### Casos sugeridos

- Minicart con costo de envío incorrecto en Farmacity
- Regionalización inconsistente en Simplicity
- Stock desactualizado al iniciar sesión en Farmacity
- Imposibilidad de inicio de sesión en The Food Market

### Nota metodológica

No presentar `bugs evitados` como métrica exacta. Presentarlo como señal preliminar de contención basada en el naming actual del Jira export.

## Qué conviene evitar

- No hacer del slide una denuncia contra VTEX o Infracommerce.
- No usar IDs de Jira en la UI.
- No hablar de criticidad como si fuera un campo exacto cuando hoy se está usando `Prioridad` como proxy.
- No saturar con tablas.
