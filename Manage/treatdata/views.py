
import time

from django.db.models import Q
from django.shortcuts import render

from index.views import page_number
from treatdata.models import DataFromweb
#计算价格平均值
def avaerage(ob):
    total=0
    for i in ob:
        total+=float(i.price)
    if len(ob)==0:
        return 0
    else:
        return total/len(ob)
# Create your views here.
#对数据进行处理分析，进行显示
def treat_data(request):
    now_year = time.gmtime().tm_year
    now_month = time.gmtime().tm_mon
    if request.method == 'POST':
        year=request.POST.get('select_year')
        print(year)
    else:
        year=now_year
        print(year)

    yulan   = DataFromweb.objects.filter(Q(productname__icontains="花") )
    haitang = DataFromweb.objects.filter(Q(productname__icontains="树"))
    wujiaofeng = DataFromweb.objects.filter(Q(productname__icontains="花") )
    dingxiang = DataFromweb.objects.filter(Q(productname__icontains="枫"))
    for i in yulan:
        print(i.mj)
    seclect_year=year
    average_year_yulan     = avaerage(yulan.filter(time__year=year))
    month_yuan_jan_average = avaerage(yulan.filter(time__year=year,time__month=1))
    month_yuan_feb_average = avaerage(yulan.filter(time__year=year, time__month=2))
    month_yuan_mar_average = avaerage(yulan.filter(time__year=year, time__month=3))
    month_yuan_apr_average = avaerage(yulan.filter(time__year=year, time__month=4))
    month_yuan_may_average = avaerage(yulan.filter(time__year=year, time__month=5))
    month_yuan_jun_average = avaerage(yulan.filter(time__year=year, time__month=6))
    month_yuan_jul_average = avaerage(yulan.filter(time__year=year, time__month=7))
    month_yuan_aug_average = avaerage(yulan.filter(time__year=year, time__month=8))
    month_yuan_sep_average = avaerage(yulan.filter(time__year=year, time__month=9))
    month_yuan_oct_average = avaerage(yulan.filter(time__year=year, time__month=10))
    month_yuan_nov_average = avaerage(yulan.filter(time__year=year, time__month=11))
    month_yuan_dec_average = avaerage(yulan.filter(time__year=year, time__month=12))

    average_year_haitang   = avaerage(haitang.filter(time__year=year))
    month_haitang_jan_average = avaerage(haitang.filter(time__year=year, time__month=1))
    month_haitang_feb_average = avaerage(haitang.filter(time__year=year, time__month=2))
    month_haitang_mar_average = avaerage(haitang.filter(time__year=year, time__month=3))
    month_haitang_apr_average = avaerage(haitang.filter(time__year=year, time__month=4))
    month_haitang_may_average = avaerage(haitang.filter(time__year=year, time__month=5))
    month_haitang_jun_average = avaerage(haitang.filter(time__year=year, time__month=6))
    month_haitang_jul_average = avaerage(haitang.filter(time__year=year, time__month=7))
    month_haitang_aug_average = avaerage(haitang.filter(time__year=year, time__month=8))
    month_haitang_sep_average = avaerage(haitang.filter(time__year=year, time__month=9))
    month_haitang_oct_average = avaerage(haitang.filter(time__year=year, time__month=10))
    month_haitang_nov_average = avaerage(haitang.filter(time__year=year, time__month=11))
    month_haitang_dec_average = avaerage(haitang.filter(time__year=year, time__month=12))

    average_year_wujiaofeng = avaerage(wujiaofeng.filter(time__year=year))
    month_wujiaofeng_jan_average = avaerage(wujiaofeng.filter(time__year=year, time__month=1))
    month_wujiaofeng_feb_average = avaerage(wujiaofeng.filter(time__year=year, time__month=2))
    month_wujiaofeng_mar_average = avaerage(wujiaofeng.filter(time__year=year, time__month=3))
    month_wujiaofeng_apr_average = avaerage(wujiaofeng.filter(time__year=year, time__month=4))
    month_wujiaofeng_may_average = avaerage(wujiaofeng.filter(time__year=year, time__month=5))
    month_wujiaofeng_jun_average = avaerage(wujiaofeng.filter(time__year=year, time__month=6))
    month_wujiaofeng_jul_average = avaerage(wujiaofeng.filter(time__year=year, time__month=7))
    month_wujiaofeng_aug_average = avaerage(wujiaofeng.filter(time__year=year, time__month=8))
    month_wujiaofeng_sep_average = avaerage(wujiaofeng.filter(time__year=year, time__month=9))
    month_wujiaofeng_oct_average = avaerage(wujiaofeng.filter(time__year=year, time__month=10))
    month_wujiaofeng_nov_average = avaerage(wujiaofeng.filter(time__year=year, time__month=11))
    month_wujiaofeng_dec_average = avaerage(wujiaofeng.filter(time__year=year, time__month=12))

    average_year_dingxiang   = avaerage(dingxiang.filter(time__year=year))
    month_dingxiang_jan_average = avaerage(dingxiang.filter(time__year=year, time__month=1))
    month_dingxiang_feb_average = avaerage(dingxiang.filter(time__year=year, time__month=2))
    month_dingxiang_mar_average = avaerage(dingxiang.filter(time__year=year, time__month=3))
    month_dingxiang_apr_average = avaerage(dingxiang.filter(time__year=year, time__month=4))
    month_dingxiang_may_average = avaerage(dingxiang.filter(time__year=year, time__month=5))
    month_dingxiang_jun_average = avaerage(dingxiang.filter(time__year=year, time__month=6))
    month_dingxiang_jul_average = avaerage(dingxiang.filter(time__year=year, time__month=7))
    month_dingxiang_aug_average = avaerage(dingxiang.filter(time__year=year, time__month=8))
    month_dingxiang_sep_average = avaerage(dingxiang.filter(time__year=year, time__month=9))
    month_dingxiang_oct_average = avaerage(dingxiang.filter(time__year=year, time__month=10))
    month_dingxiang_nov_average = avaerage(dingxiang.filter(time__year=year, time__month=11))
    month_dingxiang_dec_average = avaerage(dingxiang.filter(time__year=year, time__month=12))
    return render(
        request,
        'treat_data/treat.html',
        locals(),

    )

