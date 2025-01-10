from django_cron import CronJobBase, Schedule
from .models import ApiEndpoint
import requests
from django.utils.timezone import now

class CheckApiStatusCronJob(CronJobBase):
    RUN_EVERY_MINS = 5  # Cada n minutos

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'api_monitor.check_api_status'

    def do(self):
        endpoints = ApiEndpoint.objects.all()
        for endpoint in endpoints:
            try:
                response = requests.get(endpoint.url, timeout=10)
                endpoint.status = response.status_code == 200
            except requests.RequestException:
                endpoint.status = False
            endpoint.last_checked = now()
            endpoint.save()
