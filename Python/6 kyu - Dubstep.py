

def song_decoder(song):
    decoded = (song.replace("WUB", ' ').split())
    return (' '.join(decoded))

#song.replace replace all the WUB with ' ', but sometimes there are multiple WUB in a row (ex. 'WUBWUB') so it give us multiple ' ' backs, I removed it  by using .split() because .split() will separate each string by one space on default and if it found double space it will ignore that and turn it into single space between each string

# best practiced solution by vote is
# def song_decoder(song):
#     return " ".join(song.replace('WUB', ' ').split())
# this "best practiced" might be too short and hard to read


song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")