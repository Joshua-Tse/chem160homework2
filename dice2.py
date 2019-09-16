from random import choices
ntrials = 10000
player1wins = 0
ndice2 = 2
ndice1 = 3
for i in range(ntrials):
    total2 = 0
    total1 = 0
    dice2 = choices(range(1,7), k =ndice2)
    if dice2[0] == dice2[1]:
        continue
    total2 = total2+dice2[0]+dice2[1]
    dice1 = choices(range(1, 7), k=ndice1)
    dice1.sort(reverse=True)
    count = dice1.count(2)
    if count >= 2:
        continue
    total1 = total1+dice1[0]+dice1[1]
    if total1 > total2:
        player1wins +=1
print ("player1winratio=", player1wins/ntrials)