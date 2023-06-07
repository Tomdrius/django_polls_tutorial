from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question

def index(request): # request => obiekt HttpRequest, który zawiera informacje o żądaniu HTTP przekazanym do widoku {request=<HttpRequest object>}
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = { # context is a dictionary mapping template variable names to Python objects
        "latest_question_list": latest_question_list,
    }
    return render( request, "ankieta/index.html", context) # The render() function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument. It returns an HttpResponse object of the given template rendered with the given context.


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # try: longer version over
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    return render(request, "ankieta/detail.html", {"question": question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "ankieta/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # request.POST['choice'] returns the ID of the selected choice, as a string
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "ankieta/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("ankieta:results", args=(question.id,)))