import requests
import xlwt
from xlwt import Workbook

url = 'http://search.sunbiz.org/Inquiry/CorporationSearch/ByDocumentNumber'
myobj = {'SearchTerm': 'N20000004118','InquiryType': 'DocumentNumber'}


x = requests.post(url, data = myobj)

x=str(x.content,"UTF-8")

#print the response text (the content of the requested file):
finalDoc=list()
#print(x.text)
list=x.split("\r\n")
print(list)
details=dict()
details['corpName'] = ""
details['mailAddress'] = ""
for i in range(len(list)):

    if "detailSection corporationName" in list[i]:
        i=i+1
        print("corp available")
        while "</div>" not in list[i]:
            details['corpName']=details['corpName']+list[i].replace("<p>","").replace("</p>","").strip()+"\r\n"
            i=i+1

    if  "<span>Mailing Address</span>" in list[i]:
        i=i+1
        while "</div>" not in list[i]:
            if len(list[i].replace("<span>","").replace("<div>","").replace("\r\n","").replace("<br>","").replace("<br/>","").replace("\r\n","").strip())!=0:
                details['mailAddress']=details['mailAddress']+list[i].replace("<span>","").replace("<div>","").replace("<br>","").replace("<br/>","").replace("\r\n","").strip()+"\r\n"
            i=i+1

print(details)
wb = Workbook()

# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('sheet1.xls')
# title
style = xlwt.easyxf('font: bold 1, color red;')
sheet1.write(0, 0, details['corpName']+details['mailAddress'])

wb.save('DocsInfo.xls')










