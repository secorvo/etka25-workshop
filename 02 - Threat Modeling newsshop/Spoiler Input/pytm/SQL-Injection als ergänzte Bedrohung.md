```json
  {
    "SID": "KJINP07",
    "target": [ "Server", "Process", "Datastore", "Dataflow" ],
    "description": "SQL Injection",
    "details": "Unvalidierte Eingaben werden in SQL-Anweisungen eingefügt. Angreifer:innen können Daten lesen, ändern oder Befehle ausführen.",
    "Likelihood Of Attack": "High",
    "severity": "Very High",
    "condition": "target.controls.validatesInput is False or target.controls.usesParameterizedQueries is False",
    "prerequisites": "Die Anwendung setzt Benutzer:innen-Eingaben direkt in SQL-Statements ein, ohne Parametrisierung oder strikte Validierung.",
    "mitigations": "Verwenden Sie parametrisierte Abfragen oder Stored Procedures. Validieren und filtern Sie sämtliche Eingaben. Nutzen Sie least-privilege-Konten auf der Datenbank.",
    "example": "SELECT &ast; FROM users WHERE name = 'admin' --';",
    "references": "https://owasp.org/www-community/attacks&sol;SQL_Injection, CWE-89"
  }

```