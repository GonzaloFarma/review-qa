# review-qa

Workspace para construir y mantener la secuencia ejecutiva de slides QA orientada a la review trimestral del equipo e-commerce de Farmacity Group.

## Objetivo

El repositorio transforma datos operativos de QA en material visual breve, claro y defendible frente a owners, sponsors y stakeholders no técnicos. El objetivo actual no es rediseñar en cada iteración, sino mantener una estructura estable de slides y actualizar datos, números, labels y casos destacados con el menor costo posible.

## Estado actual

- `slider-01.html` es la slide vigente de delivery, mejoras e innovación.
- `slider-02.html` es la slide vigente de riesgo y bugs.
- `slider-03.html` es la slide vigente de ticketera TeAyudo.
- `slider-q1.html` queda solo como referencia histórica del split que originó `slider-01` y `slider-02`.
- La presentación actual se resuelve como una secuencia horizontal de `3` slides en canvas `1440x840`.

## Fuente de verdad actual

- Contexto del proyecto: `docs/contexto/qa_review_context.md`
- Sistema de mantenimiento: `docs/contexto/slide_maintenance_system.md`
- Baseline de métricas: `docs/contexto/q1_metrics_baseline.md`
- Datos de ticketera TeAyudo: `docs/contexto/teayudo_ticketera_q1.json`
- Trazabilidad de cards e iniciativas agrupadas: `docs/story/q1-data-team.md`
- Dataset principal: `docs/jira-cvs/Jira (Q1).csv`
- Datasets separados: `docs/jira-cvs/Jira-mejoras (Q1).csv` y `docs/jira-cvs/Jira-error (Q1).csv`
- Referencias visuales del equipo: `docs/ejemplos/slider-equipo/`

## Forma de trabajo

- Se trabaja desde terminal WSL en la raíz del repositorio.
- Cada sesión puede ajustar el contexto estable y ese aprendizaje debe reflejarse en `AGENTS.md` y los docs de `docs/contexto/`.
- La estructura de slides debe considerarse estable.
- La regla de mantenimiento actual es: cambiar datos antes que rediseñar bloques.
- Las métricas incompletas deben rotularse como proxy, estimación u horas registradas.

## Comandos útiles

```bash
rg --files
cat docs/contexto/qa_review_context.md
cat docs/contexto/slide_maintenance_system.md
python3 -m http.server 4173 --bind 0.0.0.0
npx playwright screenshot --device='Desktop Chrome HiDPI' --viewport-size=1440,840 http://127.0.0.1:4173/slider-01.html /tmp/slider-01.png
npx playwright screenshot --device='Desktop Chrome HiDPI' --viewport-size=1440,840 http://127.0.0.1:4173/slider-02.html /tmp/slider-02.png
npx playwright screenshot --device='Desktop Chrome HiDPI' --viewport-size=1440,840 http://127.0.0.1:4173/slider-03.html /tmp/slider-03.png
```

## Criterio de presentación

La secuencia final debe ayudar a posicionar mejor al equipo de QA mostrando impacto, prevención y gobernanza de calidad sobre la operación e-commerce, sin convertir la review en una lista de fallas ni en un espejo de Jira.
