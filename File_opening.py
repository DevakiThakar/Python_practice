trial = open('trial_1.txt')
r_file = trial.read()
print(r_file)
print('enter number:')
typed = input()
print(typed)
if int(typed) == int(r_file):
    print('file opened')
else:
    print('text does not match')
