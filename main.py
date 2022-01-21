from os import system, name

#Class to hold relevant info for a tv show
class TvShow:

    def __init__(self, name_p, curr_seas_p, curr_epi_p):
        self.name, self.currSeason, self.currEpi = name_p, curr_seas_p, curr_epi_p

    def __str__(self):
        form = '{}: season {}, episode {}'
        return form.format(self.name, self.currSeason, self.currEpi)
    
    def getSeason(self):
        return self.currSeason
    
    def setSeason(self, s):
        self.currSeason = s

    def getEpisode(self):
        return self.currEpi
    
    def setEpisode(self, e):
        self.currEpi = e


#REQUIRES
#   A dict that contains valid TvShow objects
#PROMISES
#   Displays to the console all the Tv Shows in the dict
def display_shows(show_list):
    for show in show_list:
        print(show_list[show])
    print('\n')


# TEST SHOWS
TheManda = TvShow('The Mandalorian', 2, 2)
Aot = TvShow('Attack on Titan', 4, 1)
Comm = TvShow('Community', 4, 3)
allShows = {"The Mandalorian": TheManda, "Attack on Titan": Aot, "Community": Comm}

# MAIN
def main():

    print('Welcome!\n')
    display_shows(allShows)

    #Menu Options
    print('MAIN MENU\n\n')
    print('1. Add a new show\n')
    print('2. Edit existing show\n')
    print('3. Remove a show\n')

    menu_option_in = int(input('How can I help you?\n'))

    # 1. Adding a new show
    if (menu_option_in == 1):
        try:
            inputShowName = input('Enter a new show\n')
            inputShowSeason = int(input('What season are you on?\n'))
            inputShowEpisode = int(input('What episode are you on?\n'))

            allShows[inputShowName] = TvShow(inputShowName, inputShowSeason, inputShowEpisode)

        except ValueError:
            print('Invalid input\n')
        
    # 2. Edit existing show
    elif (menu_option_in == 2):

        show_in = input("\nWhich show?\n")
        if (show_in not in allShows.keys()):
            print("Show not found")
            return
        
        print("\n")
        print("1. Edit name\n" +
        "2. Edit current season\n" +
        "3. Edit current episode\n")
        option_in_Edit = int(input())

        # 1. Edit name <- Edit existing show
        if (option_in_Edit == 1):
            editName = input("\nWhat would you like to change the name to?\n")
            temp = allShows[show_in]
            allShows.pop(show_in)
            allShows[editName] = TvShow(editName, temp.getSeason(), temp.getEpisode())
        
        # 2. Edit current season <- Edit existing show
        elif (option_in_Edit == 2):
            editSeason = input("\nWhat season are you on?\n")
            allShows[show_in].setSeason(editSeason)

        # 3. Edit current episode <- Edit existing show
        elif (option_in_Edit == 3):
            editEpisode = input("\nWhat episode are you on?\n")
            allShows[show_in].setEpisode(editEpisode)
        
        else:
            print("Invalid Input")

    # 3. Remove a show
    elif (menu_option_in == 3):

        show_in = input("What show would you like to remove?\n")
        if (show_in not in allShows.keys()):
            print("Show not found")
            return

        allShows.pop(show_in)
        pass
    
    # Default
    else:
        print("Invalid Input")
        pass

    print("\n")
    display_shows(allShows)

# Main execution
if __name__ == '__main__':
    main()