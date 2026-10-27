<#
.SYNOPSIS
    Finds unattached managed disks in Azure subscription to reduce waste.
#>
[CmdletBinding()]
param()

Write-Host "Connecting to Azure..." -ForegroundColor Cyan
# Connect-AzAccount

Write-Host "Searching for unattached Azure Managed Disks..." -ForegroundColor Yellow
$unattachedDisks = Get-AzDisk | Where-Object { -not $_.ManagedBy }

$results = foreach ($disk in $unattachedDisks) {
    [PSCustomObject]@{
        DiskName      = $disk.Name
        ResourceGroup = $disk.ResourceGroupName
        DiskSizeGB    = $disk.DiskSizeGB
        Tier          = $disk.Sku.Name
        Location      = $disk.Location
    }
}

$results | Format-Table -AutoSize
Write-Host "Total Unattached Disks Found: $($results.Count)" -ForegroundColor Green
