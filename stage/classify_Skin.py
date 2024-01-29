import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import os
import sys
from PyQt5.QtGui import *

def classify(self,imagepath):
    # Disable tensorflow compilation warnings
    os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
    img=os.path.join(imagepath)
    image_path = img
    
    # Read the image_data
    image_data = tf.gfile.FastGFile(image_path, 'rb').read()
    
    
    # Loads label file, strips off carriage return
    label_lines = [line.rstrip() for line
                       in tf.gfile.GFile(r"""skin_labels.txt""")]
    
    # Unpersists graph from file
    with tf.gfile.FastGFile(r"""skin_graph.pb""", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')
    
    str_1 = ''
    
    with tf.Session() as sess:
        # Feed the image_data as input to the graph and get first prediction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
    
        predictions = sess.run(softmax_tensor, \
                 {'DecodeJpeg/contents:0': image_data})
    
        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
        
        for node_id in top_k:
            human_string = label_lines[node_id]
            score = predictions[0][node_id]
            str_1 = str_1 + ('{} (score = {:.5f}) \n'.format(human_string, score))
            print('%s (score = %.5f)' % (human_string, score))
            
    # Create an PyQT4 application object.
  #  print(str_1)
    return str_1
    #win(str_1)
    
def win(str_1):
    #app = QApplication(sys.argv)
    w = QWidget()
    b = QLabel(w)
    b.setText(str(str_1))
    w.setGeometry(100,100,200,50)
    b.move(50,20)
    w.setWindowTitle('PyQt')
    w.show()
    #sys.exit(app.exec_())

