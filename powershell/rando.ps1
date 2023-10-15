$RANDO=0

$Logfile = "C:\it3038c-scripts\powershell\logs\rando.log"

for($i=0; $i -lt 5; $i++){
    $RANDO=Get-Random -Maximum 1000 -Minimum 1

    Write-Host($RANDO)

    Add-Content $LogFile "INFO: Random number is ${RANDO}"
}