import instagramy
from colorama import Back, Style, Fore

logo = """
=======  =     ‼   =======  +=======   ‼   ‼
   ‼     ‼ =   ‼   ‼        ‼       ‼   ‼ ‼
   ‼     ‼  =  ‼   =======  ‼ ======     ‼
   ‼     ‼   = ‼         ‼  ‼            ‼
=======  =     =   =======  ‼            ‼
"""

def one() : 
    username = input("Enter Target\'s username :\t")
    try:
        user = instagramy.InstagramUser(username)
        print(f"\nUser Name : {user.fullname}\n")
        print(f"User Email : {user.email}\n")
        print(f"User Bio : \n{user.biography}\n")
        print(f"Number of Followers : {user.number_of_followers}\n")
        print(f"Number of Following : {user.number_of_followings}\n")
        print(f"Number of Post : {user.number_of_posts}\n")
        print(f"Profile Picture Url : {user.profile_picture_url}\n")

    except KeyError or IndexError : 
        print("Invalid User !!")

def two() :
    username = input("Enter Target\'s username : \t") 
    user = instagramy.InstagramUser(username)
    posts = user.posts

    for post in posts : 
        caption = post['caption']
        likes = post['likes']
        code = post['shortcode']
        url = post['display_url']
        print(f"\nNumber of Likes : {likes}\n")
        print(f"Caption : {caption}\n")
        print(f"Post Url : {url}\n")
        print(f"Shortcode : {code}")


if __name__ == "__main__":

    print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + logo)
    opt = int(input("\n[1.] User Info\n[2.] User\'s Post Info\n[3.] Quit\n"))
    
    if opt == 1 : 
        one()

    elif opt == 2 : 
        two()

    elif opt == 3 : 
        print("Thanks for giving your time")

    else : 
        print(f"Invalid Option {opt}")