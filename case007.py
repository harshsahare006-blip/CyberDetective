def get_case():

    return {

        "title":
            "Case 007 - The Laptop Left Behind",

        "briefing":
            """
A sales executive at Sterling &
Co. Realty had his laptop stolen
from his car overnight.

It contained a spreadsheet of
prospective client contracts.
            """,

        "clues": {

            "logs":
                """
Device Management Log

Device:
Laptop SN-88213

Last Check-In:
11:45 PM

Encryption Status:
Disk Encryption Not Enabled
                """,

            "employees":
                """
Employee Record

Name:
Tom Becker

Role:
Sales Executive

Status:
Active

Note:
Reported laptop stolen from
vehicle this morning
                """,

            "network":
                """
Device Tracking

Last Known Location:
Parking Lot, Downtown Office

Current Status:
Offline, No Remote Wipe Available
                """,

            "database":
                """
File Inventory (From Backup)

File:
Q3_Prospect_Contracts.xlsx

Contains:
Client Names, Deal Values,
Contact Info
                """
        },

        "solution": {

            "responsible": [
                "thief",
                "external attacker",
                "unknown thief"
            ],

            "cause": [
                "unencrypted laptop",
                "no disk encryption",
                "stolen device",
                "lack of mdm"
            ],

            "action": [
                "enable full disk encryption",
                "enroll devices in mdm",
                "enable remote wipe capability",
                "report to authorities",
                "notify affected clients"
            ]
        },

        "hints": [
            "The laptop was left in the car overnight",
            "No disk encryption was enabled",
            "The device was not enrolled in mobile device management"
        ],

        "xp": 190
    }