# 🇮🇳 UIDAI Data Hackathon 2026 — Unlocking Societal Trends in Aadhaar Enrolment & Updates

> **Team Project** for the [UIDAI Data Hackathon 2026](https://event.data.gov.in/challenge/uidai-data-hackathon-2026/)

---

## 📌 Problem Statement

**Unlocking Societal Trends in Aadhaar Enrolment and Updates**

Identify meaningful patterns, trends, anomalies, or predictive indicators and translate them into clear insights or solution frameworks that can support informed decision-making and system improvements.

---

## 📂 Project Structure

```
UIDAI/
├── README.md                          # This file
├── Problem Statement Unlocking Societa.txt  # Original problem statement
├── deep_output.txt                    # Phase 2 anomaly detection results
│
├── data/                              # Aadhaar datasets (CSV)
│   ├── biometric/                     # Biometric update records
│   ├── demographic/                   # Demographic update records
│   └── enrolment/                     # New enrolment records
│
├── print/                             # Report & visualizations
│   ├── data_analysis_report_v3.html   # Full data analysis report (printable)
│   └── analysis_results/             # Generated charts & graphs
│
├── api_data_aadhar_biometric.zip      # Raw biometric dataset (zipped)
├── api_data_aadhar_demographic.zip    # Raw demographic dataset (zipped)
└── api_data_aadhar_enrolment.zip      # Raw enrolment dataset (zipped)
```

---

## 📊 Datasets

We processed over **1.5 million records** across three key dimensions from the UIDAI Open Data Portal:

| Dataset | Description | Key Fields |
|---------|-------------|------------|
| **Enrolment** | New Aadhaar registrations | `state`, `district`, `date`, `age_0_5`, `age_5_17`, `age_18_greater` |
| **Biometric Updates** | Fingerprint/Iris/Photo updates | `state`, `district`, `date`, `bio_age_5_17`, `bio_age_17_` |
| **Demographic Updates** | Address/Name/Mobile updates | `state`, `district`, `date`, `demo_age_5_17`, `demo_age_17_` |

### Data at a Glance

| Metric | Value |
|--------|-------|
| Total New Enrolments | **3,301,026** |
| Total Biometric Updates | **48,726,989** |
| Total Demographic Updates | **14,295,026** |
| Unique Districts Covered | **971** |
| Top Performing State | Uttar Pradesh |

---

## 🔍 Key Findings

### 1. Geographic Hotspots
- **Uttar Pradesh, Bihar, and Maharashtra** dominate in volume across all three categories, correlating with population density and highlighting where infrastructure load is highest.
- **Anomaly**: A massive spike was observed in **Moradabad, UP** on **01-07-2025** with **3,965 enrolments** in a single day.

### 2. The "Meghalaya Mystery" — Adult Enrolment Spike
- In **East Khasi Hills** and **West Khasi Hills**, over **83%** of new enrolments are adults (>18 years).
- National average for new adult enrolment is <5% — this suggests previously excluded tribal populations are finally gaining coverage or a migrant worker influx in border states.

### 3. The "Tuesday Effect" — Operational Insight
- Child enrolments (0–5 years) peak on **Tuesdays (Avg: 9.4)** and crash on **Saturdays (Avg: 2.5)**.
- This proves **Schools & Anganwadis** are the primary drivers of child enrolment, not parents visiting centers on weekends.

### 4. The "West Bengal" Data Chaos
- **5 different spellings** detected for the same state: *"WESTBENGAL", "West Bengal", "west Bengal", "Westbengal", "West bengal"*.
- This is a severe **Data Standardization Failure** that fragments analytics.

### 5. Biometric vs. Demographic Updates
- Demographic updates significantly outpace Biometric updates, indicating that **portability (migration)** is a bigger driver of system usage than biological changes.

---

## 💡 Proposed Solutions

| # | Problem | Solution |
|---|---------|----------|
| 1 | **Faded Fingerprint Deadlock** — Elderly/laborer authentication failures | **Adaptive Multi-Modal Fusion**: Auto-fallback from Fingerprint → Iris Scan → Facial Recognition with Liveness Detection |
| 2 | **Address Verification Loop** — Slow postal-based address updates for migrants | **GPS-Verified Trusted Geo-Fencing**: 5-day geo-tagging + landlord OTP vouching |
| 3 | **Spelling Mismatch Nightmare** — Inconsistent state/district naming | **Smart-State Dropdown Locks**: Master Data Management (MDM) with ISO-standardized lists + Fuzzy Matching for legacy data cleanup |
| 4 | **Working Parent Trap** — Low weekend enrolment despite demand | **Weekend Warrior Roving Camps**: Mobile Enrolment Vans deployed to malls/parks on weekends |
| 5 | **Excluded Adult Risk** — Late adult enrolments flagged as fraud | **Trust-Based Late Enrolment Tags**: Geo-Context scoring that lowers fraud thresholds for historically low-coverage regions |

---

## 🛠️ Technical Implementation Roadmap

### A. Smart-State Dropdown Locks (MDM)
- **Stack**: PostgreSQL (PostGIS), Redis, Python (FastAPI)
- Database migration with foreign key constraints for state names
- API middleware to reject non-standard geo entries

### B. Trust-Based Late Enrolment Scoring
- **Stack**: SciKit-Learn (Random Forest), Apache Spark
- Feature engineering with `geo_risk_score` and `document_strength`
- Tribal context dampener for known low-coverage regions

### C. Weekend Warrior Mobile Capacity
- **Stack**: Kafka, Google OR-Tools
- Real-time demand sensing via queue data
- Vehicle Routing Problem (VRP) optimization for mobile van placement

---

## 📈 Visualizations

All charts are stored in `print/analysis_results/`:

| Chart | Description |
|-------|-------------|
| `enrolment_age_pie_chart.png` | Enrolment distribution by age group (0–5, 5–17, 18+) |
| `top_10_states_enrolment.png` | Top 10 states by total enrolment volume |
| `updates_comparison_bar.png` | Biometric vs. Demographic update volumes |
| `biometric_updates_pie.png` | Biometric updates split by age group |
| `enrolment_time_trend.png` | Daily enrolment trend with July 2025 spike |
| `adult_enrolment_anomaly.png` | Meghalaya adult enrolment anomaly visualization |

---

## 📄 Reports

- **Full Analysis Report**: Open `print/data_analysis_report_v3.html` in a browser (print-optimized for A4)
- **Deep Anomaly Output**: See `deep_output.txt` for Phase 2 anomaly detection results

---

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/varanasirohit2006/UIDAI_PROJECT.git
   ```

2. **Extract datasets** (if not already extracted)
   ```bash
   unzip api_data_aadhar_biometric.zip -d data/biometric/
   unzip api_data_aadhar_demographic.zip -d data/demographic/
   unzip api_data_aadhar_enrolment.zip -d data/enrolment/
   ```

3. **View the report**
   Open `print/data_analysis_report_v3.html` in any modern web browser.

---

## 🏆 Why Our Analysis Stands Out

- **Depth**: Correlated age-groups with specific mandatory update protocols (MBU at ages 5 & 15)
- **Precision**: Identified specific anomaly dates (July 1st) rather than generic observations
- **Empathy**: Connected data spikes to real-world user friction points (Fingerprint Deadlock)
- **Vision**: Solutions (AI Scaling, Multi-Modal Fusion) are technically feasible and instantly scalable

---

## 👥 Team

**UIDAI Data Hackathon 2026 Participants**

---

## 📜 License

This project was created for the [UIDAI Data Hackathon 2026](https://event.data.gov.in/challenge/uidai-data-hackathon-2026/). All datasets are sourced from the UIDAI Open Data Portal.
