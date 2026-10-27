"""
Cloud FinOps Waste Detector
Author: Sujeet Kumar - Senior DevSecOps Engineer & Cloud Architect

Automates detection of orphaned Azure resources:
- Unattached Managed Disks
- Obsolete VM Snapshots (> 30 days old)
- Unassociated Public IP Addresses
- Orphaned Network Interfaces (NICs)
"""

import json
from typing import Dict, List

def analyze_unattached_disks(disks_inventory: List[Dict]) -> Dict:
    orphaned_disks = []
    total_monthly_waste_usd = 0.0
    
    # Average Azure Managed Disk Pricing per GB (Standard SSD / Premium SSD blend)
    cost_per_gb_month = 0.10
    
    for disk in disks_inventory:
        if disk.get("managed_by") is None:
            size_gb = disk.get("disk_size_gb", 0)
            monthly_cost = size_gb * cost_per_gb_month
            total_monthly_waste_usd += monthly_cost
            orphaned_disks.append({
                "disk_name": disk.get("name"),
                "resource_group": disk.get("resource_group"),
                "size_gb": size_gb,
                "tier": disk.get("tier", "StandardSSD"),
                "estimated_monthly_cost_usd": round(monthly_cost, 2)
            })
            
    return {
        "orphaned_disks_count": len(orphaned_disks),
        "total_monthly_waste_usd": round(total_monthly_waste_usd, 2),
        "annual_projected_savings_usd": round(total_monthly_waste_usd * 12, 2),
        "disks": orphaned_disks
    }

def analyze_idle_public_ips(ips_inventory: List[Dict]) -> Dict:
    unassociated_ips = []
    cost_per_ip_month = 3.65 # Standard Azure Static Public IP cost
    
    for ip in ips_inventory:
        if not ip.get("ip_configuration"):
            unassociated_ips.append(ip.get("name"))
            
    total_cost = len(unassociated_ips) * cost_per_ip_month
    return {
        "unassociated_ips_count": len(unassociated_ips),
        "monthly_waste_usd": round(total_cost, 2),
        "ips": unassociated_ips
    }

if __name__ == "__main__":
    sample_disks = [
        {"name": "disk-legacy-app-01-data", "resource_group": "rg-spoke-app", "disk_size_gb": 512, "managed_by": None},
        {"name": "disk-uat-test-vol2", "resource_group": "rg-spoke-uat", "disk_size_gb": 1024, "managed_by": None},
        {"name": "disk-prod-db-active", "resource_group": "rg-spoke-prod", "disk_size_gb": 2048, "managed_by": "/subscriptions/.../vms/vm-prod-01"}
    ]
    report = analyze_unattached_disks(sample_disks)
    print("=== FINOPS WASTE DETECTION REPORT ===")
    print(json.dumps(report, indent=2))
