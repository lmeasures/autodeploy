param (
    [string] $websiteName = $null
)

Import-Module IISAdministration;


$response = Get-IISSite $websiteName 3>&1;
if ($response -match "does not")
{
    exit 0
}
else
{
    exit 1
}