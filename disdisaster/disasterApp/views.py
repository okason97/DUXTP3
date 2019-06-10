from django.shortcuts import render

# Create your views here.
def index(request):
    breadcrumb_list = []
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
        'breadcrumb_list': breadcrumb_list,
    })

def text(request):
    breadcrumb_list = [{
        'name':'Home',
        'link':'index',
        }, {
        'name':'Text',
        'link':'text',
    }]
    text_content = "<h2>Titulo</h2><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Congue eu consequat ac felis. Fermentum leo vel orci porta non pulvinar. Velit scelerisque in dictum non consectetur a erat. Tristique senectus et netus et malesuada fames. Nunc sed id semper risus in hendrerit gravida. Pulvinar proin gravida hendrerit lectus. Laoreet id donec ultrices tincidunt arcu non sodales neque. Orci phasellus egestas tellus rutrum tellus pellentesque. Bibendum est ultricies integer quis auctor elit. Volutpat sed cras ornare arcu dui. Bibendum at varius vel pharetra vel.\n\nPharetra et ultrices neque ornare aenean euismod elementum nisi quis. Viverra accumsan in nisl nisi scelerisque eu ultrices vitae. Consequat semper viverra nam libero justo laoreet sit. Enim eu turpis egestas pretium. Nibh tellus molestie nunc non blandit massa enim. Odio tempor orci dapibus ultrices in iaculis nunc sed augue. Et ultrices neque ornare aenean euismod elementum. Quam lacus suspendisse faucibus interdum posuere lorem ipsum dolor sit. Metus vulputate eu scelerisque felis imperdiet. Fringilla est ullamcorper eget nulla facilisi. Integer eget aliquet nibh praesent tristique magna sit amet purus. Commodo quis imperdiet massa tincidunt. Mollis nunc sed id semper risus in hendrerit gravida. Donec enim diam vulputate ut pharetra sit amet.\n\nPenatibus et magnis dis parturient montes. Pretium nibh ipsum consequat nisl vel pretium. Porttitor lacus luctus accumsan tortor posuere. Pharetra pharetra massa massa ultricies mi quis hendrerit. Vitae purus faucibus ornare suspendisse sed nisi lacus. Odio ut enim blandit volutpat maecenas volutpat. Sagittis vitae et leo duis ut. In hendrerit gravida rutrum quisque non tellus. Dolor sit amet consectetur adipiscing elit ut aliquam. Sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae. Dui sapien eget mi proin sed libero enim sed faucibus. Enim eu turpis egestas pretium aenean pharetra magna. Nec ultrices dui sapien eget mi proin sed libero. Dignissim enim sit amet venenatis urna cursus eget nunc scelerisque. In fermentum et sollicitudin ac. Senectus et netus et malesuada fames.\n\nTincidunt dui ut ornare lectus sit. Nisi porta lorem mollis aliquam ut. Pulvinar sapien et ligula ullamcorper malesuada proin libero nunc consequat. Mauris pharetra et ultrices neque ornare aenean. Eu nisl nunc mi ipsum faucibus vitae. Sagittis purus sit amet volutpat consequat mauris nunc. Est sit amet facilisis magna etiam tempor orci. Lorem sed risus ultricies tristique nulla aliquet enim tortor at. Pulvinar mattis nunc sed blandit libero volutpat sed. Ornare aenean euismod elementum nisi quis eleifend. Et egestas quis ipsum suspendisse ultrices gravida dictum fusce ut. Neque convallis a cras semper auctor. Tellus pellentesque eu tincidunt tortor aliquam nulla facilisi cras fermentum. Adipiscing bibendum est ultricies integer quis auctor elit sed. Elit scelerisque mauris pellentesque pulvinar pellentesque habitant.\n\nSed tempus urna et pharetra pharetra massa. Turpis egestas pretium aenean pharetra. Felis donec et odio pellentesque diam volutpat commodo. Amet purus gravida quis blandit turpis. A diam sollicitudin tempor id eu nisl nunc. Ornare lectus sit amet est placerat in egestas. Erat imperdiet sed euismod nisi porta lorem mollis. Dictum fusce ut placerat orci. Nibh nisl condimentum id venenatis a condimentum. Sem integer vitae justo eget magna fermentum. Massa tincidunt dui ut ornare.</p>"
    return render(request, 'disasterApp/text.html', {
        'text_content': text_content,
        'breadcrumb_list': breadcrumb_list,
    })
    
def ask4Help(request):
    breadcrumb_list = [{
        'name':'Home',
        'link':'index',
        }, {
        'name':'Ask4Help',
        'link':'ask4Help',
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

def disasterInfo(request):
    breadcrumb_list = [{
        'name':'Home',
        'link':'index',
        }, {
        'name':'DisasterInfo',
        'link':'disasterInfo',
    }]
    return render(request, 'disasterApp/disasterInfo.html', {
        'breadcrumb_list': breadcrumb_list,
    })
