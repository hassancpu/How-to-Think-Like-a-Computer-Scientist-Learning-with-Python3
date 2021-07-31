
# import turtle
# import numpy as np
#
# wn = turtle.Screen()
# wn.bgcolor('blue')
#
# alex = turtle.Turtle()
# alex.color('red')
#
# def draw(tur, w, h):
#     """Hi, ...
#     """
#     tur.speed(1)
#     for i in range(4):
#         if i%2==0:
#             tur.forward(w)
#         else:
#             tur.forward(h)
#         tur.left(90)
#     tur.hideturtle()
#
# draw(alex, 100, 100)
# wn.mainloop()

#
# alex = turtle.Turtle()
# alex.color('red')
# alex.speed(1)
# alex.penup()
# alex.stamp()
#
# alex.forward(200)
# alex.left(105)
# alex.stamp()
# alex.forward(100)
#
# for i in range(11):
#     alex.stamp()
#     alex.left(30)
#     alex.forward(100)
#
# alex.hideturtle()
# wn.mainloop()

""" drawing 5 squares"""
#
# import turtle
#
# def draw(trle, sz):
#     """
#     :param trle: input turtle
#     :param sz: size of square
#     :return: nothing, just draw
#     """
#     trle.pendown()
#     trle.color('red')
#     trle.speed(1)
#     for i in range(4):
#         trle.forward(sz)
#         trle.left(90)
#
#     trle.penup()
#     trle.forward(2*sz)
#     return
#
# wn = turtle.Screen()
# wn.bgcolor('blue')
#
# alex = turtle.Turtle()
# for j in range(5):
#     draw(alex,20)
#
# wn.mainloop()

""" drawing 5 squares inside each other"""
# import turtle
#
# def draw(trle, sz):
#     """
#     :param trle: input turtle
#     :param sz: size of square
#     :return: nothing, just draw
#     """
#     trle.color('red')
#     trle.speed(1)
#     for i in range(5):
#         trle.pendown()
#         for j in range(4):
#             trle.forward(sz + i*sz)
#             trle.left(90)
#
#         trle.penup()
#         trle.right(135)
#         trle.forward(14.14)
#         trle.left(135)
#     return
#
# wn = turtle.Screen()
# wn.bgcolor('blue')
#
# alex = turtle.Turtle()
# draw(alex, 20)
#
# wn.mainloop()

""" drawing general polygan"""
#
# import turtle
#
# def draw_poly(trle, t, sz):
#     """
#     :param trle:
#     :param t:
#     :param sz:
#     :return:
#     """
#     trle.color('red')
#     trle.speed(1)
#     agl = int(360/t)
#
#     for i in range(t):
#         trle.forward(sz)
#         trle.left(agl)
#     trle.hideturtle()
#
# def draw_eqitrangle(trle, sz):
#     """
#     :param trle:
#     :param sz:
#     :return:
#     """
#     trle.color('red')
#     trle.speed(1)
#     draw_poly(trle, 3, sz)
#
#
# wn = turtle.Screen()
# wn.bgcolor('blue')
#
# alex = turtle.Turtle()
# alex.speed(1)
# # draw_poly(alex, 5, 50)
# draw_eqitrangle(alex, 200)
#
# wn.mainloop()

""" drawing pretty patterns"""
#
# import turtle
# import numpy as np
#
# def draw_pretty_square(trle, sz):
#     """
#     :param trle:
#     :param sz:
#     :return:
#     """
#     trle.color('red')
#     trle.speed(10)
#     agle = 180/5
#     for i in range(5):
#         if i >0:
#             trle.right(agle)
#         else:
#             trle.right(135)
#         trle.penup()
#         trle.forward(np.sqrt(sz**2/2))
#         trle.left(135)
#         for j in range(4):
#             trle.pendown()
#             trle.forward(sz)
#             trle.left(90)
#         trle.left(45)
#         trle.penup()
#         trle.forward(np.sqrt(sz**2/2))
#
#     trle.left(299)
#
#     trle.pendown()
#     agle_2 = 18
#     mag = int(sz/2)
#     for j in range(20):
#         trle.forward(mag)
#         trle.back(mag)
#         trle.left(agle_2)
#     trle.hideturtle()
#
#
# wn = turtle.Screen()
# wn.bgcolor('lightgreen')
#
# alex = turtle.Turtle()
# draw_pretty_square(alex, 450)
#
# wn.mainloop()

""" drawing spirals"""
# import turtle
#
# def sprl(trle, sz):
#     """
#     :param trle:
#     :param sz:
#     :return:
#     """
#     trle.color('blue')
#     trle.speed(10)
#     trle.left(180)
#
#     for i in range(200):
#         trle.forward(sz)
#         trle.right(90)
#         sz += 4
#
# tree = turtle.Turtle()
# wn = turtle.Screen()
# wn.bgcolor('lightgreen')
#
# sprl(tree, 20)
#
# wn.mainloop()
#
# import turtle
#
# def sprl(trle, sz):
#     """
#     :param trle:
#     :param sz:
#     :return:
#     """
#     trle.color('blue')
#     trle.speed(10)
#     trle.left(180)
#     agle = 90
#
#     for i in range(100):
#         trle.forward(sz)
#         trle.right(agle-1)
#         sz += 4
#
# tree = turtle.Turtle()
# wn = turtle.Screen()
# wn.bgcolor('lightgreen')
#
# sprl(tree, 20)
#
# wn.mainloop()

""" sum up function"""
# import numpy as np
#
# def sum_to(n):
#     """
#     :param n:
#     :return:
#     """
#     nums = np.arange(1, n+1)
#     return np.sum(nums)
#
# n = 10
# s = sum_to(n)
# print(f'The sum of numbers from 1 to {n} equals {s}')

""" area of circle"""
# import numpy as np
#
# def area_cir(r):
#     """
#     :param r:
#     :return:
#     """
#     are = np.pi*r*r
#     return are
#
# r = 3
# a = area_cir(r)
# print('The are of a circle with {:.1f} radius equals {:.3f}'.format(r, a))

"""draw a star"""
# import turtle
#
# def draw_star(tees, sz):
#     """
#     :param tees:
#     :param sz:
#     :return:
#     """
#     tees.color('blue')
#     agle = 144
#     tees.speed(1)
#
#     tees.left(agle)
#     tees.forward(sz)
#
#     for _ in range(4):
#         tees.right(agle)
#         tees.forward(sz)
#
#     tees.hideturtle()
#     return
#
# tees = turtle.Turtle()
#
# wn = turtle.Screen()
# wn.bgcolor('red')
#
# draw_star(tees, 300)
# wn.mainloop()

"""draw 5 stars"""
# import turtle
#
#
# def draw_star(tees, sz):
#     """
#     :param tees:
#     :param sz:
#     :return:
#     """
#     tees.color('blue')
#     agle = 144
#     tees.speed(1)
#
#     for _ in range(5):
#         tees.left(agle)
#         tees.forward(sz)
#
#         for _ in range(4):
#             tees.right(agle)
#             tees.forward(sz)
#
#         tees.forward(150)
#         tees.right(144)
#
#     tees.hideturtle()
#     return
#
#
# tees = turtle.Turtle()
#
# wn = turtle.Screen()
# wn.bgcolor('red')
#
# draw_star(tees, 50)
# wn.mainloop()

"""boolean """
# import turtle
#
# def bar(tess, sz):
#     """
#     :param tess:
#     :param sz:
#     :return:
#     """
#     tess.speed(1)
#     tess.begin_fill()
#     tess.left(90)
#     tess.forward(sz)
#     if sz < 0:
#         tess.penup()
#         tess.forward(-15)
#         tess.write('  ' + str(sz))
#         tess.forward(15)
#         tess.pendown()
#     else:
#         tess.write('  '+str(sz))
#     tess.right(90)
#     tess.forward(30)
#     tess.right(90)
#     tess.forward(sz)
#     tess.left(90)
#     tess.end_fill()
#
# xs = [-53, 100, -200, 250, 150, 230, 240, 140]
#
#
# wn = turtle.Screen()
# wn.bgcolor('purple')
#
# trle = turtle.Turtle()
# trle.pensize(2)
#
# for i in xs:
#     if i >= 200:
#         trle.color('blue', 'red')
#     elif 200 > i >= 100:
#         trle.color('blue', 'yellow')
#     elif i<100:
#         trle.color('blue', 'green')
#
#     bar(trle, i)
#     trle.penup()
#     trle.forward(20)
#     trle.pendown()
#
# wn.mainloop()

#
# def find_hyp(sz1, sz2, sz3):
#     """
#     :param sz1:
#     :param sz2:
#     :param sz3:
#     :return:
#     """
#     lenghs = [sz1, sz2, sz3]
#     lenghs.sort()
#     sz3 = lenghs[-1]
#     sz2 = lenghs[1]
#     sz1 = lenghs[0]
#
#     hyp = (sz1**2 + sz2**2)**0.5
#     if abs(hyp - sz3) < 1e-2:
#         h = True
#     else:
#         h = False
#     print(h)
#     return h
#
# find_hyp(10.60, 6.2, 8.6)
#

