print('Welcome to AskPython Quiz')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=3

if answer.lower()=='yes':
    answer=input('Question 1: What is your country name?')
    if answer.lower()=='bangladesh':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')


    answer=input('Question 2:What is your favourite programing language? ')
    if answer.lower()=='python':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer=input('Question 3:Who invented the language  ?')
    if answer.lower()=='Guido van Rossum':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer=input('Question 4:when was the language invented ?')
    if answer.lower()=='1991':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!')