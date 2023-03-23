# CBAM-Keras
* ["CBAM: Convolutional Block Attention Module"](https://arxiv.org/pdf/1807.06521) 
* ["Squeeze-and-Excitation Networks"](https://arxiv.org/pdf/1709.01507) 

## CBAM: Convolutional Block Attention Module
**CBAM** proposes an architectural unit called *"Convolutional Block Attention Module" (CBAM)* block to improve representation power by using attention mechanism: focusing on important features and supressing unnecessary ones.
This research can be considered as a descendant and an improvement of ["Squeeze-and-Excitation Networks"](https://arxiv.org/pdf/1709.01507).

### Diagram of a CBAM_block
<div align="center">
  <img src="https://github.com/kobiso/CBAM-keras/blob/master/figures/overview.png">
</div>

![explain](https://user-images.githubusercontent.com/8428372/227129861-489e1856-e23c-432a-b6a6-825423a182bc.png)

### Diagram of each attention sub-module

![explain2](https://user-images.githubusercontent.com/8428372/227129948-24a41392-8c0f-4f44-9f8a-057ed3492426.png)

<div align="center">
  <img src="https://github.com/kobiso/CBAM-keras/blob/master/figures/submodule.png">
</div>

![sam](https://user-images.githubusercontent.com/8428372/227132284-0d26d090-c775-4489-a235-87b92c5daafa.png)
![cam](https://user-images.githubusercontent.com/8428372/227132298-9fcc7c81-f458-4b77-8b45-ba1c9e0f88dc.png)

### Classification results on ImageNet-1K
![data](https://user-images.githubusercontent.com/8428372/227132279-f65ae351-588b-4360-9b30-8dfad33910f0.png)
* GFLOPs mean `10^9 Floating Point Operations Per Second`
<div align="center">
  <img src="https://github.com/kobiso/CBAM-keras/blob/master/figures/exp4.png">
</div>

<div align="center">
  <img src="https://github.com/kobiso/CBAM-keras/blob/master/figures/exp5.png"  width="750">
</div>