"""while"""
# import random
#
# def play_once(human_first):
#
#     rng = random.Random()
#     result = rng.randrange(-1, 2)
#     print(f"you_play_first: {human_first}")
#     #       f", winner {result}")
#     if result == -1:
#         print("you win!")
#     elif result == 0:
#         print("game over")
#     else:
#         print("I win!")
#
#     return result
#
# seq = [True, False]
# idx = random.Random().randrange(0, 2)
#
# human_score = 0
# my_score = 0
# all_round = 0
#
# while True:
#     play = input('Do you want to play again?  ')
#     if play == 'yes':
#         first = seq[idx]
#         all_round += 1
#         s = play_once(first)
#         if s == -1:
#             human_score += 1
#         elif s == 1:
#             my_score += 1
#         idx += 1
#         idx %= 2
#     else:
#         print(f'your score: {human_score}/{all_round}, my score: {my_score}/{all_round}, GoodBye!')
#         break

"""Strings"""
# def find(string, ch):
#     cnt = 0
#     for i in string:
#         if i == ch:
#             cnt += 1
#     return cnt
#
# print(find('hassan, ', 's'))
#
# import string
#
# My = 'Short term pleasure, gives you a long term pain and short term pain, gives you a long term pleasure.'
# punc = string.punctuation
#
# def remove_pun(string, letter):
#     cnt_e = 0
#     s_without = ""
#
#     for ch in string:
#         if ch not in punc:
#             s_without += ch
#
#     l = s_without.split()
#     for wo in l:
#         if letter in wo:
#             cnt_e += 1
#
#     percent = (cnt_e/len(l))*100
#     print('Your string contains {0} word, of which {1} ({2:.2f}%) contain an {3}.'
#           .format(len(l), cnt_e, percent, letter))
#     return l
#
# remove_pun(My, 'e')

# print a neat table
# print('\t\t', end="\t")
# for i in range(1, 13):
#     print(i, end= "\t")
#
# print('\n\t\t', ':------------------------------------------------')
#
# for i in range(1, 13):
#     print(f'\t\t{i}:', end='\t')
#     for j in range(1, 13):
#         k = i*j
#         print(k, end= "\t")
#     print('')
#
# def reverse(str):
#     rev = ''
#     i = 1
#     while i <= len(str):
#         rev += str[-i]
#         i += 1
#     return rev
#
# def mirror(str):
#     rev = reverse(str)
#     mirr = str + rev
#     return mirr
#
# def count(str, sub):
#     cnt = 0
#     equ = False
#     for i in range(len(str)):
#         if str[i] == sub[0]:
#             equ =True
#             if i + len(sub) <= len(str):
#                 for j in range(1, len(sub)):
#                         if str[i + j] != sub[j]:
#                             equ = False
#             else:
#                 equ = False
#         if equ == True:
#             cnt +=1
#             equ = False
#     return cnt
#
# print(count('Mississipi','is'))

#
# def remove(str, sub):
#     cnt = 0
#     equ = False
#     rev = ''
#     idx = []
#
#     for i in range(len(str)):
#         if str[i] == sub[0]:
#             equ =True
#             if i + len(sub) <= len(str):
#                 for j in range(1, len(sub)):
#                         if str[i + j] != sub[j]:
#                             equ = False
#             else:
#                 equ = False
#         if equ == True:
#             idx.append(i)
#             cnt +=1
#             equ = False
#     j = 0
#     while j < len(str):
#             if j not in idx:
#                 rev += str[j]
#                 j += 1
#             else:
#                 j += len(sub)
#
#     return rev
#
# print(remove('gs

"""Events"""
# import turtle
#
# turtle.setup(400,500)                # Determine the window size
# wn = turtle.Screen()                 # Get a reference to the window
# wn.title("Handling keypresses!")     # Change the window title
# wn.bgcolor("lightgreen")             # Set the background color
# tess = turtle.Turtle()               # Create our favorite turtle
#
# # The next four functions are our "event handlers".
# def h1():
#    tess.forward(30)
#
# def h2():
#    tess.left(45)
#
# def h3():
#    tess.right(45)
#
# def h4():
#     tess.color('Red')
#
# def h5():
#     tess.color('Green')
#
# def h6():
#     tess.color('Blue')
#
# def h7():
#     p = tess._pensize
#     if p < 19:
#         p += 2
#     tess.pensize(p)
#
# def h8():
#     p = tess._pensize
#     if p > 2:
#         p -= 2
#     tess.pensize(p)
#
# def h9():
#     bg = wn.bgcolor()
#     if bg == 'purple':
#         wn.bgcolor('blue')
#         wn.title('Changed!')
#     else:
#         wn.bgcolor('purple')
#         wn.title('Handling Keypresses!')
#     wn.ontimer(h9, 200)
#     # h9()
#
# def h10():
#     wn.bye()                        # Close down the turtle window
#
# # These lines "wire up" keypresses to the handlers we've defined.
# wn.onkey(h1, "Up")
# wn.onkey(h2, "Left")
# wn.onkey(h3, "Right")
# wn.onkey(h4, "R")
# wn.onkey(h5, "G")
# wn.onkey(h6, "B")
# wn.onkey(h7, "plus")
# wn.onkey(h8, "minus")
# wn.onkey(h9, "c")
# wn.onkey(h10, "q")
#
# # Now we need to tell the window to start listening for events,
# # If any of the keys that we're monitoring is pressed, its
# # handler will be called.
# wn.listen()
# wn.mainloop()

# import turtle           # Tess becomes a traffic light.
#
# turtle.setup(400,500)
# wn = turtle.Screen()
# wn.title("Tess becomes a traffic light!")
# wn.bgcolor("lightgreen")
# tess = turtle.Turtle()
#
#
# def draw_housing():
#     """ Draw a nice housing to hold the traffic lights """
#     tess.pensize(3)
#     tess.color("black", "darkgrey")
#     tess.begin_fill()
#     tess.forward(80)
#     tess.left(90)
#     tess.forward(200)
#     tess.circle(40, 180)
#     tess.forward(200)
#     tess.left(90)
#     tess.end_fill()
#
#
# draw_housing()
#
# tess.penup()
# # tess.hideturtle()
# # Position tess onto the place where the green light should be
# tess.forward(40)
# tess.left(90)
# tess.forward(50)
#
#
# # A traffic light is a kind of state machine with three states,
# # Green, Orange, Red.  We number these states  0, 1, 2
# # When the machine changes state, we change tess' position and
# # her fillcolor.
#
# # This variable holds the current state of the machine
# state_num = -1
#
#
# def advance_state_machine():
#
#     global state_num
#     if state_num == -1:
#         # Turn tess into a big green circle
#         tess.shape("circle")
#         tess.shapesize(3)
#         tess.fillcolor("green")
#         state_num = 0
#
#     if state_num == 0:       # Transition from state 0 to state 1
#         tess.forward(70)
#         tess.fillcolor("orange")
#         state_num = 1
#     elif state_num == 1:     # Transition from state 1 to state 2
#         tess.forward(70)
#         tess.fillcolor("red")
#         state_num = 2
#     else:                    # Transition from state 2 to state 0
#         tess.back(140)
#         tess.fillcolor("green")
#         state_num = 0
#     wn.ontimer(advance_state_machine, 1000)
#
# # Bind the event handler to the space key.
# wn.onkey(advance_state_machine, "space")
#
# wn.listen()                      # Listen for events
# wn.mainloop()


# import turtle           # Tess becomes a traffic light.
# import time
#
# turtle.setup(400,500)
# wn = turtle.Screen()
# wn.title("Tess becomes a traffic light!")
# wn.bgcolor("lightgreen")
#
# tess = turtle.Turtle()
# alex = turtle.Turtle()
# john = turtle.Turtle()
#
# def draw_housing(trle):
#     """ Draw a nice housing to hold the traffic lights """
#     trle.pensize(3)
#     trle.pendown()
#     trle.color("black", "darkgrey")
#     trle.begin_fill()
#     trle.forward(80)
#     trle.left(90)
#     trle.forward(200)
#     trle.circle(40, 180)
#     trle.forward(200)
#     trle.left(90)
#     trle.end_fill()
#
#
# draw_housing(tess)
#
# tess.penup()
# # Position tess onto the place where the green light should be
# tess.forward(40)
# tess.left(90)
# tess.forward(50)
#
# alex.penup()
# # Position tess onto the place where the green light should be
# alex.forward(40)
# alex.left(90)
# alex.forward(120)
#
# john.penup()
# # Position tess onto the place where the green light should be
# john.forward(40)
# john.left(90)
# john.forward(190)
#
# # This variable holds the current state of the machine
# state_num = -1
#
# def h1():
#     global state_num
#     alex.fillcolor('darkorange')
#     john.fillcolor('darkred')
#     tess.shape("circle")
#     tess.shapesize(3)
#     tess.fillcolor("green")
#     state_num = 0
#
# def h2():
#     global state_num
#     alex.shape("circle")
#     alex.shapesize(3)
#     alex.fillcolor("orange")
#     state_num = 1
#
# def h3():
#     global state_num
#     tess.fillcolor('darkgreen')
#     state_num = 2
#
# def h4():
#     global state_num
#     tess.fillcolor('darkgreen')
#     alex.fillcolor('darkorange')
#     john.shape("circle")
#     john.shapesize(3)
#     john.fillcolor("red")
#     state_num = -1
#
# def advance_state_machine():
#
#     global state_num
#
#     if state_num == -1:
#         h1()
#         time.sleep(3)
#
#     if state_num == 0:
#         h2()
#         time.sleep(1)
#
#     if state_num == 1:
#         h3()
#         time.sleep(1)
#
#     if state_num == 2:
#         h4()
#
#     wn.ontimer(advance_state_machine, 2000)
#
# # Bind the event handler to the space key.
# wn.onkey(advance_state_machine, "space")
#
# wn.listen()                      # Listen for events
# wn.mainloop()

