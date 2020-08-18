from random import choice


class Char:
    def __init__(self, name="John Doe", age="not given", genre="not given", job="not given"):
        self.name = name
        self.age = age
        self.genre = genre
        self.job = job

    def char_name(self):
        return f"Your character name is: {self.name}"

    def char_age(self):
        return f"Your character is: {self.age} years old."

    def char_genre(self):
        return f"Your character is: {self.genre}"

    def char_job(self):
        if self.age <= 18 and self.job.lower() == 'student':
            return f"Your character's job is: {self.job}."
        elif self.age < 18 and self.job.lower() != 'student':
            return f"Error! Your character needs to be a student because you're under 18 years old."
        else:
            if self.job == 'Developer':
                dev_lang = ['Python', 'C#', 'C', 'Java']
                random_lang_choice = choice(dev_lang)
                if random_lang_choice == 'Python':
                    return f"Your character's job is: {random_lang_choice} {self.job}"
                elif random_lang_choice == 'C#':
                    return f"Your character's job is: {random_lang_choice} {self.job}"
                elif random_lang_choice == "C":
                    return f"Your character's job is: {random_lang_choice} {self.job}"
                elif random_lang_choice == 'Java':
                    return f"Your character's job is: {random_lang_choice} {self.job}"

            elif self.job.lower() == 'data scientist':
                return f"Your character's job is: {self.job}"

            elif self.job.lower() == 'ciberSecurity technician':
                return f"Your character's job is: {self.job}"
            else:
                return f"You are {self.job}"