def show_data(request):
    text = DataFromweb.objects.all()
    number = request.GET.get('pagenumber')
    if number:
        data = page_number(text, int(number))
    else:
        data = page_number(text, 1)
        # 返回渲染后的招聘信息的页面的html
    return render(
        request=request,
        template_name='treat_data/show_data.html',
        # 将该实际参数传递给template对页面进行渲染
        # count表示的是不是我返回的是哪个网站的信息
        context={
            'count': 1,
            # 传递的是需要展示的信息
            'data': data['infos'],
            # 传递的是页码的显示范围
            'page_list': data['number_list'],
            # 传递的是当前显示的页码
            'number': data['number'],
            # 传递的是上一页的页码
            'per_number': data['per_number'],
            # 传递的是下一页的页码
            'next_number': data['next_number']
        }
    )
def search_data(request):
    global search_data
    if request.method == 'POST':
        search_data = request.POST.get('search')
        number = request.GET.get('pagenumber')
        if search_data=='':
            text=DataFromweb.objects.all()
        else:
            text=DataFromweb.objects.filter(productname__icontains=search_data)
        if number:
            data = page_number(text, int(number))
        else:
            data = page_number(text, 1)
    else:
        text = DataFromweb.objects.filter(productname__icontains=search_data)
        number = request.GET.get('pagenumber')
        if number:
            data = page_number(text, int(number))
        else:
            data = page_number(text, 1)
            # 返回渲染后的招聘信息的页面的html
        return render(
            request=request,
            template_name='treat_data/show_data.html',
            # 将该实际参数传递给template对页面进行渲染
            # count表示的是不是我返回的是哪个网站的信息
            context={
                'count':2,
                # 传递的是需要展示的信息
                'data': data['infos'],
                # 传递的是页码的显示范围
                'page_list': data['number_list'],
                # 传递的是当前显示的页码
                'number': data['number'],
                # 传递的是上一页的页码
                'per_number': data['per_number'],
                # 传递的是下一页的页码
                'next_number': data['next_number']
            }
        )
    return render(
        request=request,
        template_name='treat_data/show_data.html',
        # 将该实际参数传递给template对页面进行渲染
        # count表示的是不是我返回的是哪个网站的信息
        context={
            'count': 2,
            # 传递的是需要展示的信息
            'data': data['infos'],
            # 传递的是页码的显示范围
            'page_list': data['number_list'],
            # 传递的是当前显示的页码
            'number': data['number'],
            # 传递的是上一页的页码
            'per_number': data['per_number'],
            # 传递的是下一页的页码
            'next_number': data['next_number']
        }
    )
