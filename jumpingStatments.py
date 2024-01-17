# demostration of "break" keyword under Jumping Statements:

print("\ndemostration of break keyword:")
for i in range(10):
    print(i)
    if(i == 7):
        print('break')
        break


# demostration of "continue" keyword under Jumping Statements:

print("\ndemostration of continue keyword:")
for i in range(6):
    if(i == 3):
        continue
    print(i)


# demostration of "pass" keyword under Jumping Statements:

print("\ndemostration of pass keyword:")
for i in 'programming':
    if(i == 'i'):
        pass
    else:
        print(i)