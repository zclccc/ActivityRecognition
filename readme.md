# Activity Recognition

## Introduction 

My whole project is based on the [dataset](https://www.kaggle.com/uciml/human-activity-recognition-with-smartphones) provided for a competition one year ago on Kaggle. My aim was to see if I could improved the results given in the kernels through other methods, such as convolutionnal networks. The first problematic was thus the understanding of their protocol, as I wanted to gather the raw signal corresponding to the given features. The whole development on this repository represents my numerous trials, and the relative performances are given along with it.

## Model tested 

* XGBoost
* RandomForest
* 1D Convolution
* 2D Convolution
* Mixed Neural Networks

## Features

The features being used to feed both the boosted trees and the neural networks are based on the ones given in the dataset, but also my own handcrafted features, based on experience, which I could obtain due to the extracted raw signals.