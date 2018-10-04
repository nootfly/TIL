# CoreML 2

* Create ML, a new GPU-accelerated tool for native AI model training on Macs. The tool supports vision and natural language, as well as custom data.

* When we quantize a model, we are reducing the size of the weight! In iOS 11, Core ML models were stored in 32-bit models. With iOS 12, Apple has given us the ability to store the model in 16-bit and even 8-bit model.

* Install `coremltools`

  `pip install coremltools==2.0b1`

* `Linear Quantization` is when you map the weights evenly and reduce them. In a `Lookup Table Quantization`, the model constructs a table and groups the weights around based on similarity and reduces them.

* Quantization is an accuracy tradeoff. Quantized models are approximations of the size of the weight, so it is always important to run your quantized models and see how they perform.
  
* [TensorFlow (TF) to CoreML Converter](https://github.com/tf-coreml/tf-coreml)

## References

[What’s New in Core ML 2](https://www.appcoda.com/coreml2/)

[Awesome-CoreML-Models](https://github.com/likedan/Awesome-CoreML-Models)

[Apple Machine Learning](https://developer.apple.com/machine-learning/)
