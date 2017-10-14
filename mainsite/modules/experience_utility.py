from db_utility import DBUtility

class ExperienceUtility:
    def get_experiences(self, role=None):
        db_utility = DBUtility()

        experiences = db_utility.get_experiences(role)
        return experiences