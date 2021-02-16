marks = {'Andy':88, 'Amy':  66, 'James':90, 'Jules': 55, 'Arthur':77}
marks


for k, v in marks.items():
    print('Name=', k, ', Grade=', v)

    
import statistics as stats
print("Mean grade:" , stats.mean(marks.values()))
print("Maximal grade:" , max(marks.values()))
print("Minimal grade:", min(marks.values()))


for k in marks:
    if 'J' in k:
        break
    print(k)


for k in marks:
    if 'J' in k:
        continue
    print(k)


for k, v in marks.items():
    def grade(k):
        if k in marks:
            return(marks[k])
        else:
            return('Cannot find student name')
       
print(grade('Jules'))
print(grade('Annie'))
print(grade('James'))



