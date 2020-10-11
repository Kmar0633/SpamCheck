import sys
import csv
import numpy as np
from fractions import Fraction
def SpamCheck(emailInput,dataset):
    Number_of_spam_emails=1500
    Number_of_real_emails=3672
    fraction_of_spam_emails=1500/5712
    fraction_of_real_emails=3672/5712
    spamProbabilities=[]
    hamProbabilities=[]
    my_file = open(emailInput, "r")
    content = my_file.read()
    content_list1 = content.rstrip("\n")

    content_list = content_list1.split(" ")

#    print(content_list)
    num=0
    with open(dataset) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if num>=1:
                
                if(row[len(row)-1] in content_list):
                    spamProbabilities.append(float(Fraction(row[0])))
                    hamProbabilities.append(float(Fraction(row[1])))
#                    print(row[len(row)-1] +"in")
                if(row[len(row)-1] not in content_list):
                    spamProbabilities.append(1-float(Fraction(row[0])))
                    hamProbabilities.append(1-float(Fraction(row[1])))
#                    print(row[len(row)-1]+"not in")
            
            num=num+1
        
#        print(spamProbabilities)
#        print(hamProbabilities)
        probabilitySpam=np.prod(spamProbabilities)
        probabilityHam=np.prod(hamProbabilities)
        Calculation=(fraction_of_spam_emails*probabilitySpam)/((fraction_of_spam_emails*probabilitySpam)+(fraction_of_real_emails*probabilityHam))
        if(Calculation<0.5):
            print("The probability that the email is spam is "+str(Calculation)+"thus it is highly likely that is is a legitimate email")
        else:
            print("The probability that the email is spam is "+str(Calculation)+" thus it is highly likely that is is a spam email")
            
    return None
    
EmailInput=sys.argv[1]
Dataset=sys.argv[2]
#print(EmailInput)
#print(Dataset)
SpamCheck(EmailInput,Dataset)
