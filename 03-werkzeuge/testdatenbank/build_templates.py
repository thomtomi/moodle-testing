#!/usr/bin/env python3
"""Portable Moodle-Datenbankvorlagen; keine JavaScript-Abhängigkeit."""
import html
import json
from pathlib import Path
import markdown

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / '02-produkte/testdatenbank-5.2'
SRC = Path(__file__).resolve().parent
spec = json.loads((OUT/'datenbank.json').read_text())
fields = {f['name']:f for f in spec['fields']}
def tok(key):
    return '[['+fields[key]['label']+']]'
def formfield(key, wide=False):
    f=fields[key]
    req=' <span class="st-required" aria-label="Pflichtfeld">*</span>' if f['required'] else ''
    hint=f'<p class="st-hint">{html.escape(f["description"])}</p>' if f['description']!=f['label'] else ''
    return f'<div class="st-field {"st-wide" if wide else ""}"><div class="st-label">{html.escape(f["label"])}{req}</div>{hint}<div class="st-input">{tok(key)}</div></div>'
def group(num,title,hint,keys):
    return f'<fieldset class="st-panel"><legend><span class="st-step">{num}</span>{title}</legend><p class="st-muted">{hint}</p><div class="st-grid">'+''.join(formfield(k,k in ['titel','bereich','schritte','soll','ist','hindernis','verlauf','umgebung']) for k in keys)+'</div></fieldset>'

hero='<div class="st-hero"><p class="st-eyebrow">STRICKHOF · MOODLE 5.2</p><h2>Testprotokoll</h2><p>Prüfen. Festhalten. Gemeinsam abschliessen.</p><div class="st-context"><span>Tests: <a href="https://moodlestaging.strickhof.ch">Staging öffnen</a></span><span>Protokolle: moodle.strickhof.ch</span></div></div>'
add='<div class="st-db st-form">'+hero+'<div class="st-note">Ein Eintrag = ein Vorgang, eine Person, ein Browser und ein Durchlauf. Felder mit * sind zum Speichern nötig. Datum und Teststand erst bei der Durchführung ergänzen.</div>'
add+=group('01','Test zuordnen','Vorgang und Zuständigkeit festlegen.', ['testfall_id','titel','bereich','pruefumfang','person','rolle','browser','umgebung','teststand','testdatum','kurslink','bezug'])
add+=group('02','Durchführen und dokumentieren','Schritte und erwartetes Ergebnis sind vorbereitet. Nach dem Test die Beobachtung und das Ergebnis ergänzen.', ['schritte','soll','ist','ergebnis'])
add+='<details class="st-details" open><summary>03 · Problemdetails – bei Fehlern oder blockierten Tests</summary><div class="st-details-body"><p class="st-muted">Bei erfolgreichen Tests können diese Angaben leer bleiben. Kritische Probleme umgehend an Thomas melden.</p><div class="st-grid">'+''.join(formfield(k,k=='hindernis') for k in ['schweregrad','wiederholbarkeit','screenshot','anhang','hindernis'])+'</div></div></details>'
add+='<details class="st-details" open><summary>04 · Koordination und Nachverfolgung</summary><div class="st-details-body"><p class="st-muted">Neue Fehler auf «Neu» setzen. Thomas ergänzt Ticket, Zuständigkeit und Entscheid. Bei offenen Planfällen ist «Nicht nötig» noch keine Freigabe.</p><div class="st-grid">'+''.join(formfield(k,k=='verlauf') for k in ['bearbeitung','zustaendig','termin','ticket','ticketlink','verlauf'])+'</div></div></details></div>'

header='<div class="st-db">'+hero+'<div class="st-toolbar"><div><h3>Gemeinsame Testübersicht</h3><p class="st-muted">Zum Start sind 48 Testfälle vorbereitet. Für Person, Browser, Ergebnis und Bereich die erweiterte Suche verwenden.</p></div><span class="st-stamp">1 Zeile = 1 Durchlauf</span></div><div class="st-table-wrap"><table class="st-table"><caption class="visually-hidden">Testfälle mit Zuständigkeit, Ergebnis und nächstem Schritt</caption><thead><tr><th scope="col">Testfall</th><th scope="col">Zuteilung</th><th scope="col">Umgebung</th><th scope="col">Ergebnis</th><th scope="col">Bearbeitung</th><th scope="col">Aktionen</th></tr></thead><tbody>'
row='<tr><td><span class="st-code">'+tok('testfall_id')+'</span><a class="st-title" href="##moreurl##">'+tok('titel')+'</a><div class="st-small">'+tok('bereich')+'</div><div class="st-small">'+tok('pruefumfang')+'</div></td><td>'+tok('person')+'<div class="st-small">'+tok('rolle')+'</div></td><td>'+tok('browser')+'<div class="st-small">'+tok('teststand')+'</div></td><td><span class="st-pill" data-state="'+tok('ergebnis')+'">'+tok('ergebnis')+'</span><div class="st-small">'+tok('schweregrad')+'</div></td><td>'+tok('bearbeitung')+'<div class="st-small">'+tok('zustaendig')+'</div><div class="st-small">'+tok('termin')+'</div></td><td class="st-actions">##actionsmenu##</td></tr>'
footer='</tbody></table></div><p class="st-footnote">«Noch offen» und «Blockiert» zählen nicht als bestanden. Ein Nachtest erhält einen eigenen Eintrag; das ursprüngliche Ergebnis bleibt erhalten.</p></div>'

