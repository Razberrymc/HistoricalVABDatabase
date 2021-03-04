#Run this script in the Anaconda command prompt!
from docx2pdf import convert
import os

fileList = []

for filename in os.listdir(r'C:\Users\mclark\Desktop\python\flask'):
    if filename.endswith('.docx'):
        #print(os.path.join(r'C:\Users\mclark\Desktop\python\flask', filename))
        fileList.append(os.path.join(filename))
        continue
    else:
        continue

n = 0

fileList2 = [y.strip('.docx') for y in fileList]

fileList3 = [s + '.pdf' for s in fileList2]

#Ensure that the word doc or folder is in the same folder as the .py file
#When you receive a folder of word docs you can bulk convert by inputting the folder name
for iterate in range(len(fileList)):
    convert(fileList[n])

#Below is used once you have the Big Document Folder

#pdfList = []

#for pdf in os.listdir(r'C:\Users\mclark\Desktop\python\flask'):
    #if pdf.endswith(".pdf"):
        #pdfList.append(os.path.join(r'C:\Users\mclark\Desktop\python\flask', pdf))
        #continue
    #else:
        #continue

    from pdf2image import convert_from_path
    pages = convert_from_path(fileList3[n], 500)

    n = n+1

    i = 0

    for page in pages:
        i = i+1
        page.save('image' + str(i) + '.png', 'PNG')

    import tesseract
    tesseract.findFunc()

    continue

for filename in os.listdir(r'C:\Users\mclark\Desktop\python\flask'):
        if filename.endswith('.txt'):
            os.remove(filename)
