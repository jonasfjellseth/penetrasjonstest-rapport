# 🛡️ Penetrasjonstest Rapport 

## 📌 Formål
Dette prosjektet dokumenterer en pentest av nettbutikken **Boris Lockpicks**, gjennomført av fiktive bedriften **Black-Box Security**.  
Målet med pentesten var å simulere et realistisk angrep basert på metodene en ondsinnet aktør kunne brukt, identifisere sårbarheter i systemet, og gi anbefalinger for forbedringer.  

---

## 🔍 Innhold
Rapporten dekker:
- **Scope**: White-box test av webapplikasjon og tilknyttede tjenester  
- **Metodikk**: Basert på OWASP Web Security Testing Guide (WSTG)  
- **Sårbarhetsoversikt**: Klassifisert i Kritisk, Høy, Medium, Lav og Informativ  
- **Anbefalinger**: Tiltak for å styrke sikkerhet, oppdatere systemer, forbedre kode og sikre tilgangskontroll  

---

## 🛠️ Verktøy brukt
- **Nettverks- og sårbarhetsskanning**: Nmap, Nikto, Nessus, OWASP ZAP  
- **Utnyttelse**: Metasploit, Sqlmap  
- **Hash-cracking**: Hashcat  
- **Statisk kodeanalyse**: Snyk  
- **Egne scripts**: Python (Base64 fuzzing og dekoding)  

---

## 📊 Viktigste funn
- **Kritisk risiko**: Eksfiltrering av bruker-, admin- og systemdata, uautoriserte admin-logins, ukryptert trafikk  
- **Høy risiko**: SQL injection, XSS (stored & reflected), privilege escalation, session hijacking, path traversal, utdatert programvare  
- **Medium risiko**: Manglende anti-CSRF tokens, svake autentiseringsmetoder, usikrede SMB-data  
- **Lav risiko**: Cookies uten Secure/HttpOnly/SameSite, manglende sikkerhetsheadere  
- **Informativt**: TLS-versjon, forespørselsdetaljer  

---

## 📑 Repo-struktur
```bash
penetrasjonstest-rapport/
│── README.md
│── LICENSE
│── rapport/
│   └── Teknisk_Sikkerhetsrevisjon.pdf   # Full rapport med detaljer og bilder
│── scripts/
│   ├── base64_encode.py
│   └── base64_decode.py

---

## ⚠️ Disclaimer

Dette prosjektet ble gjennomført i et lukket testmiljø og inneholder kun dokumentasjon for lærings- og porteføljeformål.
Innholdet skal ikke benyttes til uautorisert aktivitet.