def detail(key):
    return '<div class="st-detail"><dt>'+html.escape(fields[key]['label'])+'</dt><dd>'+tok(key)+'</dd></div>'
def section(title, keys):
    return '<section class="st-panel"><h3>'+title+'</h3><dl class="st-grid">'+''.join(detail(k) for k in keys)+'</dl></section>'
single='<article class="st-db"><div class="st-hero"><div class="st-topline"><span class="st-eyebrow">'+tok('testfall_id')+' · TESTPROTOKOLL</span><div>##actionsmenu##</div></div><h2>'+tok('titel')+'</h2><p>'+tok('bereich')+'</p><div class="st-statusline"><span class="st-pill" data-state="'+tok('ergebnis')+'">'+tok('ergebnis')+'</span><span>'+tok('bearbeitung')+'</span></div></div>'
single+=section('Rahmen und Zuständigkeit',['person','rolle','browser','umgebung','teststand','testdatum','pruefumfang','kurslink','bezug'])
for key,title in [('schritte','01 · Voraussetzungen und Schritte'),('soll','02 · Erwartetes Ergebnis'),('ist','03 · Beobachtung')]:
    single+='<section class="st-panel st-prose"><h3>'+title+'</h3><div class="st-result-text">'+tok(key)+'</div></section>'
single+=section('Problemdetails',['schweregrad','wiederholbarkeit','screenshot','anhang','hindernis'])
single+=section('Nachverfolgung',['bearbeitung','zustaendig','termin','ticket','ticketlink','verlauf'])
single+='<div class="st-meta">Erfasst von ##user## · Angelegt: ##timeadded## · Geändert: ##timemodified##</div><div class="st-comments">##comments##</div></article>'

search='<div class="st-db"><div class="st-search-heading"><p class="st-eyebrow">GEZIELT FINDEN</p><h3>Testfälle eingrenzen</h3><p class="st-muted">Leere Suchfelder schränken das Ergebnis nicht ein. Mehrere Angaben werden kombiniert.</p></div><div class="st-grid">'+''.join('<div class="st-field"><div class="st-label">'+html.escape(fields[k]['label'])+'</div>'+tok(k)+'</div>' for k in ['testfall_id','titel','bereich','pruefumfang','person','browser','teststand','ergebnis','schweregrad','bearbeitung'])+'</div></div>'

intro_source=(ROOT/'02-produkte/anleitung-testdatenbank.md').read_text().split('---',2)[2].strip()
intro_source=intro_source.replace('# Moodle-Testing 5.2\n','',1)
intro=('<div style="border-left:5px solid #28756a;padding:18px 22px;background:#f1f7f5;border-radius:8px;margin-bottom:18px">'
       '<p style="margin:0 0 6px;color:#34645c;font-size:12px;font-weight:700;letter-spacing:.08em">STRICKHOF · MOODLE 5.2</p>'
       '<h3 style="margin:0 0 10px;color:#193e38">Gemeinsam sicher durch die Migration</h3>'
       '<p style="margin:0">Teste auf <a href="https://moodlestaging.strickhof.ch">moodlestaging.strickhof.ch</a> und halte hier Deine Ergebnisse fest. '
       'Die Protokolle liegen auf <a href="https://moodle.strickhof.ch">moodle.strickhof.ch</a>.</p></div>'
       '<details><summary><strong>Anleitung, Umgebung und Dokumentation öffnen</strong></summary><div style="padding:16px 0">'
       +markdown.markdown(intro_source,extensions=['tables'])+'</div></details>')

templates=dict(addtemplate=add,listtemplateheader=header,listtemplate=row,listtemplatefooter=footer,
               singletemplate=single,asearchtemplate=search,
               csstemplate=(SRC/'style.css').read_text(),jstemplate='',
               rsstemplate='',rsstitletemplate='',intro=intro)
for name,content in templates.items():
    ext='css' if name=='csstemplate' else 'js' if name=='jstemplate' else 'html'
    (OUT/(name+'.'+ext)).write_text(content+'\n')
(OUT/'vorlagen.json').write_text(json.dumps(templates,ensure_ascii=False,indent=2)+'\n')
print('Eingabe-, Listen-, Einzel- und Suchvorlage sowie Anleitung erzeugt.')
