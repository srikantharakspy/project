Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
pip install streamlit
SyntaxError: invalid syntax
print ("hello world")
hello world

==================================================================================== RESTART: Shell ====================================================================================
import fastai
from fastai.vision.all import *
from fastai import *

import pathlib
#pathlib.PosixPath = pathlib.WindowsPath
import streamlit as st

st.image('Header.png')
st.header('Clouds Classification Demonstrate')

model = st.radio(
    'What MODEL do you want to use?',
    ('Resnet50'             )
)

class Predict:
    def __init__(self, filename):
        self.learn_inference = load_learner(Path()/filename)
        self.img = self.get_image_from_upload()
        if self.img is not None:
            self.display_output()
            self.get_prediction()
    
    @staticmethod
    def get_image_from_upload():
        uploaded_file = st.file_uploader("Upload or Take a Cloud Image",type=['png','jpeg', 'jpg'])
        if uploaded_file is not None:
            return PILImage.create((uploaded_file))
        return None

    def display_output(self):
        st.image(self.img.to_thumb(500,500), caption='Uploaded Image')

    def get_prediction(self):

        if st.button('Click here! to Classify'):
            pred, pred_idx, probs = self.learn_inference.predict(self.img)
            st.subheader(f'Prediction: *{pred}* with Confidence: *{probs[pred_idx]*100:.02f}*%')
            #st.subheader(f'ผลการทำนาย: *{pred}* ด้วยความมั่นใจ: *{probs[pred_idx]*100:.02f}*%')
            st.subheader(f'You are currently use *{model}* model!')
    
            if pred == 'true' :
                st.image('DSC_1849.JPG', 'DSC_1353.JPG')
            elif pred == 'fales' :
                st.image('DSC_0842.JPG', 'DSC_1401.JPG')
            else :
                st.image('Sc.png')

            st.balloons()
        #else: 
           # st.write(f'Click the button to classify') 


if model == 'Resnet50':
    if __name__=='__main__':
        #st.write('You are currently use Resnet50 model')
        resnet_model ='project_resnet50_vtest.pkl'
        predictor_resnet = Predict(resnet_model)
else:
    if __name__=='__main__':
        #st.write('You are currently use VGG16 model')
        vgg16_model ='project_resnet50_vtest.pkl'
        predictor_vgg16 = Predict(vgg16_model)

                                                  
st.text('      ')
st.text('      ')
st.text('      ')
#st.text('Credit')
st.text('[developers] Patompong Oupapong, Pannawit Wantae, Pongsapat Suporn')
st.text('[advisors] Songkran Buttawong, Suthut Butchanon')
st.text('[special advisors] Pathapong Pongpatrakant')
st.text('A Capstone Project, Princess Chulabhorn Science High School Loei')
SyntaxError: multiple statements found while compiling a single statement
import fastai
from fastai.vision.all import *
from fastai import *

import pathlib
#pathlib.PosixPath = pathlib.WindowsPath
import streamlit as st

st.image('C:/Users/Dell/Downloads/LINE_ALBUM_ชุดพิธีการ_๒๓๐๒๒๐.jpg')
st.header('Clouds Classification Demonstrate')

model = st.radio(
    'What MODEL do you want to use?',
    ('Resnet50'             )
)

class Predict:
    def __init__(self, filename):
        self.learn_inference = load_learner(Path()/filename)
        self.img = self.get_image_from_upload()
        if self.img is not None:
            self.display_output()
            self.get_prediction()
    
    @staticmethod
    def get_image_from_upload():
        uploaded_file = st.file_uploader("Upload or Take a Cloud Image",type=['png','jpeg', 'jpg'])
        if uploaded_file is not None:
            return PILImage.create((uploaded_file))
        return None

    def display_output(self):
        st.image(self.img.to_thumb(500,500), caption='Uploaded Image')

    def get_prediction(self):

        if st.button('Click here! to Classify'):
            pred, pred_idx, probs = self.learn_inference.predict(self.img)
            st.subheader(f'Prediction: *{pred}* with Confidence: *{probs[pred_idx]*100:.02f}*%')
            #st.subheader(f'ผลการทำนาย: *{pred}* ด้วยความมั่นใจ: *{probs[pred_idx]*100:.02f}*%')
            st.subheader(f'You are currently use *{model}* model!')
    
            if pred == 'true' :
                st.image('DSC_1849.JPG', 'DSC_1353.JPG')
            elif pred == 'fales' :
                st.image('DSC_0842.JPG', 'DSC_1401.JPG')
            else :
                st.image('Sc.png')

            st.balloons()
        #else: 
           # st.write(f'Click the button to classify') 


