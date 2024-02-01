import requests
from django_cron import CronJobBase, Schedule

from fitness_training_project.micro_services.fitness.crons.utils import \
    get_users_whose_finished_program_from_thirty_minutes_from_now, \
    get_users_whose_not_start_program_from_ten_minutes_from_now
from fitness_training_project.micro_services.fitness.repositories.event.models import Event


class FinishesTrainingProgramNotificationCronJob(CronJobBase):
    RUN_EVERY_MINS = 30 # every 30 minutes
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'my_app.my_cron_job'    # a unique code

    def do(self):
        users = get_users_whose_not_start_program_from_ten_minutes_from_now(Event)
        # requests.post("v1/notify", data={"users":users}) # here will send notification
        print("send notifications ..")