class KeyAndAnswers:
    def __init__(self, keywords: list, answers: list):
        self.keywords = keywords
        self.answers = answers

    def update_keywords(self, keyword_list):
        self.keywords = set(self.keywords + keyword_list)
        return self

    def update_answers(self, answers_list):
        self.answers = set(self.answers + answers_list)
        return self
