from TwitterSearch import *
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['edinburgh castle']) # let's define all words we would like to have a look for
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = 'M9ZDgY0OMsvmlhlPE4qxyGdam',
        consumer_secret = 'G7Nrd770d8mOJkErCdgX8oRgN8bGaUBTyFjOqmzBctl4JzicBN',
        access_token = '218041595-yrk9WyMnTjh4PBidhApb0DwryK83Wzr32IWi6bP4',
        access_token_secret = 'GCmOzFmzrOoAv59lCpKRQrC9e7H1P0449iaBW1rI66saS'
     )

     # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)
