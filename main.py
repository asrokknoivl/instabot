
from instabot import Bot
import random
import sys

# necessary to use to instabot for some reason, wouldn't launch otherwise
import os 
import glob

try:
    cookie_del = glob.glob("config/*cookie.json")
    os.remove(cookie_del[0])
except:
    pass

# constants
DB_PATH = 'db/kpopict_girl/'
POSTED_RECORD = 'posted.txt'
USER_NAME = 'rr.constantine.ecomm@gmail.com'
PASSWORD = 'phiN!S-ATr?Glw4y!pif'
CAPTIONS = [
    '😍',
    '🥰',
    '🥵',
    '🫰🫰',
    '🫰',
    '✌🏻✌🏻✌🏻',
    '🫶🏻',
    '👅👅'
    'WOW ❤️❤️',
    '💜🖤💜',
    'Stunning <3',
    'Amazing 🫶🏻🫶🏻',
    'Cute 😙',
    'Super cute 🤩',
    'What do you think about this? 🤔🤔',
    'Rate this pic out of 10 😄😁',
    '🧐🧐',
    'OMG 👄 🫦',
    'I fucking love this 🍑'
    '🍒🍒',
    '🇰🇷🩵🇰🇷',
    '🙄🙄',
    '🫣',
    '🤩🤩🤩🤩🤩',
    '😉',
    '🥺😢',
    '😤💯',
    '💙💙💙',
    '💚💚💚',
    '💛💛💛',
    '🧡🧡🧡',
    '🩵🩵🩵',
    '💜💜💜',
    '🖤🖤🖤',
    '🤍🤍🤍',
    '🤎🤎🤎',
    '💕💞 💕💞 💕💞',
    '💗💗💗',
    '💓💓💓',
    '💖💖💖'
]
INIT_CAPTION = """
.
.
.
.
.
.
Like & follow for more content 💞
.
.
#love #instagood #instagram #art #photooftheday #photography #beautiful 
#picoftheday #happy #follow #instadaily #photo #instalike #like4like #girl
#model #fashion #style #beauty #bts #kpop #blackpink #korea #army #stan
"""
HASHTAGS = [
    '#bts'
]
USERNAMES = [
    'bts.bighitofficial',
    'lalalalisa_m',
    'jennierubyjane',
    'sooyaaa__',
    'roses_are_rosie',
    'thv',
    'j.m',
    'agustd',
    'uarmyhope',
    'jin',
    'rkive',
    'eunwo.o_c',
    'jacksonwang852g7',
    'dlwlrma',
    'real__pcy',
    'oohsehun',
    'xxxibgdrgn',
    'baekhyunee_exo',
    'taeyeon_ss',
    'hyunah_aa',
    'skuukzky',
    'somsomi0309',
    'bambam1a',
    'choi_seung_hyun_tttop',
    'yoona__lim',
    '__youngbae__',
    'yawnzzn',
    '_jeongjaehyun',
    'tiffanyyoungofficial',
    'zkdlin',
    '_imyour_joy'
]

bot = Bot()

# os.rename(f'{img}.REMOVE_ME', img)

def login(username, password):
    print('logging in...\n')
    bot.login(username=username, password=password)    

def post(filename, caption):
    bot.upload_photo(filename, caption=caption)

def post_random_pic():
    print('posting a random image...\n')
    db = os.listdir(DB_PATH)
    with open(POSTED_RECORD, 'r') as posted_record:
        posted_images = posted_record.read().split('\n')
        image = random.choice(db)
        while image in posted_images:
            image = random.choice(db)
    print(f'Image chosen: {image}\n')
    
    with open(POSTED_RECORD, 'a') as posted_record:
        posted_record.write(image+'\n')
    random_caption = random.choice(CAPTIONS) + '\n' + INIT_CAPTION
    image= 'db/kpopict_girl/'+image
    try:
        post(image, random_caption)
    except:
        post_random_pic()
    os.rename(image+'.REMOVE_ME', image)

def get_random_user_id(avoid_private=False):
    posts_ids = bot.get_user_medias(random.choice(USERNAMES), filtration=False)
    likers = bot.get_media_likers(posts_ids[0])
    user_id_to_follow = random.choice(likers)
    user_name_to_follow = bot.get_username_from_user_id(user_id_to_follow)
    user_info = bot.get_user_info(user_name_to_follow)
    if avoid_private and (user_info['is_private'] or user_info['media_count'] == 0):
        print('user\' account is private or has no media, selecting another one...')
        return get_random_user_id()
    else:
        return user_id_to_follow
    
def get_random_user_name(avoid_private=False):
    return bot.get_username_from_user_id(get_random_user_id(avoid_private))
    
def follow_random_user():
    print('following a random user...')
    bot.follow(get_random_user_id())

def unfollow_random_user():
    print('unfollowing a random user...')
    followings = bot.get_user_following('kpop.runs.my.body')
    bot.unfollow(random.choice(followings))

def like_random_post():
    print('liking a random post...')
    bot.like_user(get_random_user_name(avoid_private=True), amount=1, filtration=False)
    

def main():
    try:
        op = sys.argv[1]
    except:
        print('missing args, quitting...')
        sys.exit()
    
    login(USER_NAME, PASSWORD)
    print('\nStupid shit error above, ignore it.\n')
    match op:
        case 'post':
            post_random_pic()
        case 'follow':
            follow_random_user()
        case 'unfollow':
            unfollow_random_user()
        case 'like':
            like_random_post()
        case _:
            print('unknown parameter, try again.')

    bot.logout()
    
if __name__ == '__main__':
    main()

