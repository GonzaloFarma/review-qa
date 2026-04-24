#!/usr/bin/env python3

import csv
import re
from collections import Counter
from datetime import datetime
from statistics import median


CSV_PATH = "docs/jira-cvs/Jira (Q1).csv"
SPRINT_COLS = range(136, 146)
Q1_WINDOWS = {
    "Sprint 1": (datetime(2026, 1, 6), datetime(2026, 1, 28, 23, 59, 59)),
    "Sprint 2": (datetime(2026, 1, 29), datetime(2026, 2, 18, 23, 59, 59)),
    "Sprint 3": (datetime(2026, 2, 19), datetime(2026, 3, 11, 23, 59, 59)),
}
MONTH_MAP = {
    "ene": 1,
    "feb": 2,
    "mar": 3,
    "abr": 4,
    "may": 5,
    "jun": 6,
    "jul": 7,
    "ago": 8,
    "sep": 9,
    "oct": 10,
    "nov": 11,
    "dic": 12,
}
PROD_RE = re.compile(r"\bprod\b|producci[oó]n", re.I)


def parse_date(value):
    value = (value or "").strip()
    if not value:
        return None

    match = re.match(r"(\d{2})/([a-z]{3})/(\d{2})\s+(\d{1,2}):(\d{2})\s+(AM|PM)", value, re.I)
    if not match:
        return None

    day, month, year, hour, minute, meridian = match.groups()
    hour = int(hour) % 12 + (12 if meridian.upper() == "PM" else 0)
    return datetime(2000 + int(year), MONTH_MAP[month.lower()], int(day), hour, int(minute))


def load_records():
    with open(CSV_PATH, newline="", encoding="utf-8-sig") as handle:
        reader = csv.reader(handle)
        header = next(reader)
        rows = list(reader)

    idx = {name: i for i, name in enumerate(header)}

    def get_value(row, name):
        position = idx[name]
        return row[position].strip() if position < len(row) else ""

    records = []
    for row in rows:
        sprints = []
        for col in SPRINT_COLS:
            if col < len(row):
                value = row[col].strip()
                if value and value not in sprints:
                    sprints.append(value)

        records.append(
            {
                "key": get_value(row, "Clave de incidencia"),
                "summary": get_value(row, "Resumen"),
                "type": get_value(row, "Tipo de Incidencia"),
                "status": get_value(row, "Estado"),
                "priority": get_value(row, "Prioridad"),
                "format": get_value(row, "Campo personalizado (Formato)"),
                "qa_est": get_value(row, "Campo personalizado (Estimación QA)"),
                "assignee": get_value(row, "Persona asignada"),
                "time_worked": int(get_value(row, "Tiempo Trabajado") or "0"),
                "created": parse_date(get_value(row, "Creada")),
                "resolved": parse_date(get_value(row, "Resuelta")),
                "sprints": sprints,
                "q1_sprints": [s for s in sprints if s in Q1_WINDOWS],
            }
        )

    return records


def format_counter(counter):
    return ", ".join(f"{key}: {value}" for key, value in counter.items())


def format_hours(total_seconds):
    return round(total_seconds / 3600, 1)


def main():
    records = load_records()
    q1_records = [record for record in records if record["q1_sprints"]]
    improvements = [record for record in q1_records if record["type"] == "Mejora"]
    bugs = [record for record in q1_records if record["type"] == "Error"]
    prod_bugs = [record for record in bugs if PROD_RE.search(record["summary"])]
    contained_bugs = [record for record in bugs if not PROD_RE.search(record["summary"])]
    improvement_high = [
        record for record in improvements if record["priority"] in {"High", "Highest"}
    ]
    improvement_logged = [
        record for record in improvements if record["time_worked"] > 0
    ]
    bug_logged = [record for record in bugs if record["time_worked"] > 0]

    print("Q1 baseline")
    print(f"- Total incidencias Q1: {len(q1_records)}")
    print(f"- Mejoras: {len(improvements)}")
    print(f"- Bugs: {len(bugs)}")
    print(f"- Bugs con etiqueta de produccion en el resumen: {len(prod_bugs)}")
    print(f"- Bugs contenidos antes de produccion por inferencia de naming: {len(contained_bugs)}")
    print(f"- Incidencias con arrastre entre mas de un sprint Q1: {sum(len(r['q1_sprints']) > 1 for r in q1_records)}")
    print()

    print("KPIs delivery")
    print(f"- Mejoras high + highest: {len(improvement_high)}")
    print(
        f"- Horas registradas en mejoras: {format_hours(sum(r['time_worked'] for r in improvement_logged))} "
        f"(tickets con carga: {len(improvement_logged)})"
    )
    print(
        "- Mejoras cerradas dentro del corte Q1: "
        f"{sum(1 for r in improvements if r['resolved'] and any(start <= r['resolved'] <= end for start, end in Q1_WINDOWS.values()))}"
    )
    print(
        f"- Mejoras con arrastre entre sprints Q1: {sum(len(r['q1_sprints']) > 1 for r in improvements)}"
    )
    print()

    print("Carga por sprint")
    for sprint in Q1_WINDOWS:
        subset = [record for record in q1_records if sprint in record["q1_sprints"]]
        bug_count = sum(record["type"] == "Error" for record in subset)
        print(
            f"- {sprint}: total={len(subset)} bugs={bug_count} mejoras={len(subset) - bug_count} "
            f"formatos=[{format_counter(Counter(record['format'] for record in subset))}]"
        )
    print()

    print("Cierres por sprint")
    for sprint, (start, end) in Q1_WINDOWS.items():
        subset = [record for record in records if record["resolved"] and start <= record["resolved"] <= end]
        bug_count = sum(record["type"] == "Error" for record in subset)
        print(f"- {sprint}: cerradas={len(subset)} bugs={bug_count} mejoras={len(subset) - bug_count}")
    print()

    print("KPIs riesgo")
    cycle_times = [
        (record["resolved"] - record["created"]).total_seconds() / 86400
        for record in bugs
        if record["created"]
        and record["resolved"]
        and any(start <= record["resolved"] <= end for start, end in Q1_WINDOWS.values())
    ]
    print(
        f"- Tiempo de resolucion mediano de bugs cerrados en Q1 (dias): {round(median(cycle_times), 1) if cycle_times else 'n/d'}"
    )
    print(
        f"- Horas registradas en bugs: {format_hours(sum(r['time_worked'] for r in bug_logged))} "
        f"(tickets con carga: {len(bug_logged)})"
    )
    print(
        f"- Bugs high + highest: {sum(record['priority'] in {'High', 'Highest'} for record in bugs)}"
    )
    print()

    print("Bugs por prioridad")
    print(f"- {format_counter(Counter(record['priority'] for record in bugs))}")
    print()

    print("Bugs por formato")
    print(f"- {format_counter(Counter(record['format'] for record in bugs))}")
    print()

    print("Bugs etiquetados como produccion")
    for record in prod_bugs:
        print(f"- {record['key']} | {record['priority']} | {record['format']} | {record['summary']}")


if __name__ == "__main__":
    main()
