import random

class wild_guess(object):
    def guess(self):
        is_right = "true"
        random_number = random.randint(1, 100)
        # print random_number;
        print "please input you guess [1~100]"
        while is_right:
            try:
                guess = int(raw_input())
                if guess == random_number:
                    print "Congratulation, you find the correct number"
                    is_right = "falses"
                    break
                elif guess > random_number:
                    print "too big, please try again"
                else:
                    print "too small, please try again"

            except Exception as e:
                print "just number, please"
                guess =0

if __name__ == "__main__":
    guess = wild_guess()
    guess.guess()


dhyy_8078