def get_case():

    return {

        "title":
            "Case 002 - The Phishing Wire Transfer",

        "briefing":
            """
Brightline Logistics' finance team
wired $85,000 to a vendor account
after receiving an urgent request
that appeared to come from the CEO.

The money is gone. Find out how
the request slipped through.
            """,

        "clues": {

            "logs":
                """
Email Server Log

Sender Display Name:
Robert Chen (CEO)

Sender Email:
r.chen@brightline-finance.com

Subject:
Urgent Wire Transfer Request

Time:
9:42 AM
                """,

            "employees":
                """
Employee Record

Name:
Sarah Lopez

Role:
Accounts Payable Clerk

Status:
Active

Note:
Processed transfer per "CEO" email,
no phone confirmation was made
                """,

            "network":
                """
Domain Registration Lookup

Domain:
brightline-finance.com

Registered:
2 Days Ago

Registrar:
Privacy-protected, overseas
                """,

            "database":
                """
Bank Transfer Record

Amount:
$85,000

Destination:
Offshore Account

Status:
Funds Unrecoverable
                """
        },

        "solution": {

            "responsible": [
                "attacker",
                "external attacker",
                "scammer",
                "fraudster",
                "bec attacker"
            ],

            "cause": [
                "phishing",
                "spoofed email",
                "business email compromise",
                "bec",
                "lookalike domain"
            ],

            "action": [
                "verify requests",
                "callback verification",
                "employee training",
                "implement dmarc",
                "verify wire transfers"
            ]
        },

         "hints": [
            "The email appeared to come from the CEO",
            "No phone confirmation was made",
            "The domain looks similar to the legitimate one"
        ],

        "xp": 200
    }