#Programming Fundamentals Project BlackWater Concert
#Author: Neil O'Sullivan COMP1D-Y

#Constants
add_user=1
concert_details=2
exit=3
hour=60
musician=1
singer=2
dancer=3

#Variables
choice=0
performers=1
names= " "
acts= " "
all_minutes= " "
act= " "
total_minutes=0
no_dancer=0
no_musician=0
no_singer=0
total_dancers=0
total_musicians=0
total_singers=0
line_number=0


#Menu Heading
print("Welcome to the Annual Blackwater Concert main menu")
print()
while choice !=exit:
#Choice of option within the menu. Start of while loop with option 3 exit
     choice=int(input("What would you like to do?\n 1:Add performer.\n " "2:Generate Concert Details.\n " "3:Exit"))
     print()
#Option 1 add user
     if choice == add_user:
         print("You have chosen to add user")
         print()
         #open file
         performers_file = open("performers.txt", 'a')
         #Get number of performers to be added
         no_ofperformers=int(input("Enter the number of performers you wish to add"))
         while performers<=no_ofperformers:
             #Get performer and act info
               print(f" Performer: {performers}/ {no_ofperformers}")
               first_name=input("Enter the first name of the performer.")
               surname = input("Enter the  surname of the performer.")
               performance=(int(input("Enter the number category which the act is. 1:Musician. 2:Singer. 3:Dancer.")))
               minutes=(int(input("Enter the number of minutes of the performance")))
             #If statement for different acts dependant on users choice
               if performance==musician:
                   act= "Musician"
                   if performance== musician:
                         no_musician=1
                         total_musicians += no_musician
               elif performance==singer:
                   act= "Singer"
                   if performance == singer:
                       no_singer = 1
                       total_singers += no_singer
               elif performance==dancer:
                   act="Dancer"
                   if performance == dancer:
                     no_dancer = 1
                     total_dancers += no_dancer
               #Print information for each person and print to file
               print(f"Name: {first_name} {surname}  Performance type: {act}  Performance lenght: {minutes} minutes",file=performers_file)
             #Calculations for counters of each name act and time of performance
               names+=(f"{first_name},{surname}  ")
               acts+=(f"{act} ,  ")
               all_minutes+=(f"{minutes},    ")
               performers = performers + 1
               total_minutes+=minutes
         #Close the file
         performers_file.close()
         #Print overall information once all users has been added.
         print()
         print("The following information has been added.")
         print(f"{'Names:':5s} {names:<15} ")
         print(f"{'-' * 32}")
         print(f"{'Acts:':5s} {acts:<15}")
         print(f"{'-' * 32}")
         print(f"{'Minutes:':5s} {all_minutes:<15}")
         print(f"{'-' * 32}")
         print()
         print("Summary Notes:")
         print(f"{'-' * 32}")
         print()
         print(f"Total number of Musicians: {total_musicians}")
         print()
         print(f"Total number of Singers: {total_singers}")
         print()
         print(f"Total Number of Dancers: {total_dancers}")
         print()
         #Translate total minutes into hours and minutes
         if total_minutes>=hour:
             total_hours = int(total_minutes / hour)
         else:
             total_hours=0
         and_minutes = total_minutes % hour
         print(f"Total time for all performances: {total_hours} hours and {and_minutes} minutes")

     #Print the detail from the file for option 2
     elif choice==concert_details:
         print()
         print("Black Water Concert")
         print(f"{'-' * 32}")
         print("The following is all performers registered for the Black Water Concert. \n Name, Act and Lenght of Act")
         #Open file and organise and print the array of data
         with open("performers.txt") as numbers:
            for line in numbers:
                data =line.split()
                name = data[1]
                surname=data[2]
                (act) = data[5]
                minutes= int(data[8])
                line_number+=1
                print()
                if minutes>15:
                  print(line_number,":",name,surname,"*",act, minutes, "minutes")
                  print()
                else:
                    print(line_number,":",name,surname,act, minutes, "minutes")
                    print()
     #Exit the main menu
     elif choice== exit:
      print("You have now exited the main menu.")
      print(f"{'*' * 32}")
      print("Thank you")

     #Any option other than 1 2 or 3 print invalid entry
     else:
        print("That is not a valid entry")


