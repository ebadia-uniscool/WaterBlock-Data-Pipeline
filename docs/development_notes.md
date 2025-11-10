# Development Notes

These notes summarize design decisions and internal logic for developers maintaining or extending this project.

---

## 🧠 Core Design

The project is modular — each script performs a single, well-defined task:
- `data_combiner.py` → Merging and structural alignment.
- `data_fixer.py` → Data sanitation and numeric correction.
- `append_core_data.py` → Integration into analysis templates.

---

## 🧱 Coding Standards

- Python 3.10+  
- PEP8-compliant  
- Modular design with clear function-level docstrings.  
- Use of `pandas` for structured data and `openpyxl` for Excel operations.

---

## 🧩 Adding New Modules

When adding new scripts:
1. Create the file inside `/src`.
2. Add descriptive docstrings and CLI arguments if necessary.
3. Update this documentation and README.

---

## 🧪 Testing

Tests are stored under `/tests/` and should include:
- File existence checks.
- Data integrity validations.
- Output format consistency.


---

## 🧰 Environment Setup

Install all dependencies:
```bash
pip install -r requirements.txt
