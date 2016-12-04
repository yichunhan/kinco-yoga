from db_utility import DBUtility

class ClassUtility:
    def get_class_info(self, class_index):
        db_utility = DBUtility()

        class_info = db_utility.get_class_info(class_index)
        return class_info
