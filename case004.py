def get_case():

    return {

        "title":
            "Case 004 - The Disgruntled Departure",

        "briefing":
            """
A week after handing in his
resignation, an employee's access
at Pinegrove Engineering was
supposed to be revoked.

Critical project files have just
been deleted from the engineering
server.
            """,

        "clues": {

            "logs":
                """
Access Log

User:
d.reyes

Action:
Mass File Deletion

Files Deleted:
1,847

Time:
11:58 PM (Day Before Last Day)
                """,

            "employees":
                """
Employee Record

Name:
David Reyes

Role:
Senior Engineer

Status:
Resigned

Note:
Access was not deactivated
until the day after departure
                """,

            "network":
                """
VPN Log

User:
d.reyes

Connection:
From Home, After Hours

Session Duration:
47 Minutes
                """,

            "database":
                """
Backup Audit

Last Successful Backup:
3 Days Prior

Recoverable Files:
Partial
                """
        },

        "solution": {

            "responsible": [
                "insider",
                "former employee",
                "disgruntled employee",
                "david reyes"
            ],

            "cause": [
                "delayed offboarding",
                "access not revoked",
                "insider threat",
                "late deprovisioning"
            ],

            "action": [
                "revoke access immediately",
                "offboarding checklist",
                "disable accounts on last day",
                "restore from backup",
                "monitor departing employees"
            ]
        },

        "hints": [
            "The employee's access was not revoked until the day after their departure",
            "Files were deleted after hours from a remote location",
            "The employee had access to critical project files"
        ],

        "xp": 230

    }