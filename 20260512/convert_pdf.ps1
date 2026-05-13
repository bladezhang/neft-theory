# 使用Edge/Chrome浏览器将HTML转换为PDF，每页都带水印

$html_file = "E:\work\projs\neft\paper\20260504\neft_20260504_cited_figure.html"
$output_pdf = "E:\work\projs\neft\paper\20260504\neft_20260504_cited_figure_watermarked.pdf"

Write-Host "正在准备使用Edge浏览器转换HTML为PDF..."

# 查找Edge浏览器的可执行文件
$edgePaths = @(
    "$env:ProgramFiles(x86)\Microsoft\Edge\Application\msedge.exe",
    "$env:ProgramFiles\Microsoft\Edge\Application\msedge.exe",
    "$env:LOCALAPPDATA\Microsoft\Edge\Application\msedge.exe",
    "$env:ProgramW6432Node\Microsoft\Edge\Application\msedge.exe"
)

$edgeExe = $null
foreach ($path in $edgePaths) {
    if (Test-Path $path)) {
        $edgeExe = $path
        break
    }
}

if ($null -eq $edgeExe) {
    Write-Host "错误: 未找到Edge浏览器"
    Write-Host ""
    Write-Host "手动方法："
    Write-Host "1. 在浏览器中打开: $html_file"
    Write-Host "2. 按 Ctrl+P 打印"
    Write-Host "3. 在打印设置中勾选 '背景图形'"
    Write-Host "4. 选择 '另存为PDF'"
    Write-Host "5. 保存为: $output_pdf"
    exit
}

Write-Host "找到Edge浏览器: $edgeExe"

# 启动Edge浏览器，使用print-to-pdf功能
$arguments = "--headless --disable-gpu --print-to-pdf=`"$output_pdf`" --no-margins `"$html_file`""

Write-Host "正在转换..."
Start-Process -FilePath $edgeExe -ArgumentList $arguments -Wait -NoNewWindow

Write-Host ""
Write-Host "转换完成！"
Write-Host "PDF已保存到: $output_pdf"

# 检查文件是否存在
if (Test-Path $output_pdf) {
    Write-Host "转换成功！"
} else {
    Write-Host "转换可能未成功，请尝试手动方法"
    Write-Host ""
    Write-Host "手动方法："
    Write-Host "1. 在浏览器中打开: $html_file"
    Write-Host "2. 按 Ctrl+P 打印"
    Write-Host "3. 在打印设置中勾选 '背景图形'"
    Write-Host "4. 选择 '另存为PDF'"
    Write-Host "5. 保存为: $output_pdf"
}

Write-Host ""
Write-Host "按任意键退出..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