"""Lists"""
# def dot_prod(v1, v2):
#     s = 0
#     for i in range(len(v1)):
#         m = v1[i] * v2[i]
#         s += m
#
#     print(s)
#     return s
#
# dot_prod([1, 2, 3], [4, 5, 6])

#
# def replace(str, old, new):
#     rep = " "
#     equ = False
#     rev = []
#     in_ = ""
#
#     for ch in str.split():
#         if old in ch:
#             i = 0
#             while i < len(ch):
#                 if ch[i] == old[0]:
#                     equ =True
#                     if i + len(old) <= len(ch):
#                         for j in range(1, len(old)):
#                                 if ch[i + j] != old[j]:
#                                     equ = False
#                     else:
#                         equ = False
#
#                 if equ == True:
#                     in_ += new
#                     equ = False
#                     i += len(old)
#                 else:
#                     in_ += ch[i]
#                     i += 1
#
#             rev.append(in_)
#             in_ = ""
#         else:
#             rev.append(ch)
#
#     rep = rep.join(rev)
#     print(rep)
#     return rep, rev
#
# replace("I love spom! Spom is my favorite food. Spom, spom, yum!", "o", "a")

"""Modules"""
# def replace(str, old, new):
#     sep = str.split(old)
#     while '' in sep:
#         sep.remove('')
#     rep = new.join(sep)
#     print(rep)
#     return rep
#
# print(replace("Words will now be separated by stars."," ", "**") ==
#               "Words**will**now**be**separated**by**stars.")
#
# import string
#
# punc = string.punctuation
#
# def cleanword(wrd):
#     for p in punc:
#         if p in wrd:
#             wrd = wrd.replace(p, '')
#     return wrd
#
# def has_dashdash(wrd):
#     if '-' in wrd:
#         for idx, ch in enumerate(wrd):
#             if ch == '-' and idx+1 < len(wrd):
#                 if wrd[idx+1] == '-':
#                     return True
#         return False
#     else:
#         return False
#
# def extract_words(str):
#     spl = cleanword(str).split()
#     for i, wrd in enumerate(spl):
#         wrd = wrd.lower()
#         spl[i] = wrd.lower()
#     return spl
#
# def word_count(wrd, str):
#     cnt = 0
#     for wor in str:
#         if wrd == wor:
#             cnt += 1
#     return cnt
#
# def word_set(lis):
#     lis_uni = []
#     for wrd in lis:
#         if wrd not in lis_uni:
#             lis_uni.append(wrd)
#     lis_uni.sort()
#     return lis_uni
#
# def longest_word(lis):
#     lens = []
#     for wrd in lis:
#         lens.append(len(wrd))
#     if len(lens) == 0:
#         lens.append(0)
#     return max(lens)
#
# def test(resu):
#     if resu:
#         print('The test is passed!')
#     else:
#         print('No, try again!')

"""Files"""
# def reverse(old_path, new_path):
#     file_old = open(old_path, 'r')
#     lins = file_old.readlines()
#     lins.reverse()
#     file_old.close()
#
#     file_new = open(new_path, 'w')
#     file_new.writelines(lins)
#     file_new.close()
#     return
#
# reverse('1.txt', '2.txt')
#

# def number(path, path_num):
#     file = open(path, 'r')
#     file_num = open(path_num, 'w')
#
#     cnt = 1
#     while True:
#         lin = file.readline()
#         if len(lin) == 0:
#             break
#         r = 4 - len(str(cnt))
#         lin = ' '*r + str(cnt) + ' ' + lin
#         file_num.writelines(lin)
#         cnt += 1
#
#     file.close()
#     file_num.close()
#
# number('1.txt', '3.txt')

# def de_number(path, path_denum):
#     file = open(path, 'r')
#     file_denum = open(path_denum, 'w')
#
#     cnt = 1
#     while True:
#         lin = file.readline()
#         if len(lin) == 0:
#             break
#         lin = lin[4:]
#         file_denum.writelines(lin)
#         cnt += 1
#
#     file.close()
#     file_denum.close()
#
# de_number('3.txt', '4.txt')

"""List Algorithm"""
#
# def comm(lis1, lis2):
#     c = []
#     for x1 in lis1:
#         if x1 in lis2:
#             c.append(x1)
#     return c
#
# def union(lis1, lis2):
#     c = []
#     for x1 in lis1:
#         if x1 in lis2:
#             lis2.remove(x1)
#     c = lis1 + lis2
#     return c
#
# def bagdiff(lis1, lis2):
#     bd = []
#     for x in lis2:
#         if x in lis1:
#             lis1.remove(x)
#     bd = lis1
#     return bd

# import numpy as np
#
# def share_diag(x0, y0, x1, y1):
#     diff_x = abs(x1 - x0)
#     diff_y = abs(y1 - y0)
#     return diff_x == diff_y
#
# def col_clash(per, c):
#     for i in range(c):
#         if share_diag(i, per[i], c, per[c]):
#             return True
#     return False
#
# def had_clash(boa):
#     for i in range(1, len(boa)):
#         if col_clash(boa, i):
#             return True
#     return False
#
# def main(sz):
#     import random
#     rnd = random.Random()
#
#     boar = list(range(sz))
#     all_solu = []
#     num_fou = 0
#     itr = 0
#     while num_fou < 10:
#         rnd.shuffle(boar)
#         if not had_clash(boar):
#             if boar not in all_solu:
#                 print(f"solution {boar} found in {itr} iterations.")
#                 all_solu.append(boar[:])
#                 num_fou += 1
#                 itr = -1
#         itr += 1
#
# def mirror_y(ans):
#     midd = len(ans)//2
#     res = len(ans) - 2*midd
#     ans_ref = []
#
#     if res==0:
#         for xs in ans:
#             xs_ref = xs + 2*(midd - xs) - 1
#             ans_ref.append(xs_ref)
#     else:
#         for xs in ans:
#             xs_ref = xs + 2*(midd - xs)
#             ans_ref.append(xs_ref)
#     return ans_ref
#
# def mirror_x(ans):
#     ans_ref = ans[:]
#     ans_ref.reverse()
#     return ans_ref
#
# def mirror_diag(ans):
#     col = np.arange(len(ans))
#     ans_ref = []
#     ans_sor = []
#     for i,n in enumerate(ans):
#         ans_ref.append((i, col[n]))
#     ans_ref = np.array(ans_ref)
#     cols_ind = list(ans_ref[:, 1])
#     for j in range(len(ans)):
#         idx = cols_ind.index(j)
#         ans_sor.append(ans_ref[idx, 0])
#     return ans_sor
#
# def mirror_antidiag(ans):
#     col = np.arange(len(ans))
#     ans_ref = []
#     ans_sor = []
#     for i,n in enumerate(ans):
#         ans_ref.append((i, col[n]))
#     ans_ref = np.array(ans_ref)
#     ans_sum = len(ans) - np.sum(ans_ref, axis= -1, keepdims= True) - 1
#     ans_ref += ans_sum
#     cols_ind = list(ans_ref[:, 0])
#     for j in range(len(ans)):
#         idx = cols_ind.index(j)
#         ans_sor.append(ans_ref[idx, 1])
#     return ans_sor
#
# def rotate(ans, n):
#     if n != 0:
#         ans_rot = []
#         for i in range(len(ans)):
#             idx = ans.index(i)
#             idx_ref = len(ans) - idx
#             ans_rot.append(idx_ref - 1)
#     else:
#         return ans
#
#     return rotate(ans_rot, n-1)
#
# # print(rotate([0,4,7,5,2,6,1,3], 2))
#
# def symm(ans):
#     sym = []
#     sym.append(ans)
#     sym.append(mirror_x(ans))
#     sym.append(mirror_y(ans))
#     sym.append(mirror_diag(ans))
#     sym.append(mirror_antidiag(ans))
#
#     for i in range(3):
#         sym.append(rotate(ans, i+1))
#     return sym
#
# ans = [0,4,7,5,2,6,1,3]
#
# def main_unique(sz, num_uni_sol):
#     import random
#     rnd = random.Random()
#
#     boar = list(range(sz))
#     all_symm = []
#     num_fou = 0
#     itr = 0
#     while num_fou < num_uni_sol:
#         rnd.shuffle(boar)
#         if not had_clash(boar):
#             if boar not in all_symm:
#                 print(f"solution {boar} found in {itr} iterations.")
#                 all_symm.extend(symm(boar))
#                 print(all_symm)
#                 num_fou += 1
#                 itr = -1
#         itr += 1
#
# main_unique(5, 2)

