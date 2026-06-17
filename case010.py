def get_case():

    return {

        "title":
            "Case 010 - The Relentless Login Attempts",

        "briefing":
            """
Falcon Freight's admin portal
logged thousands of failed login
attempts overnight.

One account was eventually
compromised. Find out how.
            """,

        "clues": {

            "logs":
                """
Authentication Log

Account:
admin

Failed Attempts:
22,841

Time Range:
12:00 AM - 5:30 AM

Successful Login:
5:31 AM
                """,

            "employees":
                """
Employee Record

Name:
Shared "admin" Account

Role:
IT Administrator Group

Note:
Password unchanged for 3 years,
no lockout policy configured
                """,

            "network":
                """
IP Reputation Check

Source IP:
Associated With Known
Credential-Stuffing Botnet
                """,

            "database":
                """
Admin Panel Audit

Changes Made:
New Admin User Created

Permissions Granted:
Full Database Export Access
                """
        },

        "solution": {

            "responsible": [
                "attacker",
                "external attacker",
                "hacker",
                "bot"
            ],

            "cause": [
                "brute force attack",
                "weak password",
                "no account lockout",
                "shared admin account"
            ],

            "action": [
                "enforce account lockout",
                "implement mfa",
                "strong password policy",
                "remove shared accounts",
                "rate limit login attempts"
            ]
        },
            "hints": [
                "The admin account password was never changed",
                "The account lockout policy was not configured",
                "The account is a shared administrative account"
            ],
        "xp": 220
    }