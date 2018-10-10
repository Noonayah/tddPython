#Fonction Hello World:
def hello_world():
    bjr = 'hello world'
    return bjr


#Fonction de Calcul de Score selon le nom:
def calculScore(nom,age):
    if nom == 'Joseph' and age == 15:
        score = '66%'
        return score
    if nom == 'Marie' and age == 33:
        score = '50%'
        return score
    elif nom == 'Marc' and age == 60:
        score = '43%'
        return score
    elif nom == 'Ely' and age == 28:
        score = '75%'
        return score