# ClusterFL
This is the repo for MobiSys 2021 paper: "<a href="https://dl.acm.org/doi/10.1145/3458864.3467681"> ClusterFL: A Similarity-Aware Federated Learning System for Human Activity Recognition </a>" and TOSN 2022 paper: "<a href="https://github.com/xmouyang/xmouyang.github.io/blob/master/data/TOSN_ClusterFL_camera_ready_final.pdf"> ClusterFL: A Clustering-based Federated Learning System for Human Activity Recognition </a>".
<br>

# Requirements
The program has been tested in the following environment: 
* Ubuntu 18.04
* Python 3.6.8
* Tensorflow 2.4.0
* sklearn 0.23.1
* opencv-python 4.2.0
* Keras-python 2.3.1
* numpy 1.19.5
<br>

# ClusterFL Overview
<p align="center" >
	<img src="https://github.com/xmouyang/ClusterFL/blob/main/figures/ClusterFL-system-overview.png" width="500">
</p>

* ClusterFL on client: 
	* do local training with the collabrative learning variables;
	* communicate with the server.
* ClusterFL on server: 
	* recieve model weights from the clients;
	* learn the relationship of clients;
	* update the collabrative learning variables and send them to each client.


# Project Strcuture
```
|-- client                    // code in client side
    |-- client_cfmtl.py/	// main file of client 
    |-- communication.py/	// set up communication with server
    |-- data_pre.py/		// prepare for the FL data
    |-- model_alex_full.py/ 	// model on client 
    |-- desk_run_test.sh/	// run client 

|-- server/    // code in server side
    |-- server_cfmtl.py/        // main file of client
    |-- server_model_alex_full.py/ // model on server 

|-- README.md

|-- pictures               // figures used this README.md
```
<br>

# Quick Start
* Download the `dataset` folders (collected by ourself) from [FL-Datasets-for-HAR](https://github.com/xmouyang/FL-Datasets-for-HAR) to your client machine.
* Chooose one dataset from the above four datasets and change the "read-path" in 'data_pre.py' to the path on your client machine.
* Change the 'server_x_test.txt' and 'server_y_test.txt' according to your chosen dataset, default as the one for "imu_data_7".
* Change the "server_addr" and "server_port" in 'client_cfmtl.py' as your true server address. 
* Run the following code on the client machine
    ```bash
    cd client
    ./desk_run_test.sh
    ```
* Run the following code on the server machine
    ```bash
    cd server
    python3 server_cfmtl.py
    ```
    ---

# Citation
The code and datasets of this project are made available for non-commercial, academic research only. If you would like to use the code or datasets of this project, please cite the following paper:
```
@inproceedings{ouyang2021clusterfl,
  title={ClusterFL: a similarity-aware federated learning system for human activity recognition},
  author={Ouyang, Xiaomin and Xie, Zhiyuan and Zhou, Jiayu and Huang, Jianwei and Xing, Guoliang},
  booktitle={Proceedings of the 19th Annual International Conference on Mobile Systems, Applications, and Services},
  pages={54--66},
  year={2021}
}
```
    
```
@article{ouyang2022clusterfl,
  title={ClusterFL: a clustering-based federated learning system for human activity recognition}},
  author={Ouyang, Xiaomin and Xie, Zhiyuan and Zhou, Jiayu and Xing, Guoliang and Huang, Jianwei},
  journal={ACM Transactions on Sensor Networks (TOSN)},
  volume={18},
  number={4},
  year={2022},
  publisher={ACM New York, NY}
}
```
