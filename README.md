# PDFImageExtractor

PDFImageExtractor是一个从 PDF 文件中提取图像的 Python GUI使用程序。使用pyinstaller打包成执行文件。
使用PyMuPDF和等库Pillow，它可以高效地扫描 PDF 的每一页，隔离嵌入的图像，并将它们保存在指定的目录中。

# 安装与运行
如果下载了预编译的打包文件，可以直接运行。

##### 下载预编译文件
- [Windows](https://github.com/Zzhenping/PDFImageExtractor/releases/download/v1.0.0.0/PDFImageExtractor.exe)

##### 源码安装（Python 版本）
- 克隆该项目
```angular2html
git clone https://github.com/Zzhenping/PDFImageExtractor.git
```

- 安装依赖
```angular2html
pip install -r requirements.txt
```

- 运行
```angular2html
python main.py
```

# Windows 打包 exe 文件
```angular2html
 pyinstaller --onefile --windowed --icon=app.ico .\main.py 
```

**项目截图**

![项目截图](https://github.com/Zzhenping/PDFImageExtractor/blob/main/docs/image.png?raw=true)