def song_decoder(song):
    s = song.split('WUB')
    for i in s[::-1]:
        if i == '':
            s.pop(s.index(i))
    x = ' '.join(s)
    return x


print(song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"))
print(song_decoder("AWUBWUBWUBBWUBWUBWUBC"))