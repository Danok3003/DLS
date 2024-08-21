from django.shortcuts import render
from detection.models import Det_model, Det_result
from .Yolo_detection import Detection_YOLO
from django.core.files.base import ContentFile
import os

def detect_view(request):
    photo = Det_model.objects.first()
    photo_res = False
    if request.method == 'POST':
        if request.FILES:
            try:
                del_photo = Det_model.objects.get(title='Пользовательское фото')
                del_photo.delete()
            except:
                pass
            file = request.FILES['new_photo']
            new_photo = Det_model()
            new_photo.title = 'Пользовательское фото'
            new_photo.file = file
            new_photo.save()

            # Подгрузка пути
            photo = Det_model.objects.get(title='Пользовательское фото')
            photo.photo = photo.file.name
            photo.save()

            path_save = Detection_YOLO(photo.photo.name.split('/')[-1])
        else:
            path_save = Detection_YOLO(photo.photo.name.split('/')[-1])
        # for ph in photo:
        #     path_save = Detection_YOLO(ph.photo.url)
            # new_image = Det_result()
            # new_image.title = 'test'
            # new_image.photo = path_save
            # new_image.save()

        photo_res = os.path.join('../../', path_save[10:])
    content = {
        'photo': photo,
        'photo_res': photo_res if photo_res else None
    }

    return render(request, 'detection/Detect_page.html', content)
