from django.views.generic import View
from django.shortcuts import render
from ..models import Questionnaire, AnswerGroup, Answer


class SaveAnswerView(View):
    template_name = "questionnaire/save-answer-view.html"
    model = Questionnaire

    def get(self, request, *args):

        return render(
            request,
            self.template_name,
            {"questionnaire": self.get_questionnaire_object()},
        )

    def post(self, request, *args):
        questionnaire = self.get_questionnaire_object()
        self.save_answer_group(questionnaire, request.POST)
        return render(request, self.template_name, {"questionnaire": questionnaire})

    def get_questionnaire_object(self):
        return self.model.objects.get()

    def save_answer_group(self, questionnaire, request_post):
        """
        Сохранение ответов в базу
        """
        answer_group = AnswerGroup.objects.create(
            last_name=request_post["last_name"],
            first_name=request_post["first_name"],
            second_name=request_post["second_name"],
            pos=request_post["pos"],
        )
        answers = []
        for question in questionnaire.questions.all():
            key_question = "question_" + str(question.pk)
            answers.append(
                Answer(
                    answer_group=answer_group,
                    question=question,
                    value=int(request_post.get(key_question)),
                )
            )

        Answer.objects.bulk_create(answers)
