# sentence_generator_model


This project here is an extension to my `sentence-generator` project
which can be found here <a href=""></a>. I use to serve my model on the same place as my website. In this project I sepereate my model from my website. In this project I have mi model and a api which I host on a seperate server from my website. It takes requests and sends back a generated sentence. 


# Getting Started 
To begin you can clone the repo. Before you can start this project up you should create a virtual enviorment to install all the packages. You can create a virtual envoirment witht this command. 

```


python3 -m venv env

```


Once you have the virtual enviorment you can now install the packages with. 

```

pip install -r requirements.txt

```

Once the packages are done installing you can now start up the api to send requests. 


# Trying It Out

To test out that it works we can do `python3 api.py` in the terminal. It'll then let you know that the server has started on localhost on port 5000, which you can change if need be. To test it that its working you can now open a new tab on the terminal and send a request to the server. Here is an example.

```

$ curl http://localhost:5000/todos -d "task=a random sentence" -X POST -v

```


