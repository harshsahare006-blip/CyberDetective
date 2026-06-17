def get_case():

    return {

        "title":
            "Case 001 - The Missing Database",

        "briefing":
            """
NeoTech Solutions reported that
customer information has appeared
on an underground forum.

Management suspects an insider.

Your job is to investigate.
            """,

        "clues": {

            "logs":
                """
Database Export Event

User:
j.smith

Time:
02:14 PM

Records Exported:
5000
                """,

            "employees":
                """
Employee Record

Name:
John Smith

Role:
Database Administrator

Status:
Vacation Leave

Last Office Visit:
7 Days Ago
                """,

            "network":
                """
VPN Login Detected

Time:
02:11 PM

Source:
Unknown External IP

Location:
Unrecognized
                """,

            "database":
                """
Database Audit

Customer Table Exported

Rows:
5000

Destination:
Unknown
                """
        },

        "solution": {

            "responsible": [
                "attacker",
                "external attacker",
                "hacker"
            ],

            "cause": [
                "vpn",
                "stolen credentials",
                "compromised account"
            ],

            "action": [
                "reset",
                "password reset",
                "revoke access",
                "change credentials"
            ]
        },
        
            "hints": {
              "1": "Start by checking database logs.",
              "2": "Look for unusual export activity.",
              "3": "Match VPN login time with employee activity."
         },

        "xp": 250
    }