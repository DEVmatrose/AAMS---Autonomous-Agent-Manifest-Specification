# WORKPAPER — Fix: LTM Python-Interpreter-Ambiguität

**Session:** 2026-02-23
**Status:** OPEN
**Typ:** Bugfix / Live-Process-Issue

---

## Problem (im Liveprozess festgestellt)

READ-AGENT.md enthielt keine expliziten Python-Befehle für LTM-Operationen.  
Resultat: Agent wählte eigenständig einen Python-Interpreter — in einer Session, in der zuletzt `wsl -e python3` für andere Zwecke verwendet worden war, führte der Agent die LTM-Befehle ebenfalls unter WSL-Python aus.

### Symptomkette
1. Agent interpretiert "Query LTM" als generischen Python-Aufruf
2. Letzter aktiver Python-Kontext in der Session: WSL (`wsl -e python3`)
3. WSL-Python hat `chromadb` nicht installiert
4. Fehler → Agent will `pip install chromadb` in WSL-Environment ausführen
5. Falsches Environment wird modifiziert, LTM-Query schlägt fehl

### Root Cause
READ-AGENT.md spezifizierte LTM-Aktionen ("Query WORKING/MEMORY/", "Ingest workpaper") ohne konkreten Befehl — kein Interpreter, kein Pfad, keine Warnung.

---

## Lösung

### Änderung 1 — READ-AGENT.md: neuer Block "LTM Commands"

**Eingefügt nach:** Tabelle "Mandatory LTM triggers"

**Inhalt (Nachher):**
```powershell
# Query (Sessionstart):
.venv\Scripts\python.exe WORKING\AGENT-MEMORY\query.py "<Session-Thema>"

# Ingest (Sessionende):
.venv\Scripts\python.exe WORKING\AGENT-MEMORY\ingest.py
```

Dazu explizite Warnung: NICHT `wsl python3`, `python`, oder System-Python.  
Begründung: Nur das Workspace-`.venv` hat `chromadb` + `sentence-transformers` installiert.

### Warum kein Quick-Start-Block nötig war
READ-AGENT.md hatte bisher keinen separaten Quick-Start-Block mit python-Befehlen — der Fehler lag darin, dass keine Befehle existierten. Die Lösung ist ein neuer, eigenständiger Befehle-Block direkt bei den LTM-Triggers.

---

## File Protocol

| Action | File | Detail |
|---|---|---|
| EDIT | `READ-AGENT.md` | LTM Commands Block nach Triggers-Tabelle eingefügt |

---

## Principle (abgeleitet)

> **Ambiguität in Werkzeug-Aufrufen ist ein Agentenfehler-Multiplikator.**  
> Jeder Befehl der Agenten ausführen sollen muss: vollständigen Pfad, expliziten Interpreter, und eine negative Abgrenzung ("NICHT x") enthalten — besonders wenn der falsche Weg plausibel erscheint.

---

## Next Steps

- [ ] Commit + Push dieser Änderung
- [ ] Prüfen: Gibt es andere Stellen in READ-AGENT.md oder SPEC.md wo Python-Befehle ohne `.venv`-Pfad stehen?
- [ ] Workpaper schließen + LTM ingesten
