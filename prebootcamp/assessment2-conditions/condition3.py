grade = int(input('Hey, pls gimme ur grade:'))

 #main:
if grade == 1:
    score = float(input('score:'))
    score2 = float(input('score:'))
    if score < 10 or score2 < 10:
        print(int((score + score2) / (grade + 1)), 'mardood')
    else:
        print(int((score + score2)/(grade + 1)), 'ghabool')

if grade == 2:
    score = float(input('score:'))
    score2 = float(input('score:'))
    score3 = float(input('score:'))
    if score < 10 or score2 < 10 or score3 < 10:
        print(int((score + score2 + score3) / (grade + 1)), 'mardood')
    else:
        print(int((score + score2 + score3)/(grade + 1)), 'ghabool')

if grade == 3:
    score = float(input('score:'))
    score2 = float(input('score:'))
    score3 = float(input('score:'))
    score4 = float(input('score:'))
    if score < 10 or score2 < 10 or score3 < 10 or score4 < 10:
        print(int((score + score2 + score3 + score4) / (grade + 1)), 'mardood')
    else:
        print(int((score + score2 + score3 + score4)/(grade + 1)), 'ghabool')




'''

x = grade + 1
scores = 0
p = 0
while x > 0:
    x -= 1
    score = float(input('pls gimme scores one by one on each line:'))
    if score < 10:
        p = 1
    scores += score
if p == 1:
    print('GPA is:', int(scores/(grade+1)), 'mardood')
else:
    print('GPA is:', int(scores/(grade+1)), 'ghabool')

'''



