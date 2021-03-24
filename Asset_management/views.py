from django.shortcuts import render

from AssetManagement import settings
from Asset_management.models import Zc
from Asset_management.saveimg import saveimg as si
import os


# Create your views here.
def get_index_page(request):
    return render(request, template_name='index.html')


# 接收请求数据 增加
def submit(request):
    if request.method == 'GET':
        return render(request, template_name='index.html')
    elif request.method == 'POST':
        zc = Zc()
        if len(Zc.objects.all().filter(ZcId__exact=request.POST.get('IpZcID'))) == 0:
            zc.ZcId = request.POST.get('IpZcID')
        else:
            Error = '编号重复！'
            return render(request, 'error.html',{'Error':Error})
        zc.ZcName = request.POST.get('IpZcName')
        zc.UsePart = request.POST.get('InUsePart')
        zc.UsePeople = request.POST.get('InUsePeople')
        zc.UseLocat = request.POST.get('InUseLocat')
        # 图片处理开始
        print(request.POST.get('rimg1'))
        if request.FILES.get('img1') != None:
            obj = request.FILES.get('img1')  # get的是 type= ‘file’标签的名字
            file_path = os.path.join(settings.IMG_UPLOAD,
                                     request.POST.get('IpZcName') + 'a.png')  # upload提前创建的文件夹，用于存放上传的文件  obj.name 是文件名
            zc.img1 = si(obj, file_path)
        if request.FILES.get('img2') != None:
            obj2 = request.FILES.get('img2')
            file_path2 = os.path.join(settings.IMG_UPLOAD,
                                     request.POST.get('IpZcName') + 'b.png')  # upload提前创建的文件夹，用于存放上传的文件  obj.name 是文件名
            zc.img2 = si(obj2, file_path2)
        if request.FILES.get('img3') != None:
            obj3 = request.FILES.get('img3')
            file_path3 = os.path.join(settings.IMG_UPLOAD,
                                      request.POST.get('IpZcName') + 'c.png')  # upload提前创建的文件夹，用于存放上传的文件  obj.name 是文件名
            zc.img3 = si(obj3, file_path3)
        zc.save()
        # 图片处理结束
    return render(request, template_name='ok.html')
# 修改
def update(request):
    if request.method == 'GET':
        return render(request, template_name='index.html')
    elif request.method == 'POST':
        zc = Zc()

        ID = request.POST.get('IpZcID')
        Name = request.POST.get('IpZcName')
        Part = request.POST.get('InUsePart')
        People = request.POST.get('InUsePeople')
        Locat = request.POST.get('InUseLocat')
        bimg1 = ''
        bimg2 = ''
        bimg3 = ''

        # 图片处理开始
        if request.FILES.get('img1') != None:
            obj = request.FILES.get('img1')  # get的是 type= ‘file’标签的名字
            file_path = os.path.join(settings.IMG_UPLOAD,
                                     request.POST.get(
                                         'IpZcName') + 'a.png')  # upload提前创建的文件夹，用于存放上传的文件  obj.name 是文件名
            bimg1 = si(obj, file_path)
        if request.FILES.get('img2') != None:
            obj2 = request.FILES.get('img2')
            file_path2 = os.path.join(settings.IMG_UPLOAD,
                                      request.POST.get(
                                          'IpZcName') + 'b.png')  # upload提前创建的文件夹，用于存放上传的文件  obj.name 是文件名
            bimg2 = si(obj2, file_path2)
        if request.FILES.get('img3') != None:
            obj3 = request.FILES.get('img3')
            file_path3 = os.path.join(settings.IMG_UPLOAD,
                                      request.POST.get(
                                          'IpZcName') + 'c.png')  # upload提前创建的文件夹，用于存放上传的文件  obj.name 是文件名
            bimg3 = si(obj3, file_path3)
        # 图片处理结束

        NewData = {"ZcName":Name,"UsePart":Part,"UsePeople":People,"UseLocat":Locat,"img1":bimg1,"img2":bimg2,"img3":bimg3}
        # 更新内容判断开始
        if ID != "":
            if len(Zc.objects.all().filter(ZcId__exact=ID)) != 0:
                for key,value in NewData.items():
                    if value != "":
                        Val = value
                        field = key
                        Zc.objects.filter(ZcId=ID).update(**{field:Val}) #update字段名不支持变量，但支持字典，重新组成字典传入变量
            else:
                Error = '编号不存在！'
                return render(request,'error.html',{'Error':Error})
        else:
            Error = '编号不能为空！'
            return render(request, 'error.html',{'Error':Error})
    return render(request, template_name='ok.html')



