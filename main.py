import sys
import ar_ro_numeral_conv as conv # importing numeral our numeral converting lib, as conv 
  

def main():
  while( True ):
    input_value = input(" Please, enter roman or arabic number: ")
    print( input_value + " is " +  conv.road_fork( input_value.upper() ))


main()