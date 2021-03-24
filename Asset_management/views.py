from django.shortcuts import render

from AssetManagement import settings
from Asset_management.models import Zc
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
            return render(request, 'error.html', {'Error': Error})
        zc.ZcName = request.POST.get('IpZcName')
        zc.UsePart = request.POST.get('InUsePart')
        zc.UsePeople = request.POST.get('InUsePeople')
        zc.UseLocat = request.POST.get('InUseLocat')
        # 图片处理开始
        print(request.POST.get('rimg1'))
        if request.FILES.get('img1') != None:
            zc.img1 = request.POST.get('rimg1')
            print('----')
            print(request.POST.get('rimg1'))
        if request.FILES.get('img2') != None:
            zc.img2 = request.POST.get('rimg2')
        if request.FILES.get('img3') != None:
            zc.img3 = request.POST.get('rimg3')
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
            bimg1 = request.POST.get('rimg1')
        if request.FILES.get('img2') != None:
            bimg2 = request.POST.get('rimg2')
        if request.FILES.get('img3') != None:
            bimg3 = request.POST.get('rimg3')
        # 图片处理结束

        NewData = {"ZcName": Name, "UsePart": Part, "UsePeople": People, "UseLocat": Locat, "img1": bimg1,
                   "img2": bimg2, "img3": bimg3}
        # 更新内容判断开始
        if ID != "":
            if len(Zc.objects.filter(ZcId__exact=ID)) != 0:
                for key, value in NewData.items():
                    if value != "":
                        Val = value
                        field = key
                        Zc.objects.filter(ZcId=ID).update(**{field: Val})  # update字段名不支持变量，但支持字典，重新组成字典传入变量
            else:
                zc.ZcId = ID
                zc.save()
                for key, value in NewData.items():
                    if value != "":
                        Val = value
                        field = key
                        Zc.objects.filter(ZcId=ID).update(**{field: Val})
        else:
            Error = '编号不能为空！'
            return render(request, 'error.html', {'Error': Error})
    return render(request, template_name='ok.html')
