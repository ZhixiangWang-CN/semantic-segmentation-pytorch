import os
import wget, tarfile


# Image and model names
TEST_IMG='ADE_val_00001519.jpg'
MODEL_NAME='ade20k-resnet50dilated-ppm_deepsup'
MODEL_PATH='ckpt/'+MODEL_NAME
RESULT_PATH='./'

ENCODER=MODEL_NAME+'/encoder_epoch_20.pth'
DECODER=MODEL_NAME+"/decoder_epoch_20.pth"

os.makedirs(MODEL_PATH)

data_url = 'http://sceneparsing.csail.mit.edu/model/pytorch/$ENCODER'
target_name = wget.filename_from_url(data_url)
file_name = wget.download(data_url, out=os.path.join(MODEL_PATH))