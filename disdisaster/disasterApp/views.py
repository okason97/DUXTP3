from django.shortcuts import render
import re

def getDisasterList():
    disasterList = []
    disasterList.append({
        'name': 'Inundación',
        'description': 'No te hundas',
        'image': '/media/disasterApp/inundacion.jpg',
        'template': 'inundacion.html'
    })
    disasterList.append({
        'name': 'Tornado',
        'description': 'No te vueles',
        'image': '/media/disasterApp/tornado.jpg',
        'template': 'lorenIpsum.html'
    })
    disasterList.append({
        'name': 'Aluvión',
        'description': 'No te deslices',
        'image': '/media/disasterApp/aluvion.jpg',
        'template': 'lorenIpsum.html'
    })
    disasterList.append({
        'name': 'Terremoto',
        'description': 'No seas tipo electrico',
        'image': '/media/disasterApp/terremoto.jpg',
        'template': 'terremoto.html'
    })
    disasterList.append({
        'name': 'Erupcion',
        'description': 'No te tires a la lava',
        'image': '/media/disasterApp/volcan.jpg',
        'template': 'lorenIpsum.html'
    })
    disasterList.append({
        'name': 'Incendio',
        'description': 'No te quemes',
        'image': '/media/disasterApp/incendio.jpg',
        'template': 'lorenIpsum.html'
    })
    disasterList.append({
        'name': 'Tormenta de nieve',
        'description': 'No te congeles',
        'image': '/media/disasterApp/frio.jpg',
        'template': 'lorenIpsum.html'
    })
    disasterList.append({
        'name': 'Epidemias',
        'description': 'STARS',
        'image': '/media/disasterApp/epidemia.jpg',
        'template': 'lorenIpsum.html'
    })
    return disasterList
def findByName(list,name):
    for element in list:
        if (element['name'] == name):
            return element
    return None


def mobile(request):
    MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)

    if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
        return True
    else:
        return False

def to_small(disaster):
    disaster['image'] = disaster['image'].split('.',1)[0] + '_small.jpg'
    return disaster

# Create your views here.
def index(request):
    breadcrumb_list = [{
        'name':'Home',
        'link':'index'
    }]
    disasterList = getDisasterList()

    if mobile(request):
        disasterList = map(to_small, disasterList)

    return render(request, 'disasterApp/index.html', {
        'disasterList': disasterList,
        'breadcrumb_list': breadcrumb_list,
    })

def text(request, disasterName):
    breadcrumb_list = [{
        'name':'Home',
        'link':'index',
        }, {
        'name': disasterName,
        'link':'text',
    }]

    disasterList = getDisasterList()
    disaster = findByName(disasterList, disasterName)
    if disaster is not None:
        return render(request, 'disasterApp/'+disaster['template'], {
            'breadcrumb_list': breadcrumb_list,
        })
    else:
        return render(request, 'disasterApp/lorenIpsum.html', {
            'breadcrumb_list': breadcrumb_list,
        })
    
def ask4Help(request):
    breadcrumb_list = [{
        'name':'Home',
        'link':'index',
        }, {
        'name':'Pedir ayuda',
        'link':'Pedir ayuda',
    }]
    if request.POST:
        return render(request, 'disasterApp/ask4Help.html', {
            'helpSent': True, 
            'telephone' : request.POST["telephone"],
            'breadcrumb_list': breadcrumb_list,
        })
    else:
        return render(request, 'disasterApp/ask4Help.html',  {
            'helpSent': False,
            'breadcrumb_list': breadcrumb_list,
        })
