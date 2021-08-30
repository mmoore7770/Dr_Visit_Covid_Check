import sys
from datetime import datetime

def program():
        now = datetime.now()
        date = now.strftime('%B %d, %Y ')
        time= now.strftime(' %H:%M:%S')

        clinic = ('Minute Clinic')
        greeting = ('Welcome to ' + clinic + '! ') 
        print(greeting)

        # now = datetime.now()
        # date = now.strftime('%B %d, %Y %H:%M:%S')
        # time= now.strftime(' %H:%M:%S')
        print('Today\'s date is ' + str(date) )

        print('The current time is ' + time)

        
        

 

# have you recently been exposed to someone with covid? add to list
# ask which dr they are seeing and add to [information  list] that is printed from patient_info



        name = input('Please enter your name: ') 
        print('Nice to meet you, '+ name)

        age = input('Please enter your age: ')
        age_int = int(age)
        current_year = 2021
        birth_year = current_year - age_int
        print('Thank you! That means your birth year is  ' + str((birth_year))) # Dertmines Birth year

       


#add country to determine degrees f or c
        
        
        ins_card = input('Do you have insurance? Enter Y/N: ')

        if ins_card == 'Yes' or ins_card == 'y' or ins_card == 'yes' or ins_card == 'YES':
                print('Great! This visit is covered!')
        else:
  
                print('Sorry. The Goverment says you pay full price : ')
           
        patient_info = [
                'Name: ' + name, 'Age: '+ str(age),'Birth Year: '+ str(birth_year)
        ]
        print(patient_info)

        cust_confirm_1 = input('Is all of your information correct? Y/N: ')
        if cust_confirm_1 == 'Yes' or cust_confirm_1 == 'y' or cust_confirm_1 == 'Y':
                print('Great!')
        if cust_confirm_1 == 'No' or cust_confirm_1 == 'n':
                cust_confirm_1 = ans_y =  input("Would you like to restart this program? ")
                if ans_y == 'Yes' or ans_y == 'y':
                        program()

                else:
                         ans_y == 'No' or ans_y =='n'
                print( 'Program terminating. Goobye. ')



program()

def covid_s():
        
        

        def symp_func():
                
                patient_country = input('Which country are you from? US/CANADA:' )
                
                
                sympt = 'We will now check your symptoms to see if you may have COVID-19'
                print(sympt)
                all_in = 0
                vac_stat = input('Have you been vacinated?: Y/N: ')
                if vac_stat == 'Y' or vac_stat == 'Yes' or vac_stat == 'YES' or vac_stat == 'yes' or vac_stat == 'y':
                        vac_stat = True
                if vac_stat == True:
                        vac_stat = ('Vaccine: Yes')
                if vac_stat == 'N' or vac_stat == 'No' or vac_stat == 'NO' or vac_stat == 'no' or vac_stat == 'n':
                        vac_stat = False
                if vac_stat == False:
                     vac_stat = ('Vaccine: No')   
        
 # if CA country is selected the temp is converted to C, C conversion is used to determine fever