#
# import time
#
# start = time.clock()
# main(4)
# end = time.clock()
# print("{0:1.2f} seconds take to run!".format(end-start))
#
# import numpy as np
#
# def lotto_draw():
#     while True:
#         lott = list(np.random.randint(1, 50, 6))
#         lott_rem = lott[:]
#         cnt = 0
#         for _ in range(6):
#             val = lott_rem.pop(0)
#             if val in lott_rem:
#                 cnt += 1
#         if cnt == 0:
#             break
#     return lott
#
# def compare(tick, lott):
#     eq = 0
#     for i in range(6):
#         if tick[i] == lott[i]:
#             eq += 1
#     return eq
#
# def compare_each(tick, draw):
#     eq = []
#     for i in range(len(tick)):
#         t = tick[i]
#         cnt = 0
#         for j in range(6):
#             if t[j] in draw:
#                 cnt += 1
#         eq.append(cnt)
#     return eq
#
# def prime(nubs):
#     ps = []
#     for i in nubs:
#         cnt = 0
#         for j in range(1, i+1):
#             if i % j == 0:
#                 cnt += 1
#         if cnt == 2:
#             ps.append(i)
#     return ps, len(ps)
#
# def miss_primes(lis):
#     pris, _ = prime(np.arange(1, 50))
#     pris = list(pris)
#
#     miss = []
#     for l in lis:
#         for i in l:
#             if i in pris:
#                 pris.remove(i)
#     return pris
#
# def corr_picks():
#     ite = 0
#     while True:
#         lot = lotto_draw()
#         corr = []
#         for t in ticket:
#             cnt = 0
#             for i in lot:
#                 if i in t:
#                     cnt += 1
#             corr.append(cnt)
#         ite += 1
#         if min(corr) >= 4:
#             return ite
#
# def ave():
#     reps = []
#     for _ in range(20):
#         reps.append(corr_picks())
#     return sum(reps)/20, reps

"""Objects & Classes"""
# import numpy as np
#
# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def reflex_y(self):
#         self.y_ref = - self.y
#         return (self.x, self.y_ref)
#
#     def slope_origin(self):
#         if self.x != 0:
#             self.s = self.y/self.x
#         else:
#             self.s = np.inf
#         return self.s
#
#     def get_line_to(self, inst):
#         if self.x != inst.x:
#             m = (self.y - inst.y)/(self.x - inst.x)
#             c = self.y - m*self.x
#         else:
#             m = np.inf
#             c = self.x
#         return (m, c)
#
#     def move(self, off_x, off_y):
#         self.x = self.x + off_x
#         self.y = self.y + off_y
#
#     def __str__(self):
#         return '{}'.format((self.x, self.y))

# p1 = Point(3, 4)
#print(p1.reflex_y())
#print(p1.slope_origin())
#
# p2 = Point(5, 7)
# print(p2.get_line_to(p1))
#
# def distance(p_1, p_2):
#     """The distance between two points!"""
#     d_x  = (p_2.x - p_1.x)**2
#     d_y = (p_2.y - p_1.y)**2
#     d = (d_x + d_y)**0.5
#     return  d

#print(f'{distance(p1, p2):.2f}')
#
# def mid(p1, p2, p3, p4):
#     x_1 = p1.x; x_2 = p2.x; x_3 = p3.x; x_4 = p4.x
#     y_1 = p1.y; y_2 = p2.y; y_3 = p3.y; y_4 = p4.y
#     try:
#         den = (((y_2-y_1)/(x_1-x_2))*(2*x_3 - 2*x_4) + (2*y_3 - 2*y_4))
#         y_0 = (y_3**2 - y_4**2 + x_3**2 - x_4**2 + (2*x_4 - 2*x_3)*(y_1**2 - y_2**2 + x_1**2 - x_2**2)/(2*x_1 - 2*x_2))/den
#         x_0 = (y_1**2 - y_2**2 + x_1**2 - x_2**2 + y_0*(2*y_2 - 2*y_1))/(2*x_1 - 2*x_2)
#         return x_0, y_0
#     except:
#         print('change the order of points or find another points!')
#
# p1 = Point(1, -3)
# p2 = Point(-5, -3)
# p3 = Point(-2, 0)
# p4 = Point(-2, -6)
# print(mid(p1, p2, p3, p4))


#
# class SMS_store():
#     def __init__(self):
#         self.all_mess = []
#
#     def add_new_arrival(self, from_number, time_arrived, text):
#         self.all_mess.append((False, from_number, time_arrived, text))
#
#     @property
#     def message_count(self):
#         return len(self.all_mess)
#
#     @property
#     def get_unread_indexes(self):
#         idxs = [i for i,j in enumerate(self.all_mess) if j[0] is False]
#         return idxs
#
#     def get_message(self, i):
#         try:
#             temp = (True, self.all_mess[i][1], self.all_mess[i][2], self.all_mess[i][3])
#             self.all_mess[i] = temp
#             return self.all_mess[i]
#         except:
#             return None
#
#     def delete(self, i):
#         try:
#             self.all_mess.pop(i)
#         except:
#             pass
#
#     def clear(self):
#         self.all_mess = []
#
#
# post = SMS_store()
# post.add_new_arrival(+98933, 'today', 'hi, ...')
# print(post.message_count)
# print(post.get_unread_indexes)
# print(post.get_message(0))

"""Objects & Classes: A Little Deeper!"""
# class Rectang():
#     def __init__(self, width, height, corner):
#         self.w = width
#         self.h = height
#         self.c = corner
#
#     def grow(self):
#         self.w += 10
#         self.h += 10
#
#     def move(self, inc_x, inc_y):
#         self.c.x += inc_x
#         self.c.y += inc_y
#
#     def __str__(self):
#         return 'A rectangle with height {0}, width {1}, and corner coordinates {2}'.format(self.h, self.w, self.c)
#
#     def area(self):
#         return self.w*self.h
#
#     def peri(self):
#         return (self.w + self.h)*2
#
#     def flip(self):
#         w = self.w
#         h = self.h
#
#         self.w = h
#         self.h = w
#         return self.w, self.h
#
#     def fall_within(self, poin):
#         if self.c.x <= poin.x < self.c.x + self.w and self.c.y <= poin.y < self.c.y + self.h:
#             return True
#         else:
#             return False

# box = Rectang(10, 5, Point(0, 0))
# print(box.fall_within(Point(-3, -3)))
#
# def collide(rec1, rec2):
#     for i in range(2):
#         for j in range(2):
#             a = rec2.c.x + i * rec2.w
#             b = rec2.c.y + j * rec2.h
#             con = rec1.fall_within(Point(a, b))
#             if con:
#                 return True
#     for i in range(2):
#         for j in range(2):
#             a = rec1.c.x + i * rec1.w
#             b = rec1.c.y + j * rec1.h
#             con = rec2.fall_within(Point(a, b))
#             if con:
#                 return True
#     return False
#
# rec1 = Rectang(1, 3, Point(1, 3))
# rec2 = Rectang(2, 3, Point(2, 3))
# print(collide(rec1, rec2))

"""PyGame"""
# import pygame
#
# the_board = [6, 4, 2, 0, 5, 7, 1, 3]
# the_board_duke = [(0,1), (5,2)]
#
# pygame.init()
# colors = [(255, 255, 255), (0,0,0)]    # Set up colors [red, black]
#
# n = len(the_board)         # This is an NxN chess board.
# surface_sz = 480           # Proposed physical surface size.
# sq_sz = surface_sz // n    # sq_sz is length of a square.
# surface_sz = n * sq_sz     # Adjust to exactly fit n squares.
#
# # Create the surface of (width, height), and its window.
# surface = pygame.display.set_mode((surface_sz, surface_sz))
#
# ball = pygame.image.load("ball.jpeg")
# duck = pygame.image.load("duke_seq.png")
# # Use an extra offset to centre the ball in its square.
# # If the square is too small, offset becomes negative,
# #   but it will still be centered :-)
# ball_offset = (sq_sz-ball.get_width()) // 2
# duke_offset = 10
#

# while True:
#
#     # Look for an event from keyboard, mouse, etc.
#     ev = pygame.event.poll()
#     if ev.type == pygame.QUIT:
#         break;
#
#     # Draw a fresh background (a blank chess board)
#     for row in range(n):           # Draw each row of the board.
#         c_indx = row % 2           # Alternate starting color
#         for col in range(n):       # Run through cols drawing squares
#             the_square = (col*sq_sz, row*sq_sz, sq_sz, sq_sz)
#             surface.fill(colors[c_indx], the_square)
#             # Now flip the color index for the next square
#             c_indx = (c_indx + 1) % 2
#
#     # Now that squares are drawn, draw the queens.
#     for (col, row) in enumerate(the_board):
#       surface.blit(ball,
#                (col*sq_sz+ball_offset,row*sq_sz+ball_offset))
#
#     pygame.display.flip()

