from db_utility import DBUtility

class CoachUtility:
    def get_coach_info(self, coach_name):
        db_utility = DBUtility()

        coach_info = db_utility.get_coach_info(coach_name)
        return coach_info
