def get_case():

    return {

        "title":
            "Case 006 - The Vanishing Records",

        "briefing":
            """
Customer records are disappearing
from UrbanCart's online store
database.

Support tickets mention a strange
error about "syntax." Investigate
the storefront's search feature.
            """,

        "clues": {

            "logs":
                """
Web Server Log

Request:
' OR '1'='1'; DROP TABLE customers;

Endpoint:
/search?query=

Time:
2:03 AM
                """,

            "employees":
                """
Employee Record

Name:
N/A

Note:
No employee activity recorded
at time of incident
                """,

            "network":
                """
WAF Status

Web Application Firewall:
Disabled (Maintenance Mode,
Never Re-Enabled)
                """,

            "database":
                """
Database Audit

Table Affected:
customers

Rows Deleted:
8,200

Query Source:
Public Search Field
                """
        },

        "solution": {

            "responsible": [
                "attacker",
                "external attacker",
                "hacker"
            ],

            "cause": [
                "sql injection",
                "unsanitized input",
                "missing input validation",
                "disabled waf"
            ],

            "action": [
                "use parameterized queries",
                "re-enable waf",
                "input validation",
                "patch search endpoint",
                "restore from backup"
            ]
        },

        "hints": [
            "The search query contained SQL injection payloads",
            "The WAF was disabled during maintenance",
            "No input validation was performed on the search field"
        ],

        "xp": 240
    }