def get_case():

    return {

        "title":
            "Case 008 - The USB In The Parking Lot",

        "briefing":
            """
An employee at Harborview Health
Systems found a USB drive labeled
"Salary Review 2026" in the
parking lot.

Curious, she plugged it into her
work computer.
            """,

        "clues": {

            "logs":
                """
Endpoint Detection Log

Device:
USB-PNY-2240

Action:
Autorun Executed

File:
salary_review.exe

Time:
8:14 AM
                """,

            "employees":
                """
Employee Record

Name:
Linda Park

Role:
HR Coordinator

Status:
Active

Note:
Found and inserted unknown USB
drive into work laptop
                """,

            "network":
                """
Outbound Connection Log

Destination:
Unknown External IP

Data Transferred:
Small Beacon Packets Every 5 Min
                """,

            "database":
                """
Malware Scan Report

Detected:
Trojan.GenericKD

Status:
Quarantined After 3 Days Active
                """
        },

        "solution": {

            "responsible": [
                "attacker",
                "external attacker",
                "linda park",
                "employee error"
            ],

            "cause": [
                "usb drop attack",
                "malicious usb",
                "social engineering",
                "autorun malware"
            ],

            "action": [
                "disable autorun",
                "usb device control policy",
                "security awareness training",
                "isolate infected machine",
                "full malware scan"
            ]
        },

        "hints": [
            "The USB drive was found in the parking lot",
            "The autorun feature was enabled on the USB drive",
            "The executable file on the USB drive is flagged as malicious"
        ],

        "xp": 210
    }