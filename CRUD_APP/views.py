from django.shortcuts import render,redirect

from . models import *
from ACCOUNT.models import *

# Create your views here.

# home page
def index(request):
    return render(request, 'index.html')

# menu
def Menu(request):
    main_course = MAIN_COURSE.objects.all()
    return render(request, 'menu.html',locals())

# add food items
def Add_Food_Items_Form(request):
    return render(request,'Add-Food-Items.html')

# adding main-course

def Add_Main_Course(request):
    if request.method == "POST":
        item_code = request.POST.get('item_code')
        item_name = request.POST.get('item_name').title()
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        image = request.FILES.get('image')

        #print(item_code,item_name,price,quantity)

        try:
            MAIN_COURSE.objects.get(item_code=item_code)
            return render(request, 'Add-Food-Items.html', {'error': 'already exists..!'})
        except MAIN_COURSE.DoesNotExist:
            main_course = MAIN_COURSE.objects.create(item_code=item_code,
                                                     item_name=item_name,
                                                     price=price,
                                                     quantity=quantity,
                                                     image=image,
                                                     category="main-course"
                                                     )
            main_course.save()

            return redirect(Menu)
    else:
        return redirect(Add_Food_Items_Form)


# delete main-course
def delete_main_course(request,id):
    MAIN_COURSE.objects.filter(id=id).delete()
    return redirect(Menu)


# update main-course
def update_main_course(request, id):
    main_course = MAIN_COURSE.objects.filter(id=id)
    return render(request, 'update-main-course.html', locals())


# updating
def update_new_main_course(request,id):
    if request.method == "POST":
        item_code = request.POST.get('item_code')
        item_name = request.POST.get('item_name').title()
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        MAIN_COURSE.objects.filter(id=id).update(item_code=item_code,
                                                 item_name=item_name,
                                                 price=price,
                                                 quantity=quantity)
        return redirect(Menu)
    else:
        return redirect(update_main_course)
