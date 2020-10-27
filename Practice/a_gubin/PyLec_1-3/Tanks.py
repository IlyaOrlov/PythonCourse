import random
import time
import math


class Arena:

    def draw_arena(self, state, message):
        state.sort(key=lambda obj: obj['y'] * 10 + obj['x'])
        print('#', end='')
        for i in range(10):
            print(f' {i} #', end='')
        print('')
        for i in range(10):
            self.print_row(i, [{'x': x['x'], 'shape': x['shape']} for x in state if x['y'] == i])
            if i < 9:
                print('#', '---+' * 9, '---', '#', sep='')
        print('#' * 41)
        print(message)

    def print_row(self, index, units):
        print(index, end='')
        for i in range(10):
            if units and i == units[0]['x']:
                print(f" {units[0]['shape']} |", end='')
                del units[0]
            else:
                print('   |', end='')
        print('\b#')


class Positional:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

    def get_position(self):
        return self.x_pos, self.y_pos

    def set_position(self, x, y):
        self.x_pos = x
        self.y_pos = y

    def shift_position(self, x, y):
        self.x_pos += x
        self.y_pos += y

    def next_position(self, x, y):
        return self.x_pos + x, self.y_pos + y

    def is_position_equal(self, other):
        return self.x_pos == other.x_pos and self.y_pos == other.y_pos


class Drawable(Positional):
    def __init__(self, x_pos, y_pos, shape):
        super().__init__(x_pos, y_pos)
        self._shape = shape

    def get_state(self):
        return {'x': self.x_pos, 'y': self.y_pos, 'shape': self.shape}

    @property
    def shape(self):
        return self._shape


class Tank(Drawable):
    def __init__(self, speed, distance):
        super().__init__(4, 5, 'T')
        self.speed = speed
        self.distance = distance
        self.orientation = {'x': 1, 'y': 0}

    def set_position(self, x, y):
        self.orientation['x'] = x - self.x_pos
        self.orientation['y'] = y - self.y_pos
        self.x_pos = x
        self.y_pos = y

    def get_bullet_data(self):
        return self.x_pos, self.y_pos, self.orientation


class Bullet(Drawable):
    def __init__(self, x, y, orientation):
        super().__init__(x, y, '*')
        self.orientation = orientation

    def shift_position(self, *args):
        self.x_pos += self.orientation['x']
        self.y_pos += self.orientation['y']

    def next_position(self, *args):
        return self.x_pos + self.orientation['x'], self.y_pos + self.orientation['y']

    def set_position(self, x, y):
        pass


class Target(Drawable):
    def __init__(self):
        super().__init__(4, 5, '@')
        self.is_alive = True

    @property
    def shape(self):
        return self._shape if self.is_alive else 'X'


