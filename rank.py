# ==========================================
# CyberDetectiveX - Rank System
# ==========================================

def get_rank(xp):

    if xp >= 5000:
        return "Legendary Cyber Detective"

    elif xp >= 3500:
        return "Chief Investigator"

    elif xp >= 2500:
        return "Cyber Detective"

    elif xp >= 1500:
        return "Digital Forensics Expert"

    elif xp >= 800:
        return "Threat Hunter"

    elif xp >= 400:
        return "Cyber Investigator"

    elif xp >= 150:
        return "Junior Analyst"

    else:
        return "Intern"