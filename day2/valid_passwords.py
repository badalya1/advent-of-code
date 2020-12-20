def is_valid(policy, password:str):
    interval, letter = policy.split(" ")
    low, high = (int(num) for num in interval.split("-"))
    return low <= password.count(letter) <= high

def is_valid2(policy:str, password:str):
    indecies, letter = policy.split(" ")
    first_i, second_i = (int(num) for num in indecies.split("-"))
    if (password[first_i-1]==letter) ^ (password[second_i-1]==letter):
        return True
    return False



def main(entries):
    total = 0
    for policy, password in entries:
        if not is_valid2(policy, password):
            print(policy, password)
        else:
            total+=1
    print(f'There are {total} right passwords')


    

if __name__=="__main__":
    entries = []
    with open("input.txt") as f:
        for line in f:
            entries.append(line.strip().split(": "))
    main(entries)
