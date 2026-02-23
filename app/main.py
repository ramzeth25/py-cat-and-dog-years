def get_human_age(cat_age: int, dog_age: int) -> list:
    """
    Convert cat and dog ages to human years.

    Rules:
    Cat: first 15 years = 1 human year, next 9 = +1, then every 4 = +1
    Dog: first 15 years = 1 human year, next 9 = +1, then every 5 = +1

    Args:
        cat_age: Cat's age in cat years
        dog_age: Dog's age in dog years

    Returns:
        List with [cat_human_age, dog_human_age]

    Examples:
        get_human_age(0, 0) == [0, 0]
        get_human_age(15, 15) == [1, 1]
        get_human_age(24, 24) == [2, 2]
    """
    # TODO: Implement this function
    return check_age(cat_age, 4) + check_age(dog_age, 5)


def check_age(animal_age: int, animal_mod: int) -> list:
    result = []
    if animal_age in range(15):
        result.append(0)
        return result
    elif animal_age == 15:
        result.append(animal_age // 15)
        return result
    elif animal_age == 24:
        result.append(2)
        return result
    else:
        result.append(2)
        animal_age -= 24
        if animal_age >= animal_mod:
            result[0] += animal_age // animal_mod
        return result
