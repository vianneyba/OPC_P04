from dateutil.parser import parse


class Validation:

    @classmethod
    def first_name(self, firstname, error):
        if firstname == '':
            error.message = 'le prénom n\'est pas conforme'
            error.error = True
        else:
            error.next = True
            return firstname

    @classmethod
    def last_name(self, lastname, error):
        if lastname == '':
            error.message = 'le nom n\'est pas conforme'
            error.error = True
        else:
            error.next = True
            return lastname

    @classmethod
    def gender(self, gender, error):
        if gender.lower() not in ['h', 'f']:
            error.message = 'le genre n\'est pas conforme'
            error.error = True
        else:
            error.next = True
            return gender

    @classmethod
    def rating(self, rating, error):
        message = 'le classement est un nombre positif'
        try:
            rating = int(rating)
            if rating < 1:
                error.message = message
                error.error = True
            else:
                error.next = True
                return rating
        except ValueError:
            error.error = True
            error.message = message

    @classmethod
    def tournament_name(self, name, error):
        if name == '':
            error.message = 'le nom n\'est pas conforme'
            error.error = True
        else:
            error.next = True
            return name

    @classmethod
    def tournament_place(self, place, error):
        if place == '':
            error.message = 'le lieu n\'est pas conforme'
            error.error = True
        else:
            error.next = True
            return place

    @classmethod
    def tournament_date_start(self, date_start, error):
        try:
            d = parse(date_start, fuzzy=False)
            error.next = True
            return "{}/{}/{}".format(d.day, d.month, d.year)
        except ValueError:
            error.message = 'la date n\'est pas conforme'
            error.error = True

    @classmethod
    def tournament_duration(self, duration, error):
        message = 'le nombre n\'est pas conforme'
        if duration == '':
            error.next = True
            return 1

        try:
            duration = int(duration)
            if duration < 1:
                error.message = message
                error.error = True
            else:
                error.next = True
                return duration
        except ValueError:
            error.error = True
            error.message = message

    @classmethod
    def tournament_rounds(self, nbr_rounds, error):
        message = 'le nombre n\'est pas conforme'
        if nbr_rounds == '':
            error.next = True
            return 4

        try:
            nbr_rounds = int(nbr_rounds)
            if nbr_rounds < 1:
                error.message = message
                error.error = True
            else:
                error.next = True
                return nbr_rounds
        except ValueError:
            error.error = True
            error.message = message

    @classmethod
    def tournament_ctr_time(self, ctr_time, error):
        error.message = 'le côntrole du temps n\'est pas conforme'
        ctr = ['1', '2', '3', 'bullet', 'blitz', 'coup rapide']
        if ctr_time.lower() in ctr:
            error.next = True
            return ctr_time.lower()
        else:
            error.error = True

    @classmethod
    def tournament_description(self, description, error):
        error.next = True
        return description
