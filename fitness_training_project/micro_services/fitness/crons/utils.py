from datetime import datetime, timedelta


def get_users_whose_finished_program_from_thirty_minutes_from_now(model):
    start_timestamp = datetime.now() - timedelta(minutes=30)  # Start from 30 minutes ago
    end_timestamp = datetime.now() - timedelta(hours=1)  # End at 1 hour ago
    # Get a QuerySet of all model objects where the timestamp is within the range from start_timestamp to end_timestamp
    return list(model.objects.filter(timestamp__range=(start_timestamp, end_timestamp)).values_list('user', flat=True))


def get_users_whose_not_start_program_from_ten_minutes_from_now(model):
    # Function to get users who opened the app and did not start any training program within the last 10 minutes
    def get_items_whose_time_is_less_than_thirty_minutes_from_now(model):
        # Define the time range: 10 minutes ago and 11 minutes ago
        ten_minutes_ago = datetime.now() - timedelta(minutes=10)
        eleven_minutes_ago = datetime.now() - timedelta(minutes=11)

        # Get users who opened the app within the last 10 minutes
        users_open_app = model.objects.filter(timestamp__range=(ten_minutes_ago, eleven_minutes_ago),
                                              type__title='app_launch').values_list('user', flat=True)

        # Get users who started a training program within the last 10 minutes
        users_who_do_programs_in_less_than_ten_minutes = model.objects.filter(timestamp__gt=ten_minutes_ago,
                                                                              training_program__isnull=False)

        # Subtract the second set of users from the first set to get the final list of users
        users = list(set(list(users_open_app)) - set(list(users_who_do_programs_in_less_than_ten_minutes)))

        # Return the final list of users
        return users
