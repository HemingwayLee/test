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

```python3
from tensorflow.keras.layers import Flatten, Dense, Multiply, Activation
from tensorflow.keras import backend as K

def channel_gate(x, gate_channels, reduction_ratio=16, pool_types=['avg', 'max']):
    channel_att_sum = None
    for pool_type in pool_types:
        if pool_type=='avg':
            avg_pool = layers.AveragePooling2D(pool_size=(7, 7))(x)
            channel_att_raw = Dense(gate_channels // reduction_ratio)(Flatten()(avg_pool))
            channel_att_raw = Activation('relu')(channel_att_raw)
            channel_att_raw = Dense(gate_channels)(channel_att_raw)
        elif pool_type=='max':
            max_pool = layers.MaxPooling2D(pool_size=(7, 7))(x)
            channel_att_raw = Dense(gate_channels // reduction_ratio)(Flatten()(max_pool))
            channel_att_raw = Activation('relu')(channel_att_raw)
            channel_att_raw = Dense(gate_channels)(channel_att_raw)

        if channel_att_sum is None:
            channel_att_sum = channel_att_raw
        else:
            channel_att_sum += channel_att_raw

    scale = Activation('sigmoid')(channel_att_sum) # broadcasting
    return Multiply()([x, scale])
```

```python3
class Flatten(nn.Module):
    def forward(self, x):
        return x.view(x.size(0), -1)

class ChannelGate(nn.Module):
    def __init__(self, gate_channels, reduction_ratio=16, pool_types=['avg', 'max']):
        super(ChannelGate, self).__init__()
        self.gate_channels = gate_channels
        self.mlp = nn.Sequential(
            Flatten(),
            nn.Linear(gate_channels, gate_channels // reduction_ratio),
            nn.ReLU(),
            nn.Linear(gate_channels // reduction_ratio, gate_channels)
            )
        self.pool_types = pool_types
    def forward(self, x):
        channel_att_sum = None
        for pool_type in self.pool_types:
            if pool_type=='avg':
                avg_pool = F.avg_pool2d( x, (x.size(2), x.size(3)), stride=(x.size(2), x.size(3)))
                channel_att_raw = self.mlp( avg_pool )
            elif pool_type=='max':
                max_pool = F.max_pool2d( x, (x.size(2), x.size(3)), stride=(x.size(2), x.size(3)))
                channel_att_raw = self.mlp( max_pool )
            elif pool_type=='lp':
                lp_pool = F.lp_pool2d( x, 2, (x.size(2), x.size(3)), stride=(x.size(2), x.size(3)))
                channel_att_raw = self.mlp( lp_pool )
            elif pool_type=='lse':
                # LSE pool only
                lse_pool = logsumexp_2d(x)
                channel_att_raw = self.mlp( lse_pool )

            if channel_att_sum is None:
                channel_att_sum = channel_att_raw
            else:
                channel_att_sum = channel_att_sum + channel_att_raw

        scale = F.sigmoid( channel_att_sum ).unsqueeze(2).unsqueeze(3).expand_as(x)
        return x * scale
```

### Classification results on ImageNet-1K
![data](https://user-images.githubusercontent.com/8428372/227132279-f65ae351-588b-4360-9b30-8dfad33910f0.png)
* GFLOPs mean `10^9 Floating Point Operations Per Second`
<div align="center">
  <img src="https://github.com/kobiso/CBAM-keras/blob/master/figures/exp4.png">
</div>

![res](https://user-images.githubusercontent.com/8428372/227133143-05dd7630-fed7-4702-9e20-cd4f5987e3e1.png)

<div align="center">
  <img src="https://github.com/kobiso/CBAM-keras/blob/master/figures/exp5.png"  width="750">
</div>

### Network Visualization with Grad-CAM

![heatmap](https://user-images.githubusercontent.com/8428372/227133712-ee8aac95-ab12-48d4-87c7-931ad3c9173a.png)
