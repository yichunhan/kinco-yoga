from db_utility import DBUtility

class HomeUtility:
    def get_news(self):
        db_utility = DBUtility()

        news = db_utility.get_news()

        return news