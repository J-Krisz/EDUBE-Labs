# PCAP lab 2.4.1.6
# print digits in seven segment display style on to terminal

pattern ={
"1": ['  #', '  #', '  #', '  #', '  #'],
"2": ['###', '  #', '###', '#  ', '###'],
"3": ['###', '  #', '###', '  #', '###'],
"4": ['# #', '# #', '###', '  #', '  #'],
"5": ['###', '#  ', '###', '  #', '###'],
"6": ['###', '#  ', '###', '# #', '###'],
"7": ['###', '  #', '  #', '  #', '  #'],
"8": ['###', '# #', '###', '# #', '###'],
"9": ['###', '# #', '###', '  #', '###'],
"0": ['###', '# #', '# #', '# #', '###'],
".": ['   ', '   ', '   ', '   ', '  #']}       # dictionary containing patter for each digit

def ssd(n):
    """
    The function prints non negative floats in seven segment display style
    :param n: input digit
    :return:  seven segment representation of a digit
    """

    for i in range(len(pattern['0'])):          # loop in the range of dict value length(5)
        digits = []                             # create 5 lists
        for digit in n:                         # iterate over input digits
            digits.append(pattern[digit][i])    # append iteration of dict values to our lists
        print("  ".join(digits))                # join elements of the list in to a string

num = input("Enter a number : ")


ssd(num)

