function getIP {
    (Get-NetIPAddress).IPv4Address | Select-String "192*"
}

write-host(getIP)
$IP = getIP
$Date = ""
$Body = "This machine's IP is $IP. User is $env:username. Hostname is $. PowerShell Version . Today's date is $Date"

write-host($Body) 

#Send-MailMessage -To "aj.bothe@gmail.com" -From "aj.bothe@gmail.com" -Subject "IT3038C Windows SysInfo" -Body $Body -SmtpServer smtp.google.com -port 587 -UseSSL -Credential (Get-Credential)  
