class InfiniteLineup:                        # class infinite lineup 
    def __init__(self, players):             # create the init method here and self and players passed in
        self.players = players               # so you can bring in players list 

    def lineup(self):                         # linup takes in self to have access to players
        lineup_max = len(self.players)        # create the variable called lineup_max and set it equal to len players (brings in a count of players)
        idx = 0                             # set the index(idx) to zero

        while True:                         # create the infite loop using while true
            if idx < lineup_max:            # conditional if the index is less than the lineup max
                yield self.players[idx]     # you want to-yield keyword(yielding to generator) to self players index
            else:                           # 
                idx = 0                     # set the index to zero
                yield self.players[idx]     # still want to yield to self players index

            idx += 1                        # increment the indx by one

    def __repr__(self):                      # dudner repr takes in self and returns the entire object(string)
        return f'InfiniteLineup({self.players})'    

    def __str__(self):                       # dunder string method takes in self
        return f"InfiniteLineup with the players: {', '.join(self.players)}"    # pass in a comma and join the players


astros = [
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

full_lineup = InfiniteLineup(astros)  # full lineup variable that takes in(instatiate) takes the list of players
astros_lineup = full_lineup.lineup()  # create an instance of astros lineup-set equal to the full lineup.lineup function()
                                      # in between- you have to start the process by saying next and call the astros lineup
                                      # whenever you put a yield it tells python a generator-and next has to be used
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))

print(repr(full_lineup))  

print(str(full_lineup))