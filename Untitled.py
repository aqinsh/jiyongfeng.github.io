import math
def convert_recipe(recipe):
    s = list(recipe.split(' '))
    y = s
    for i in range(len(s)):
        if s[i] == 'tbsp':
            y.insert(i+1, '('+str(math.ceil(eval(s[i-1])*15)) + 'g'+')')            
        if s[i] == 'tsp':
            y.insert(i+1, '('+str(math.ceil(eval(s[i-1])*5)) + 'g'+')')            
    return ' '.join(y)


r = "Add to the mixing bowl and coat well with 1 tbsp of olive oil & 1/2 tbsp of dried dill"

print(convert_recipe(r))
