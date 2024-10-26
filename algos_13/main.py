recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
# 0


def cakes(recipe, available):
    if all(ingrid in available.keys() for ingrid in recipe.keys()) == False:
        return 0
    return min([available[i] // recipe[i] for i in recipe.keys()])


print(cakes(recipe, available))