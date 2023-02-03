class NegativeTitlesError(Exception):
    def __init__(self, message: dict):
        self.message = message


class InvalidYearCupError(Exception):
    def __init__(self, message: dict):
        self.message = message


class ImpossibleTitlesError(Exception):
    def __init__(self, message: dict):
        self.message = message


def data_processing(data: dict):
    year = int(data["first_cup"][0:4])

    if data["titles"] < 0:
        raise NegativeTitlesError("titles cannot be negative")

    if year < 1930 or (year - 1930) % 4 != 0:
        raise InvalidYearCupError("there was no world cup this year")

    if 2022 - (year + int(data["titles"]) * 4) < 0:
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")
