class Programmer:
    def __init__ (self,name,language,skills):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course, lang, earned_skills):
        if lang == self.language:
            self.skills += earned_skills
            return f'{self.name} watched {course}'
        return f'{self.name} does not know {lang}'

    def change_language(self, new_lang, skills_needed):
        if self.skills >= skills_needed and new_lang != self.language:
            prev_lang = self.language
            self.language = new_lang
            return f'{self.name} switched from {prev_lang} to {new_lang}'

        elif new_lang == self.language:
            return f'{self.name} already knows {self.language}'

        else:
            return f'{self.name} needs {abs(self.skills - skills_needed)} more skills'


programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))