if model == 'Resnet50':
    if __name__=='__main__':
        #st.write('You are currently use Resnet50 model')
        resnet_model ='project_resnet50_vtest.pkl'
        predictor_resnet = Predict(resnet_model)
else:
    if __name__=='__main__':
        #st.write('You are currently use VGG16 model')
        vgg16_model ='project_resnet50_vtest.pkl'
        predictor_vgg16 = Predict(vgg16_model)

                                                  
st.text('      ')
st.text('      ')
st.text('      ')
#st.text('Credit')
st.text('[developers] Patompong Oupapong, Pannawit Wantae, Pongsapat Suporn')
st.text('[advisors] Songkran Buttawong, Suthut Butchanon')
st.text('[special advisors] Pathapong Pongpatrakant')
st.text('A Capstone Project, Princess Chulabhorn Science High School Loei')
SyntaxError: multiple statements found while compiling a single statement
import fastai
from fastai.vision.all import *
from fastai import *

import pathlib
#pathlib.PosixPath = pathlib.WindowsPath
import streamlit as st

st.image('C:/Users/Dell/Downloads/LINE_ALBUM_ชุดพิธีการ_๒๓๐๒๒๐.jpg')
st.header('verify ceremonial uniform')

model = st.radio(
    'What MODEL do you want to use?',
    ('Resnet50')
)

class Predict:
    def __init__(self, filename):
        self.learn_inference = load_learner(Path()/filename)
        self.img = self.get_image_from_upload()
        if self.img is not None:
            self.display_output()
            self.get_prediction()
    
    @staticmethod
    def get_image_from_upload():
        uploaded_file = st.file_uploader("Upload or Take a Cloud Image",type=['png','jpeg', 'jpg'])
        if uploaded_file is not None:
            return PILImage.create((uploaded_file))
        return None

    def display_output(self):
        st.image(self.img.to_thumb(500,500), caption='Uploaded Image')

    def get_prediction(self):

        if st.button('Click here! to Classify'):
            pred, pred_idx, probs = self.learn_inference.predict(self.img)
            st.subheader(f'Prediction: *{pred}* with Confidence: *{probs[pred_idx]*100:.02f}*%')
            #st.subheader(f'ผลการทำนาย: *{pred}* ด้วยความมั่นใจ: *{probs[pred_idx]*100:.02f}*%')
            st.subheader(f'You are currently use *{model}* model!')
    
            if pred == 'true' :
                st.image('DSC_1849.jpg','DSC_1353.jpg')
            elif pred == 'false' :
                st.image('DSC_0842.jpg','DSC_1401.jpg')
            else :
                st.image('Sc.png')

            st.balloons()
        #else: 
           # st.write(f'Click the button to classify') 


if model == 'Resnet50':
    if __name__=='__main__':
        #st.write('You are currently use Resnet50 model')
        resnet_model ='resnet50_vtest.pkl'
        predictor_resnet = Predict(resnet_model)
else:
    if __name__=='__main__':
        #st.write('You are currently use VGG16 model')
        vgg16_model ='resnet50_vtest.pkl'
        predictor_vgg16 = Predict(vgg16_model)


st.text('      ')
st.text('      ')
st.text('      ')
#st.text('Credit')
st.text('[developers] Patompong Oupapong, Pannawit Wantae, Pongsapat Suporn')
st.text('[advisors] Songkran Buttawong, Suthut Butchanon')
st.text('[special advisors] Pathapong Pongpatrakant')
st.text('A Capstone Project, Princess Chulabhorn Science High School Loei')
SyntaxError: multiple statements found while compiling a single statement
import fastai
from fastai.vision.all import *
from fastai import *

import pathlib
#pathlib.PosixPath = pathlib.WindowsPath
import streamlit as st

st.image('LINE_ALBUM_ชุดพิธีการ_๒๓๐๒๒๐.jpg')
st.header('verify ceremonial uniform')

model = st.radio(
    'What MODEL do you want to use?',
    ('Resnet50')
)

