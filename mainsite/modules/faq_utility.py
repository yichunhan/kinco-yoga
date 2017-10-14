from db_utility import DBUtility

class FAQUtility:
    def get_faqs(self, role=None):
        db_utility = DBUtility()

        course_faqs = db_utility.get_faqs(faq_type='course')
        register_faqs = db_utility.get_faqs(faq_type='register')

        return course_faqs, register_faqs