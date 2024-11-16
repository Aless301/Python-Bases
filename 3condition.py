# code
wallet = int(input("Combien d'argent avez vous ? "))
computerPrice = int(input("Combien coute l'ordinateur ? "))

# verification, prix pc inferieur à 1000€
if computerPrice < 1000: 
    print("le prix de l'ordinateur est inferieur à 1000€. Il coute : " + str(computerPrice))
    if wallet >= computerPrice:
        print("Vous pouvez acheter l'ordinateur")
    else:
        print("Vous n'avez pas assez d'argent pour acheter l'ordinateur")
elif computerPrice == 1000:
    print("le prix de l'ordinateur est égal à 1000€, il est donc cher")
    if wallet >= computerPrice:
        print("Vous pouvez acheter l'ordinateur")
    else:
        print("Vous n'avez pas assez d'argent pour acheter l'ordinateur")
else:
    print("le prix de l'ordinateur est superieur à 1000€, il est donc très cher. Il coute : " + str(computerPrice))
    if wallet >= computerPrice:
        print("Vous pouvez acheter l'ordinateur")
    else:
        print("Vous n'avez pas assez d'argent pour acheter l'ordinateur")