from django.shortcuts import render

# Create your views here.
def cook_off_view(request, *args, **kwargs):
    return render(request, 'cook_off/cook_off.html', {})

def cook_div1_view(request, *args, **kwargs):
    return render(request, 'cook_off/div1/landing.html', {})

def cook_div2_view(request, *args, **kwargs):
    return render(request, 'cook_off/div2/landing.html', {})

def div1A_view(request, *args, **kwargs):
    queryset = Div1A.objects.all().order_by('-accuracy')
    context = {
        "object_list": queryset
    }
    return render(request, 'cook_off/div1/a.html', context)

def div1B_view(request, *args, **kwargs):
    queryset = Div1B.objects.all().order_by('-accuracy')
    context = {
        "object_list": queryset
    }
    return render(request, 'cook_off/div1/b.html', context)

def div1C_view(request, *args, **kwargs):
    queryset = Div1C.objects.all().order_by('-accuracy')
    context = {
        "object_list": queryset
    }
    return render(request, 'cook_off/div1/c.html', context)

def div1D_view(request, *args, **kwargs):
    queryset = Div1D.objects.all().order_by('-accuracy')
    context = {
        "object_list": queryset
    }
    return render(request, 'cook_off/div1/d.html', context)

def div1E_view(request, *args, **kwargs):
    queryset = Div1E.objects.all().order_by('-accuracy')
    context = {
        "object_list": queryset
    }
    return render(request, 'cook_off/div1/e.html', context)

def div1F_view(request, *args, **kwargs):
    queryset = Div1F.objects.all().order_by('-accuracy')
    context = {
        "object_list": queryset
    }
    return render(request, 'cook_off/div1/f.html', context)

def div1G_view(request, *args, **kwargs):
    queryset = Div1G.objects.all().order_by('-accuracy')
    context = {
        "object_list": queryset
    }
    return render(request, 'cook_off/div1/g.html', context)

def div2A_view(request, *args, **kwargs):
    queryset = Div2A.objects.all().order_by('-accuracy')
    context = {
        "object_list": queryset
    }
    return render(request, 'cook_off/div2/a.html', context)

def div2B_view(request, *args, **kwargs):
    queryset = Div2B.objects.all().order_by('-accuracy')
    context = {
        "object_list": queryset
    }
    return render(request, 'cook_off/div2/b.html', context)

def div2C_view(request, *args, **kwargs):
    queryset = Div2C.objects.all().order_by('-accuracy')
    context = {
        "object_list": queryset
    }
    return render(request, 'cook_off/div2/c.html', context)

def div2D_view(request, *args, **kwargs):
    queryset = Div2D.objects.all().order_by('-accuracy')
    context = {
        "object_list": queryset
    }
    return render(request, 'cook_off/div2/d.html', context)

def div2E_view(request, *args, **kwargs):
    queryset = Div2E.objects.all().order_by('-accuracy')
    context = {
        "object_list": queryset
    }
    return render(request, 'cook_off/div2/e.html', context)

def div2F_view(request, *args, **kwargs):
    queryset = Div2F.objects.all().order_by('-accuracy')
    context = {
        "object_list": queryset
    }
    return render(request, 'cook_off/div2/f.html', context)

def div2G_view(request, *args, **kwargs):
    queryset = Div2G.objects.all().order_by('-accuracy')
    context = {
        "object_list": queryset
    }
    return render(request, 'cook_off/div2/g.html', context)

