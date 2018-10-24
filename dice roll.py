"""This is a program that rolls a pair of dice and ask the user to guess the sum. If the user guesses right he/she wins otherwise the computer wins"""
from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input( 'Guess the number:'))
  return guess
  
def roll_dice(number_of_sides):
  first_roll = randint( 1, number_of_sides)
  second_roll = randint( 1, number_of_sides)
  max_val = number_of_sides * 2
  print ('The max possible value is: %d') % max_val
  guess = get_user_guess()
  if guess > max_val:
  	print ( 'Invalid guess' )
  else:
    print ( ' rolling...' )
    sleep(2)
    print ( ' The 1st roll is: %d' % first_roll)
    sleep(1)
    print ( ' The 2nd roll is: %d' % second_roll)
    sleep(1)
    print (' Result...')
    sleep(1)
    total_roll = first_roll+ second_roll
    if guess== total_roll:
      print (' You Win!!! ')
    else:
      print ( ' You lost, Try again!')
      
      
roll_dice(6)
