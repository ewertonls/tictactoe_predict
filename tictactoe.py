from pandas import read_csv
from sklearn import model_selection, tree, metrics
import sys
import re
import math

GAME_LEN = 9
def parse_games(input: str) -> list[str]:
    game_count = math.ceil(len(input) / GAME_LEN);
    if game_count <= 1:
        return [input.ljust(GAME_LEN, 'b')]

    games: list[str] = []
    for i in range(game_count):
        fromidx = i * GAME_LEN
        to = fromidx + GAME_LEN
        games.append(input[fromidx: to].ljust(GAME_LEN, 'b'))

    return games

def fn(x: str) -> int:
    if x == 'x' or x == 'X':
        return 1
    if x == 'o' or x == 'O':
        return -1
    return 0

def map_game(game: str) -> list[int]:
    return [fn(i) for i in game]


def print_game(game: str):
    g = game.replace('b', ' ')
    if len(g) < 9:
        print(g)
        return
    print(f'{g[0]} | {g[1]} | {g[2]}')
    print(f'{g[3]} | {g[4]} | {g[5]}')
    print(f'{g[6]} | {g[7]} | {g[8]}')

data = read_csv('data.csv')

data = data.replace(to_replace=['o', 'x', 'b', 'negativo', 'positivo'], value=[-1, 1, 0, -1, 1])
data_train, data_test = model_selection.train_test_split(data, test_size=0.2, train_size=0.8)

train_labels = data_train['resultado'].values.tolist()
test_labels = data_test['resultado'].values.tolist()

data_train.pop('resultado')
data_test.pop('resultado')

clf_tree = tree.DecisionTreeClassifier()

clf_tree = clf_tree.fit(X=data_train.values, y=train_labels)

pred_result = clf_tree.predict(data_test.values)

model_report = metrics.classification_report(test_labels, pred_result)

print(f'Games trained: {len(data_train)}')
print(model_report)

args = sys.argv[1:]

games = re.sub('\s', '', "".join(args))

games = parse_games(games)
pred_games = clf_tree.predict(list(map(map_game, games)))

for i in range(len(pred_games)):
    result = pred_games[i]
    game = games[i]

    if result == 1:
        result = 'yes'
    else:
        result = 'no'

    print()
    print_game(game)

    print(f'X will win: {result}')
    print('-' * 10)