# input C converts to F to use F formula    
                
                while True:
                        try:
                                temp = input('Please enter your temp: ')
                                temp= int(temp)
                                break
                        except ValueError:
                                print('Number invalid. Please try again...')
        
                temp_2 = temp * 9  / 5 + 32 
                if patient_country == ('CA') or patient_country == ('ca'):
                        temp = round(temp_2)
                


                if temp == 97 or temp == 98:
                        print('You do not have a fever')
                elif temp == 99 or temp == 100:
                        print('You have a fever')
                elif temp == 101 or temp == 102 or temp == 103:
                        print('You really have a fever and need to see a DR.')
                elif temp == 95 or temp == 96:
                        print('You are really cold and should probably go see a DR.')
                else:
                        temp <= 94 or temp >= 104
                        print('You are probably dead')


                # if temp_2 == 97 or temp == 98:
                #         print('You do not have a fever')
                # elif temp_2 == 99 or temp == 100:
                #         print('You have a fever')
                # elif temp_2 == 101 or temp == 102 or temp == 103:
                #         print('You really have a fever and need to see a DR.')
                # elif temp_2 == 95 or temp == 96:
                #         print('You are really cold and should probably go see a DR.')
                # else:
                #         temp_2 <= 94 or temp >= 104
                #         print('You are probably dead')

        
       
                cough_sy = input('Do you have a cough? Y/N: ')
        

                if cough_sy == 'Y' or cough_sy == 'Yes' or cough_sy == 'YES' or cough_sy == 'yes' or cough_sy == 'y':
                
                        cough_sy = True

                        if cough_sy == True:    
                                all_in = all_in + int(1)
                        cough_sy = ('Cough: Yes')
                        
                                
                elif cough_sy == 'N' or cough_sy == 'No' or cough_sy == 'NO' or cough_sy == 'no' or cough_sy == 'n':
                        cough_sy = False
                if cough_sy == False:
                        cough_sy = ('Cough: No')
        
        
                fatigue_sy = input('Do you have Fatigue? Y/N: ')

                if fatigue_sy == 'Y' or fatigue_sy == 'Yes' or fatigue_sy == 'YES' or fatigue_sy == 'yes' or fatigue_sy == 'y':
                        fatigue_sy = True
                        if fatigue_sy == True:
                         all_in = all_in + int(1)
                        fatigue_sy = 'Fatigue: Yes'
                elif fatigue_sy == 'N' or fatigue_sy == 'No' or fatigue_sy == 'NO' or fatigue_sy == 'no' or fatigue_sy == 'n':
                        fatigue_sy = False
                if fatigue_sy == False:
                        fatigue_sy = ('Fatigue: No')
        
        
                body_ach_sy = input('Do you have body aches? Y/N: ')
        
                if body_ach_sy == 'Y' or body_ach_sy == 'Yes' or body_ach_sy == 'YES' or body_ach_sy == 'yes' or body_ach_sy == 'y':
                 body_ach_sy = True
                if body_ach_sy == True:
                        all_in  = all_in + int(1)
                        body_ach_sy = 'Body Ache: Yes'

                elif body_ach_sy == 'N' or body_ach_sy == 'No' or body_ach_sy == 'NO' or body_ach_sy == 'no' or body_ach_sy == 'n':
                        body_ach_sy = False
                if body_ach_sy == False:
                        body_ach_sy = ('Body Ache: No')

        
                loss_taste_smell_sy = input('Have you had a loss of taste or smell? Y/N: ')

                if loss_taste_smell_sy == 'Y' or loss_taste_smell_sy == 'Yes' or loss_taste_smell_sy == 'YES' or loss_taste_smell_sy == 'yes' or loss_taste_smell_sy == 'y':
                        loss_taste_smell_sy = True
                if loss_taste_smell_sy == True:
                        all_in = all_in + int(1)
                        loss_taste_smell_sy = 'Loss of taste or smell: Yes'
                elif loss_taste_smell_sy == 'N' or loss_taste_smell_sy == 'No' or loss_taste_smell_sy == 'NO' or loss_taste_smell_sy == 'no' or loss_taste_smell_sy == 'n':
                        loss_taste_smell_sy = False
                if loss_taste_smell_sy == False:
                        loss_taste_smell_sy = ('Loss of taste or smell: No')
        
       
                sore_throat_sy = input('Have you currently or recently had a sore throat? Y/N: ')
        
                if sore_throat_sy == 'Y' or sore_throat_sy == 'Yes' or sore_throat_sy == 'YES' or sore_throat_sy == 'yes' or sore_throat_sy == 'y':
                        sore_throat_sy = True
                if sore_throat_sy == True:
                        all_in = all_in + int(1)
                        sore_throat_sy = 'Sore Throat: Yes'

                elif sore_throat_sy == 'N' or sore_throat_sy == 'No' or sore_throat_sy == 'NO' or sore_throat_sy == 'no' or sore_throat_sy == 'n':
                        sore_throat_sy = False
                if sore_throat_sy == False:
                
                        sore_throat_sy = ('Sore Throat: No')
        


                patient_sy = [
                        cough_sy, fatigue_sy, body_ach_sy, loss_taste_smell_sy, sore_throat_sy, vac_stat
                        ]



                print (patient_sy)

        
                confirm_sy = input('Is all the information correct? Y/N: ')
        
        
                if confirm_sy == 'Y' or confirm_sy == 'Yes' or confirm_sy == 'YES' or confirm_sy == 'yes' or confirm_sy == 'y':
                        confirm_sy = True
                        if confirm_sy == True:
                                print('Thank you for confirming!')

        
        
        
                else:
                                confirm_sy == 'N' or confirm_sy == 'No' or confirm_sy == 'NO' or confirm_sy == 'no' or confirm_sy == 'n'
                                confirm_sy = False
                                if confirm_sy == False:

                                        confirm_sy = confirm_sy_rest = input('Would you like to start the Symptoms check over?: Y/N: ')

     #local variable 'confirm_sy_rest' referenced before assignment      
                                if confirm_sy_rest == 'Y' or confirm_sy_rest == 'Yes' or confirm_sy_rest == 'YES' or confirm_sy_rest == 'yes' or confirm_sy_rest == 'y': 
                                        confirm_sy_rest = True
                                if confirm_sy_rest == True:
                                        covid_s() # Loops to start of Symptoms check over
                                else:
                                        print('Terminating program. Goodbye!')
                # print('You have ' + str(all_in) + ' COVID symptoms.')
        # symp_int = int((cough_sy + fatigue_sy + body_ach_sy + loss_taste_smell_sy + sore_throat_sy))
                if all_in <= 2:
                        print('You have 2 or less symptoms. You probably do not have COVID-19.')
                elif all_in >= 3:
                        print('You have 3 or more symptoms. You may have COVID-19.')
        symp_func()



# if missing 2 sypmtoms, may not have covid
# if has more than 3, may have covid

                
covid_s()





def exit_prompt():
        
        exit_p = ('Thank you for that information. The Dr will be with you shortly.')

        print(exit_p)

exit_prompt()