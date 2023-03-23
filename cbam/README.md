# CBAM-Keras
This is a Keras implementation of ["CBAM: Convolutional Block Attention Module"](https://arxiv.org/pdf/1807.06521).
This repository includes the implementation of ["Squeeze-and-Excitation Networks"](https://arxiv.org/pdf/1709.01507) as well, so that you can train and compare among base CNN model, base model with CBAM block and base model with SE block.

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

<div align="center">
  <img src="https://github.com/kobiso/CBAM-keras/blob/master/figures/exp4.png">
</div>

<div align="center">
  <img src="https://github.com/kobiso/CBAM-keras/blob/master/figures/exp5.png"  width="750">
</div>



