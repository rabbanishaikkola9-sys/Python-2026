import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("Hey this is the example of external module using python which is from thirdparty you need to create the virutal env for the running of these externa modules bcz it defines the workspace of the python")
engine.runAndWait()