#
# gravity = 0.0001
#
# class QueenSprite:
#
#     def __init__(self, img, target_posn):
#         self.image = img
#         self.target_posn = target_posn
#         (x, y) = target_posn
#         self.posn = (x, 0)     # Start ball at top of its column
#         self.y_velocity = 0    #    with zero initial velocity
#
#     def update(self):
#         (x_tar, y_tar) = self.target_posn
#         (x, y) = self.posn
#         if y_tar > y:
#             self.y_velocity += gravity       # Gravity changes velocity
#             new_y_pos = y + self.y_velocity  # Velocity moves the ball
#             self.posn = (x, new_y_pos)       #   to this new position.
#
#     def draw(self, target_surface):      # Same as before.
#         target_surface.blit(self.image, self.posn)
#
#     def contains_point(self, pt):
#         """ Return True if my sprite rectangle contains point pt """
#         (my_x, my_y) = self.posn
#         my_width = self.image.get_width()
#         my_height = self.image.get_height()
#         (x, y) = pt
#         return (x >= my_x and x < my_x + my_width and
#                 y >= my_y and y < my_y + my_height)
#
#     def handle_click(self):
#         self.y_velocity += -0.3  # Kick it up
#
#
# all_sprites = []      # Keep a list of all sprites in the game
# # Create a sprite object for each queen, and populate our list.
# for (col, row) in enumerate(the_board):
#     a_queen = QueenSprite(ball,
#                (col*sq_sz+ball_offset, row*sq_sz+ball_offset))
#     all_sprites.append(a_queen)
#
# while True:
#     # Look for an event from keyboard, mouse, etc.
#     ev = pygame.event.poll()
#     if ev.type == pygame.QUIT:
#         break;
#
#     if ev.type == pygame.KEYDOWN:
#         key = ev.dict["key"]
#         if key == 27:  # On Escape key ...
#             break  # leave the game loop.
#         if key == ord("r"):
#             colors[0] = (255, 0, 0)  # Change to red + black.
#         elif key == ord("g"):
#             colors[0] = (0, 255, 0)  # Change to green + black.
#         elif key == ord("b"):
#             colors[0] = (0, 0, 255)  # Change to blue + black.
#
#     if ev.type == pygame.MOUSEBUTTONDOWN:
#         posn_of_click = ev.dict["pos"]
#         for sprite in all_sprites:
#             if sprite.contains_point(posn_of_click):
#                 sprite.handle_click()
#                 break
#
#     # Ask every sprite to update itself.
#     for sprite in all_sprites:
#         sprite.update()
#
#     # Draw a fresh background (a blank chess board)
#     for row in range(n):           # Draw each row of the board.
#         c_indx = row % 2           # Alternate starting color
#         for col in range(n):       # Run through cols drawing squares
#             the_square = (col*sq_sz, row*sq_sz, sq_sz, sq_sz)
#             surface.fill(colors[c_indx], the_square)
#             # Now flip the color index for the next square
#             c_indx = (c_indx + 1) % 2
#
#     # Ask every sprite to draw itself.
#     for sprite in all_sprites:
#         sprite.draw(surface)
#
#     pygame.display.flip()
#
#
# class DukeSprite:
#
#     def __init__(self, img, target_posn):
#         self.image = img
#         self.posn = target_posn
#         self.anim_frame_count = 0
#         self.curr_patch_num = 0
#
#     def update(self):
#         if self.anim_frame_count > 0:
#            self.anim_frame_count = (self.anim_frame_count + 1 ) % 60
#            self.curr_patch_num = self.anim_frame_count // 6
#
#     def draw(self, target_surface):
#         patch_rect = (self.curr_patch_num * 50, 0,
#                        50, self.image.get_height())
#         target_surface.blit(self.image, self.posn, patch_rect)
#
#     def contains_point(self, pt):
#          """ Return True if my sprite rectangle contains  pt """
#          (my_x, my_y) = self.posn
#          my_width = self.image.get_width()/6
#          my_height = self.image.get_height()
#          (x, y) = pt
#          return ( x >= my_x and x < my_x + my_width and
#                   y >= my_y and y < my_y + my_height)
#
#     def handle_click(self):
#          if self.anim_frame_count == 0:
#             self.anim_frame_count = 5
#
# all_sprites = []      # Keep a list of all sprites in the game
# # Create a sprite object for each queen, and populate our list.
# for (col, row) in the_board_duke:
#     a_duck = DukeSprite(duck,
#                (col*sq_sz+duke_offset, row*sq_sz-duke_offset))
#     all_sprites.append(a_duck)
#
# while True:
#     # Look for an event from keyboard, mouse, etc.
#     ev = pygame.event.poll()
#     if ev.type == pygame.QUIT:
#         break;
#
#     if ev.type == pygame.KEYDOWN:
#         key = ev.dict["key"]
#         if key == 27:  # On Escape key ...
#             break  # leave the game loop.
#         if key == ord("r"):
#             colors[0] = (255, 0, 0)  # Change to red + black.
#         elif key == ord("g"):
#             colors[0] = (0, 255, 0)  # Change to green + black.
#         elif key == ord("b"):
#             colors[0] = (0, 0, 255)  # Change to blue + black.
#
#     if ev.type == pygame.MOUSEBUTTONDOWN:
#         posn_of_click = ev.dict["pos"]
#         for sprite in all_sprites:
#             if sprite.contains_point(posn_of_click):
#                 sprite.handle_click()
#                 break
#
#     # Ask every sprite to update itself.
#     for sprite in all_sprites:
#         sprite.update()
#
#     # Draw a fresh background (a blank chess board)
#     for row in range(n):           # Draw each row of the board.
#         c_indx = row % 2           # Alternate starting color
#         for col in range(n):       # Run through cols drawing squares
#             the_square = (col*sq_sz, row*sq_sz, sq_sz, sq_sz)
#             surface.fill(colors[c_indx], the_square)
#             # Now flip the color index for the next square
#             c_indx = (c_indx + 1) % 2
#
#     for (col, row) in enumerate(the_board):
#       surface.blit(ball,
#                (col*sq_sz+ball_offset,row*sq_sz+ball_offset))
#
#     # Ask every sprite to draw itself.
#     for sprite in all_sprites:
#         sprite.draw(surface)
#
#     pygame.display.flip()

# import random
# import numpy as np
# import pygame
#
# cards = list(np.arange(0, 52))
# random.shuffle(cards)
#
# color = (0, 255, 0)
#
# cards_img = pygame.image.load("cards.png")
# card_offset_w = cards_img.get_width()/13
# card_offset_h = cards_img.get_height()/4
# surface_sz_w = round(5*card_offset_w)
# surface_sz_h = round(card_offset_h)
#
# # Create the surface of (width, height), and its window.
# surface = pygame.display.set_mode((surface_sz_w, surface_sz_h))
# # the_square = (0, 0, surface_sz_w, surface_sz_h)
# # surface.fill(color, the_square)
#
#
# while True:
#
#     # Look for an event from keyboard, mouse, etc.
#     ev = pygame.event.poll()
#     if ev.type == pygame.QUIT:
#         break;
#
#     random.shuffle(cards)
#     your_cards = np.random.choice(cards, 5, replace= False)
#
#     for i, c in enumerate(your_cards):
#         row = int(c/13)
#         col = int(c%13)
#         surface.blit(cards_img, (i*card_offset_w, 0*card_offset_h), (col*card_offset_w, row*card_offset_h
#                                                                      , card_offset_w, card_offset_h))
#
#     # Now draw your cards.
#     pygame.display.flip()
#     pygame.time.delay(5000)

"""Recursion"""
# def r_max(nested_num_list):
#     tot_m = ""
#     for element in nested_num_list:
#         if type(element) == type([]):
#             tot_m = r_max(element)
#         elif element > tot_m:
#             tot_m = element
#     return tot_m
#
# print(r_max(["sss", ["sam", "ben"]]))

# def r_max(nested_num_list, tot_m):
#     for element in nested_num_list:
#         if type(element) == type([]):
#             tot_m = r_max(element, tot_m)
#         elif element > tot_m:
#             tot_m = element
#     return tot_m
#
# print(r_max(["sss", ["sam", "ben"]], ""))
# def depth(number):
#     print("The number is {0}".format(number))
#     if number + 1 < 1000:
#         depth(number + 1)
#
# depth(1)

# def fibonachy(n, s1, s2):
#     if n == 1:
#         print('the fib number given two numbers is: {0}'.format(s1+s2))
#     else:
#         print('the fib number given two numbers is: {0}'.format(s1+s2))
#         s1_new = s2
#         s2_new = s1+s2
#         fibonachy(n-1, s1_new, s2_new)

# def fibonachy(n):
#     if n <= 1:
#         return n
#     fib = fibonachy(n-1) + fibonachy(n-2)
#     return fib
#
# print(fibonachy(41))
#
# import turtle
#
# alex = turtle.Turtle()
# screen = turtle.Screen()
# screen.bgcolor('red')
#
# def koch(t, order, size):
#     if order == 0:
#         t.forward(size)
#     else:
#         for angle in [60, -120, 60, 0]:
#             koch(t, order-1, size/3)
#             t.left(angle)
#
# def snowfalke(t, order, size):
#     if order == 0:
#         koch(t, 2, size)
#     else:
#         if order > 3:
#             for i in range(3):
#                 snowfalke(t, 0, size)
#                 t.left(240)
#             t.penup()
#             t.forward(size+20)
#             t.pendown()
#             snowfalke(t, order-3, size)
#         else:
#             for i in range(order):
#                 snowfalke(t, 0, size)
#                 t.left(240)
#
# alex.color('blue')
# alex.speed(1)
# snowfalke(alex, 6, 300)
# screen.mainloop()
#
# import turtle
#
# alex = turtle.Turtle()
# screen = turtle.Screen()
#
# def cesaro(t, order, size, deg):
#     if order == 0:
#         t.forward(size)
#     else:
#         for angle in [275, 170-deg, -85+deg, 0]:
#             x = size/(2 + 2*np.cos(85 * np.pi / 180))
#             cesaro(t, order-1, x, deg)
#             t.left(angle)
#
# alex.color('red')
# screen.bgcolor('blue')
# alex.speed(1)
# cesaro(alex, 3, 900)
# screen.mainloop()

