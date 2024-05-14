import random
import math

def reqemleri_yarat_ve_kvadrat_et():
    # 20 ilə 50 arası 5 rəqəmlik siyahı yaradın
    reqemler = [random.randint(20, 50) for _ in range(5)]
    
    # Cüt rəqəmləri kvadrata yüksəldin
    kvadrat_reqemler = [math.pow(reqem, 2) if reqem % 2 == 0 else reqem for reqem in reqemler]
    
    return kvadrat_reqemler

# Funksiyanı çağırın və nəticəni göstərin
netice = reqemleri_yarat_ve_kvadrat_et()
print("Nəticə:", netice)