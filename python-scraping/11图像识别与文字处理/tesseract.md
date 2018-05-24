## Tesseract
Tesseract 是目前公认最优秀、最精确的开源 OCR 系统

Tesseract 是一个 Python 的命令行工具

### 安装
- 在 Windows 系统上，下载方便的可执行安装文件（https://code.google.com/p/tesseract-ocr/
downloads/list）安装即可

- $sudo apt-get tesseract-ocr

### 数据文件
- 要使用 Tesseract 的功能，比如后面的示例中训练程序识别字母，你需要先在系统中设置一
个新的环境变量 $TESSDATA_PREFIX ，让 Tesseract 知道训练的数据文件存储在哪里
- linux: $export TESSDATA_PREFIX=/usr/local/share/
- windows: #setx TESSDATA_PREFIX C:\Program Files\Tesseract OCR\
