def get_case():

    return {

        "title":
            "Case 003 - The Encrypted Files",

        "briefing":
            """
Monday morning, employees at
Coastal Manufacturing Co. find
every file on the shared drive
renamed with a ".locked" extension.

A ransom note demands payment
in Bitcoin. Find the entry point.
            """,

        "clues": {

            "logs":
                """
Firewall Log

Port:
3389 (RDP)

Status:
Open To Internet

Failed Login Attempts:
14,392 (Past 30 Days)

Successful Login:
03:07 AM
                """,

            "employees":
                """
Employee Record

Name:
Mike Torres

Role:
IT Support

Status:
Active

Note:
Set up RDP for remote work,
no MFA was configured
                """,

            "network":
                """
Threat Intelligence Alert

Source IP:
Flagged In Ransomware Botnet

Activity:
Mass Scanning For Open RDP Ports
                """,

            "database":
                """
File Server Audit

Files Modified:
41,203

Extension Changed To:
.locked

Ransom Note:
Found In Every Directory
                """
        },

        "solution": {

            "responsible": [
                "attacker",
                "ransomware gang",
                "external attacker",
                "hacker"
            ],

            "cause": [
                "exposed rdp",
                "open rdp port",
                "weak rdp security",
                "no mfa",
                "brute force rdp"
            ],

            "action": [
                "close rdp port",
                "disable rdp",
                "implement mfa",
                "restore from backup",
                "use vpn for remote access"
            ]
        },
           "hints": [
            "The RDP port was open to the internet",
            "No multi-factor authentication was configured",
            "The source IP is flagged in a ransomware botnet"
        ],
        "xp": 220
    }