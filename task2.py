casino_blacklist = {'John Dow', 'Misha Sutiahin', 'Scam Peterson', 'Perun Nefedov'}
poker_blacklist = {'John Dow', 'Misha Sutiahin', 'Marina Seredovski'}
alcohol_blacklist = {'John Dow', 'Misha Sutiahin', 'Leo Truba', 'Karina Dju'}

those_who_are_on_all_blacklists = casino_blacklist.intersection(poker_blacklist, alcohol_blacklist)


print('People on all blacklists:', those_who_are_on_all_blacklists)
