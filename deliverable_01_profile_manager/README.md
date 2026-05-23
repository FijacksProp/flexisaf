# Profile Manager

This program collects a user's profile information, checks that the input is valid, saves the profile in a JSON file, and can display the saved profile later.

## What the Program Does

- Asks the user for:
  - Full name
  - Age
  - Email
  - Phone number
  - Course or field of study
  - School name
- Validates the age, email, and phone number
- Saves the profile in `profile.json`
- Reads and displays the saved profile

## Required Libraries

This program only uses built-in Python libraries:

- `json`
- `pathlib`


## How to Run

Open your terminal in the project folder and run:

```bash
python deliverable_01_profile_manager/profile_manager.py
```

Then choose from the menu:

```text
1. Create or update profile
2. Display saved profile
3. Exit
```

The profile is saved in:

```text
profile.json
```
