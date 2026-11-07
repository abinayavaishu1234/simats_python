
import re
import time

# Normalize phone number
def normalize_phone(phone):
    digits = re.sub(r"\D", "", phone)

    if len(digits) == 12 and digits.startswith("91"):
        digits = digits[2:]

    return digits if len(digits) == 10 else ""


# Normalize name
def normalize_name(name):
    return " ".join(name.lower().split())


# Merge contacts
def merge_contacts(contact_lists):
    merged = {}

    for contacts in contact_lists:
        for contact in contacts:

            name = normalize_name(contact.get("name", ""))

            phone = normalize_phone(
                contact.get("phone", "")
            )

            email = contact.get("email", "").strip().lower()

            # Use phone as key; use email if phone is missing
            if phone:
                key = "phone:" + phone
            elif email:
                key = "email:" + email
            else:
                continue

            if key not in merged:
                merged[key] = {
                    "name": name,
                    "phones": set(),
                    "emails": set()
                }

            if phone:
                merged[key]["phones"].add(phone)

            if email:
                merged[key]["emails"].add(email)

    return merged


# Contacts from three sources
phone1 = [
    {
        "name": "Dr. Ravi",
        "phone": "+91 98400 12345",
        "email": "ravi@gmail.com"
    },
    {
        "name": "Priya",
        "phone": "9876543210",
        "email": "priya@gmail.com"
    }
]

phone2 = [
    {
        "name": "Ravi Kumar",
        "phone": "9840012345",
        "email": "RAVI@GMAIL.COM"
    },
    {
        "name": "Arun",
        "phone": "9123456780",
        "email": "arun@gmail.com"
    }
]

sim = [
    {
        "name": "Ravi",
        "phone": "98400 12345",
        "email": "ravi.office@gmail.com"
    }
]

contact_lists = [phone1, phone2, sim]

# Merge and display
result = merge_contacts(contact_lists)

print("Merged Contacts:")

for contact in result.values():
    print("\nName:", contact["name"].title())
    print("Phone numbers:", sorted(contact["phones"]))
    print("Email addresses:", sorted(contact["emails"]))


# Performance measurement
for n in [1000, 100000]:
    test_contacts = [[
        {
            "name": "Person " + str(i),
            "phone": str(9000000000 + i),
            "email": "person" + str(i) + "@gmail.com"
        }
        for i in range(n)
    ]]

    start = time.perf_counter()
    merge_contacts(test_contacts)
    elapsed = time.perf_counter() - start

    print("\nContacts:", n)
    print("Time taken:", elapsed)
