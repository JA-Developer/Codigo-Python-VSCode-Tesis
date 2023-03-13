# A PID Control Algorithm With Adaptive Tuning Using Continuous Artificial Hydrocarbon Networks for a Two-Tank System

This repository contains the source code of the research described in [A PID Control Algorithm With Adaptive Tuning Using Continuous Artificial Hydrocarbon Networks for a Two-Tank System](https://ieeexplore.ieee.org/document/9930515), which was developed using Python and VSCode.

<p align="center">
  <a href="https://github.com/JA-Developer/Codigo-Python-VSCode-Tesis">
    <img src="https://ieeexplore.ieee.org/mediastore_new/IEEE/content/media/6287639/9668973/9930515/josel4-3217209-large.gif" width="400" alt="PID Control Algorithm">
  </a>
</p>

The system consists of a PID controller whose parameters are tuned in real time by an artificial hydrocarbon network (Tuner based on artificial hydrocarbon networks). This artificial network in charge of tuning is trained by the backward difference method. To improve the efficiency of the backward difference method, another artificial hydrocarbon network is used to predict the plant behaviour Yp(k+1).

## Abstract

Owing to their ease of implementation, proportional-integral-derivative (PID) control systems are widely used to control physical systems. However, when environmental disturbances or changes in system parameters occur, the complexity of tuning the gains of PID controllers increases because, in these cases, their performance decreases. To solve this problem, an AI-based online self-tuning algorithm adjusts the PID gains when system parameters are changed. Thus, the objective of this study was to develop a PID control algorithm with adaptive parameter tuning using artificial hydrocarbon networks, which is a supervised learning artificial intelligence technique inspired by hydrocarbon networks. Artificial hydrocarbon networks were designed to be trained using a prior set of data. Therefore, the motivation of this study was to demonstrate that they can be trained in real time for use in the control of nonlinear systems. Because this type of network has not been commonly used for this specific application, existing studies on adaptive control based on artificial neural networks were taken as a reference. The AMSGrad optimization algorithm was used to train the parameters in real time, for which a “continuous” model of artificial hydrocarbon networks was also proposed. Finally, an algorithm capable of adapting to variations in the operating conditions of a tank system was successfully designed, although its performance was similar to that of the Ziegler-Nichols method.

<p align="center">
  <a href="https://github.com/JA-Developer/Codigo-Python-VSCode-Tesis">
    <img src="https://ieeexplore.ieee.org/mediastore_new/IEEE/content/media/6287639/9668973/9930515/josel3-3217209-large.gif" width="400" alt="PID Control Algorithm">
  </a>
</p>

## Contributing

Desert Legends was developed by Jesús Sánchez Palma and José Luis Ordoñez Ávila using Python and VSCode.