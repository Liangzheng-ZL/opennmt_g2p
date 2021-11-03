# OpenNMT-based Seq2Seq-G2P(grapheme-to-phoneme) model.

## November 2nd / 2021

In this repo, we try to find an efficient way to do the conversion of grapheme to phoneme, epecially on person names. We used the latest cmudict-0.7b\[1] as the dataset of our G2P model. We divided the datset into train set and test set. The conversion of grapheme-to-phoneme is similar with transduction. As a classic neural machine translation model and eural sequence learning, OpenNMT works well on sequence modeling and transduction problems. We tested whether OpenNMT can be used for seq2seq-g2p. Our results showed that OpenNMT-based G2P model can generate promising pronunciation, and the words in test set were completelya different from the words in train set, proving that OpenNMT is suitable for Seq2Seq-G2P.

## Preparation
To use OpenNMT-based seq2seq-g2p model, install OpenNMT first:
OpenNMT-py requires:
 + Python>=3.6
 + PyTorch==1.6.0


 Install `OpenNMT-py` from pip:
 
```sh
pip install OpenNMT-py
```
or from the sources:
```bash
git clone https://github.com/OpenNMT/OpenNMT-py.git
cd OpenNMT-py
pip install -e .
```

Note: if you encounter a `MemoryError` during installation, try to use `pip` with `--no-cache-dir`.

*(Optional)* Some advanced features (e.g. working pretrained models or specific transforms) require extra packages, you can install them with:

```bash
pip install -r requirements.opt.txt
```
## Quickstart
### Step 1: build a configuration file
We need to build a YAML configuration file to specify the data and model that will be used:
```bash 
vi cmudict_g2p_transformer.yaml
```
### Step 2: generate pronunciations
To generate pronunciations for an English word list with a trained model:
```bash
onmt_translate -model g2p_model/model_step_1000.pt -src valid_s.txt -output exp/pred_valid_1000.txt -gpu 0 -verbose
```
The word list is a text file with one word per line, and each character in the word is separated by a space:
```bash
H E L L O
```


We can also wirte a script to run conversion:
```bash
checkpoint=10000
src=valid_s
tgt=valid_t
onmt_translate \
         -gpu 0 \
         -batch_size 2 \
         -beam_size 3 \
         -model g2p_model_0.5_10000/cmu_g2p_model_step_${checkpoint}.pt \
         -src $src.txt \
         -output run/pred_${src}_${checkpoint}.txt \
         -tgt $tgt.txt \
         -verbose \
         --n_best 3 \
         &> run/translate.log&
```


## Train G2P model
### Step 1: Prepare the data

To get started, we propose to download a CMUdict for grapheme-to-phoneme, also we provide the processed CMUdict in this repo:

```bash
git clone https://github.com/Alexir/CMUdict.git
```
We can use the latest cmudict-0.7b. We also need to do the following:
Convert words into character sequences：
```bash
HELLO ---> H E L L O
```
Remove the markers after multi-pronounced words：
```bash

```
If you want to train a g2p-model for perosn names, we advice you delete the 

