import schedule, time

def main(part1,part2, part3):
    def task1():
        print("Executing task1")
    def task2():
        print("Executing task2")
    def rerunTask():
        print("reruning main task")
        main(1,2,3)

    schedule.every(1).seconds.do(task1)
    schedule.every(3).seconds.do(task2)
    schedule.every(5).seconds.do(rerunTask)


main(1,2,3)

time.sleep(100)
