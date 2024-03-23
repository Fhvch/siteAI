from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from transformers import pipeline


summarizer = pipeline("summarization", model="facebook/blenderbot-400M-distill")

@csrf_protect
def generate(request):
    error = ''
    summarizer_ans = ''

    if request.method == 'POST':
            input_text = request.POST.get('input_text')
            summarizer_output = summarizer(input_text, max_length=130, min_length=30, do_sample=False)
            summarizer_ans = summarizer_output[0]['summary_text']
            error = 'Форма заполнена неверно'

    data = {
        'error': error,
        'summarizer_ans': summarizer_ans,
    }
    return render(request, 'AI/AI_home.html', data)

