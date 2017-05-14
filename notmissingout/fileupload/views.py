from django.http import (
    HttpResponseBadRequest,
    HttpResponseServerError,
    HttpResponseForbidden,
)
from django.shortcuts import render
from . import models
from django.utils.translation import ugettext_lazy as _

ATTACHMENT_FILESIZE_LIMIT = 40 * 1024 * 1024

def upload_attachment(request):
    if request.method != 'POST':
        return HttpResponseBadRequest(_('Only POST method is allowed'))

    if not request.user.is_authenticated():
        return HttpResponseForbidden(_('Only authenticated users are allowed'))

    if not request.FILES.getlist('files'):
        return HttpResponseBadRequest(_('No files were requested'))

    try:
        attachments = []

        for file in request.FILES.getlist('files'):

            # create instance of appropriate attachment class
            klass = models.Attachment()
            attachment = klass()

            attachment.file = file
            attachment.name = file.name

            if file.size > ATTACHMENT_FILESIZE_LIMIT:
                return HttpResponseBadRequest(
                    _('File size exceeds the limit allowed and cannot be saved')
                )

            # remove unnecessary CSRF token, if found
            request.POST.pop("csrfmiddlewaretoken", None)
            kwargs = request.POST
            # calling save method with attachment parameters as kwargs
            attachment.save(**kwargs)

            attachments.append(attachment)

        return render(request, 'django_summernote/upload_attachment.json', {
            'attachments': attachments,
        })
    except IOError:
        return HttpResponseServerError(_('Failed to save attachment'))
