import fitz,os
from tkinter import filedialog

def main():
    print("这是一个能把手动双面扫描的pdf的页面梳理顺序的小脚本。——wyx230314\n")
    while 1:
        print("打开文件……")
        f_path = filedialog.askopenfilename(initialdir='./',filetypes=(('PDF files','*.pdf'),))
        if not f_path:
            print("未选择，退出。")
            exit()

        print("处理中……")
        pdf_in = fitz.open(f_path) # 读取一个pdf文件
        (pre_path,file_name)=os.path.split(f_path)

        pagenum=pdf_in.page_count
        if pagenum%2!=0:
            input("总页数不是偶数，不对吧！按回车退出。")
            exit()

        # 核心仅是下面两句话！举例：4面的双面文档，正面、背面扫描后，生成文档的页码顺序是1,3,4,2。
        # 故不停把最后一页移到前面的相应位置即可：
        for i in range(pagenum//2-1): #整除！
            pdf_in.move_page(pagenum-1,2*i+1)

        new_name=pre_path+"/[已理序]"+file_name
        pdf_in.save(new_name)
        print("\n已完成，保存到"+new_name+"\n")
        input("按回车再处理一份……")

if __name__=="__main__":
    main()