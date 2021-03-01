

import xlrd
from django.core.paginator import Paginator

from django.shortcuts import render, redirect

# Create your views here.


# 创建一个进行分页处理的函数
# 其中形式参数ob,是接受对那些数据进行分页的，number接收的是返回第几页的数据
from index.models import Seedtable, Waretable


def page_number(ob, number):
    # 分页方法利用Paginator类创建分页对象其中object_list接收的是对那些数据进行分页
    # per_page接收的是每页有几条数据，固定值为每页8条数据
    page = Paginator(object_list=ob, per_page=7)
    # 利用Paginator类的page_range属性，该属性存放的是页码组成的可迭代对象
    page_list = page.page_range
    # 首先就要判读分页以后是不是一共小于等于10页
    if page_list[-1]<=10:
        # 返回页码可迭代对象的时候就直接返回当前的page_list
        number_list = page.page_range
    # 判断需要显示数据的页码是不是小于6页表示显示页码的列表是从1-10
    elif number<6 :
        number_list = page_list[:10]
    # 判断需要显示数据的页码是最后的四页表示显示页码的列表是最后10页
    elif number>page.page_range[-5]:
        number_list = page_list[-10:]
    # 如果需要显示的页码在正常范围内，当前页码就是回显页码列表中的第6个元素
    else:
        number_list = page_list[number-6:number+4]
    #  判断当前页码是否是最后一页，如果是最后一页，就让下一页的页码等于当前页
    #  否则下一页的页码等于当前页码加上1
    if number == page_list[-1]:
        next_number = number
    else:
        next_number = number + 1
    return {
        # 返回当前页的所有数据
        'infos': page.page(number),
        # 返回当前页的页码
        'number': number,
        # 返回上一页的页码
        'per_number': number - 1,
        # 返回下一页的页码
        'next_number': next_number,
        # 返回在页面中提供的页码的列表
        'number_list': number_list,
    }


def index(request):

    return render(request, 'index/index.html')
def things_in(request):
    if request.method=='GET':
        return render(
            request=request,
            template_name="index/index.html"
        )
    if request.method == 'POST':
        name = request.POST.get('name')
        level = request.POST.get('level')
        xingtai = request.POST.get('xingtai')
        number = request.POST.get('number')
        width = request.POST.get('width')
        high = request.POST.get('high')
        address = request.POST.get('address')
        time = request.POST.get('time')
        price = request.POST.get('price')
        cost=request.POST.get('cost')
        phone=request.POST.get('phone')

        Seedtable(name=name, level=level,xingtai=xingtai,width=width
        ,high=high,address=address,number=number,
        time=time,price=price,cost=cost,phone=phone).save()

        return redirect('/index/')

