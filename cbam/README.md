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

### Diagram of each attention sub-module
<div align="center">
  <img src="https://github.com/kobiso/CBAM-keras/blob/master/figures/submodule.png">
</div>

### Classification results on ImageNet-1K
* GFLOPS mean `10^9 Floating Point Operations Per Second`
<div align="center">
  <img src="https://github.com/kobiso/CBAM-keras/blob/master/figures/exp4.png">
</div>

<div align="center">
  <img src="https://github.com/kobiso/CBAM-keras/blob/master/figures/exp5.png"  width="750">
</div>



