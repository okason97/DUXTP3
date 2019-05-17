from django.shortcuts import render

# Create your views here.
def index(request):
    disasterList = []
    disasterList.append({
        'name': 'Inundación',
        'description': 'mucha agua',
        'image': '../media/inundacion.jpg'
    })
    disasterList.append({
        'name': 'Tornado y tormenta electrica',
        'description': 'thundurus',
        'image': '../media/tornado.webp'
    })
    disasterList.append({
        'name': 'Aluvión y deslizamiento',
        'description': 'slide',
        'image': '../media/aluvion.jpeg'
    })
    disasterList.append({
        'name': 'Terremoto',
        'description': 'graveler',
        'image': '../media/terremoto.jpg'
    })
    disasterList.append({
        'name': 'Erupcion volcanica y ceniza',
        'description': 'groundoun',
        'image': '../media/volcan.jpg'
    })
    disasterList.append({
        'name': 'Incendio silvestre',
        'description': 'charizard',
        'image': '../media/incendio.jpg'
    })
    disasterList.append({
        'name': 'tormenta de nieve y helada',
        'description': 'abomasnow',
        'image': '../media/frio.jpg'
    })
    disasterList.append({
        'name': 'epidemias, brotes y pandemias',
        'description': 'resident evil',
        'image': '../media/epidemia.jpg'
    })
    return render(request, 'disasterApp/index.html', {
        'disasterList': disasterList,
    })