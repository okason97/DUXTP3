from django.shortcuts import render

# Create your views here.
def index(request):
    disasterList = []
    disasterList.append({
        'name': 'Inundación',
        'description': 'No te hundas',
        'image': '/media/disasterApp/inundacion.jpg'
    })
    disasterList.append({
        'name': 'Tornado',
        'description': 'No te vueles',
        'image': '/media/disasterApp/tornado.jpg'
    })
    disasterList.append({
        'name': 'Aluvión',
        'description': 'No te deslices',
        'image': '/media/disasterApp/aluvion.jpg'
    })
    disasterList.append({
        'name': 'Terremoto',
        'description': 'No seas tipo electrico',
        'image': '/media/disasterApp/terremoto.jpg'
    })
    disasterList.append({
        'name': 'Erupcion',
        'description': 'No te tires a la lava',
        'image': '/media/disasterApp/volcan.jpg'
    })
    disasterList.append({
        'name': 'Incendio',
        'description': 'No te quemes',
        'image': '/media/disasterApp/incendio.jpg'
    })
    disasterList.append({
        'name': 'Tormenta de nieve',
        'description': 'No te congeles',
        'image': '/media/disasterApp/frio.jpg'
    })
    disasterList.append({
        'name': 'Epidemias',
        'description': 'STARS',
        'image': '/media/disasterApp/epidemia.jpg'
    })
    return render(request, 'disasterApp/index.html', {
        'disasterList': disasterList,
    })

def ask4Help(request):
    return render(request, 'disasterApp/ask4Help.html', )

def disasterInfo(request):
    return render(request, 'disasterApp/disasterInfo.html', )