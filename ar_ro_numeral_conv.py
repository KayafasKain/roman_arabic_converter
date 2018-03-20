import re

#the ditcionary of common roman numerals
roman_dict = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1
}

#precompiling regular expressions, to optimize processing of huge amounts of numerals
compiled_roman = re.compile("^(?=[MDCLXVI])M*(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$") 
compiled_arab = re.compile("^[0-9]*$")


def road_fork( value ):
  """ 
    These function provides validation, recognition of input values and
    invokes proper functions to process received data.
  """
  try:
    
    if len( value ) == 0:
      raise ValueError(" input must not be empty ")
    elif( compiled_roman.search( value )):
      return to_arab( value )
    elif( compiled_arab.search( value )):
      return to_roman( value )
    else:
      raise ValueError( value + " - is wrong, please use arabic or latin numerals ")
      
  except ValueError as error:
    return str(error)
    
def to_arab( r_num ):
  """
    Here goes the process of converting roman numbers to arabic
    function accepts and returns string
  """
  result = 0
  prev_val = 0 # cotains previous number, in order to convert statements like these: IV, CM, etc.
  for num in r_num:
    current_val = roman_dict[num]
    if current_val > prev_val: # if previous numeral < current, then subtracting it rom result variable
      result += current_val - 2 * prev_val # multiply to compensate previous records in result
    else:
      result += current_val
    prev_val = current_val
    
  return str(result)

def to_roman( a_num ):
  """
    Here goes the process of converting arabic numbers to roman
    function accepts and returns string
  """
  result = ""
  a_num = int( a_num )
  for num in roman_dict:# crowling trough roman numeral dictionary
    count = int( a_num / roman_dict[num] )# figuring out how many roman numerals in arabic number are
    if count == 1:
      result += num # if it is only one instance of roman numeral, then adding it to resoult
    elif count > 1:  
      for i in range( count ): # otherwise adding few numerals  
        result += num
    a_num -= roman_dict[num] * count # calculating remaining arabic number
  return str(result)
  
  
  
  