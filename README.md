# PDFImageExtractor

PDFImageExtractor是一个从 PDF 文件中提取图像的 Python GUI使用程序。使用pyinstaller打包成执行文件。
使用PyMuPDF和等库Pillow，它可以高效地扫描 PDF 的每一页，隔离嵌入的图像，并将它们保存在指定的目录中。

# Windows 打包 exe 文件
```angular2html
 pyinstaller --onefile --windowed --icon=app.ico .\main.py 
```


**项目截图**

![项目截图](https://github.com/Zzhenping/PDFImageExtractor/blob/main/docs/image.png?raw=true)