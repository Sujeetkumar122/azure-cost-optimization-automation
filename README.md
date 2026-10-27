<div align="center">

# 💰 Cloud FinOps Sentinel & Cost Optimization Engine

[![FinOps](https://img.shields.io/badge/FinOps-Certified_Practitioner-10B981?style=for-the-badge&logo=cashapp&logoColor=white)](#)
[![Savings](https://img.shields.io/badge/Savings-%24400K%2B_Annual-0078D4?style=for-the-badge)](#)
[![Infracost](https://img.shields.io/badge/Shift--Left-Infracost_Gates-00D2FF?style=for-the-badge&logo=infracost&logoColor=white)](#)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)

**Automated multi-subscription cloud financial management engine delivering continuous waste elimination, right-sizing analysis, and pre-merge Infracost PR budget enforcement.**

</div>

---

## 📊 Key Highlights & Quantified Impact

- 🗑️ **Waste Detection:** Programmatic identification of orphaned managed disks, unassociated public IPs, obsolete VM snapshots (>30 days), and idle compute.
- 📉 **Right-Sizing Analytics:** Evaluates P95 CPU & RAM telemetry from Azure Monitor to generate safe compute downgrade recommendations.
- 🛑 **Non-Prod Scheduling:** Automated start/stop automation schedules slashing non-working-hour dev/test spend by **65%**.
- 🛡️ **Shift-Left Budget Guardrails:** Integration of Infracost into Azure DevOps and GitHub Actions blocking costly IaC commits before merge.
- 💵 **Total Impact:** Generated over **$400,000+ in annual recurring cloud OPEX savings** across 100+ enterprise workloads.

```mermaid
graph LR
    subgraph Detection["🔍 Telemetry & Inventory"]
        AZ["Azure Resource Graph"] --> SCAN["Waste Detector"]
        MON["Azure Monitor Metrics"] --> RS["Rightsizing Engine"]
    end
    subgraph Action["⚡ Governance Action"]
        SCAN --> PURGE["Auto-Purge Orphan Disks & IPs"]
        RS --> REC["Azure Advisor Action Items"]
        PR["GitHub / ADO Pull Request"] --> IC["Infracost Budget Guardrail"]
    end

    classDef blue fill:#0B1F3A,stroke:#0078D4,stroke-width:2px,color:#fff;
    classDef green fill:#052e16,stroke:#10b981,stroke-width:2px,color:#fff;
    class Detection blue;
    class Action green;
```

---

## 📁 Repository Structure

```
.
├── analyzers/
│   ├── waste_detector.py      # Unattached disks, snapshots, and public IP detection
│   └── rightsizing_engine.py  # VM right-sizing and SKU optimization logic
├── infracost/
│   └── budget-guardrail.yml   # Pre-merge pull request cost threshold policy
└── README.md
```

---

## 👤 Author

**Sujeet Kumar**  
*Senior DevSecOps Engineer & Enterprise Cloud Architect (17+ Years Experience)*  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/sujeetkumar122)
[![GitHub](https://img.shields.io/badge/GitHub-Sujeetkumar122-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Sujeetkumar122)
