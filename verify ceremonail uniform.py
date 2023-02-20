"""
import fastai
from fastai.vision.all import *
from fastai import *

import pathlib
#pathlib.PosixPath = pathlib.WindowsPath
"""
import streamlit as st

st.image('DSC_0842.JPG')
st.header('verify ceremonial uniform')

"""
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
...                 st.image('29072.png')
...             else pred == 'false' :
...                 st.image('29072.png')
...            
... 
...             st.balloons()
...         #else: 
...          #   st.write(f'Click the button to classify') 
... 
... 
... 
...if __name__=='__main__':
...         #st.write('You are currently use Resnet50 model')
...     resnet_model ='project_resnet50_vtest.pkl'
...     predictor_resnet = Predict(resnet_model)
... """
...""" 
... st.text('      ')
... st.text('      ')
... st.text('      ')
... #st.text('Credit')
... st.text('[developers] Thasinee Srikantharak,Phatcharapa Suratewee')
... st.text('[advisors] Suthut Butchanon')
"""
