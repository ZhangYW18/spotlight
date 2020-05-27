# SpotLight - I Know Your Heart

SpotLight is a wondeful web system that can guess the sentiment which hides behind your words.

It is super smart and can learn from your feedbacks.

## Running SpotLight Locally

### 1. Related Repository - Machine Learning Part

[Twitter Sentiment Analysis](https://github.com/ZhangYW18/AppliedTextMining)

If you intend to run spotlight on your own machine, you may need to produce model.h5 and tokenizer.pkl using this repo first and put it under path index/static/models. You can also download pre-trained model according to the following link:

Link:https://pan.baidu.com/s/1CJkDQPuAAdHkH6DFGUHKNw  
Password:1qay

### 2. Run SpotLight in Terminal
Run the following command in the project root folder:
```shell script
$ python manage.py runserver
```



## Examples

The Home Page

![index](./docs/images/index.png)

Some Predictions

![neutral](./docs/images/neutral.png)

![positive](./docs/images/positive.png)
