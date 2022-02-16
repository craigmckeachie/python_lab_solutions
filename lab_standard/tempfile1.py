import tempfile

tf = tempfile.TemporaryFile()
tf.write(b'I am a temp') # has to be bytes

tf.seek(0)
tf.read()

tf.close()

with tempfile.TemporaryDirectory() as tmpdirname:
    print('created temporary directory', tmpdirname)
