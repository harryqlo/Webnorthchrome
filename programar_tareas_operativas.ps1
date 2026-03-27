param(
    [string]$ProjectDir = "C:\Users\bodega.NORTHCHROME\Downloads\north_chrome2\north_chrome",
    [string]$DailyTime = "07:30",
    [string]$WeeklyTime = "08:00"
)

$DailyTaskName = "NorthChrome-Checks-Diarios"
$WeeklyTaskName = "NorthChrome-Restore-Semanal"

$DailyBatch = Join-Path $ProjectDir "ejecutar_jobs_operativos.bat"
$WeeklyBatch = Join-Path $ProjectDir "ejecutar_restore_semanal.bat"

if (-not (Test-Path $DailyBatch)) {
    Write-Error "No existe: $DailyBatch"
    exit 1
}
if (-not (Test-Path $WeeklyBatch)) {
    Write-Error "No existe: $WeeklyBatch"
    exit 1
}

Write-Host "Programando tareas de confiabilidad operativa..."

schtasks /Create /TN $DailyTaskName /TR "\"$DailyBatch\"" /SC DAILY /ST $DailyTime /F | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-Error "No se pudo crear tarea diaria"
    exit 2
}

schtasks /Create /TN $WeeklyTaskName /TR "\"$WeeklyBatch\"" /SC WEEKLY /D SUN /ST $WeeklyTime /F | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-Error "No se pudo crear tarea semanal"
    exit 3
}

Write-Host "OK - Tarea diaria: $DailyTaskName ($DailyTime)"
Write-Host "OK - Tarea semanal: $WeeklyTaskName (DOM $WeeklyTime)"
Write-Host "Puedes revisar en Task Scheduler o con: schtasks /Query /TN NorthChrome-Checks-Diarios"
