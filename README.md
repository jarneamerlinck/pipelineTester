# Tracking your models with MLFlow
Alright, we managed to write some simple unit tests that will ensure our data behaves correctly!  
Compared to where we started, I would say that we already made a whole lot of progress towards CI/CD in a Machine Learning setting: 
1. We cleaned up and restructured our code
2. We created an automated pipeline
3. We're checking our data automatically

A big part of Machine Learning that we still haven't talked about are of course the trained models themselves.
Data Science is an iterative process: we test a model, we make some small changes either to the model itself or to the data, and we then test the model again.  
Some production workflows are set-up to test tens or hundreds of models per **day**. How do we keep track of which model with which parameters performed best? We could just output our results to a .txt file each time, however that's going to get real messy real quick...

## Theory

MLFlow is a popular, open-source platform that aims to help you with exactly that.
It can:
1. Track the performance of your models for you
2. Package data science code in a format to reproduce runs on any platform
3. Deploy Machine Learning models
4. Store, annotate, discover, and manage models in a central repository

Today we'll only look at the first two capabilities, but if you're interested in Machine Learning I strongly encourage you to look into the other functions as well.
Documentation can be found here: https://mlflow.org/

### Model Tracking
MLFlow's model tracking allows you to keep track of three things:
1. The model performance scores (e.g. accuracy in a classifier). We keep track of this to objectively decide which model performs best.
2. All (hyper)parameters that can change between model runs (e.g. the number of trees trained in a random forrest, which independent variables were used, the size of our dataset, or even the type of model itself). We keep track of this to test which parameters were used to achieve the highest model performance scores
3. Model artifacts. Generally these are important files or figures that you'd like to keep track of as well. (e.g. a dataset version file)

You can implement model tracking in your code with the python SDK. Simply run ```pip install mlflow``` to get started.

### Packaging code
I already told you about conda environments, and we can now go one step further with something called MLProjects.
Our previous conda environment still required the user of our code to manually update the environment everytime we make a change to the environment.yml.
An MLProject file will do this for you, while also keeping tracking of your previous environments.

Instead of running the training script directly using ```python train.py```, we can now run our training script by running ```mlflow run . -e train```, since we have this MLProject file in our repository which will check what the entrypoint 'train' is required to do.

I'm using conda environments for ease of use here, but we can go further with MLProject files as well! Docker is completely integrated into MLFlow, so you can use Docker files in the MLProject file instead of conda environment files.

## Exercises

1. Again, clone this repository to your github account and then to your local machine.
2. Install MLFlow by running ```pip install mlflow```
3. Go through the *train.py* script and understand what changes were made to track our model.
4. Inspect the run of the model that has already been saved in this repository under the /mlruns folder. MLFlow wil automatically save your runs to an /mlruns folder in the root directory you are running the script from.
5. Now run ```mlflow ui``` in your terminal to inspect the run visually.
6. Think about which interesting metrics and parameters we could track as well and add those to the code. For metrics, you can look here for inspiration: https://scikit-learn.org/stable/modules/model_evaluation.html?msclkid=db5995c5a84011ec9ee1dd8ac072e1ad
7. Now do a run of the training script and ensure your new metrics and parameters are logged to the /mlruns folder. If you dont want to use the MLProject file with the conda environment, you can simply run the training script with ```python train.py --mlflow_run=1``` else, use the ```mlflow run . -e train``` command.
8. Run the ```mlflow ui``` again and inspect the results.

## Exercises for home

1. Continue experimenting with your model and try to train a better model (based on the validation accuracy) than the one that's already trained.
2. What if you like the visuals and capabilities of Azure Machine Learning studio much better than MLFlow's, but to keep your project completely open-source you are forced to track all metrics using MLFlow? Not to worry! Mlflow is completely integrated within Azure and you can log your mlflow runs to Azure's Machine Learning Studio. Go through the following documentations [here](https://docs.microsoft.com/en-us/azure/machine-learning/concept-mlflow?msclkid=30b688aea84411ec92be8d2011ff1cda) and [here](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-use-mlflow?msclkid=30b6b1ada84411eca5c8a4739bde81c8) and log your mlflow runs to Azure Machine Learning studio.
3. Optional: Github Actions is completely integrated within Azure as well! Go through the documentation [here](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-github-actions-machine-learning#:~:text=1%20Prerequisites.%20An%20Azure%20account%20with%20an%20active,model%20to%20Azure%20Machine%20Learning%20to%20ACI.%20?msclkid=0af4e03ca84511ecaf6f285e20a759a2) and think of ways you could integrate your Github Actions with Azure Machine Learning (e.g. you could automatically start and stop an Azure Compute instance each time new data is pushed to your repository and train your model on Azure instead. This is especially useful if you're training larger models or models that require a GPU, since Github VMs aren't very strong and only provide a CPU)

## The end
I hope you learned something new today. And if not, I hope you managed to do something else productive in our time together instead.
If you have any questions or you just want to talk about Data Science, you can always reach me at Lukas.Mahieu@arinti.ai


