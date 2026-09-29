---
title: "Bisheriger Testablauf – Quellmaterial"
author: lamt
date: 2026-09-29
---

# Bisheriger Testablauf (Quellmaterial)

Dieses Dokument enthält den bisherigen, von Thomas verfassten Testablauf sowie die bestehende Checkliste unverändert als Rohmaterial. Es dient als Referenz für die Weiterentwicklung des Testprozederes, nicht als bereits finale Fassung.

## Ablauf des Testings – Dezember 2025 bis Februar 2026

Vielen Dank bereits jetzt für eure Unterstützung beim Testen. Unten findet ihr den gesamten Ablauf in übersichtlichen Schritten.

### Vor dem Testen

1. **Plugins vorschlagen (bis 15.12.2025)**
   Postet eure Plugin-Vorschläge im «Manager-Treff» unter:
   «[Moodle-Plugin 2526] 🧩 Start des Plugin-Prozesses für das Moodle-Upgrade 2025/26».
   Bitte ergänzt eine kurze Beschreibung oder ein typisches Einsatzszenario.

2. **Inspiration holen**
   Wenn du weitere Moodle-Plugins in Aktion sehen möchtest, findest du im Moodle des MBA viele Kurse, in denen verschiedene Plugins eingesetzt werden. Du kannst sie dort auch selbst ausprobieren – beantrage einfach einen eigenen Kurs. Falls du noch keinen Zugang hast, schreib mir kurz.

3. **Abstimmung (bis 19.12.2025)**
   Bitte nimm an beiden Abstimmungen teil:
   – Welche neuen Plugins wollen wir testen?
   – Welche Plugins werden nicht mehr verwendet?

4. **Einverständnis (bis 19.12.2025)**
   Bitte bestätige kurz im gleichen Thread:
   «Ich bin einverstanden» oder «Ich bin nicht einverstanden».
   Erst danach kann Marc die Plugins auf testmoodle2.strickhof.ch installieren.

5. **Browserwahl**
   Damit wir möglichst alle Browser-Engines abdecken, fülle bitte die Abstimmung «Welchen Browser nutzt du?» aus.

### Start der Testphase (ab 05.01.2026)

1. **Testing starten**
   Sobald alle Plugin-Anpassungen erfolgt sind, starten wir offiziell mit dem Testen. Das Vorgehen findest du im Abschnitt «Vorgehen beim Testen».

2. **Was funktioniert?**
   Bitte markiere alle Aktivitäten, die einwandfrei funktionieren, in den Checklisten «Wahl der funktionierenden Moodle-Aktivitäten» und «Checkliste | Moodle-Grundfunktionen».

3. **Wenn etwas nicht funktioniert**
   Erstelle bitte einen Beitrag im «Manager-Treff» unter:
   «⬆️ Moodle Upgrade auf 5.1»
   und notiere:
   – welches Plugin / welche Aktivität betroffen ist
   – mit welchem Browser du getestet hast
   – wie du vorgegangen bist
   – ggf. Fehlermeldung oder Screenshot
   Nach deiner Meldung eröffne ich ein Ticket bei der Informatik.

4. **Testing abschliessen (bis Ende Januar 2026)**
   Bitte schliesst eure Tests bis Ende Januar ab. Mitte Januar erinnere ich nochmals daran.

5. **Zustimmung zum Upgrade (KW 6)**
   Nach Abschluss des Testings benötige ich euer «Go». Bitte postet im Thread «⬆️ Moodle Upgrade auf 5.1»:
   «Ich bin einverstanden mit einem Upgrade auf 5.1» oder «Ich bin nicht einverstanden mit einem Upgrade auf 5.1».
   Bei Zustimmung gehe ich davon aus, dass für euch keine kritischen Probleme mehr bestehen. Anschliessend schlägt Marc einen Termin für das Upgrade vor und kommuniziert ihn im «Manager-Treff».

### Am Tag des Upgrades

- Falls am Tag des Upgrades Probleme auftreten, meldet dies bitte sofort im «Manager-Treff».

## Bestehende Checkliste «Checkliste | Moodle-Grundfunktionen»

- Kreuze unter «Welchen Browser nutzt Du?» an, welchen Browser du verwendest.
- Überprüfung der Benutzerprofile, um sicherzustellen, dass alle Benutzerdaten korrekt angezeigt werden.
- Erstelle einen neuen Kurs und überprüfe, ob alle Kursverwaltungsfunktionen wie Hinzufügen/Entfernen von Teilnehmern und Blöcken einwandfrei funktionieren.
- Bearbeite einen bestehenden Kurs (wenn möglich einen eigenen Kurs) und überprüfe, ob alle Inhalte und Aktivitäten intakt sind.
- Probiere folgende Funktionen aus:
  - Rollenwechsel
  - Nutzer/innen erfassen in Kurse (Einschreibemethoden)
  - Block erstellen
  - Berichte (Logs werden angezeigt und können gefiltert werden)
  - Badge kann angelegt werden und an Kriterien gebunden werden
  - Fragesammlung ist editierbar
  - Lade verschiedene Arten von Dateien (z. B. Dokumente, Bilder, Videos) in Kursmaterialien hoch und überprüfe, ob sie korrekt angezeigt werden.
- Prüfe mindestens 5 Plugins und markiere diese in der Liste «Wahl der funktionierenden Moodle-Aktivitäten». Achte darauf, wenn möglich Plugins zu wählen, die noch nicht getestet wurden.
- Teste die Messaging-Funktionen.
- Erstelle einen Forumseintrag im Manager-Treff.

## Offene Punkte (aus Sicht der Weiterentwicklung)

- Aktuell sind Ablauftext, Checkliste und Plugin-Liste «Wahl der funktionierenden Moodle-Aktivitäten» separate Moodle-Elemente. Ziel ist eine konsolidierte, robustere Lösung (vgl. `moodle-aktivitaetstypen.md`).
- Es ist noch nicht festgelegt, wie ein einzelner Bug-Report strukturiert im System erfasst wird (bisher Freitext-Forenbeitrag).
