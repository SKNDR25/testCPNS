param (
    [Parameter(Mandatory=$true)]
    [string]$Message
)

$token = "9222609422:AAGjZ8WGlwiabwzJlN3QoUujauHKwksTK_Q"
$chatId = "5678164024"

$body = @{
    chat_id = $chatId
    text = $Message
    parse_mode = "Markdown"
} | ConvertTo-Json

try {
    $response = Invoke-RestMethod -Uri "https://api.telegram.org/bot$token/sendMessage" -Method Post -Body $body -ContentType "application/json"
    if ($response.ok) {
        Write-Output "Telegram notification sent successfully."
    } else {
        Write-Error "Telegram API returned non-ok: $($response.description)"
    }
} catch {
    Write-Error "Failed to send Telegram notification: $_"
}
