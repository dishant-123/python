import wikipedia
import wolframalpha

while True:
	input=raw_input("Queshion: ")

	try:
		#wolframalpha
		app_id = "623RUK-QPT76HP2YE"
		client = wolframalpha.Client(app_id)#call on app 			id and client id

		res=client.query(input)

		answer =next (res.results).text#so that it doesnot 			give graph

		print answer
	except:
		#wikipedia
		print wikipedia.summary(input,sentences="4")

