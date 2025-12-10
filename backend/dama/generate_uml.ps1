$ErrorActionPreference = "Stop"

Write-Host "`n Gerando diagrama UML" -ForegroundColor Cyan

Write-Host "Verificando Graphviz" -ForegroundColor Yellow

$dotCommand = Get-Command dot -ErrorAction SilentlyContinue
if (-not $dotCommand) {
    $dotPath = "C:\Program Files\Graphviz\bin\dot.exe"
    if (Test-Path $dotPath) {
        $dotCommand = $dotPath
        Write-Host "Graphviz encontrado: $dotPath" -ForegroundColor Green
    } else {
        Write-Host "Graphviz não encontrado" -ForegroundColor Red
        Write-Host "`nInstale o Graphviz:" -ForegroundColor Yellow
        Write-Host "  - Chocolatey: choco install graphviz -y" -ForegroundColor White
        Write-Host "  - Manual: https://graphviz.org/download/" -ForegroundColor White
        Write-Host "`nOu veja: INSTALL_GRAPHVIZ.md" -ForegroundColor Cyan
        exit 1
    }
} else {
    Write-Host "Graphviz encontrado no PATH" -ForegroundColor Green
    $dotCommand = "dot"
}

Write-Host "`nGerando diagram_domain.dot (app api)" -ForegroundColor Cyan
try {
    python manage.py graph_models api --pydot -o diagram_domain.dot
    if ($LASTEXITCODE -ne 0) { throw "Erro ao gerar .dot" }
    Write-Host "Arquivo .dot gerado" -ForegroundColor Green
} catch {
    Write-Host "Erro ao gerar diagram_domain.dot" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
    exit 1
}

# Converter para PNG
Write-Host "`nConvertendo para PNG" -ForegroundColor Cyan
try {
    if ($dotCommand -is [string] -and $dotCommand -eq "dot") {
        & dot -Tpng diagram_domain.dot -o uml_diagram_domain.png
    } else {
        & $dotCommand -Tpng diagram_domain.dot -o uml_diagram_domain.png
    }
    if ($LASTEXITCODE -ne 0) { throw "Erro ao converter para PNG" }
    Write-Host "Gerado: uml_diagram_domain.png" -ForegroundColor Green
} catch {
    Write-Host "Erro ao converter para PNG" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
    exit 1
}

# Gerar diagrama completo (opcional)
Write-Host "`nGerando diagram_all.dot (todas as models)" -ForegroundColor Cyan
try {
    python manage.py graph_models -a --pydot -o diagram_all.dot
    if ($LASTEXITCODE -eq 0) {
        if ($dotCommand -is [string] -and $dotCommand -eq "dot") {
            & dot -Tpng diagram_all.dot -o uml_diagram_all.png
        } else {
            & $dotCommand -Tpng diagram_all.dot -o uml_diagram_all.png
        }
        Write-Host "Gerado: uml_diagram_all.png" -ForegroundColor Green
    }
} catch {
    Write-Host "Não foi possível gerar diagram_all.png" -ForegroundColor Yellow
}

# Mostrar arquivos gerados
Write-Host "`nDiagramas gerados com sucesso" -ForegroundColor Green
Write-Host "`nArquivos gerados:" -ForegroundColor Cyan
Get-ChildItem -Filter "uml_diagram_*.png" -ErrorAction SilentlyContinue | ForEach-Object {
    $sizeKB = [math]::Round($_.Length/1KB, 2)
    Write-Host "   - $($_.Name) ($sizeKB KB)" -ForegroundColor White
}

# Abrir imagem principal
Write-Host "`nAbrindo uml_diagram_domain.png" -ForegroundColor Cyan
Start-Process uml_diagram_domain.png

Write-Host "`nOs diagramas foram gerados" -ForegroundColor Green