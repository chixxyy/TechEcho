import json

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string

from answers.models import Answer
from questions.models import Question


def home_index(request):
    return render(request, "home/index.html")


def search_form_index(request):
    return render(request, "search/search_form.html")


def search_view(request):
    query = request.GET.get("q", "")
    results = []
    search_terms = []
    if query:
        try:
            tags = json.loads(query)
            if isinstance(tags, list):
                search_terms = [
                    tag["value"]
                    for tag in tags
                    if isinstance(tag, dict) and "value" in tag
                ]
            elif isinstance(tags, dict) and "value" in tags:
                search_terms = [tags["value"]]
            else:
                search_terms = [query]
        except json.JSONDecodeError:
            search_terms = [query]

        q_objects = Q()
        for term in search_terms:
            q_objects |= Q(title__icontains=term) | Q(details__icontains=term)

        results = Question.objects.filter(q_objects).distinct()

    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        html = render_to_string("search/search_results.html", {"results": results})
        return JsonResponse({"html": html})
    else:
        return render(
            request,
            "search/search_form.html",
            {"results": results, "query": ", ".join(search_terms)},
        )
