# Open Health: Digital Public Goods Vaccination Tracker System

## Overview
This lightweight Python application provides a privacy-focused Patient Record and Vaccination Tracker System designed for community health centers. Developed for Object-Oriented Programming 1 (PROG211) at Limkokwing University of Creative Technology.

---

## Digital Public Goods (DPG) Standard Alignment

Our solution adheres strictly to standard DPG principles:

1. **Open-Source & Reusable Modular Architecture:**
   - Source code is fully modular, allowing independent extension of classes (`Patient`, `VaccineRecord`, `VaccinationTrackerSystem`).
   - Released under the open MIT License.

2. **Privacy-Respecting Design (Data Minimization):**
   - Personal Identifiable Information (PII) is anonymized at the class construction level using a `@staticmethod`. Patient names are automatically converted to initials (e.g., `Amandus Coker` becomes `A. C.`).
   - No national identification numbers, biometric markers, or sensitive demographic profiles are stored.

3. **Inclusive and Accessible Design:**
   - Standard console outputs require minimal bandwidth and hardware specifications, ensuring reliability in low-resource clinic settings.

---

## Features & Python OOP Design

- **Classes & Objects:** `Patient` and `VaccineRecord` interact to build dynamic health logs.
- **Data Structures:** 
  - **Dictionary:** Used for fast key-value lookup of patient files using unique patient IDs as keys.
  - **Tuple:** Used for immutable geospatial coordinates (Latitude, Longitude) tracking health center locations.
- **Methods Implemented:**
  - **Instance Methods:** `update_record()` and `display_info()`.
  - **Class Method:** `@classmethod get_total_patients()` tracks total registered patient instances across the system.
  - **Static Method:** `@staticmethod anonymize_name()` enforces privacy compliance logic.

---

## Folder Structure

```text
dpg-vaccination-tracker/
│
├── main.py
├── README.md
└── images/
    ├── code_screenshot.png
    └── terminal_output.png