class Lineup:
    
    def __init__(self, players):                              # init method pass in self and players
        self.players = players                                # self.players and set equal to players
        self.last_player_index = (len(self.players) - 1)      # length of the players list

    def __iter__(self):                                       # function dunder iter and passed in self
        self.n = 0                                            # 2 things -when iter is called create a counter variable by self.n and set it equal to 0-(starting)
        return self

    def get_player(self, n):                                  # fucntion created get player and takes in self and n
        return self.players[n]                                #  returns self players and calls n

    def __next__(self):                                       # dunder next to call next on the item
        if self.n < self.last_player_index:                   # if the self.n is les than the last player index
            player = self.get_player(self.n)                  # player vairable set equal to get.player and calling the self.n from the get player function
            self.n += 1                                       # incrementer self.n plus 1
            return player
        elif self.n == self.last_player_index:                # else if self.n is equal to  the last player index
            player = self.get_player(self.n)                  # player vairable set equal to get.player and calling the self.n from the get player function
            self.n = 0                                        # set self to 0 to start over again
            return player


astros = [             #python list here of strings
  'Springer',
  'Bregman',
  'Altuve',
  'Correa',
  'Reddick',
  'Gonzalez',
  'McCann',
  'Davis',
  'Tucker'
]

astros_lineup = Lineup(astros) # set it equal to linup and pass in the list
process = iter(astros_lineup)  # create the process and call the iter function on the astros lineup class

print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))