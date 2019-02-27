def QuestionMarks(s):
     qnum=0
     has10=False
     dig=0
     for ch in s:
         if ch.isdigit():
             if int(ch)+dig==10:
                if qnum!=3:
                    return "false"
                has10=True
             dig=int(ch)
             qnum=0
         elif ch=="?":
             qnum+=1
     return "true" if has10 else "false"
print(QuestionMarks("acc?7??sss?3rr1??????5"))
