# OpenNMT-based Seq2Seq-G2P(grapheme-to-phoneme) model.

## November 2nd / 2021

In this report, we try to find an efficient way to do the conversion of grapheme to phoneme, epecially on person names. We used the latest cmudict-0.7b\[1] as the dataset of our G2P model. We divided the datset into train set and test set. The conversion of grapheme-to-phoneme is similar with transduction. As a classic neural machine translation model and eural sequence learning, OpenNMT works well on sequence modeling and transduction problems. We tested whether OpenNMT can be used for seq2seq-g2p. Our results showed that OpenNMT-based G2P model can generate promising pronunciation, and the words in test set were completelya different from the words in train set, proving that OpenNMT is suitable for Seq2Seq-G2P.

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


