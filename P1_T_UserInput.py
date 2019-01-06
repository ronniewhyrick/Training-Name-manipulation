#comment tester
#Ron Whyrick
#Project 1: User Input

#Description********************************************************************************************************************

#takes input and stores the string in the variable 'name'
#Then finds how many characters are in the string and stores as name_len
#prints both values
#runs through a boolean check to makes sure the name given fits into the arbitrary parameters, if not, it is categorized as such 

def main():
    run = True
    while(run):
        print("please enter your name")
        name = input()
        name_len_raw = len(name)
        spacecnt = name.count(' ')
        #print(spacecnt)
        name_len = name_len_raw - spacecnt
        if any(char.isdigit() for char in name):
            number = True
        else:
            number = False 
        if name_len  == 1 or number == True:
          print("Don't play with me now, that's not your name")

        elif name_len > 50:
            print ("You have a really long name, Please enter a shorter version")

        else:
            print("Nice to meet you " + name")
            vowels = 0
            counts = {i:0 for i in 'AaEeIiOoUuYy'}
            for char in name:
             if char in counts:
                vowels += 1
            consonants = name_len - vowels
            l_str = str(name_len)
            v_str = str(vowels)
            c_str = str(consonants)
            print("Your name has " + l_str + " letters in it")
            print("it has " + v_str + " vowels and subsequently " + c_str + " consonants")
            print("What a lovely name, be sure to check out my creators other programs")
            run = False
#When python runs a source file as a main function it sets the internal variable (__name__== "__main__") so we define the
#'main' function as definitions go first, then check the boolean which will be true, this executes the 'main' function        

if __name__== "__main__":
  main()
    