#
# import turtle
# import numpy as np
#
# alex = turtle.Turtle()
# screen = turtle.Screen()
#
# def cesaro_square(t, order, size):
#     if order == 0:
#         t.forward(size)
#     else:
#         for i in range(4):
#             cesaro(t, order, size, 0)
#             t.left(-90)
#
# alex.color('red')
# alex.speed(1)
# alex.penup()
# alex.left(180)
# alex.forward(400)
# alex.left(-180)
# alex.pendown()
#
# screen.bgcolor('blue')
# cesaro_square(alex, 1, 200)
#
# alex.penup()
# alex.forward(210)
# alex.pendown()
# alex.color('green')
# cesaro_square(alex, 2, 200)
#
# alex.penup()
# alex.forward(210)
# alex.pendown()
# alex.color('yellow')
# cesaro_square(alex, 3, 200)
#
# screen.mainloop()
#
# import turtle
#
# def sier_pinski(t, size, order, depth):
#     if order == 0:
#         for angle in [60, -120, -120]:
#             t.left(angle)
#             t.forward(size)
#     else:
#         if depth >= 0:
#             colors = ['red', 'blue', 'magenta']
#         else:
#             colors = [t.pencolor(), t.pencolor(), t.pencolor()]
#
#         t.color(colors[0])
#         sier_pinski(t, size/2, order-1, depth-1)
#         t.left(180)
#         t.penup()
#         t.forward(size/2)
#         t.color(colors[1])
#         t.pendown()
#         sier_pinski(t, size/2, order-1, depth-1)
#         t.left(-60)
#         t.penup()
#         t.forward(size/2)
#         t.left(-120)
#         t.color(colors[2])
#         t.pendown()
#         sier_pinski(t, size/2, order-1, depth-1)
#         t.left(60)
#         t.penup()
#         t.forward(size/2)
#         t.left(-60)
#         t.pendown()
#
#
# alex = turtle.Turtle()
# screen = turtle.Screen()
#
# screen.bgcolor('lightgreen')
# alex.color('red')
# alex.speed(1)
#
# sier_pinski(alex, 1000, 5, 0)
# alex.hideturtle()
# screen.mainloop()

# import numpy as np
#
# def recursive_min(inp):
#     """
#     :param inp:
#     :return:
#     """
#     min_ = np.inf
#     tmp_min = np.inf
#
#     for i in inp:
#         if type(i) == type([]):
#             tmp_min = recursive_min(i)
#         elif i < min_:
#             min_ = i
#         if  tmp_min < min_:
#             min_ = tmp_min
#     return  min_
#
# print(recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6]))

# def recursive_count(c, inp):
#     cnt = 0
#     for i in inp:
#         if type(i) == type([]):
#             tmp_cnt = recursive_count(c, i)
#             cnt = cnt + tmp_cnt
#         elif i == c:
#             cnt += 1
#     return cnt
#
# print(recursive_count("a", [["this",["a",["thing","a"],"a"],"is"], ["a","easy"]]))

# def recursive_flatten(inp):
#     all_l = []
#     for i in inp:
#         if type(i) == type([]):
#             tmp_l = recursive_flatten(i)
#             all_l.extend(tmp_l)
#         else:
#             all_l.append(i)
#     return all_l
#
# print(recursive_flatten([["this",["a",["thing"],"a"],"is"],["a","easy"]]))
#
# def fibonachi(n):
#     if n == 1 or n == 2:
#         return 1
#     fib_ = fibonachi(n-1) + fibonachi(n-2)
#     return fib_
#
# print(fibonachi(40))

# def without(n):
#     if n <= 1:
#         return n
#     all_ = [1, 1]
#     for i in range(n-2):
#         all_.append(all_[-2] + all_[-1])
#     return all_[-1]
#
# print(without(500))

# import os
#
# def get_dirlist(path):
#     """
#       Return a sorted list of all entries in path.
#       This returns just the names, not the full path to the names.
#     """
#     dirlist = os.listdir(path)
#     dirlist.sort()
#     return dirlist
#
# def collect_files(path):
#     all_ = []
#     """ Print recursive listing of contents of path """
#     dirlist = get_dirlist(path)
#     for f in dirlist:
#         fullname = os.path.join(path, f)   # Turn name into full pathname
#         if os.path.isdir(fullname):        # If a directory, recurse.
#             tmp_all = collect_files(fullname)
#             all_.extend(tmp_all)
#         else:
#             all_.append(fullname)
#     return all_
#
# print(collect_files('/home/hassan/PycharmProjects'))

# import os
#
# def get_dirlist(path):
#     """
#       Return a sorted list of all entries in path.
#       This returns just the names, not the full path to the names.
#     """
#     gen = os.walk(path)
#     list_ = next(gen)[1]
#     dirlist = []
#
#     for file in list_:
#         dirlist.append(file)
#     dirlist.sort()
#
#     return dirlist
#
# def litter(path):
#     all_ = []
#     """ Print recursive listing of contents of path """
#     dirlist = get_dirlist(path)
#     for f in dirlist:
#         fullname = os.path.join(path, f)   # Turn name into full pathname
#
#         if get_dirlist(fullname):        # If a directory, recurse.
#             tmp_all = litter(fullname)
#             all_.extend(tmp_all)
#             open(fullname + '/trash.txt', 'w').write('')
#         else:
#             all_.append(fullname)
#             open(fullname + '/trash.txt', 'w').write('')
#     if len(all_) == 0:
#         all_.append(path)
#     return all_
#
# def cleanup(path):
#     all_ = []
#     """ Print recursive listing of contents of path """
#     dirlist = get_dirlist(path)
#     for f in dirlist:
#         fullname = os.path.join(path, f)  # Turn name into full pathname
#
#         if get_dirlist(fullname):        # If a directory, recurse.
#             tmp_all = cleanup(fullname)
#             all_.extend(tmp_all)
#             try:
#                 os.remove(fullname + '/trash.txt')
#             except:
#                 pass
#         else:
#             all_.append(fullname)
#             try:
#                 os.remove(fullname + '/trash.txt')
#             except:
#                 pass
#     if len(all_) == 0:
#         all_.append(path)
#     return all_
#
# print(cleanup('/home/hassan/PycharmProjects'))

"""Exceptions"""
# def recursion_depth(number):
#     print("Recursion depth number", number)
#     try:
#         recursion_depth(number + 1)
#     except:
#         print("I cannot go any deeper into this wormhole.")
#
# recursion_depth(0)

# def readpoint():
#     inp = input('please enter the number... ')
#     res = -1
#     try:
#         inp_pos = int(inp)
#         res = inp_pos - inp_pos
#         div = 1/res
#     except:
#         if res == 0:
#             raise ValueError('The {} is not a positive number.'.format(inp_pos))
#         else:
#             raise ValueError('The {} is not convertible to an int number.'.format(inp))
#
# readpoint()

"""Dictionaries"""
# import string

# def count_string(sent):
#     all_str = {}
#     for i in sent:
#         if not i.isspace() and i not in string.punctuation :
#             i = i.lower()
#             try:
#                 all_str[i] = all_str[i] + 1
#             except:
#                 all_str[i] = 1
#     all_str = list(all_str.items())
#     all_str.sort()
#     for i, j in all_str:
#         print(i,' ', j)
#     return all_str
#
# count_string('ThiS is String with Upper and lower case Letters')

# def add_fruit(inventory, fruit, quantity=0):
#     try:
#         inventory[fruit] = inventory[fruit] + quantity
#     except:
#         inventory[fruit] = quantity
#     return inventory
#
# # Make these tests work...
# new_inventory = {}
# add_fruit(new_inventory, "strawberries", 10)
# print("strawberries" in new_inventory)
# print(new_inventory["strawberries"] == 10)
# add_fruit(new_inventory, "strawberries", 25)
# print(new_inventory["strawberries"] == 35)

# import string
# import sys
#
# def count_words(sent):
#     all_str = {}
#     puns = string.punctuation.replace('-', '')
#
#     for i in sent.split():
#             i = i.lower()
#             for k in puns:
#                 if k in i:
#                     i = i.replace(k, '')
#             if '--' in i:
#                 i = i.replace('--', '')
#             if not i.isnumeric() and len(i) != 0:
#                 try:
#                     all_str[i] = all_str[i] + 1
#                 except:
#                     all_str[i] = 1
#     all_str = list(all_str.items())
#     all_str.sort()
#     for i, j in all_str:
#         print('{:<28} {:<3}'.format(i, j))
#     return all_str
#
# def alice_words(inp_txt, out_txt):
#
#     counts = count_words(inp_txt.read())
#     print(k, end="\t")
#     with open(out_txt, 'w') as f:
#         f.write('Word' '\t\t\t\t\t\t' 'Count' '\n' '=================================' '\n')
#         for i, j in counts:
#             f.write(f'{i}' '\t\t\t\t\t\t\t' f'{j}' '\n')
#     f.close()
#     return counts
#
# def alice_words(inp_txt, out_txt):
#
#     counts = count_words(inp_txt.read())
#     orig_stdout = sys.stdout
#     with open(out_txt, 'w') as f:
#         f.write('Word' '\t\t\t\t\t\t' 'Count' '\n' '=================================' '\n')
#         sys.stdout = f
#         for i, j in counts:
#             print('{:<28} {:<3}'.format(i, j))
#     sys.stdout = orig_stdout
#     f.close()
#     return counts
#
# inp = open('./alice_in_wonderland.txt')
# alice_words(inp, './alice_words.txt')

