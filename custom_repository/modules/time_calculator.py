class TimeCalculator():
    def __init__(self):
        self.initial_time = None
    
    def reset_initial_time_to_now(self, now):
        self.initial_time = now

    def get_total_time_passed_from_previous_loop(self, now):
        return now - self.initial_time 