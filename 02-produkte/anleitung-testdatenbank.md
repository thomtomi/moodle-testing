---
title: "Anleitung – Moodle-Testing 5.2"
author: lamt
date: 2026-09-29
status: Entwurf für die Aktivitätsbeschreibung
---

# Moodle-Testing 5.2

Mit dieser Datenbank dokumentieren wir gemeinsam die Tests der Moodle-Migration. Halte fest, welchen Vorgang Du geprüft hast, welches Ergebnis Du erwartest und was tatsächlich passiert ist. Dokumentiere auch erfolgreiche Tests.

Die Testprotokolle führen wir auf [moodle.strickhof.ch](https://moodle.strickhof.ch). Die eigentlichen Tests führst Du in Deinen dafür vorgesehenen Testkursen auf [moodlestaging.strickhof.ch](https://moodlestaging.strickhof.ch) durch. Dadurch bleiben die Protokolle beim Erneuern der Testinstanz erhalten.

**Umgebung und Instanzen**

| Angabe | Wert |
| --- | --- |
| Moodle SaaS | 3000 |
| Speicherplatz / Disc quota | 800 GB |
| Moodle-Version für das Vorhaben | 5.2 |
| TEST-Migration Domain | [moodlestaging.strickhof.ch](https://moodlestaging.strickhof.ch) |
| PROD-Migration: Production instance, bestehend | [moodle.strickhof.ch](https://moodle.strickhof.ch) |
| PROD-Migration: Staging instance | [moodlestaging.strickhof.ch](https://moodlestaging.strickhof.ch) |

**Dokumentation**

- [TEST-Instanz: TODOs / Tasks](https://track.liip.ch/projects/STR/articles/STR-A-3/TEST-Instanz-TODOs-Tasks)
- [Check-Liste (DE) Inhalt, Look+Feel, Konsistenz](https://track.liip.ch/projects/STR/articles/STR-A-2/Check-Liste-DE-Inhalt-LookFeel-Konsistenz)

**Vor dem Testen**

1. Öffne die Liste der vorbereiteten Testfälle und prüfe Deine Zuteilung. Noch nicht durchgeführte Tests tragen das Ergebnis «Noch offen».
2. Prüfe, welchen Browser, welche Rolle und welche Testmaterialien Du für den Vorgang brauchst. Für Abgaben, Buchungen, Bewertungen und Sichtbarkeit verwendest Du ein eingeschriebenes Lernenden-Testkonto.
3. Kontrolliere vor dem Start die Adresse: Die zu testende Aktivität muss auf `moodlestaging.strickhof.ch` liegen.
4. Verwende die vereinbarte Teststand-Kennung. Nach einer bereitgestellten Korrektur wird ein neuer Teststand festgehalten, damit sich Ergebnisse zuordnen lassen.

Testbeginn, Rückmeldefrist und die Verteilung auf Personen und Browser werden vor dem Start von Thomas ergänzt.

**Einen Test dokumentieren**

Ein Eintrag steht für einen konkreten Testfall, eine testende Person, einen Browser mit Gerät und einen Durchlauf. Beispiel: «Eine Datei als Lernende abgeben». Für einen weiteren Browser oder einen Nachtest entsteht ein eigener Eintrag mit derselben Testfall-ID.

1. Öffne den passenden vorbereiteten Eintrag. Ergänze bei Bedarf einen zusätzlichen Testfall mit eindeutigem Kurztitel und stimme die Testfall-ID mit Thomas ab.
2. Führe die beschriebenen Schritte aus. Ergänze Abweichungen und nötige Voraussetzungen, damit der Vorgang wiederholt werden kann.
3. Trage die tatsächlich testende Person, Rolle, Browser-Version, Betriebssystem, Gerät, Teststand und Testdatum ein.
4. Ergänze den direkten Link zur geprüften Stelle auf der Testinstanz.
5. Beschreibe das tatsächliche Ergebnis und wähle den passenden Ergebnisstatus.

| Testergebnis | Wann verwenden? |
| --- | --- |
| Noch offen | Der geplante Test wurde noch nicht durchgeführt. |
| Bestanden | Die Schritte wurden durchgeführt und das erwartete Ergebnis ist eingetreten. |
| Fehler | Das tatsächliche Ergebnis weicht vom erwarteten Ergebnis ab. |
| Blockiert | Eine Voraussetzung fehlt und verhindert die Prüfung. Beschreibe das Hindernis. |
| Entfällt | Der Test wird begründet aus dem Umfang genommen. Thomas bestätigt die Entscheidung. |

Bei einem erfolgreichen Test genügt eine kurze konkrete Beobachtung, etwa «Die abgegebene Datei ist für die Lehrperson sichtbar und lässt sich öffnen».

**Ein Problem melden**

Ergänze bei einem Fehler die genaue Beobachtung und gegebenenfalls den Wortlaut der Fehlermeldung. Halte fest, ob sich das Problem wiederholen lässt und welche Auswirkungen es auf den Unterricht hat. Füge einen hilfreichen Screenshot oder eine Testdatei bei, wenn damit der Fehler verständlicher wird.

- Kritisch: Ein zentraler Vorgang ist unmöglich, wesentliche Daten oder Ergebnisse gehen verloren oder es besteht unzulässiger Zugriff. Informiere Thomas umgehend.
- Erheblich: Eine wichtige Funktion ist beeinträchtigt; eine Übergangslösung ist möglich oder nur ein Teil der Nutzung betroffen.
- Gering: Ein begrenztes Darstellungs- oder Komfortproblem; der Vorgang bleibt korrekt ausführbar.

Setze bei einem neuen Fehler den Bearbeitungsstatus auf «Neu». Thomas klärt die Meldung und ergänzt Zuständigkeit, Ticketverweis und nächsten Schritt. Wenn Du denselben Fehler in einem anderen Test beobachtest, verlinke den bereits vorhandenen Eintrag.

**Korrekturen nachtesten**

Nach Bereitstellung einer Korrektur wird der neue Teststand angegeben und ein Nachtest zugeteilt. Erfasse den Nachtest als eigenen Durchlauf und verlinke den ursprünglichen Eintrag. Das frühere Testergebnis bleibt erhalten. Thomas schliesst die Bearbeitung anhand des dokumentierten Nachtests ab oder hält einen ausdrücklichen Entscheid zum verbleibenden Problem fest.

**Testing abschliessen**

Prüfe vor Deiner abschliessenden Rückmeldung, ob Deine zugeteilten Tests vollständig dokumentiert sind. Weise ausdrücklich auf offene Fehler und blockierte Vorgänge hin. Thomas führt die Rückmeldungen zusammen und dokumentiert den Go/No-Go-Entscheid.
