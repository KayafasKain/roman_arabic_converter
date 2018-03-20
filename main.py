import sys
import ar_ro_numeral_conv as conv # importing numeral our numerl converting lib, as conv 
  

def main():
    " Receiving data. If args was specified, otherwise program asks of manual input "
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
          print( arg + " is " + conv.road_fork( arg.upper() ))
    else:
      while( True ):
        input_value = input(" Please, enter roman or arabic numeral: ")
        print( input_value + " is " +  conv.road_fork( input_value.upper() ))

if __name__ == "__main__":
    main()