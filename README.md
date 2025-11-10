# WaterBlock Data Pipeline

This project provides a modular set of Python scripts for processing, cleaning, and merging experimental data related to water block thermal testing.

---

## 📌 Overview

The pipeline automates three main tasks:

1. **Combine** raw CSV files into unified datasets.
2. **Fix and clean** numeric values (remove invalid or zero entries).
3. **Append** selected temperature and voltage data into Excel analysis templates.

This ensures all experiment data is consistently formatted and ready for visualization or thermal analysis.

---

## 📂 Project Structure
```text
├── data/
│ ├── raw/ # Input CSV/XLSX data
│ ├── processed/ # Output cleaned data
│ └── temp/ # Optional intermediate files
│
├── src/
│ ├── data_combiner.py
│ ├── data_fixer.py
│ └── append_core_data.py
│
├── docs/
│ ├── overview.md
│ ├── usage_guide.md
│ └── development_notes.md
│
├── .gitignore
├── requirements.txt
├── LICENSE
└── README.md
```
---

## ⚙️ How to Use

1. **Combine data files**
```bash
python src/data_combiner.py
``` 

Merges two CSV files side-by-side into a single combined dataset.

2. **Clean numeric data**
```bash
python src/data_fixer.py
```
Removes invalid values, replaces zeros and outliers, and fills gaps.

3. **Append core temperature data**

```bash
python src/append_core_data.py
```
Appends selected columns (e.g., temperature and voltage) into an Excel file for analysis.

## 🧰 Requirements

Install dependencies with:

 ```bash
pip install -r requirements.txt
``` 

Dependencies:
- pandas
- openpyxl

## 🧪 Example Workflow

1. Place raw CSVs in data/raw/
2. Run:
```bash
python src/data_combiner.py
python src/data_fixer.py
python src/append_core_data.py
```
3. Check results in data/processed/

## 🧑‍💻 Authors

Developed by UniSCool
(Data processing pipeline for experimental validation of water block performance.)

## 📄 License

MIT License – see LICENSE file for details.


---