def show(request):
    text = Seedtable.objects.all()
    number = request.GET.get('pagenumber')
    if number:
        data = page_number(text, int(number))
    else:
        data = page_number(text, 1)
            # 返回渲染后的招聘信息的页面的html
    return render(
                request=request,
                template_name='index/show.html',
                # 将该实际参数传递给template对页面进行渲染
                # count表示的是不是我返回的是哪个网站的信息
                context={
                    'count':1,
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
def search(request):
    global search_data
    if request.method == 'POST':
        search_data = request.POST.get('search')
        number = request.GET.get('pagenumber')
        if search_data=='':
            text=Seedtable.objects.all()
        else:
            text=Seedtable.objects.filter(name__icontains=search_data)
        if number:
            data = page_number(text, int(number))
        else:
            data = page_number(text, 1)
    else:
        text = Seedtable.objects.filter(name=search_data)
        number = request.GET.get('pagenumber')
        if number:
            data = page_number(text, int(number))
        else:
            data = page_number(text, 1)
            # 返回渲染后的招聘信息的页面的html
        return render(
            request=request,
            template_name='index/show.html',
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
        template_name='index/show.html',
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

def excel_upload(request,):
        '''
        :param request:
        :return: 上传文件excel表格 ,并进行解析
        '''
        if request.method == "POST":
            f = request.FILES['my_file']
            print(type(f))
            type_excel = f.name.split('.')[1]
            if 'xlsx' == type_excel:
                # 开始解析上传的excel表格
                wb = xlrd.open_workbook(filename=None, file_contents=f.read())  # 关键点在于这里
                table = wb.sheets()[0]
                nrows = table.nrows  # 行数
                for j in range(1,nrows):
                    print(j)
                    rowValues = table.row_values(j)  # 一行的数据
                    name = rowValues[0]
                    level = rowValues[2]
                    xingtai = rowValues[1]
                    number = rowValues[5]
                    width = rowValues[3]
                    high = rowValues[4]
                    address = rowValues[7]
                    time=rowValues[9]
                    print(time)
                    price = rowValues[10]
                    cost = rowValues[8]
                    phone = rowValues[6]
                    print(rowValues[1])
                    Seedtable(name=name, level=level, xingtai=xingtai, width=width
                              , high=high, address=address, number=number,
                               time=time,price=price, cost=cost, phone=phone).save()
            return redirect('/index/')


def manage(request):
    text = Seedtable.objects.all()
    number = request.GET.get('pagenumber')
    if number:
        data = page_number(text, int(number))
    else:
        data = page_number(text, 1)
        # 返回渲染后的招聘信息的页面的html
    return render(
        request=request,
        template_name='index/manage.html',
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

def manage_search(request):
    global search_data
    if request.method == 'POST':
        search_data = request.POST.get('search')
        number = request.GET.get('pagenumber')
        if search_data=='':
            text=Seedtable.objects.all()
        else:
            text=Seedtable.objects.filter(name__icontains=search_data)
        if number:
            data = page_number(text, int(number))
        else:
            data = page_number(text, 1)
    else:
        text = Seedtable.objects.filter(name=search_data)
        number = request.GET.get('pagenumber')
        if number:
            data = page_number(text, int(number))
        else:
            data = page_number(text, 1)
            # 返回渲染后的招聘信息的页面的html
        return render(
            request=request,
            template_name='index/manage.html',
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
        template_name='index/manage.html',
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
def  delete(request):
    my_id=request.GET.get("nid")
    Seedtable.objects.filter(id=my_id).delete()
    print(my_id)
    return redirect("/manage/")
def change(request):
    if request.method == 'POST':
        my_id=request.POST.get('my_id')
        print(my_id)
        my_table=Seedtable.objects.get(id=my_id)
        my_table.name = request.POST.get('name')
        my_table.level = request.POST.get('level')
        my_table.xingtai = request.POST.get('xingtai')
        my_table.number = request.POST.get('number')
        my_table.width = request.POST.get('width')
        my_table.high = request.POST.get('high')
        my_table.address = request.POST.get('address')
        my_table.time = request.POST.get('time')
        my_table.price = request.POST.get('price')
        my_table.cost=request.POST.get('cost')
        my_table.phone=request.POST.get('phone')


        my_table.save()
        return redirect("/manage/")
def edit(request):
    #h获取需要修改的信息的id
    my_id = request.GET.get("nid")
    #根据id获取数据库对象
    table = Seedtable.objects.get(id=my_id)

    name=table.name
    level=table.level
    width=table.width
    high=table.high
    xingtai=table.xingtai
    number=table.number
    phone=table.phone
    address=table.address
    cost=table.cost

    date_time=table.time
    str_time=str(date_time)
    str_time.replace("年", "-")
    str_time.replace("月", "-")
    str_time.replace("日", "-")

    time=str_time

    price=table.price

    return render(
        request,
        'index/edit.html',
        #传输数据给前台
        locals(),
    )
def warehouse(request):
    return render(
        request,
        'index/warehouse.html'
    )
def show_warehouse(request):
    text = Waretable.objects.all()
    number = request.GET.get('pagenumber')
    if number:
        data = page_number(text, int(number))
    else:
        data = page_number(text, 1)
        # 返回渲染后的招聘信息的页面的html
    return render(
        request=request,
        template_name='index/warehouse.html',
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
def search_ware(request):
    global search_data
    if request.method == 'POST':
        search_data = request.POST.get('search')
        number = request.GET.get('pagenumber')
        if search_data == '':
            text = Waretable.objects.all()
        else:
            text = Waretable.objects.filter(name__icontains=search_data)
        if number:
            data = page_number(text, int(number))
        else:
            data = page_number(text, 1)
    else:
        text = Waretable.objects.filter(name=search_data)
        number = request.GET.get('pagenumber')
        if number:
            data = page_number(text, int(number))
        else:
            data = page_number(text, 1)
            # 返回渲染后的招聘信息的页面的html
        return render(
            request=request,
            template_name='index/warehouse.html',
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
    return render(
        request=request,
        template_name='index/warehouse.html',
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
def warehousein(request):
    if request.method=='GET':
        return render(
            request=request,
            template_name="index/warehouse.html"
        )
    if request.method == 'POST':
        name = request.POST.get('name')
        level = request.POST.get('level')
        xingtai = request.POST.get('xingtai')
        number = request.POST.get('number')
        width = request.POST.get('width')
        high = request.POST.get('high')
        time = request.POST.get('time')
        price = request.POST.get('price')
        cost=request.POST.get('cost')
        phone=request.POST.get('phone')

        Waretable(name=name, level=level,xingtai=xingtai,width=width
        ,high=high,number=number,
        time=time,price=price,cost=cost,phone=phone).save()

        return redirect('/warehouse/')

def edit_ware(request):
    #h获取需要修改的信息的id
    my_id = request.GET.get("nid")
    #根据id获取数据库对象
    table = Waretable.objects.get(id=my_id)

    name=table.name
    level=table.level
    width=table.width
    high=table.high
    xingtai=table.xingtai
    number=table.number
    phone=table.phone
    address=table.address
    cost=table.cost

    date_time=table.time
    str_time=str(date_time)
    str_time.replace("年", "-")
    str_time.replace("月", "-")
    str_time.replace("日", "-")

    time=str_time

    price=table.price

    return render(
        request,
        'index/ware_edit.html',
        #传输数据给前台
        locals(),
    )

def  delete_ware(request):
    my_id=request.GET.get("nid")
    Seedtable.objects.filter(id=my_id).delete()
    print(my_id)
    return redirect("/warehouse/")
def change_ware(request):
    if request.method == 'POST':
        my_id=request.POST.get('my_id')
        print(my_id)
        my_table=Waretable.objects.get(id=my_id)
        my_table.name = request.POST.get('name')
        my_table.level = request.POST.get('level')
        my_table.xingtai = request.POST.get('xingtai')
        my_table.number = request.POST.get('number')
        my_table.width = request.POST.get('width')
        my_table.high = request.POST.get('high')
        my_table.time = request.POST.get('time')
        my_table.price = request.POST.get('price')
        my_table.cost=request.POST.get('cost')
        my_table.phone=request.POST.get('phone')


        my_table.save()
        return redirect("/warehouse/")