from django.shortcuts import render

# Create your views here.

# http://127.0.0.1:8000/


def audio_test(request):

    audio_file = "/audio/admiral_mcraven_speech.mp3"

    # audio_file = '/audio/eric_sprott.mp3'
    # audio_file = "/audio/all_in_rkj_interview.mp3"
    # audio_file = "/audio/david_lin_interview_doomberg.mp3"
    # audio_file = "/audio/forward_guidance_micheal_pettis.mp3"
    context = {
        'audio_file': audio_file,
    }
    return render(request, 'audio_test.html', context)

