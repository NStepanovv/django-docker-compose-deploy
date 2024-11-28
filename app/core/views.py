from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from .models import Video

def get_video(request, week_number):
    """Получить информацию о видео по номеру недели."""
    video = get_object_or_404(Video, week_number=week_number)
    if now().date() >= video.access_date:
        return JsonResponse({"title": video.title, "video_url": video.video_file.url})
    else:
        return JsonResponse({"message": f"Данное видео пока недоступно. Дата доступа: {video.access_date}"}, status=403)

def get_last_available_video(request):
    """Получить последнее доступное видео."""
    today = now().date()
    video = Video.objects.filter(access_date__lte=today).order_by('-access_date').first()
    if video:
        return JsonResponse({"title": video.title, "video_url": video.video_file.url})
    return JsonResponse({"message": "Нет доступных видео"}, status=404)