"""More on OOP"""
# class Time():
#
#     def __init__(self, t):
#         self.t = self.to_seconds(t)
#
#     def to_seconds(self, rt):
#         return rt[0]*3600 + rt[1]*60 + rt[2]
#
#     def between(self, t1, t2):
#         t1 = self.to_seconds(t1)
#         t2 = self.to_seconds(t2)
#         if  t1 <= self.t < t2:
#             return True
#         return False
#
# time=  Time((2, 30, 50))
# print(time.between((1, 10, 30), (3, 40, 50)))
#
# class Time():
#
#     def __init__(self, t):
#         self.t = self.to_seconds(t)
#
#     def to_seconds(self, rt):
#         return rt[0]*3600 + rt[1]*60 + rt[2]
#
#     def increment(self, sec):
#         if sec < 0 and abs(sec) > self.t:
#             sec = -self.t
#
#         self.t += sec
#         self.hours = self.t //3600
#         self.mins = (self.t % 3600) // 60
#         self.secs =  self.t % 3600 % 60
#         return (self.hours, self.mins, self.secs)
#
#     def __str__(self):
#         return 'total seconds:{0:5.0f}'.format(self.t)
#
#     def __lt__(self, other):
#         return other.t > self.t
#
# time = Time((2, 30, 57))
# print(time.increment(-20000))
#
# time1 = Time((1, 30, 51))
# time2 = Time((3, 30, 53))
#
# print(time2 > time)
#
# def between(t1, t2, t):
#     if time1.t <= time.t < time2.t:
#         return True
#     return False
#
# print(between(time1, time2, time))

"""Collection of Objects"""
# class Card:
#     suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
#     ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7",
#              "8", "9", "10", "Jack", "Queen", "King"]
#
#     def __init__(self, suit=0, rank=0):
#         self.suit = suit
#         self.rank = rank
#
#     def __str__(self):
#         return (self.ranks[self.rank] + " of " + self.suits[self.suit])
#
#     def cmp(self, other):
#         # Check the suits
#         if self.suit > other.suit:
#             return 1
#
#         if self.suit < other.suit:
#             return -1
#
#         # Suits are the same... check ranks
#         if self.rank == 1:
#             return 1
#
#         elif other.rank == 1:
#             return -1
#
#         elif self.rank > other.rank:
#             return 1
#
#         elif self.rank < other.rank:
#             return -1
#         # Ranks are the same... it's a tie
#         return 0
#
#     def __eq__(self, other):
#         return self.cmp(other) == 0
#
#     def __le__(self, other):
#         return self.cmp(other) <= 0
#
#     def __ge__(self, other):
#         return self.cmp(other) >= 0
#
#     def __gt__(self, other):
#         return self.cmp(other) > 0
#
#     def __lt__(self, other):
#         return self.cmp(other) < 0
#
#     def __ne__(self, other):
#         return self.cmp(other) != 0
#
# card1 = Card(1, 13)
# card2 = Card(1, 1)
#
# print(card2 > card1)

"""Inheritance"""
# class Card:
#     suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
#     ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7",
#              "8", "9", "10", "Jack", "Queen", "King"]
#
#     def __init__(self, suit=0, rank=0):
#         self.suit = suit
#         self.rank = rank
#
#     def __str__(self):
#         return (self.ranks[self.rank] + " of " + self.suits[self.suit])
#
#     def cmp(self, other):
#         # Check the suits
#         if self.suit > other.suit:
#             return 1
#
#         if self.suit < other.suit:
#             return -1
#
#         # Suits are the same... check ranks
#         if self.rank == 1:
#             return 1
#
#         elif other.rank == 1:
#             return -1
#
#         elif self.rank > other.rank:
#             return 1
#
#         elif self.rank < other.rank:
#             return -1
#         # Ranks are the same... it's a tie
#         return 0
#
#     def __eq__(self, other):
#         return self.cmp(other) == 0
#
#     def __le__(self, other):
#         return self.cmp(other) <= 0
#
#     def __ge__(self, other):
#         return self.cmp(other) >= 0
#
#     def __gt__(self, other):
#         return self.cmp(other) > 0
#
#     def __lt__(self, other):
#         return self.cmp(other) < 0
#
#     def __ne__(self, other):
#         return self.cmp(other) != 0
#
# class Deck:
#     def __init__(self):
#         self.cards = []
#         for suit in range(4):
#             for rank in range(1, 14):
#                 self.cards.append(Card(suit, rank))
#
#     def print_deck(self):
#         for card in self.cards:
#             print(card)
#
#     def __str__(self):
#         s = ""
#         for i in range(len(self.cards)):
#             s = s + " " * i + str(self.cards[i]) + "\n"
#         return s
#
#     def shuffle(self):
#         import random
#         rng = random.Random()  # Create a random generator
#         rng.shuffle(self.cards)  # uUse its shuffle method
#
#     def remove(self, card):
#         if card in self.cards:
#             self.cards.remove(card)
#             return True
#         else:
#             return False
#
#     def pop(self):
#         return self.cards.pop()
#
#     def is_empty(self):
#         return self.cards == []
#
#     def deal(self, hands, num_cards=999):
#         num_hands = len(hands)
#         for i in range(num_cards):
#             if self.is_empty():
#                 break  # Break if out of cards
#             card = self.pop()  # Take the top card
#             hand = hands[i % num_hands]  # Whose turn is next?
#             hand.add(card)  # Add the card to the hand
#
# class Hand(Deck):
#     def __init__(self, name=""):
#         self.cards = []
#         self.name = name
#
#     def add(self, card):
#         self.cards.append(card)
#
#     def __str__(self):
#         s = "Hand " + self.name
#         if self.is_empty():
#             s += " is empty\n"
#         else:
#             s += " contains\n"
#         return s + Deck.__str__(self)
#
# class CardGame:
#     def __init__(self):
#         self.deck = Deck()
#         self.deck.shuffle()
#
# class OldMaidHand(Hand):
#     def remove_matches(self):
#         count = 0
#         original_cards = self.cards[:]
#         for card in original_cards:
#             match = Card(3 - card.suit, card.rank)
#             if match in self.cards:
#                 self.cards.remove(card)
#                 self.cards.remove(match)
#                 print("Hand {0}: {1} matches {2}"
#                         .format(self.name, card, match))
#                 count += 1
#         return count
#
# class OldMaidGame(CardGame):
#     def play(self, names):
#         # Remove Queen of Clubs
#         self.deck.remove(Card(0,12))
#
#         # Make a hand for each player
#         self.hands = []
#         for name in names:
#             self.hands.append(OldMaidHand(name))
#
#         # Deal the cards
#         self.deck.deal(self.hands)
#         print("---------- Cards have been dealt")
#
#         self.print_hands()
#
#         # Remove initial matches
#         matches = self.remove_all_matches()
#         print("---------- Matches discarded, play begins")
#         self.print_hands()
#
#         # Play until all 50 cards are matched
#         turn = 0
#         num_hands = len(self.hands)
#         while matches < 25:
#             matches += self.play_one_turn(turn)
#             turn = (turn + 1) % num_hands
#
#         print("---------- Game is Over")
#         self.print_hands()
#
#     def remove_all_matches(self):
#         count = 0
#         for hand in self.hands:
#             count += hand.remove_matches()
#         return count
#
#     def play_one_turn(self, i):
#         if self.hands[i].is_empty():
#             return 0
#         neighbor = self.find_neighbor(i)
#         picked_card = self.hands[neighbor].pop()
#         self.hands[i].add(picked_card)
#         print("Hand", self.hands[i].name, "picked", picked_card)
#         count = self.hands[i].remove_matches()
#         self.hands[i].shuffle()
#         return count
#
#     def find_neighbor(self, i):
#         num_hands = len(self.hands)
#         for next in range(1, num_hands):
#             neighbor = (i + next) % num_hands
#             if not self.hands[neighbor].is_empty():
#                 return neighbor
#
#     def print_hands(self):
#         for h in self.hands:
#             print("The hands of {}:".format(h.name))
#             print("suits and ranks ==>", end= '\t')
#             for i, c in enumerate(h.cards):
#                 if i != len(h.cards) - 1:
#                     print('({:<3}, {:<2})'.format(c.suits[c.suit], c.rank), end= ',\t')
#                 else:
#                     print('({:<3}, {:<2})'.format(c.suits[c.suit], c.rank), end= '.\n')
#
# game = OldMaidGame()
# hands = game.play(["Allen","Jeff","Chris"])
#
# import turtle
# import random
#
# Turtle= turtle.Turtle
#
# class TurtleGTX(Turtle):
#     def __init__(self):
#         super(TurtleGTX, self).__init__()
#         self.odo = 0
#         self.alex = Turtle()
#         self.cnt = 0
#
#     def forward(self, jump):
#         if self.cnt > 20:
#             raise ValueError("flat tire!")
#         else:
#             self.alex.color('red')
#             self.alex.stamp()
#             self.alex.penup()
#             self.alex.forward(jump)
#             self.alex.pendown()
#             self.odo += abs(jump)
#             self.cnt += 1
#         return self.odo
#
#     def change_tyre(self):
#         self.cnt  = 0
#
# wg = turtle.Screen()
# wg.bgcolor('lightgreen')
# tur_gtx = TurtleGTX()
# for i in range(40):
#     j = random.randint(-400, 400)
#     try:
#         print(tur_gtx.forward(j))
#     except:
#         tur_gtx.change_tyre()
# wg.mainloop()
#
# class Go:
#     def __init__(self, a):
#         self.a = a
#     def to_do(self):
#         return self.a**2
#
# class FO(Go):
#     def __init__(self, f):
#         super(FO, self).__init__(f)
#         self.f = f
#     def to_fo(self):
#         return self.f*2
#
# fo = FO(3)
# print(fo.to_do())

