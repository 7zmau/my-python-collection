import random

def getAnswer(AnswerNumber):
    if AnswerNumber==1:
        return 'It is certain'
    elif AnswerNumber==2:
        return 'It is decidely so'
    elif AnswerNumber==3:
        return 'Yes'
    elif AnswerNumber==4:
        return 'Reply Hazy try again'
    elif AnswerNumber==5:
        return 'Ask again later'
    elif AnswerNumber==6:
        return 'Concentrate and ask again'
    elif AnswerNumber==7:
        return 'My reply is no'
    elif AnswerNumber==8:
        return 'Outlook not so good'
    elif AnswerNumber==9:
        return 'Very doubtful'

r=random.randint(1, 9)
fortune=getAnswer(r)
print(fortune)
