"""This is a program that will find the area of both a circle and a triangle"""
print ' The program is running'
option = raw_input ( 'Enter C for circle or T for triangle ')
if option == 'C':
  radius = float(raw_input ( 'What is the radius?'))
  area = 3.14159*radius**2
  print 'The area of the given circle is %f'% area
elif option == 'T':
  base = float(raw_input( 'What is the base of the triangle?'))
  height = float(raw_input( 'What is the height of the triangle?'))
  area= 0.5 * base * height
  print 'the area of the given triangle is %f'% area
else:
  print 'Invalid shape'
print 'Exiting Program'
