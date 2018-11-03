# Install Tensorflow on Windows 10

1. Before the setup, check Python version, cuDNN and CUDA versions on [Build from source on Windows](https://www.tensorflow.org/install/source_windows)

2. Follow [Setup a Python Environment for Machine Learning and Deep Learning](https://towardsdatascience.com/setup-an-environment-for-machine-learning-and-deep-learning-with-anaconda-in-windows-5d7134a3db10)

3. If you see "ImportError: DLL load failed" issue, you need to check the right versions of cuDNN and CUDA. For example, `tensorflow_gpu-1.11.0` -> `CUDA 9.0` -> `cuDNN v7.3.1` -> `Python 3.6.4`. Also make sure adding cuDNN into Environment Path

4. If you see this issue [failed to create cublas handle: CUBLAS_STATUS_ALLOC_FAILED](https://github.com/tensorflow/tensorflow/issues/7072) when you run `Mnist_Mlp.Py`, you can add the following code.

   ```python
   import tensorflow as tf
   from keras.backend.tensorflow_backend import set_session
   config = tf.ConfigProto()
   config.gpu_options.allow_growth = True  # dynamically grow the memory used on the GPU
   config.log_device_placement = True  # to log device placement (on which device the operation ran)
                                       # (nothing gets printed in Jupyter, only if you run it standalone)
   sess = tf.Session(config=config)
   set_session(sess)  # set this TensorFlow session as the default session for Keras
   ```
5.  Solve [TensorFlow session fails with error not compiled to use AVX2](https://stackoverflow.com/questions/51924370/tensorflow-session-fails-with-error-not-compiled-to-use-avx2) issue, add 

    ```python
    import os
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
    ```