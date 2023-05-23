import pyrebase 

def database():
    firebaseConfig = {
    "apiKey": "AIzaSyC9tLok-Tc8xadK2ucNHa4KM8sCUv3ITZo",
    "authDomain": "rvmproject-5057e.firebaseapp.com",
    "databaseURL": "https://rvmproject-5057e-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "rvmproject-5057e",
    "storageBucket": "rvmproject-5057e.appspot.com",
    "messagingSenderId": "6742122919",
    "appId": "1:6742122919:web:c81a75a24a6c2ab7e05682",
    }

    firebase = pyrebase.initialize_app(firebaseConfig)
    auth=firebase.auth()
    database = firebase.database()  
    return database 


    


