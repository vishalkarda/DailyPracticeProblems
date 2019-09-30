import math


class War:
    def __init__(self):
        self.batlions = ['horse', 'elephant', 'tanks', 'guns']
        self.lengaburu_army = dict(horse=100, elephant=50, tanks=10, guns=5)
        self.deployed_len_army = dict(horse=0, elephant=0, tanks=0, guns=0)
        self.fal_army = dict(horse=300, elephant=200, tanks=40, guns=20)
        deployed_fal_army = dict(horse=0, elephant=0, tanks=0, guns=0)
        diff = dict(horse=0, elephant=0, tanks=0, guns=0)


print('Enter the input')
data = input()
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

diff['horse'] = math.ceil(deployed_fal_army['horse']/2)
diff['elephant'] = math.ceil(deployed_fal_army['elephant']/2)
diff['tanks'] = math.ceil(deployed_fal_army['tanks']/2)
diff['guns'] = math.ceil(deployed_fal_army['guns']/2)

for value in batlions:
    if diff[value] <= lengaburu_army[value]:
        deployed_len_army[value] = diff[value]
        lengaburu_army[value] -= diff[value]
        diff[value] = 0
    else:
        deployed_len_army[value] = lengaburu_army[value]
        diff[value] -= lengaburu_army[value]
        lengaburu_army[value] = 0

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
                        deployed_len_army[batlions[value + 1]] += lengaburu_army[batlions[value+1]]
                        diff[batlions[value]] -= (lengaburu_army[batlions[value+1]]*2)
                        lengaburu_army[batlions[value]] = 0
                else:
                    pass
            elif value == 3:
                req = diff[batlions[value]]*2
                if lengaburu_army[batlions[value-1]] != 0:
                    if req <= lengaburu_army[batlions[value-1]]:
                        deployed_len_army[batlions[value-1]] += req
                        lengaburu_army[batlions[value-1]] -= req
                        diff[batlions[value]] = 0
                    else:
                        deployed_len_army[batlions[value-1]] += lengaburu_army[batlions[value-1]]
                        diff[batlions[value]] -= math.ceil(lengaburu_army[batlions[value-1]]*0.5)
                        lengaburu_army[batlions[value]] = 0
            else:
                req_lower_rank = diff[batlions[value]] * 2
                req_higher_rank = math.ceil(diff[batlions[value]] / 2)
                if lengaburu_army[batlions[value-1]] != 0 and req_lower_rank <= lengaburu_army[batlions[value-1]]:
                    deployed_len_army[batlions[value - 1]] += req_lower_rank
                    lengaburu_army[batlions[value - 1]] -= req_lower_rank
                    diff[batlions[value]] = 0

                elif lengaburu_army[batlions[value-1]] != 0 and req_lower_rank > lengaburu_army[batlions[value-1]]:
                    deployed_len_army[batlions[value - 1]] += lengaburu_army[batlions[value - 1]]
                    req_lower_rank -= lengaburu_army[batlions[value - 1]]
                    lengaburu_army[batlions[value - 1]] = 0
                    diff[batlions[value]] = math.ceil(req_lower_rank/2)
                    remaining = math.ceil(req_lower_rank/4)
                    if lengaburu_army[batlions[value + 1]] != 0 and remaining <= lengaburu_army[batlions[value + 1]]:
                        deployed_len_army[batlions[value+1]] += remaining
                        lengaburu_army[batlions[value + 1]] -= remaining
                        diff[batlions[value]] = 0
                    elif lengaburu_army[batlions[value + 1]] != 0:
                        deployed_len_army[batlions[value + 1]] += lengaburu_army[batlions[value + 1]]
                        remaining -= lengaburu_army[batlions[value + 1]]
                        diff[batlions[value]] = remaining*2

                elif lengaburu_army[batlions[value+1]] != 0 and req_higher_rank <= lengaburu_army[batlions[value+1]]:
                    deployed_len_army[batlions[value + 1]] += req_higher_rank
                    lengaburu_army[batlions[value + 1]] -= req_higher_rank
                    diff[batlions[value]] = 0

                elif lengaburu_army[batlions[value+1]] != 0:
                    deployed_len_army[batlions[value + 1]] += lengaburu_army[batlions[value + 1]]
                    diff[batlions[value]] -= (lengaburu_army[batlions[value + 1]] * 2)
                    lengaburu_army[batlions[value]] = 0
        else:
            pass


total = sum(diff.values())
result = 'wins'
if total > 0:
    result = 'loses'
print(f"Lengaburu deploys {deployed_len_army['horse']} H {deployed_len_army['elephant']} E {deployed_len_army['tanks']}"
      f" AT {deployed_len_army['guns']} SG & {result}")




