from django.shortcuts import render, get_object_or_404
from .models import Project
from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def home(request):
    featured_projects = Project.objects.filter(is_featured=True)
    return render(request, 'main/index.html', {'projects': featured_projects})

def project_detail(request, slug):
    project = get_object_or_404(
        Project.objects.select_related('images'),
        slug=slug,
        is_featured=True  # или убрать, если нужно показывать все
    )
    return render(request, 'projects/detail.html', {
        'project': project,
        'images': project.images.all().order_by('order')
    })

import json
import logging
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.template.loader import render_to_string

logger = logging.getLogger(__name__)


@require_http_methods(["POST"])
def consultation_request(request):
    try:
        logger.info("Начало обработки запроса")
        logger.debug("Заголовки: %s", request.headers)
        logger.debug("Метод: %s", request.method)

        # Проверка AJAX
        if not request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            logger.warning("Не AJAX-запрос")
            return JsonResponse({'error': 'Требуется AJAX-запрос'}, status=400)

        # Парсинг данных
        try:
            if request.content_type == 'application/json':
                data = json.loads(request.body.decode('utf-8'))
            else:
                data = request.POST.dict()

            logger.debug("Полученные данные: %s", data)
        except Exception as e:
            logger.error("Ошибка парсинга данных: %s", str(e))
            return JsonResponse({'error': 'Ошибка обработки данных запроса'}, status=400)

        # Валидация
        errors = {}
        required_fields = ['first_name', 'last_name', 'email']
        for field in required_fields:
            if not data.get(field, '').strip():
                errors[field] = 'Это поле обязательно'
                logger.warning("Не заполнено обязательное поле: %s", field)

        if 'email' in data and not errors.get('email'):
            try:
                validate_email(data['email'])
            except ValidationError:
                errors['email'] = 'Неверный формат email'
                logger.warning("Неверный формат email: %s", data['email'])

        if errors:
            logger.info("Ошибки валидации: %s", errors)
            return JsonResponse({'success': False, 'errors': errors}, status=400)

        # Подготовка и отправка письма
        try:
            email_subject = 'Новая заявка на консультацию'
            email_body = render_to_string('emails/consultation_request.html', {
                'first_name': data["first_name"],
                'last_name': data["last_name"],
                'email': data["email"],
                'message': data.get("message", ""),
            })

            logger.debug("Тема письма: %s", email_subject)
            logger.debug("Тело письма: %s", email_body)

            send_mail(
                email_subject,
                '',  # plain-text версия
                'noreply@yourdomain.com',  # from
                ['zotenkovad@gmail.com'],  # to (ваш email)
                fail_silently=False,
                html_message=email_body,
            )
            logger.info("Письмо успешно отправлено")
        except Exception as e:
            logger.exception("Ошибка отправки письма")
            return JsonResponse({'error': 'Ошибка при отправке письма'}, status=500)

        return JsonResponse({'success': True, 'message': 'Заявка принята!'})

    except Exception as e:
        logger.exception("Непредвиденная ошибка")
        return JsonResponse({'error': 'Внутренняя ошибка сервера'}, status=500)

def privacy_policy(request):
    return render(request, 'main/privacy-policy.html')

#------------------------------------------------
from django.http import HttpResponse
import logging


def test_logging(request):
    # Инициализация логгеров
    django_logger = logging.getLogger('django')
    request_logger = logging.getLogger('django.request')
    security_logger = logging.getLogger('django.security')

    # Тест general.log (через основной логгер)
    django_logger.info("Тестовое info сообщение для general.log")

    # Тест errors.log и почты
    try:
        raise ValueError("Тестовая ошибка для errors.log")
    except ValueError:
        request_logger.error("Ошибка запроса", exc_info=True)

    # Тест security.log
    security_logger.warning("Попытка неавторизованного доступа")

    return HttpResponse("Проверка логирования завершена")
