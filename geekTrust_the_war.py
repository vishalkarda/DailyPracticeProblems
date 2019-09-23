import math
# class Army:
#     def __init__(self, H, E, A, SG):
#         self.horses = H
#         self.elephant = E
#         self.tanks = A
#         self.sling_guns = SG
#
#
# class Lengaburu(Army):
#     def __init__(self, horse, elephant, tanks, guns):
#         super().__init__(horse, elephant, tanks, guns)
#
#
# class Falcone(Army):
#     def __init__(self, horse, elephant, tanks, guns):
#         super().__init__(horse, elephant, tanks, guns)

# Falicornia attacks with 100 H, 101 E, 20 AT, 5 SG
data = 'Falicornia attacks with 250 H, 78 E, 20 AT, 15 SG'
statement = data.split(' ')

batlions = ['horse', 'elephant', 'tanks', 'guns']
lengaburu_army = dict(horse=100, elephant=50, tanks=10, guns=5)
deployed_len_army = dict(horse=0, elephant=0, tanks=0, guns=0)
fal_army = dict(horse=300, elephant=200, tanks=40, guns=20)
deployed_fal_army = dict(horse=0, elephant=0, tanks=0, guns=0)
diff = dict(horse=0, elephant=0, tanks=0, guns=0)

deployed_fal_army['horse'] = int(statement[3])
deployed_fal_army['elephant'] = int(statement[5])
deployed_fal_army['tanks'] = int(statement[7])
deployed_fal_army['guns'] = int(statement[9])
print(deployed_fal_army, 'attacking team')
diff['horse'] = math.ceil(deployed_fal_army['horse']/2)
diff['elephant'] = math.ceil(deployed_fal_army['elephant']/2)
diff['tanks'] = math.ceil(deployed_fal_army['tanks']/2)
diff['guns'] = math.ceil(deployed_fal_army['guns']/2)
print(diff, 'initial')

for value in batlions:
    if diff[value] <= lengaburu_army[value]:
        deployed_len_army[value] = diff[value]
        lengaburu_army[value] -= diff[value]
        diff[value] = 0
    else:
        deployed_len_army[value] = lengaburu_army[value]
        diff[value] -= lengaburu_army[value]
        lengaburu_army[value] = 0

print(lengaburu_army, 'bachi')
print(diff, 'fasala')
for value in range(len(batlions)):

    if diff[batlions[value]] != 0:
        if lengaburu_army[batlions[value]] == 0:
            req = math.ceil(diff[batlions[value]] / 2)
            if value == 0:
                if lengaburu_army[batlions[value + 1]] != 0:
                    if req <= lengaburu_army[batlions[value + 1]]:
                        deployed_len_army[batlions[value+1]] += req
                        lengaburu_army[batlions[value+1]] -= req
                        diff[batlions[value]] = 0
                    else:
                        print('yes')
                        deployed_len_army[batlions[value + 1]] = lengaburu_army[batlions[value+1]]
                        diff[batlions[value+1]] -= lengaburu_army[batlions[value]]
                        lengaburu_army[batlions[value]] = 0
            elif value == 3:
                pass
            else:
                pass

        else:
            if value == 0:
                req = math.ceil(diff[batlions[value]] / 2)
                if lengaburu_army[batlions[value+1]] != 0 & req <= lengaburu_army[batlions[value+1]]:
                    deployed_len_army[batlions[value]] += req


print(deployed_len_army, '+ve')
print(lengaburu_army, 'remaining army')
print(diff, 'difference')
# print(f'Lengaburu deploys {horse_r} H {elephant_r} E {tanks_r}'
#       f' AT {guns_r} SG & wins')




