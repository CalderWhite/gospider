import pip
print("Checking dependancies")
#Yes, I know this isn't the best way to do this, but it works.
dep = ["nltk","bs4"]
nltkDep = ["brown","averaged_perceptron_tagger","stopwords","punkt"]
for i in dep:
    r = pip.main(["install",i])
    # if the package is already installed, attempt to update it.
    if r:
        r = pip.main(["install",i,"--upgrade"])
# some custom stuff for nltk
import nltk
print("Grabbing required nltk packages")
for i in nltkDep:
    nltk.download(i)