class Predict:
    def __init__(self, filename):
        self.learn_inference = load_learner(Path()/filename)
        self.img = self.get_image_from_upload()
        if self.img is not None:
            self.display_output()
            self.get_prediction()
    
    @staticmethod
    def get_image_from_upload():
        uploaded_file = st.file_uploader("Upload or Take a Cloud Image",type=['png','jpeg', 'jpg'])
        if uploaded_file is not None:
            return PILImage.create((uploaded_file))
        return None

    def display_output(self):
        st.image(self.img.to_thumb(500,500), caption='Uploaded Image')

    def get_prediction(self):

        if st.button('Click here! to Classify'):
            pred, pred_idx, probs = self.learn_inference.predict(self.img)
            st.subheader(f'Prediction: *{pred}* with Confidence: *{probs[pred_idx]*100:.02f}*%')
            #st.subheader(f'ผลการทำนาย: *{pred}* ด้วยความมั่นใจ: *{probs[pred_idx]*100:.02f}*%')
            st.subheader(f'You are currently use *{model}* model!')
    
            if pred == 'true' :
                st.image('DSC_1849.jpg','DSC_1353.jpg')
            elif pred == 'fales' :
                st.image('DSC_0842.jpg','DSC_1401.jpg')
            else :
                st.image('Sc.png')

            st.balloons()
        #else: 
           # st.write(f'Click the button to classify') 


if model == 'Resnet50':
    if __name__=='__main__':
        #st.write('You are currently use Resnet50 model')
        resnet_model ='
        project_resnet50_vtest.pkl'
        predictor_resnet = Predict(resnet_model)


st.text('      ')
st.text('      ')
st.text('      ')
#st.text('Credit')
st.text('[developers] Patompong Oupapong, Pannawit Wantae, Pongsapat Suporn')
st.text('[advisors] Songkran Buttawong, Suthut Butchanon')
st.text('[special advisors] Pathapong Pongpatrakant')
st.text('A Capstone Project, Princess Chulabhorn Science High School Loei')
SyntaxError: multiple statements found while compiling a single statement
import fastai
from fastai.vision.all import *
from fastai import *

import pathlib
#pathlib.PosixPath = pathlib.WindowsPath
import streamlit as st

st.image('LINE_ALBUM_ชุดพิธีการ_๒๓๐๒๒๐.jpg')
st.header('verify ceremonial uniform')

model = st.radio(
    'What MODEL do you want to use?',
    ('Resnet50')
)

class Predict:
    def __init__(self, filename):
        self.learn_inference = load_learner(Path()/filename)
        self.img = self.get_image_from_upload()
...         if self.img is not None:
...             self.display_output()
...             self.get_prediction()
...     
...     @staticmethod
...     def get_image_from_upload():
...         uploaded_file = st.file_uploader("Upload or Take a Cloud Image",type=['png','jpeg', 'jpg'])
...         if uploaded_file is not None:
...             return PILImage.create((uploaded_file))
...         return None
... 
...     def display_output(self):
...         st.image(self.img.to_thumb(500,500), caption='Uploaded Image')
... 
...     def get_prediction(self):
... 
...         if st.button('Click here! to Classify'):
...             pred, pred_idx, probs = self.learn_inference.predict(self.img)
...             st.subheader(f'Prediction: *{pred}* with Confidence: *{probs[pred_idx]*100:.02f}*%')
...             #st.subheader(f'ผลการทำนาย: *{pred}* ด้วยความมั่นใจ: *{probs[pred_idx]*100:.02f}*%')
...             st.subheader(f'You are currently use *{model}* model!')
...     
...             if pred == 'true' :
...                 st.image('DSC_1843.jpg','DSC_1353.jpg'DSC_)
...             elif pred == 'false' :
...                 st.image('DSC_0842.jpg','DSC_1401')
...             else :
...                 st.image('Sc.png')
... 
...             st.balloons()
...         #else: 
...            # st.write(f'Click the button to classify') 
... 
... 
... if model == 'Resnet50':
...     if __name__=='__main__':
...         #st.write('You are currently use Resnet50 model')
...         resnet_model ='project_resnet50_vtest.pkl'
...         predictor_resnet = Predict(resnet_model)
... 
... 
... st.text('      ')
... st.text('      ')
... st.text('      ')
... #st.text('Credit')
... st.text('[developers] Thasinee Srikantharak,Phatcharapa Suratewee')
... st.text('[advisors] Suthut Butchanon')
