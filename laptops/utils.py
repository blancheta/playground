from django.shortcuts import get_object_or_404

from laptops.models import Question


def prepare_form_data(answer: dict, files):
    """
    Prepare answer received for a given question
    for form validation
    """

    form_data = {
        "comment": answer[1],
        "question": answer[0],
    }
    form_param = [form_data]

    question = get_object_or_404(Question, pk=int(form_data["question"]))

    if question.attachment_required:
        # attachment_field_name = "attachment_{}".format(answer[0])
        attachment_field_name = f"attachment_{answer[0]}"
        form_files = {
            "attachment": files.get(attachment_field_name)
        }
        form_param.append(form_files)


    # [form_data] if attachment is not required
    # [form_data, form_files] if attachment is required
    return form_param