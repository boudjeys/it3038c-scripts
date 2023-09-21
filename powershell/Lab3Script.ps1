# Function to get the machine's IPv4 address
function Get-IP {
    (Get-NetIPAddress | Where-Object {$_.AddressFamily -eq 'IPv4'}).IPAddress
}

# Collect system information
$IP = Get-IP
$User = $env:UserName
$Ver = $PSVersionTable.PSVersion
$HOSTName = $env:ComputerName
$DATE = Get-Date -Format "dddd, MMMM dd, yyyy"

# Create the email body
$BODY = "This machine's IP is $IP. User is $User. Hostname is $HOST. PowerShell Version $Ver. Today's Date is $DATE."

# Configure Gmail SMTP settings
$SMTPServer = "smtp.gmail.com"
$SMTPPort = 587
$SMTPUser = "yanis2002fr@gmail.com"
$SMTPPassword = "rhov jhez smhe awqq" 

#List of recipients
$Recipients = "broximp@gmail.com", "leonardf@uc.mail.edu" #The people receiving this email

# Send the email
Send-MailMessage -To $Recipients -From $SMTPUser -Subject "IT3038C Windows SysInfo" -Body $BODY -SmtpServer $SMTPServer -Port $SMTPPort -UseSSL -Credential (New-Object System.Management.Automation.PSCredential ($SMTPUser, (ConvertTo-SecureString $SMTPPassword -AsPlainText -Force)))
