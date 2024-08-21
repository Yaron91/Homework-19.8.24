import random

oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone",
"Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"}
titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"}
dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"}
avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo",
"Chris Hemsworth", "Jeremy Renner"}
iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"}
legendary_actors = {"Al Pacino", "Robert De Niro", "Marlon Brando", "Jack Nicholson", "Dustin Hoffman"}
actor_list = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Leonardo DiCaprio", "Tom Hanks"}
movie_cast = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"}

#a.
oscar_winners.add("Emma Watson")
print("a.",oscar_winners)

#b.
#oscar_winners.clear()
#print("b.",oscar_winners)

#c.
new_oscar_winners= oscar_winners.copy()
print("c.",new_oscar_winners)

#d.
oscar_winners.discard("Meryl Streep")
print("d.",oscar_winners)

#e.
print("e.",titanic_actors.intersection(dark_knight_actors))

#f.
print("f.",iron_man_actors.intersection(avengers_actors))

#g.

print("g.",actor_list.issubset(oscar_winners))

#h.
print("h.",avengers_actors.issubset(actor_list))

#i.
rand_choice= random.choice(list(movie_cast))
movie_cast.remove(rand_choice)
print("i.",movie_cast)

#j.
movie_cast.discard("Matt Damon") # to avoid errors instead of remove in case Matt Damom is removed in the random question.
print("j.",movie_cast)

#k.
print("k.",titanic_actors.difference(oscar_winners))
#l.
only_dark_knight = dark_knight_actors - titanic_actors
only_titanic = titanic_actors - dark_knight_actors
print("l.",only_dark_knight.union(only_titanic))
#m.
oscar_winners.update(["Cate Blanchett", "Daniel Day Lewis"])
print("m.",oscar_winners)
#n.
print("n.",titanic_actors.union(dark_knight_actors))
#o.
dark_knight_rises_actors = {"Christian Bale", "Michael Caine", "Gary Oldman",
"Tom Hardy", "Joseph Gordon-Levitt"}

print("o.", dark_knight_rises_actors >= dark_knight_actors)
#p.
print("p.",legendary_actors >= oscar_winners)
#q.
print("q.", avengers_actors - iron_man_actors)
#r.
print("r.", dark_knight_actors ^ avengers_actors)
#s.
print("s.", dark_knight_actors | iron_man_actors)
#t.
legendary_actors_frozen = frozenset(legendary_actors)
print("t.", legendary_actors_frozen)