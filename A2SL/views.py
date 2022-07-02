from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
from django.contrib.staticfiles import finders
from django.contrib.auth.decorators import login_required

def home_view(request):
	return render(request,'home.html')

def animation_view(request):
	if request.method == 'POST':
		text = request.POST.get('sen')
		#tokenizing the sentence
		text.lower()
		#tokenizing the sentence
		words = word_tokenize(text)

		tagged = nltk.pos_tag(words)
		tense = {}
   		 # 1. VBP -> Verb, non-3rd person singular present
		 # 2. VBZ -> Verb, gerund or present participle
         # 3. VBG -> Verb, 3rd person singular present
		tense["future"] = len([word for word in tagged if word[1] == "MD"])		# md -> modal
		tense["present"] = len([word for word in tagged if word[1] in ["VBP", "VBZ","VBG"]])	
		tense["past"] = len([word for word in tagged if word[1] in ["VBD", "VBN"]])	# verb, past participle, past tense
		tense["present_continuous"] = len([word for word in tagged if word[1] in ["VBG"]])	



		#stopwords that will be removed
		stop_words = set(["will","mightn't", 're', 'wasn', 'wouldn', 'be', 'has', 'does', 'shouldn', "you've",'off', 'for', "didn't", 'ain', 'haven', "weren't", 'are', "she's", "wasn't", 'its', "haven't", "wouldn't", 'don', 'weren', "don't", 'doesn', "hadn't", 'is', 'was', "that'll", "should've", 'then', 'the', 'mustn', 'nor', 'as', "it's", "needn't", 'am', 'have',  'hasn', "aren't", "couldn't", "you're", "mustn't", 'didn', "doesn't", 'an', 'hadn', 'whom', "hasn't", 'itself', 'couldn', 'needn', "shan't", 'isn', 'been', 'such', 'shan', "shouldn't", 'aren', 'being', 'were', 'did', 'having', 'mightn', 've', "isn't", "won't"])

		#removing stopwords and applying lemmatizing nlp process to words
		lr = WordNetLemmatizer()
		filtered_text = []
		for w,p in zip(words,tagged):
			if w not in stop_words:
				if p[1]=='VBG' or p[1]=='VBD' or p[1]=='VBZ' or p[1]=='VBN' or p[1]=='NN':
					filtered_text.append(lr.lemmatize(w,pos='v'))
				elif p[1]=='JJ' or p[1]=='JJR' or p[1]=='JJS'or p[1]=='RBR' or p[1]=='RBS':
					filtered_text.append(lr.lemmatize(w,pos='a'))

				else:
					filtered_text.append(lr.lemmatize(w))


		#adding the specific word to specify tense
		words = filtered_text
		temp=[]
		for w in words:
			if w=='I':
				temp.append('Me')
			else:
				temp.append(w)
		words = temp
		probable_tense = max(tense,key=tense.get)

		# if probable_tense == "past" and tense["past"]>=1:
		# 	temp = ["Before"]
		# 	temp = temp + words
		# 	words = temp
		# elif probable_tense == "future" and tense["future"]>=1:
		# 	if "Will" not in words:
		# 			temp = ["Will"]
		# 			temp = temp + words
		# 			words = temp
		# 	else:
		# 		pass
		# elif probable_tense == "present":
		# 	if tense["present_continuous"]>=1:
		# 		temp = ["Now"]
		# 		temp = temp + words
		# 		words = temp


		filtered_text = []
		for w in words:
			path = w + ".mov"
			f = finders.find(path)
			#splitting the word if its animation is not present in database
			if not f:
				for c in w:
					filtered_text.append(c)
			#otherwise animation of word
			else:
				filtered_text.append(w)
		words = filtered_text;



		return render(request,'animation.html',{'words':words,'text':text})
	else:
		return render(request,'animation.html')




# def signup_view(request):
#     return render("Signup")
	# if request.method == 'POST':
	# 	form = UserCreationForm(request.POST)
	# 	if form.is_valid():
	# 		user = form.save()
	# 		login(request,user)
	# 		# log the user in
	# 		return redirect('animation')
	# else:
	# 	form = UserCreationForm()
	# return render(request,'signup.html',{'form':form})



# def login_view(request):
# 	if request.method == 'POST':
# 		form = AuthenticationForm(data=request.POST)
# 		if form.is_valid():
# 			#log in user
# 			user = form.get_user()
# 			login(request,user)
# 			if 'next' in request.POST:
# 				return redirect(request.POST.get('next'))
# 			else:
# 				return redirect('animation')
# 	else:
# 		form = AuthenticationForm()
# 	return render(request,'login.html',{'form':form})


# def logout_view(request):
# 	logout(request)
# 	return redirect("home")


def index(request):
    return render(request, 'index.html')

def MotionDashboard(request):
    return render(request, 'MotionDashboard.html')

def animation(request):
    return render(request, 'animation.html')

def ColorsTutorial(request):
    return render(request, 'ColorsTutorial.html')

def AnimalsTutorials(request):
    return render(request, 'AnimalsTutorials.html')

def NumbersTutorials(request):
    return render(request, 'NumbersTutorials.html')
	
def AlphabetsTutorials(request):
        return render(request, 'AlphabetsTutorials.html')

def Courses(request):
    return render(request, 'Courses.html')

def AnimalsTutorials(request):
    return render(request, 'AnimalsTutorials.html')

def NumbersTutorial(request):
    return render(request, 'NumbersTutorial.html')

def Article(request):
    return render(request, 'Article.html')

def MotionDetection(request):
    return render(request, 'MotionDetection.html')

def TutorialChoose(request):
    return render(request, 'TutorialChoose.html')

def TrainYourself(request):
    return render(request, 'TrainYourself.html')

def ChooseArticle(request):
    return render(request, 'ChooseArticle.html')

  