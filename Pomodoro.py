import time, os,datetime

def pomodoro( a, b, i):
    os.system("clear")
    mensaje("Study Time")
    print(f"{i+1}/4: Studing time for {a} minutes ...")
    print(datetime.datetime.now())
    time_(a) ;#time.sleep(60*int(a))
    os.system("clear")
    mensaje("Break Time")
    print(f"{i+1}/4: Break time for {b} minutes ...")
    print(datetime.datetime.now())
    time_(b) ; #time.sleep(60*int(b))

def time_(a):
    a = int(a)
    m=1
    while a>=m:
        print(f"Minute {m} / {a}...")
        time.sleep(60)
        m+=1

def chronom()->int:
    print("\nThis program is used as a Tool for Studing Pomodoro Method")
    print("of 3 rounds of studing time plus 3 rest times")
    print("You just need to enter Studing and Break time\n")
    default = 20
    a = input("Input studing time in minutes [Default = 20]: ")
    if a =="":
        a = default
    default = 5
    b = input("Input break time in minutes [Default = 5]: ")
    if b =="":
        b = default
    return a,b

def mensaje(variable):
    a = len(variable)
    for i in range(a+4):
        print("#", end="")
    print("\n#",variable,"#")
    for i in range(a+4):
        print("#", end="")
    print()

if __name__ == "__main__":
    os.system("clear")
    begin0 = datetime.datetime.now()
    a, b = chronom()
    for i in range(4):
        pomodoro(a,b,i)
    print(f"Final Break time, {int(b*3)} minutes ...")
    time.sleep(60*2*int(b))
    end0 = datetime.datetime.now()
    print(f"\nBegin: {begin0}\nEnd: {end0}")