class Game:
    def __init__(self):
        self.arena = Arena()
        self.tank = None
        self.target = None
        self.game_state = []
        self.game_objects = []
        self.temp_game_objects = []
        self.message = ''
        # self.directions = ['q', 'w', 'e', 'd', 'c', 'x', 'z', 'a']
        self.directions = {'q': (-1, -1), 'w': (0, -1), 'e': (1, -1), 'd': (1, 0),
                           'c': (1, 1), 'x': (0, 1), 'z': (-1, 1), 'a': (-1, 0)}
        self.player_win = False
        self.player_exit = False

    def menu(self):
        while True:
            prompt = '\n*****TANK*****\n' \
                     'Choose type of tank:\n' \
                     '1 - Light (speed = 2, distance = 1)\n' \
                     '2 - Heavy (speed = 1, distance = 2)\n' \
                     'or enter "exit" for exit\n\nType of tank : '
            type_of_tank = input(prompt)
            if type_of_tank == 'exit':
                break
            elif type_of_tank in ['1', '2']:
                self.start_game(type_of_tank)
            else:
                print('Unknown command, please try again')

    def start_game(self, type_of_tank):
        self.create_game_objects(type_of_tank)
        self.set_default_game_state()
        self.arena.draw_arena(self.get_game_state(), self.message)
        self.play()

    def create_game_objects(self, type_of_tank):
        if type_of_tank == '1':
            self.tank = Tank(2, 1)
        elif type_of_tank == '2':
            self.tank = Tank(1, 2)
        self.target = Target()
        self.game_objects.clear()
        self.game_objects.append(self.tank)
        self.game_objects.append(self.target)

    def set_default_game_state(self):
        while self.distance(self.tank.get_position(), self.target.get_position()) < self.tank.distance:
            self.target.set_position(random.randrange(10), random.randrange(10))
        self.temp_game_objects.clear()
        self.message = ''
        self.player_win = False
        self.player_exit = False

    def play(self):
        while self.next_turn():
            self.tank_turn()
            self.target_turn()
            self.end_turn()

    def next_turn(self):
        if self.player_exit:
            return False
        if self.player_win:
            input('Push any button')
            return False
        return True

    def target_turn(self):
        if self.player_exit:
            return
        if self.target.is_alive:
            time.sleep(1)
            while not self.step(random.choice(list(self.directions.keys())), self.target, self.tank):
                pass
        else:
            self.message = "*****WIN*****"
            self.player_win = True
        self.arena.draw_arena(self.get_game_state(), self.message)

    def tank_turn(self):
        while True:
            action = input("Enter a command ('q, w, e, a, d, z, x, c' - move, ' ' - fire, 'exit' - exit): ")
            if action == 'exit':
                self.player_exit = True
                break
            elif action in self.directions:
                if self.moving(action):
                    break
            elif action == ' ':
                if self.firing():
                    break
            else:
                print('Unknown command')

    def end_turn(self):
        self.temp_game_objects.clear()

    def get_game_state(self):
        self.game_state.clear()
        for unit in self.game_objects:
            self.game_state.append(unit.get_state())
        self.game_state += self.temp_game_objects
        return self.game_state

    def moving(self, action):
        moves = self.tank.speed
        while True:

            if action in self.directions:
                if self.step(action, self.tank, self.target):
                    self.message = ''
                    moves -= 1
                else:
                    self.message = f'Impossible to move. You can move {moves} time(s)'
                self.arena.draw_arena(self.get_game_state(), self.message)
            else:
                print('Unknown command')

            if moves:
                action = input(f"Enter a direction (q, w, e, a, d, z, x, c). You have {moves} move(s): ")
            else:
                break

        return True

    def firing(self):
        if self.fire_to_nowhere(self.tank.next_position(*list(self.tank.orientation.values()))):
            self.arena.draw_arena(self.get_game_state(), self.message)
            return False

        get_in = self.fire()
        self.arena.draw_arena(self.get_game_state(), self.message)
        if not get_in:
            self.temp_game_objects.clear()
        return True

    def fire_to_nowhere(self, position):
        if self.is_into_arena(position):
            return False
        self.message = 'You shoot to nowhere, change position'
        return True

    def fire(self):
        bullet = Bullet(*self.tank.get_bullet_data())
        shifts = self.tank.distance
        while True:
            bullet.shift_position()
            shifts -= 1

            if self.is_into_arena(bullet.get_position()):
                strike_place = bullet.get_position()
                if bullet.is_position_equal(self.target):
                    self.target.is_alive = False
                    return True
                self.temp_game_objects.append(bullet.get_state())
                if shifts:
                    self.arena.draw_arena(self.get_game_state(), self.message)
                    time.sleep(1)
                    continue
            break
        self.message = f'You missed. Distance is {self.distance(strike_place, self.target.get_position()):.1f}'
        return False

    def distance(self, point1, point2):
        return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

    def is_into_arena(self, position):
        return 0 <= position[0] <= 9 and 0 <= position[1] <= 9

    def step(self, direction, active, passive):
        active_position = Positional(*active.next_position(*self.directions[direction]))
        if self.is_into_arena(active_position.get_position()) and not active_position.is_position_equal(passive):
            active.set_position(*active_position.get_position())
            return True
        return False


Game().menu()
