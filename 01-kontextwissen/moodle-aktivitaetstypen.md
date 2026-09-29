---
title: "Moodle-Aktivitätstypen für Testdokumentation – Referenzwissen"
author: lamt
date: 2026-09-29
---

# Moodle-Aktivitätstypen für Testdokumentation (Referenzwissen)

Kurzer Vergleich möglicher Moodle-Aktivitäten, um das Testprozedere (Testschritte, Bug-Reports, Auswertung) in einer einzigen, robusten Aktivität statt in verstreuten Foren-/Checklisten-Elementen abzubilden. Dies ist Referenzwissen für eine spätere Design-Entscheidung — hier wird noch nichts festgelegt.

## Übersicht

| Aktivität                          | Grundidee                                                                                                                      | Eignung für strukturierte Bug-Reports                                                                                        | Eignung für Checklisten-artiges Abhaken                                                   |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `mod_data` (Datenbank)             | Nutzer:innen füllen Einträge mit frei definierbaren Feldern aus, alle Einträge sind gemeinsam einsehbar/filterbar/exportierbar | hoch – Felder wie Plugin/Aktivität, Browser, Vorgehen, Fehlermeldung, Screenshot, Status frei definierbar                    | mittel – kein natives Abhak-Verhalten, müsste über Felder simuliert werden                |
| `mod_checklist` (Checklist-Plugin) | Vordefinierte Liste von Punkten, die einzelne Nutzer:innen abhaken, optional mit Kommentarfunktion                             | gering – kein strukturiertes Formular für Bug-Details, nur Freitext-Kommentar                                                | hoch – genau dafür gebaut                                                                 |
| `mod_feedback` (Feedback)          | Fragebogen/Umfrage mit anonymer oder personalisierter Auswertung, gut für aggregierte Auswertungen                             | mittel – Formularfelder möglich, aber schwächer filter-/durchsuchbar als `mod_data`, keine laufende Statuspflege pro Eintrag | gering – für Ja/Nein-Fragen nutzbar, aber kein «Fortschritt pro Person» wie bei Checklist |

## Einschätzung

- **`mod_data`** eignet sich am besten, wenn ein einzelner Bug-Report als strukturierter Datensatz erfasst werden soll (Plugin/Aktivität, Browser, Vorgehen, Fehlermeldung, Screenshot-Upload, Status). Einträge sind für alle drei Lehrpersonen und für Thomas einsehbar, filterbar und lassen sich als Grundlage für Tickets an die Informatik nutzen. Nachteil: kein eingebautes Abhak-Verhalten für «habe ich getestet»-Listen, das müsste über ein zusätzliches Statusfeld nachgebildet werden.
- **`mod_checklist`** bleibt gut geeignet für die reine «funktioniert / funktioniert nicht»-Abarbeitung der Grundfunktionen-Liste, liefert aber keine strukturierten Bug-Daten.
- **`mod_feedback`** ist eher für eine abschliessende Auswertung/Stimmungsbild geeignet (z. B. «Go/No-Go»-Abfrage am Ende der Testphase) als für die laufende Bug-Erfassung.

**Vorläufige Tendenz** (nicht final): `mod_data` als zentrale Aktivität für Bug-Reports, ergänzt durch eine einfache Checkliste für die Grundfunktionen und ggf. `mod_feedback` für den abschliessenden Go/No-Go-Entscheid. Die konkrete Feldstruktur und ob eine Kombination oder eine einzelne Aktivität sinnvoller ist, wird in einem eigenen Design-Schritt geklärt.

## Offene Punkte

- Wie granular sollen Felder in `mod_data` sein (z. B. Status-Feld mit fixen Werten wie «offen/gemeldet/behoben»)?
- Soll pro Lehrperson ein eigener Datenbank-Eintrag pro getestetem Plugin entstehen, oder ein Eintrag pro gefundenem Problem?
- Wie wird die bestehende Liste «Wahl der funktionierenden Moodle-Aktivitäten» in die neue Struktur überführt?
