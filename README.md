# review-qa

Workspace para construir y versionar slides ejecutivos de QA orientados a las reviews trimestrales del equipo e-commerce de Farmacity Group.

## Objetivo

El repositorio busca transformar datos operativos de QA en material visual breve, claro y defendible frente a owners, sponsors y stakeholders no técnicos. El foco no es mostrar solo volumen de bugs, sino explicar qué protegió QA, qué riesgos se contuvieron y dónde hay oportunidades reales de mejora.

## Fuente de verdad actual

- Contexto del proyecto: `docs/contexto/qa_review_context.md`
- Dataset principal: `docs/jira-cvs/Jira (Q1).csv`
- Dataset complementario de capacidad: `docs/jira-cvs/Capacity (sprint 3).csv`
- Referencias visuales reutilizables: `docs/ejemplos-html/`

## Estado actual

- `slider-01.html` y `slider-02.html` quedaron de un proyecto anterior.
- Ambos archivos se conservan como base reutilizable para definir la maqueta final de las slides Q1.
- El trabajo se va a ordenar por fases, empezando por contexto, narrativa, criterios de medición y luego refinamiento visual.

## Forma de trabajo

- Se trabaja desde terminal WSL en la raíz del repositorio.
- Cada sesión puede ajustar el contexto y ese aprendizaje debe reflejarse en `AGENTS.md`.
- Las slides deben mantenerse en lenguaje de negocio, con lectura rápida y sin sobrecarga técnica.
- Los HTML se validan localmente con Playwright CLI cuando haya cambios visuales.

## Comandos útiles

```bash
rg --files
cat docs/contexto/qa_review_context.md
npm run pw:chrome
```

## Criterio de presentación

La presentación final debe ayudar a posicionar mejor al equipo de QA mostrando impacto, prevención y gobernanza de calidad sobre la operación e-commerce, sin convertir la review en una lista de fallas de proveedores o plataformas.
