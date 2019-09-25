## Recommender System Microservices

### Install Requirements
```
pip3 install git+https://github.com/maciejkula/spotlight.git@master#egg=spotlight
pip3 install implicit
pip3 install pandas
pip3 install numpy

# In case you use CPU
pip3 install torch==1.2.0+cpu torchvision==0.4.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
```

### Usages:
**model_type:** factorization, sequence
######
**request_type:** inference, update
- Start API
```
python3 start_api.py -m <model_type> 
```

- Test API
```
python3 test_api.py -m <model_type> -r <request_type>
```

- Tuning Model:
```
python3 tuning.py -m <model_type> 
```