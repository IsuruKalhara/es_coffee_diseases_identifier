from experta import *
from PIL import Image
diseases_list = []
diseases_symptoms = []
symptom_map = {}
d_desc_map = {}
d_treatment_map = {}

def preprocess():
	global diseases_list,diseases_symptoms,symptom_map,d_desc_map,d_treatment_map
	diseases = open("diseases.txt")
	diseases_t = diseases.read()
	diseases_list = diseases_t.split("\n")
	diseases.close()
	for disease in diseases_list:
		if(disease==""):
			continue
		disease_s_file = open("Disease symptoms/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		s_list = disease_s_data.split("\n")
		diseases_symptoms.append(s_list)
		symptom_map[str(s_list)] = disease
		disease_s_file.close()
		disease_s_file = open("Disease descriptions/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		d_desc_map[disease] = disease_s_data
		disease_s_file.close()
		disease_s_file = open("Disease treatments/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		d_treatment_map[disease] = disease_s_data
		disease_s_file.close()
	

def identify_disease(*arguments):
	symptom_list = []
	for symptom in arguments:
		symptom_list.append(symptom)
	# Handle key error
	return symptom_map[str(symptom_list)]

def get_details(disease):
	return d_desc_map[disease]

def get_treatments(disease):
	return d_treatment_map[disease]

def if_not_matched(disease):
		print("")
		id_disease = disease
		disease_details = get_details(id_disease)
		treatments = get_treatments(id_disease)
		print("")
		print("The most probable disease that you have is %s\n" %(id_disease))
		print("A short description of the disease is given below :\n")
		print(disease_details+"\n")
		#print("The common medications and procedures suggested are: \n")
		#print(treatments+"\n")

		if(id_disease == "Coffee Leaf Rust"):
			im = Image.open("images/Coffee Leaf Rust.png")
			im.show(title="Coffee Rust")
		if(id_disease == "Nematode"):
			im = Image.open("images/Nematode.png")
			im.show(title="Nematode")
		if(id_disease == "Brown Eye Spot of Coffee"):
			im = Image.open("images/Brown Eye Spot of Coffee.png")
			im.show(title="Brown Eye")
		if(id_disease == "Upas Fungus"):
			im = Image.open("images/Upas Fungus.png")
			im.show(title="Upas Fungus")
		if(id_disease == "Brown Root Fungus"):
			im = Image.open("images/Brown Root Fungus.png")
			im.show(title="Brown Fungus")
		if(id_disease == "Black Root Fungus"):
			im = Image.open("images/Black Root Fungus.png")
			im.show(title=Black Fungus)
		if(id_disease == "White Root Fungus"):
			im = Image.open("images/White Root Fungus.png")
			im.show(title="White Fungus")

# @my_decorator is just a way of saying just_some_function = my_decorator(just_some_function)
#def identify_disease(headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness,low_body_temp ,fever,sunken_eyes):
class Greetings(KnowledgeEngine):
	@DefFacts()
	def _initial_action(self):
		print("")
		print("Expert System in Detecting Coffee Plant Diseases")
		print("Please answer a few questions about the plan conditions")
		print("Can you see any of the following symptoms:")
		print("")
		yield Fact(action="find_disease")


	@Rule(Fact(action='find_disease'), NOT(Fact(yellowLeaves=W())),salience = 1)
	def symptom_0(self):
		self.declare(Fact(yellowLeaves=input("Leaves becomes yellow? : ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(brownYellowSpots=W())),salience = 1)
	def symptom_1(self):
		self.declare(Fact(brownYellowSpots=input("Brownish yellow spots appear on the leaf? : ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(leavesEasyFallen=W())),salience = 1)
	def symptom_2(self):
		self.declare(Fact(leavesEasyFallen=input("Leaves becomes easily fallen? : ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(dullLeaves=W())),salience = 1)
	def symptom_3(self):
		self.declare(Fact(dullLeaves=input("Dull, shriveled, and hang leaves? : ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(orangePowder=W())),salience = 1)
	def symptom_4(self):
		self.declare(Fact(orangePowder=input("Leaves have orange powdery spots on the underside of leaves? : ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(baldLeaves=W())),salience = 1)
	def symptom_5(self):
		self.declare(Fact(baldLeaves=input("Leaves become bald? : ")))
	 
	@Rule(Fact(action='find_disease'), NOT(Fact(patchesLeaves=W())),salience = 1)
	def symptom_6(self):
		self.declare(Fact(patchesLeaves=input("Patches spreading leaves? : ")))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(prematureLeaves=W())),salience = 1)
	def symptom_7(self):
		self.declare(Fact(prematureLeaves=input("Premature and empty leaves? : ")))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(shortStem=W())),salience = 1)
	def symptom_8(self):
		self.declare(Fact(shortStem=input("Short stem? : ")))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(rottenRoot=W())),salience = 1)
	def symptom_9(self):
		self.declare(Fact(rottenRoot=input("Decomposed and rotten root? : ")))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(fruitSpot=W())),salience = 1)
	def symptom_10(self):
		self.declare(Fact(fruitSpot=input("Spots appear on fruit so it becomes rotten? : ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(fruitHalo=W())),salience = 1)
	def symptom_11(self):
		self.declare(Fact(fruitHalo=input("Circular spots appear on fruit forming a halo? : ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(rootSoilGrain=W())),salience = 1)
	def symptom_12(self):
		self.declare(Fact(rootSoilGrain=input("Roots covered by a crust of soil grains? : ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(rootYarnBlack=W())),salience = 1)
	def symptom_13(self):
		self.declare(Fact(rootYarnBlack=input("Roots have woven yarn blackish brown fungus? : ")))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(rootBlackSpot=W())),salience = 1)
	def symptom_14(self):
		self.declare(Fact(rootBlackSpot=input("Black spots on the roots? : ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(stemBlackSpot=W())),salience = 1)
	def symptom_15(self):
		self.declare(Fact(stemBlackSpot=input("black spots on the stem? : ")))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(rootWovenWhite=W())),salience = 1)
	def symptom_16(self):
		self.declare(Fact(rootWovenWhite=input("Roots have woven threads of white fungus? : ")))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(stemSilk=W())),salience = 1)
	def symptom_17(self):
		self.declare(Fact(stemSilk=input("Stem has a thin threads of fungi such as silk? : ")))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(stemNecrosis=W())),salience = 1)
	def symptom_18(self):
		self.declare(Fact(stemNecrosis=input("Stem necrosis? : ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(fruitNecrosis=W())),salience = 1)
	def symptom_19(self):
		self.declare(Fact(fruitNecrosis=input("Fruit necrosis? : ")))

	@Rule(Fact(action='find_disease'),Fact(yellowLeaves="yes"),OR(Fact(brownYellowSpots="yes"),Fact(leavesEasyFallen="yes")),Fact(dullLeaves="no"),OR(Fact(orangePowder="yes"),Fact(baldLeaves="yes"),
	Fact(patchesLeaves="yes")),OR(Fact(prematureLeaves="no"),Fact(shortStem="no"),Fact(rottenRoot="no")),OR(Fact(fruitSpot="no"),Fact(fruitHalo="no")),OR(Fact(rootSoilGrain="no"),Fact(rootYarnBlack="no")),
	OR(Fact(rootBlackSpot="no"),Fact(stemBlackSpot="no")),Fact(rootWovenWhite="no"),OR(Fact(stemSilk="no"),Fact(stemNecrosis="no"),Fact(fruitNecrosis="no")),NOT(Fact(clrShowed=W())))
	def disease_0(self):
		self.declare(Fact(disease="Coffee Leaf Rust"))
		im = Image.open("images/Coffee Leaf Rust.png")
		im.show()
		print("leaf rust")
		self.declare(Fact(clrShowed="yes"))


	@Rule(Fact(action='find_disease'),Fact(yellowLeaves="yes"),OR(Fact(brownYellowSpots="yes"),Fact(leavesEasyFallen="yes")),Fact(dullLeaves="no"),OR(Fact(orangePowder="yes"),Fact(baldLeaves="yes"),
	Fact(patchesLeaves="yes")),OR(Fact(prematureLeaves="yes"),Fact(shortStem="yes"),Fact(rottenRoot="yes")),OR(Fact(fruitSpot="no"),Fact(fruitHalo="no")),OR(Fact(rootSoilGrain="no"),Fact(rootYarnBlack="no")),
	OR(Fact(rootBlackSpot="no"),Fact(stemBlackSpot="no")),Fact(rootWovenWhite="no"),OR(Fact(stemSilk="no"),Fact(stemNecrosis="no"),Fact(fruitNecrosis="no")),NOT(Fact(nShowed=W())))
	def disease_1(self):
		self.declare(Fact(disease="Nematode"))
		im = Image.open("images/Nematode.png")
		im.show()
		print("nematode")
		self.declare(Fact(nShowed="yes"))

	@Rule(Fact(action='find_disease'),Fact(yellowLeaves="yes"),OR(Fact(brownYellowSpots="yes"),Fact(leavesEasyFallen="yes")),Fact(dullLeaves="no"),OR(Fact(orangePowder="yes"),Fact(baldLeaves="yes"),
	Fact(patchesLeaves="yes")),OR(Fact(prematureLeaves="yes"),Fact(shortStem="yes"),Fact(rottenRoot="yes")),OR(Fact(fruitSpot="yes"),Fact(fruitHalo="yes")),OR(Fact(rootSoilGrain="no"),Fact(rootYarnBlack="no")),
	OR(Fact(rootBlackSpot="no"),Fact(stemBlackSpot="no")),Fact(rootWovenWhite="no"),OR(Fact(stemSilk="no"),Fact(stemNecrosis="no"),Fact(fruitNecrosis="no")),NOT(Fact(besShowed=W())))
	def disease_2(self):
		self.declare(Fact(disease="Brown Eye Spot of Coffee"))
		im = Image.open("images/Brown Eye Spot of Coffee.png")
		im.show()
		print("brown eye")
		self.declare(Fact(besShowed="yes"))


	@Rule(Fact(action='find_disease'),Fact(yellowLeaves="yes"),OR(Fact(brownYellowSpots="no"),Fact(leavesEasyFallen="no")),Fact(dullLeaves="no"),OR(Fact(orangePowder="no"),Fact(baldLeaves="no"),
	Fact(patchesLeaves="no")),OR(Fact(prematureLeaves="no"),Fact(shortStem="no"),Fact(rottenRoot="no")),OR(Fact(fruitSpot="no"),Fact(fruitHalo="no")),OR(Fact(rootSoilGrain="no"),Fact(rootYarnBlack="no")),
	OR(Fact(rootBlackSpot="no"),Fact(stemBlackSpot="no")),Fact(rootWovenWhite="no"),OR(Fact(stemSilk="yes"),Fact(stemNecrosis="yes"),Fact(fruitNecrosis="yes")),NOT(Fact(ufShowed=W())))
	def disease_3(self):
		self.declare(Fact(disease="Upas Fungus"))
		im = Image.open("images/Upas Fungus.png")
		im.show()
		print("upas fungus")
		self.declare(Fact(ufShowed="yes"))

	@Rule(Fact(action='find_disease'),Fact(yellowLeaves="yes"),OR(Fact(brownYellowSpots="yes"),Fact(leavesEasyFallen="yes")),Fact(dullLeaves="yes"),OR(Fact(orangePowder="no"),Fact(baldLeaves="no"),
	Fact(patchesLeaves="no")),OR(Fact(prematureLeaves="no"),Fact(shortStem="no"),Fact(rottenRoot="no")),OR(Fact(fruitSpot="no"),Fact(fruitHalo="no")),OR(Fact(rootSoilGrain="yes"),Fact(rootYarnBlack="yes")),
	OR(Fact(rootBlackSpot="no"),Fact(stemBlackSpot="no")),Fact(rootWovenWhite="no"),OR(Fact(stemSilk="no"),Fact(stemNecrosis="no"),Fact(fruitNecrosis="no")),NOT(Fact(brownrfShowed=W())))
	def disease_4(self):
		self.declare(Fact(disease="Brown Root Fungus"))
		im = Image.open("images/Brown Root Fungus.png")
		im.show()
		print("brown root")
		self.declare(Fact(brownrfShowed="yes"))

	@Rule(Fact(action='find_disease'),Fact(yellowLeaves="yes"),OR(Fact(brownYellowSpots="yes"),Fact(leavesEasyFallen="yes")),Fact(dullLeaves="yes"),OR(Fact(orangePowder="no"),Fact(baldLeaves="no"),
	Fact(patchesLeaves="no")),OR(Fact(prematureLeaves="no"),Fact(shortStem="no"),Fact(rottenRoot="no")),OR(Fact(fruitSpot="no"),Fact(fruitHalo="no")),OR(Fact(rootSoilGrain="yes"),Fact(rootYarnBlack="yes")),
	OR(Fact(rootBlackSpot="yes"),Fact(stemBlackSpot="yes")),Fact(rootWovenWhite="no"),OR(Fact(stemSilk="no"),Fact(stemNecrosis="no"),Fact(fruitNecrosis="no")),NOT(Fact(blackrfShowed=W())))
	def disease_5(self):
		self.declare(Fact(disease="Black Root Fungus"))
		im = Image.open("images/Black Root Fungus.png")
		im.show()
		print("blackroot")
		self.declare(Fact(blackrfShowed="yes"))

	@Rule(Fact(action='find_disease'),Fact(yellowLeaves="yes"),OR(Fact(brownYellowSpots="yes"),Fact(leavesEasyFallen="yes")),Fact(dullLeaves="yes"),OR(Fact(orangePowder="no"),Fact(baldLeaves="no"),
	Fact(patchesLeaves="no")),OR(Fact(prematureLeaves="no"),Fact(shortStem="no"),Fact(rottenRoot="no")),OR(Fact(fruitSpot="no"),Fact(fruitHalo="no")),OR(Fact(rootSoilGrain="yes"),Fact(rootYarnBlack="yes")),
	OR(Fact(rootBlackSpot="yes"),Fact(stemBlackSpot="yes")),Fact(rootWovenWhite="yes"),OR(Fact(stemSilk="no"),Fact(stemNecrosis="no"),Fact(fruitNecrosis="no")),NOT(Fact(wrfShowed=W())))
	def disease_6(self):
		self.declare(Fact(disease="White Root Fungus"))
		im = Image.open("images/White Root Fungus.png")
		im.show()
		print("whiteroot")
		self.declare(Fact(wrfShowed="yes"))

	@Rule(Fact(action='find_disease'),Fact(yellowLeaves="no"),Fact(brownYellowSpots="no"),Fact(leavesEasyFallen="no"),Fact(dullLeaves="no"),Fact(orangePowder="no"),Fact(baldLeaves="no"),
	Fact(patchesLeaves="no"),Fact(prematureLeaves="no"),Fact(shortStem="no"),Fact(rottenRoot="no"),Fact(fruitSpot="no"),Fact(fruitHalo="no"),Fact(rootSoilGrain="no"),Fact(rootYarnBlack="no"),
	Fact(rootBlackSpot="no"),Fact(stemBlackSpot="no"),Fact(rootWovenWhite="no"),Fact(stemSilk="no"),Fact(stemNecrosis="no"),Fact(fruitNecrosis="no"))
	def disease_7(self):
		self.declare(Fact(disease="Disease Not Detected"))


	@Rule(Fact(action='find_disease'),Fact(disease=MATCH.disease),salience = -998)
	def disease(self, disease):
		print("")
		id_disease = disease
		disease_details = get_details(id_disease) 
		treatments = get_treatments(id_disease)
		print("")
		if(id_disease == "Disease Not Detected"):
			print("Your plant is healthy")
		else:	
			print("The most probable disease that the plant has is %s\n" %(id_disease))
		print("A short description is given below :\n")
		print(disease_details+"\n")
		#print("The common medications and procedures suggested are: \n")
		#print(treatments+"\n")

	@Rule(Fact(action='find_disease'),
		  Fact(yellowLeaves=MATCH.yellowLeaves),
		  Fact(brownYellowSpots=MATCH.brownYellowSpots),
		  Fact(leavesEasyFallen=MATCH.leavesEasyFallen),
		  Fact(dullLeaves=MATCH.dullLeaves),
		  Fact(orangePowder=MATCH.orangePowder),
		  Fact(baldLeaves=MATCH.baldLeaves),
		  Fact(patchesLeaves=MATCH.patchesLeaves),
		  Fact(prematureLeaves=MATCH.prematureLeaves),
		  Fact(shortStem=MATCH.shortStem),
		  Fact(rottenRoot=MATCH.rottenRoot),
		  Fact(fruitSpot=MATCH.fruitSpot),
		  Fact(fruitHalo=MATCH.fruitHalo),
		  Fact(rootSoilGrain=MATCH.rootSoilGrain),
		  Fact(rootYarnBlack=MATCH.rootYarnBlack),
		  Fact(rootBlackSpot=MATCH.rootBlackSpot),
		  Fact(stemBlackSpot=MATCH.stemBlackSpot), 
		  Fact(rootWovenWhite=MATCH.rootWovenWhite),
		  Fact(stemSilk=MATCH.stemSilk),
		  Fact(stemNecrosis=MATCH.stemNecrosis),
		  Fact(fruitNecrosis=MATCH.fruitNecrosis),NOT(Fact(disease=MATCH.disease)),salience = -999)

	def not_matched(self,yellowLeaves, brownYellowSpots, leavesEasyFallen, dullLeaves, orangePowder, baldLeaves, patchesLeaves, prematureLeaves,shortStem ,rottenRoot ,
	fruitSpot ,fruitHalo ,rootSoilGrain, rootYarnBlack, rootBlackSpot, stemBlackSpot, rootWovenWhite, stemSilk, stemNecrosis, fruitNecrosis):
		print("\nDid not find any disease that matches given exact symptoms")
		lis = [yellowLeaves, brownYellowSpots, leavesEasyFallen, dullLeaves, orangePowder, baldLeaves, patchesLeaves, prematureLeaves,shortStem ,rottenRoot ,
		fruitSpot ,fruitHalo ,rootSoilGrain, rootYarnBlack, rootBlackSpot, stemBlackSpot, rootWovenWhite, stemSilk, stemNecrosis, fruitNecrosis]
		
		max_count = 0
		max_disease = ""
		for key,val in symptom_map.items():
			count = 0
			temp_list = eval(key)
			for j in range(0,len(lis)):
				if(temp_list[j] == lis[j] and lis[j] == "yes"):
					count = count + 1
			if count > max_count:
				max_count = count
				max_disease = val
		if_not_matched(max_disease)
		


if __name__ == "__main__":
	preprocess()
	engine = Greetings()
	while(1):
		engine.reset()  # Prepare the engine for the execution.
		engine.run()  # Run it!
		print("Would you like to diagnose some other symptoms?")
		if input() == "no":
			exit()
		#print(engine.facts)
