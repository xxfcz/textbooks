import glob
import fitz  # 导入本模块需安装pymupdf库
import os

# 将文件夹中所有jpg图片全部转换为一个指定名称的pdf文件，并保存至指定文件夹
def pic2pdf_1(img_path, pdf_path, pdf_name):
    doc = fitz.open()

    for img in sorted(glob.glob(img_path + r"\*.jpg")):  # 读取图片，确保按文件名排序
        # print(img)  # 输出图片地址
        imgdoc = fitz.open(img)                 # 打开图片
        pdfbytes = imgdoc.convertToPDF()        # 使用图片创建单页的 PDF
        imgpdf = fitz.open("pdf", pdfbytes)
        doc.insertPDF(imgpdf)                   # 将当前页插入文档
    doc.save(pdf_path + pdf_name)               # 保存pdf文件
    doc.close()

if __name__ == '__main__':
    img_path = r'E:\download\物理'
    pdf_path = r'E:\xxf\崽\八年级上\电子课本'
    pdf_name1 =r'/物理_八上.pdf'
    pic2pdf_1(img_path=img_path, pdf_path=pdf_path, pdf_name=pdf_name1)

