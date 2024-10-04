from django.db.models import OuterRef, Subquery
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, CreateView
from django_filters.views import FilterView

from laptops.filters import LaptopFilter
from laptops.forms import AnswerForm
from laptops.models import Laptop, Answer, Question
from laptops.utils import prepare_form_data


class LaptopListView(FilterView):

    template_name = "laptops.html"
    model = Laptop
    filterset_class = LaptopFilter

    class Meta:
        model = Laptop


class LaptopCreateView(CreateView):

    model = Laptop

    fields = ["name", "brand", "vendor", "image"]

    template_name = "laptop_form.html"


class AnswerCreateView(CreateView):
    template_name = "answer_form.html"
    form_class = AnswerForm

    def get_initial(self):
        initial = super().get_initial()
        answer = Answer.objects.filter(id=4).first()
        initial["comment"] = answer.comment
        return initial

    def get_success_url(self):
        return ""

class MultiAnswerFormView(TemplateView):
    template_name = "report_questions_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        answers = Answer.objects.filter(question_id=OuterRef('pk')).values("comment")[:1]

        questions = Question.objects.filter(parent=1)
        questions_with_found_user_answer = questions.annotate(
            found_answer=Subquery(answers)
        )
        context["questions"] = questions_with_found_user_answer
        return context

    def post(self, request, *args, **kwargs):
        questions = request.POST.getlist("question")
        # [question 1, question 2]
        contents = request.POST.getlist("comment")
        # [comment 1, comment 2]
        answers = list(zip(questions, contents))

        # [(question 1, comment1), (question 2, comment 2)]

        for answer in answers:
            form_param = prepare_form_data(answer, request.FILES)

            form = AnswerForm(*form_param)
            if form.is_valid():
                answer = Answer.objects.filter(
                    question_id=int(answer[0])
                ).first()
                if answer:
                    form.instance.pk = answer.id
                form.save()

        return HttpResponseRedirect("multi-questions")