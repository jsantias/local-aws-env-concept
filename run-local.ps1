# Checks for docker-compose command as that is required
if ((Get-Command "docker-compose" -ErrorAction SilentlyContinue) -eq $null) {
    Write-Error "Docker isn't installed. Please install"
    exit 1
  }

# Settings
$projectName = Split-Path -Path $PSScriptRoot -Leaf
$dockerPath = './.docker'

if (Test-Path $dockerPath) {
  $dockerComposeFilesToRun = "-f  $dockerPath/docker-compose.localstack.yml -f  $dockerPath/docker-compose.app.yml -f  $dockerPath/docker-compose.bootstrap.yml -f $dockerPath/docker-compose.observability.yml"
  $dockerComposeFilesToRun = $dockerComposeFilesToRun + " --env=./.env -p $projectName";
  $dockerComposeFilesToRun = $dockerComposeFilesToRun + ' up --build'
} 
else {
  Write-Error "$dockerPath doesn't exist"
  exit 1
}

# Write out the docker compose command line
Write-Host "`nRunning" $dockerComposeFilesToRun -ForegroundColor Green

Start-Process -FilePath "docker-compose" -Wait -ArgumentList $dockerComposeFilesToRun -WorkingDirectory $PSScriptRoot -NoNewWindow
