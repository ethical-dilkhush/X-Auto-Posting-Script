# import tweepy
# import schedule
# import time
# from datetime import datetime
# BEARER_TOKEN='AAAAAAAAAAAAAAAAAAAAAFAoxgEAAAAAkut53OfOoNZfR%2BycsMa9aR2II50%3DZY7zRPAYqmcYTzH52f0pqrcOF1dGK1FrTQK5qzFbtq1UNAjB4o'
# API_KEY = 'RulAFlB0jRvbCm1hgVq9qOtGG'
# API_SECRET_KEY = 'iLRN5tCb1zfOPqj6pZuUWPMHoxcNOH7j5m7enElQirFcRXIcuO'
# ACCESS_TOKEN = '853478865234165760-hbLegTExKP8wEufl3onmH3bTCR9JPAA'
# ACCESS_TOKEN_SECRET = 'HB9LNUr1ATvOi9Bb3hNsyrJZUjCKIgKVLrQZzufF8wAct'
# client = tweepy.Client(
#     consumer_key=API_KEY,
#     consumer_secret=API_SECRET_KEY,
#     access_token=ACCESS_TOKEN,
#     access_token_secret=ACCESS_TOKEN_SECRET,
#     bearer_token=BEARER_TOKEN
# )
# # Function to post a tweet
# def post_tweet(message):
#     try:
#         response = client.create_tweet(text=message)
#         print(f"Tweet posted: {message}")
#     except tweepy.TweepyException as e:
#         print(f"Error posting tweet: {e}")

# # Function to auto-post at intervals
# def auto_post(tweets, interval_seconds):
#     try:
#         for tweet in tweets:
#             post_tweet(tweet)
#             time.sleep(interval_seconds)  # Wait for the specified interval
#     except KeyboardInterrupt:
#         print("\nAuto-posting interrupted by user. Exiting gracefully.")
        
# # List of tweets to post
# tweets_to_post = [
#     "Every dip is a chance, not a loss. Stay patient. 🧘‍♂️📉 #CryptoMindset #BuyTheDip",
#     "HODL strong, FOMO wrong! 💎🙌 #HODL #CryptoTrading",
#     "Your next 100x starts with research, not hype. 🔍🚀 #DYOR #Altcoins",
#     "Free airdrops today, potential wealth tomorrow! 🎁💰 #Airdrop #CryptoRewards",
#     "Mint early, sell smart, repeat wisely. 🎨💎 #NFTs #Minting",
#     "The market tests patience, not luck. ⏳⚡ #CryptoWisdom #InvestSmart",
#     "Small trades, big lessons. Grow daily! 📊📚 #CryptoTrading #LearnAndEarn",
#     "Risk management = Wealth management. 🏦🔑 #TradeSafe #CryptoSuccess",
#     "Bear markets breed millionaires. 🐻💰 #BearMarket #CryptoInvesting",
#     "If you believe, you win. If you doubt, you miss. 🚀🔥 #StayFocused #Crypto",
#     "The blockchain rewards those who learn. 📖⛓️ #Web3 #CryptoEducation",
#     "Airdrops aren’t free—your knowledge earns them! 🎯📩 #FreeCrypto #CryptoTips",
#     "Mint wisely, not blindly. 🖼️🧐 #NFTDrops #SmartInvestor",
#     "Crypto success = patience + strategy. 🏆💡 #CryptoStrategy #LongTerm",
#     "Not every pump is a trap, but every trap starts with a pump. 📈⚠️ #CryptoTrading #NoFOMO",
#     "Your first 10x is education, not profit. 📚🚀 #CryptoKnowledge #DYOR",
#     "The longer the vision, the bigger the reward. 👀💎 #LongTermHODL #Wealth",
#     "Bull runs favor the prepared, not the lucky. 🚀📊 #CryptoMarket #BeReady",
#     "DYOR: Your best defense against scams. 🔍🚨 #CryptoSecurity #StaySafe",
#     "Passive income from staking = Wealth on autopilot. ⛓️💰 #StakingRewards #CryptoPassiveIncome",
#     "Stay ahead, read whitepapers, not just tweets. 📜📲 #CryptoResearch #SmartInvestor",
#     "Your wallet is your business. Treat it like one! 🎯💼 #CryptoWallet #SecureYourFunds",
#     "Early birds catch the mint, but late birds catch the trend. 🦅🕰️ #NFTMinting #CryptoOpportunities",
#     "Fear and greed are your biggest enemies. 😱🤑 #TradeWisely #CryptoMindset",
#     "Crypto isn’t about luck; it’s about knowledge. 📖💡 #LearnAndEarn #CryptoTips",
#     "Every loss is tuition for your future wins. 🎓📈 #CryptoLessons #InvestWisely",
#     "The best time to buy? Before the hype. 🕵️‍♂️📊 #CryptoGems #PrePump",
#     "The best traders adapt, not panic. ⚖️🧠 #StayCalm #TradeSmart",
#     "You only lose when you stop learning. 📚💎 #CryptoWisdom #KeepGrowing",
#     "Airdrop hunters win by staying informed. 🔔🎁 #AirdropHunter #CryptoRewards",
#     "Your seed phrase is your fortune. Protect it! 🔐📜 #CryptoSecurity #NotYourKeysNotYourCoins",
#     "FOMO fades, but strategy wins. 🎯🚀 #NoFOMO #SmartMoney",
#     "Real wealth is built in the bear market. 🏗️🐻 #CryptoWealth #BearMarket",
#     "Stay calm, stay liquid, stay winning. 🏆💰 #CryptoMindset #InvestSmart",
#     "Timing the top is a myth, securing profit is real. 💎💰 #TakeProfits #CryptoWisdom",
#     "Minting is a lottery; research is the jackpot. 🎟️💡 #NFTMinting #DYOR",
#     "Security first, profits second. 🔐💰 #CryptoSafety #ProtectYourAssets",
#     "Crypto patience = compound profits. ⏳📈 #HODL #WealthBuilding",
#     "Airdrops are rewards for action takers. 🎁📩 #AirdropHunting #FreeCrypto",
#     "Your first mistake? Rushing in without a plan. 🛑⚠️ #CryptoStrategy #ThinkBeforeYouTrade",
#     "Buy the fear, sell the greed. 🛒🔥 #BuyLowSellHigh #CryptoMarket",
#     "Airdrops = Free money. Scams = Lost money. Learn the difference. 💡🚀 #CryptoSecurity #StaySafe",
#     "Mint hype fades, utility stays. 🔥💎 #NFTUtility #LongTermHold",
#     "Survivors of bear markets become kings of bull runs. 🦁🐂 #CryptoWinners #BearToBull",
#     "In crypto, quitting is the only real loss. 🏆⏳ #NeverGiveUp #KeepInvesting",
#     "The best wallets are the ones that grow. 💰📊 #CryptoProfits #WealthMindset",
#     "Your biggest asset? Patience and research. 🧠⏳ #SmartInvestor #CryptoKnowledge",
#     "Airdrops love early adopters, not latecomers. 🥇🎁 #BeEarly #CryptoRewards",
#     "Smart contracts don’t make you rich; smart moves do. 📜💡 #DeFi #CryptoSuccess",
#     "Crypto is a marathon, not a sprint. Stay in the game! 🏃‍♂️🚀 #LongTermHODL #CryptoJourney"
# ]
# # Auto-post tweets every 1 hour (3600 seconds)
# auto_post(tweets_to_post, interval_seconds=10)
print("Hello World")
