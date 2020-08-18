from random import choice


class Char:
    def __init__(self, name, age, genre, job):
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
        if self.age <= 18 and self.job == 'Student':
            return f"Your character's job is: {self.job}."
        elif self.age <= 18 and self.job != 'Student':
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

            elif self.job == 'Data Scientist':
                return f"Your character's job is: {self.job}"

            elif self.job == 'CiberSecurity Technician':
                return f"Your character's job is: {self.job}"
