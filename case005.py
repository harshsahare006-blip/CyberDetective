def get_case():

    return {

        "title":
            "Case 005 - The Open Bucket",

        "briefing":
            """
A security researcher emailed
Lumen Retail Group warning that
a cloud storage bucket of customer
invoices is publicly viewable
by anyone with the link.
            """,

        "clues": {

            "logs":
                """
Cloud Access Log

Bucket:
lumen-invoices-prod

Permission:
Public Read Access

Configured:
6 Months Ago
                """,

            "employees":
                """
Employee Record

Name:
Priya Nair

Role:
Cloud Engineer

Status:
Active

Note:
Set bucket public for a vendor
test, never reverted the setting
                """,

            "network":
                """
External Scan Report

Source:
Security Researcher

Finding:
Bucket Indexed By Search Engine,
No Authentication Required
                """,

            "database":
                """
Storage Audit

Files Exposed:
12,400 Invoices

Contains:
Customer Names, Addresses,
Partial Payment Info
                """
        },

        "solution": {

            "responsible": [
                "cloud engineer",
                "internal mistake",
                "human error",
                "misconfiguration"
            ],

            "cause": [
                "misconfigured bucket",
                "public access enabled",
                "cloud misconfiguration",
                "human error"
            ],

            "action": [
                "restrict bucket to private",
                "audit cloud permissions",
                "implement access reviews",
                "remove public access",
                "notify affected customers"
            ]
        },
            "hints": [
            "The bucket was set to public for a vendor test",
            "The bucket is indexed by search engines",
            "No authentication is required to access the bucket"
        ],
        "xp": 200
    }