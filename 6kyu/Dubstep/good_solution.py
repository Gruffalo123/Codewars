def song_decoder(song):
    return ' '.join(song.replace('WUB',' ').split())


print(song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"))
print(song_decoder("AWUBWUBWUBBWUBWUBWUBC"))