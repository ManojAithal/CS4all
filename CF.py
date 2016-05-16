# A very simple music recommender system.

PREF_FILE = "musicrec-store.txt"

def loadUsers(fileName):
	file = open(fileName,'r')
	userDict = {}
	for line in file:
		[userName,bands] = line.strip().split(":")
		bandList = bands.split(",")
		bandList.sort()
		userDict[userName] = bandList
	file.close()
	return userDict


def getPreferences(userName,userMap):
	newPref = ""
	if userName in userMap:
		prefs = userMap[userName]
		print("I see that you jace used the system before")
		print("your user preferences include:")
		for artist in prefs:
			print(artist)
		print("please enter other artist you like")
		print("or just press enter")
		newPref = input("to see your recomandations:")
	else:
		prefs = []
		print("I see that you are a new user")
		print("please enter the name of an artist or band:")
		newPref = input("that you like:")	
	while newPref != "":
		"""prefs.append(newPrefs.strip().title())"""
		prefs.append(newPref.strip().title())
		print("Please enter another artist or band that you")
		print("like, or just press enter")
		newPref = input("to see your recommendations: ")

	prefs.sort()
	return prefs

def getRecommendations(currUser,prefs,userMap):
	recommandations = []
	bestUser = findBestUser(currUser,prefs,userMap)
	if bestUser != None:
		recommandations = drop(prefs,userMap[bestUser])
	return recommandations

def findBestUser(currUser,prefs,userMap):
	users = userMap.keys()
	bestUser = None
	bestScore = -1
	for user in users:
		score = numMatches(prefs,userMap[user])
		if score > bestScore and currUser != user:
			bestScore = score
			bestUser = user
	return bestUser

def drop(list1,list2):
	list3 = []
	i = 0
	j = 0
	while i<len(list1) and j<len(list2):
		if list1[i] == list2[j]:
			i+=1
			j+=1
		elif list1[i]<list2[i]:
			i+=1
		else:
			list3.append(list2[j])
			j+=1
	return list3

def numMatches(list1,list2):
	matches = 0
	i = 0
	j = 0
	while i<len(list1) and j<len(list2):
		if list1[i] == list2[j]:
			matches+=1
			i+=1
			j+=1
		elif list1[i]<list2[j]:
			i+=1
		else:
			j+=1
	return matches

def saveUserPreferences(userName,prefs,userMap,fileName):
	userMap[userName] = prefs
	file = open(fileName,"w")
	for user in userMap:
		tosave = str(user) +":"+",".join(userMap[user]) + \
				"\n"
		file.write(tosave)
	file.close()

def main():
	userMap = loadUsers(PREF_FILE)
	print("Welcome to the  Music Recomander System")
	userName = input("enter your name:")
	print("Welcome",userName)
	
	prefs = getPreferences(userName,userMap)
	recs = getRecommendations(userName,prefs,userMap)
	
	if len(recs) == 0:
		print("System have No Recomondations for you right now")
	else:
		print("Based on the Users I currently know that you may like:")
		for artist in recs:
			print(artist)
		print("Hope you will like them!! System will save your preferences")
		print("and will have new recomndations for you in the future")
	saveUserPreferences(userName,prefs,userMap,PREF_FILE)

if __name__ == "__main__": main()
