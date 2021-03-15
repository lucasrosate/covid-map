import logging

from django.conf import settings
from django.core.management.base import BaseCommand

from apscheduler.schedulers.blocking import BlockingScheduler
from django_apscheduler.jobstores import DjangoJobStore
from apscheduler.triggers.cron import CronTrigger

from covidmap.data_management.functions.get_new_data import get_new_data

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Run apscheduler to fetch data"
    
    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")
        
        scheduler.add_job(
            get_new_data,
            trigger=CronTrigger(
                hour="10",
                minute="00"
            ),
            max_instances=1,
            replace_existing=True
        )
        
        logger.info("Added fetch data job.")
    
        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shutdown successfully!")
            