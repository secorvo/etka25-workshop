# Workshop #ETKA25 "Secure Software Engineering"

In diesem Repository sind Übungen und Lösungsideen für den Workshop "Secure Software Engineering" auf dem Entwicklertag Karlsruhe 2025 (#ETKA) hinterlegt.

Wir wünschen viel Erfolg und vor allem viel Spaß!

## Zeitplan

| Zeit          | Thema                                    |
|:--------------|:-----------------------------------------|
| 09:00 - 09:45 | Vorstellung: Warum ist Security wichtig? |
| 09:45 - 10:45 | Hacking _newsshop_                       |
| 10:45 - 11:00 | _Pause_                                  |
| 11:00 - 12:00 | Threat Modeling _newsshop_               |
| 12:00 - 13:00 | _Mittagspause_                           |
| 13:00 - 14:30 | Fixing _newsshop_                        |
| 14:30 - 14:45 | _Pause_                                  |
| 14:45 - 15:45 | Praxisherausforderungen                  |
| 15:45 - 16:00 | Zusammenfassung und Abschluss            |

## Trainingsumgebung

Die Trainingsumgebung ist eine virtuelle Maschine mit Kali-Linux, die über Deskmate bereitgestellt wird. Die Login-Daten werden zu Beginn des Workshops bereitgestellt.

[Secorvo @ Deskmate](https://secorvo.deskmate.me/)

### Optimierungsmöglichkeit

Ein kleiner Nachteil der Deskmate-Lösung ist die eingeschränkte Bedienung der GUI über den Browser. Vor allem funktioniert _Copy and Paste_ in dieser Umgebung nicht. Im Folgenden wird eine Möglichkeit vorgestellt, diesen Nachteil durch die Nutzung von SSH zu kompensieren.

#### Tailscale.com

Eine einfache Möglichkeit, die virtuellen Maschinen von Deskmate für einen externen Zugang zu öffnen bietet [Tailscale](https://tailscale.com/). Tailscale ist eine Verwaltungslösung um auf Basis der [Wireguard](https://www.wireguard.com/)-Technologie komfortabel ein Meshed-VPN aufzusetzen. Für kleine Umgebungen ist Tailscale kostenlos verfügbar. Zunächst muss man sich bei Tailscale anmelden sowie den eigenen Client mit der Tailscale-Software ausstatten und dort registrieren.

#### Tailscale auf dem Deskmate-Rechner

Auf dem Deskmate Rechner kann Tailscale einfach[^einfach] mit 

[^einfach]: Einfach ist natürlich nur sicher, wenn man sich vorher das Script angeschaut[^verstanden] hat :wink:
[^verstanden]: ... und verstanden :wink:

```bash
curl -fsSL https://tailscale.com/install.sh | sudo sh
sudo tailscale up
```

installiert werden. Mit dem am Ende der Installation bereitgestellten Link kann man die Maschine bei Tailscale registrieren. Es empfiehlt sich, in der Admin-Konsole den Rechner ggf. umzubenennen (z. B. in `etka-deskmate`).

#### SSH auf dem Deskmate-Rechner

Auf einem Kali-Linux ist der SSH-Dienst deaktiviert. Dieser kann wie folgt aktiviert werden:

```bash
sudo dpkg-reconfigure openssh-server
sudo systemctl start ssh.service 
```

#### Anmeldung per SSH

Nach den Vorbereitungen kann man sich per `ssh` auf dem Deskmate-Rechner mit `ssh tpsse@etka-deskmate` (s. o.) anmelden. Ggf. richtet man noch Public-Key-Authentication ein.