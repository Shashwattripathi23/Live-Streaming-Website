
# views.py
from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import WebcamStream
import cv2


@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def video_feed(request, stream_key):
    return StreamingHttpResponse(generate_frames(stream_key), content_type='multipart/x-mixed-replace; boundary=frame')


def generate_frames(stream_key):
    stream = get_object_or_404(WebcamStream, stream_key=stream_key)
    cap = cv2.VideoCapture(0)

    while True:
        success, frame = cap.read()
        if not success:
            break

        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    cap.release()
