"""
Compute Rightsizing Engine
Author: Sujeet Kumar - Senior DevSecOps Engineer & Cloud Architect

Evaluates P95 CPU & RAM telemetry from Azure Monitor to recommend right-sizing.
"""

from typing import Dict, List

def recommend_vm_rightsizing(vm_metrics: List[Dict]) -> List[Dict]:
    recommendations = []
    
    for vm in vm_metrics:
        avg_cpu = vm.get("p95_cpu_percent", 0.0)
        avg_ram = vm.get("p95_ram_percent", 0.0)
        current_sku = vm.get("current_sku", "")
        
        # Idle / Heavily Oversized
        if avg_cpu < 10.0 and avg_ram < 25.0:
            recommendations.append({
                "vm_name": vm.get("vm_name"),
                "current_sku": current_sku,
                "recommended_sku": "Standard_B2s",
                "action": "Downgrade SKU (Oversized)",
                "estimated_monthly_savings_usd": 120.0
            })
        elif avg_cpu < 30.0 and avg_ram < 40.0:
            recommendations.append({
                "vm_name": vm.get("vm_name"),
                "current_sku": current_sku,
                "recommended_sku": "Standard_D2s_v5",
                "action": "Right-size compute",
                "estimated_monthly_savings_usd": 75.0
            })
            
    return recommendations