"""Linked Lists"""
# def print_list(lis):
#     if lis is not None:
#         print('[', end= "")
#         for k, i in enumerate(lis):
#             if k != len(lis)-1:
#                 print(f'{i}', end= ", ")
#             else:
#                 print(f'{i}]')
#
# print_list([1, 2, 3])

"""Stacks"""
# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         return self.items.pop()
#
#     def is_empty(self):
#         return (self.items == [])
#
# def eval_postfix(expr):
#     import re
#     token_list = re.split("([^0-9])", expr)
#     stack = Stack()
#     for token in token_list:
#         if token == "" or token == " ":
#             continue
#         if token == "+":
#             sum = stack.pop() + stack.pop()
#             stack.push(sum)
#         elif token == "*":
#             product = stack.pop() * stack.pop()
#             stack.push(product)
#         else:
#             stack.push(int(token))
#     return stack.pop()
#
# print(eval_postfix("2 3 * 1 +"))

"""Queues"""
# class Node:
#     def __init__(self, cargo=None, next=None):
#         self.cargo = cargo
#         self.next  = next
#
#     def __str__(self):
#         return str(self.cargo)
#
#     def print_backward(self):
#         if self.next is not None:
#             tail = self.next
#             tail.print_backward()
#         print(self.cargo, end=" ")
#
#
# class ImprovedQueue:
#     def __init__(self):
#         self.length = 0
#         self.head = None
#         self.last = None
#
#     def is_empty(self):
#         return self.length == 0
#
#     def insert(self, cargo):
#         node = Node(cargo)
#         if self.length == 0:
#             # If list is empty, the new node is head and last
#             self.head = self.last = node
#         else:
#             # Find the last node
#             last = self.last
#             # Append the new node
#             last.next = node
#             self.last = node
#         self.length += 1
#
#     def remove(self):
#         cargo = self.head.cargo
#         self.head = self.head.next
#         self.length -= 1
#         if self.length == 0:
#             self.last = None
#         return cargo
#
# iq = ImprovedQueue()
# iq.insert('hassan')
# iq.insert('hossein')
# iq.insert('fatemeh')
#
# lis = []
#
# def is_empty(l = lis):
#     return len(lis) == 0
#
# def insert(cargo, last_pre= None, length= 0):
#     node = Node(cargo)
#     if is_empty():
#         # If list is empty, the new node is head and last
#         head = last_pre = node
#         lis.append(head)
#     else:
#         # Find the last node
#         last = last_pre
#         # Append the new node
#         last.next = node
#         last_pre = node
#         lis.append(node)
#
#     length += 1
#     try:
#         return head, last_pre, length
#     except:
#         return  last_pre, length
#
# head, last, length= insert('hassan')
# last, length= insert('hossein', last, length)
# last, length= insert('fatemeh', last, length)
#
# def remove(head= head, length= length):
#     cargo = head.cargo
#     head = head.next
#     length -= 1
#     if length == 0:
#         last = None
#     lis.pop(0)
#     return cargo, length, lis
#
# cargo, length, lis = remove(lis[0])
#
# class PriorityQueue:
#     def __init__(self):
#         self.items = []
#
#     def is_empty(self):
#         return not self.items
#
#     def insert(self, item):
#         self.items.append(item)
#         self.items.sort()
#         self.items.reverse()
#
#     def remove(self):
#         maxi = 0
#         item = self.items[maxi]
#         del self.items[maxi]
#         return item
#
# p = PriorityQueue()
# p.insert(1)
# p.insert(2)
# p.insert(5)
# print(p.remove())

"""Trees"""
# import pickle
#
# class Tree:
#     def __init__(self, cargo, left=None, right=None):
#         self.cargo = cargo
#         self.left = left
#         self.right = right
#
#     def __str__(self):
#         return str(self.cargo)
#
# tree = Tree("+", Tree(1), Tree("*", Tree(2), Tree(3)))
#
# def print_tree_inorder(tree, stri):
#     if tree is None:
#         return stri
#     stri = print_tree_inorder(tree.left, stri)
#     if type(tree.cargo) == type(0):
#         # print("(",tree.cargo, end='')
#         stri += "("
#         stri += str(tree.cargo)
#         stri += " "
#     else:
#         # print(tree.cargo, end='')
#         stri += tree.cargo
#         stri += " "
#
#     stri = print_tree_inorder(tree.right, stri)
#     return stri
#
# ss = print_tree_inorder(tree, '')
# ss += "))"
#
# def token(stri):
#     spli = stri.split()
#     token = []
#     for i in spli:
#         if '(' in i:
#             i_ref = i.replace('(', ' ( ')
#             i_spli = i_ref.split()
#             for j in i_spli:
#                 try:
#                     j = int(j)
#                 except:
#                     pass
#                 token.append(j)
#         elif ')' in i:
#             i_ref = i.replace(')', ' ) ')
#             i_spli = i_ref.split()
#             for j in i_spli:
#                 try:
#                     j = int(j)
#                 except:
#                     pass
#                 token.append(j)
#         else:
#             try:
#                 i = int(i)
#             except:
#                 pass
#             token.append(i)
#     token.append('end')
#     return token
#
# print(token('(((3 + 7)) * 9)'))
#
# def get_token(token_list, expected):
#     if token_list[0] == expected:
#         del token_list[0]
#         return True
#     return False
#
# def get_number(token_list):
#     if get_token(token_list, "("):
#         x = get_sum(token_list)         # Get the subexpression
#         if not get_token(token_list, ")"):
#             raise ValueError('Missing close parenthesis')
#         return x
#     else:
#         x = token_list[0]
#         if type(x) != type(0): return None
#         del token_list[0]
#         return Tree(x, None, None)
#
# def get_product(token_list):
#     a = get_number(token_list)
#     if get_token(token_list, "*"):
#         b = get_product(token_list)       # This line changed
#         return Tree("*", a, b)
#     return a
#
# def get_sum(token_list):
#     a = get_product(token_list)
#     if get_token(token_list, "+"):
#         b = get_sum(token_list)
#         return Tree("+", a, b)
#     return a
#
# def print_tree_inorder(tree):
#     if tree is None: return
#     print_tree_inorder(tree.left)
#     print(tree.cargo, end=" ")
#     print_tree_inorder(tree.right)
#
# def print_tree_postorder(tree):
#     if tree is None: return
#     print_tree_postorder(tree.left)
#     print_tree_postorder(tree.right)
#     print(tree.cargo, end=" ")

# token_list = [9, 11, "end"]
# x = get_number(token_list)
# print_tree_postorder(x)
#
# token_list = token('9 * (11 + 5) * 7')
# tree = get_sum(token_list)
# print_tree_postorder(tree)
#
# def yes(ques):
#     ans = input(ques).lower()
#     return ans[0] == "y"
#
# def animal():
#     # Start with a singleton
#     root = Tree("bird")
#     # tree = root
#     # Loop until the user quits
#     for i in range(3):
#         print()
#         if not yes("Are you thinking of an animal? "): break
#
#         # Walk the tree
#         tree = root
#
#         while tree.left is not None:
#             prompt = tree.cargo + "? "
#             if yes(prompt):
#                 tree = tree.right
#             else:
#                 tree = tree.left
#
#         # Make a guess
#         guess = tree.cargo
#         prompt = "Is it a " + guess + "? "
#         if yes(prompt):
#             print("I rule!")
#             continue
#
#         # Get new information
#         prompt = "What is the animal's name? "
#         animal = input(prompt)
#         prompt = "What question would distinguish a {0} from a {1}? "
#         question = input(prompt.format(animal, guess))
#
#         # Add new information to the tree
#         tree.cargo = question
#         prompt = "If the animal were {0} the answer would be? "
#         if yes(prompt.format(animal)):
#             tree.left = Tree(guess)
#             tree.right = Tree(animal)
#         else:
#             tree.left = Tree(animal)
#             tree.right = Tree(guess)
#     return tree
#
# t = animal()
#
# with open('tree.pkl', 'wb') as f:
#     pickle.dump(t, f)
#
# with open('tree.pkl', 'rb') as f:
#     t1 = pickle.load(f)

"""Some tips, tricks, and common mistakes"""
# import numpy as np
#
# def all_odd(lis):
#     for l in lis:
#         if l % 2 == 0:
#             return False
#     return True
#
# print(all_odd([3, 5, 7, 9, 8]))
#
# def three_odd(lis):
#     counts = 0
#     for l in lis:
#         if l % 2 == 1:
#             counts += 1
#         if counts > 2:
#             return True
#     return counts > 2
#
# three_odd([3, 12, 8, 10, 7, 6])
#
# web = np.loadtxt('./web.txt', dtype= str, delimiter= '\n')
# for l in web:
#     idx = l.find('http')
#     if idx > 0:
#         idx_las = l.find(' ', idx)
#         print(f'The site is : {l[idx-1:idx_las]}')
#
# def angle_str(strin):
#     idx_st = strin.find('<')
#     idx_en = strin.find('>')
#
#     print(strin[idx_st+1:idx_en])
#
# angle_str('Hello, come here and <Be The Exception>...')
