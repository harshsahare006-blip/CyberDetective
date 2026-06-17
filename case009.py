def get_case():

    return {

        "title":
            "Case 009 - The Vendor's Weak Link",

        "briefing":
            """
Crestwood Insurance Group's
customer support software,
provided by a third-party vendor,
pushed an update overnight.

The update secretly contained
a backdoor.
            """,

        "clues": {

            "logs":
                """
Update Log

Software:
SupportDesk Pro v4.2.1

Installed:
Automatically Via Vendor Channel

Time:
3:00 AM
                """,

            "employees":
                """
Employee Record

Name:
N/A

Note:
Update was automatic, no
employee action was involved
                """,

            "network":
                """
Network Traffic Analysis

New Outbound Connections:
To Vendor's Compromised Server

Behavior:
Beaconing To C2 Infrastructure
                """,

            "database":
                """
Vendor Security Bulletin

Vendor:
SupportDesk Pro

Statement:
Confirms Build Server Compromise,
Malicious Code Inserted Into
Update Package
                """
        },

        "solution": {

            "responsible": [
                "vendor",
                "third-party vendor",
                "supply chain attacker",
                "external attacker"
            ],

            "cause": [
                "supply chain attack",
                "compromised vendor update",
                "compromised build server"
            ],

            "action": [
                "pause automatic updates",
                "verify software integrity",
                "isolate affected systems",
                "contact vendor",
                "review vendor security practices"
            ]
        },
           "hints": [
            "The update was pushed automatically without user intervention",
            "The vendor's build server was compromised",
            "The backdoor was hidden within the update package"
        ],
        "xp": 250
    }