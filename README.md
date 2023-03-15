# scan2sides
手动双面扫描后，用来把页序调整过来的小脚本

## 问题
市面上的打印一体机的进纸器一般都是单面扫描的，如果要用进纸器扫描双面文档的话，就得正面扫一次，背面扫一次，这样页码就乱掉了。

例如，对于一个有6页的双面文档，正面看过去是`1,3,5`页，背面看过去是`6,4,2`页。这样你正面然后背面扫完之后，合成得到的pdf文档页序就是`1,3,5,6,4,2`页。需要把这个页码整理过来。
## 方法
不难看出两种整理方法：
1. 依次从文档的头、尾各取一页，组合成新的文档，循环总页数的一半次；
2. 依次把最后一页前移到它应在的位置上，循环总页数的一半减一次。

第二种方法少循环一次，因为过程如下：

 - `1,3,5,6,4,2` 
 -  `1,2,3,5,6,4`  
 -  `1,2,3,4,5,6`

由于第二次循环结束后，`6`页自己就已在文档最后，所以不需要移动了，这样就省了一次循环。因此这里我是用的第二种方法。使用`fitz`包，工作的部分只需两行：
```python
for i in range(pagenum//2-1): 
   pdf_in.move_page(pagenum-1,2*i+1)
```
即：循环总页数一半减一等于两（`pagenum//2-1`）次，把最后一页（`pagenum-1`）移动（`move_page()`）到它本来的后一页（`2*i+1`）之前（注意fitz的页码是从0开始的）。
## 代码
添加上程序必要的上下文之后，就得到了最简的实现代码：
 ```python
 import fitz
 pdf_in = fitz.open('myscan.pdf')
 pagenum = pdf_in.page_count
for i in range(pagenum//2-1): 
    pdf_in.move_page(pagenum-1,2*i+1)
pdf_in.save('[altered]myscan.pdf')
```
自己偶尔一用的话，这样就可以了。

如果你想更用户友好一点，比如使用图形化界面选取文件啦，打印一些提示啦，最后封装成exe传给文秘点开就用之类的，可再添加一点额外的细节，比如附件中的例子。
