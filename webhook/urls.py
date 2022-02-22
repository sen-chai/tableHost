from django.urls import path
from .views import WebhookEtapas, webhook

urlpatterns=[
    path('',WebhookEtapas.as_view())
    # path('',webhook)
]
