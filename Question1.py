import math
def calculate_sq_root(number, guess,iterations=5):
    if not (guess and number):
        return "Please enter a number and guess value: "
    if not (isinstance(guess, int) or isinstance(guess, float)):
        return "The guess number must be an integer or float. "

    for _ in range(iterations):
        guess = 0.5 * (guess + (number / guess))

    return guess



def main():
    number= float(input("Please enter a number t find the square root of:- "))
    guess = float(input("Please enter a guess value:- "))
    iterations = int(input("Please enter number of iterations:- "))
    accuracy = int(input("Please enter the accuracy you want:- "))
    print(f"The root of {number} is {calculate_sq_root(number,guess) :.{accuracy+1}}")
    if calculate_sq_root(number,guess,iterations) == math.sqrt(number):
        print("The value of root of a is fixed.")

if __name__ == '__main__':
    main()